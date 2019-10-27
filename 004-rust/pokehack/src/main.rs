extern crate reqwest;

extern crate serde;
extern crate serde_json;

use std::io;
use std::io::Write;
use std::convert::TryInto;

use serde::{Serialize, Serializer};

use rand::Rng;

const SPECIES:      &str    = "charmander";
const GAME_SERVER:  &str    = "http://192.168.69.1:42069";
const NUM_MOVES:    usize   = 4;

#[derive(Clone, Serialize)]
struct Pokemon {
    pkmn:       u16,
    nickname:   String,
    moves:      [Move; NUM_MOVES],
    level:      u32
}

impl Pokemon {
    fn new() -> Self {
        Pokemon {
            pkmn:       4,
            nickname:   String::new(),
            moves:      [Move::new(); NUM_MOVES],
            level:      420
        }
    }
}

#[derive(Copy, Clone)]
struct Move {
    index:  u16
}

impl Move {
    fn new() -> Self {
        Move {
            index:  u16::max_value()
        }
    }

    // TODO: should prolly be a Result lol
    fn name(self: &Move) -> String {
        let url = format!("https://pokeapi.co/api/v2/move/{}", self.index);
        match get(&url) {
            Ok(response) => 
            { 
                return response["name"]
                    .to_string()
                    .replace("\"", ""); 
            },
            Err(e) => println!("{}", e)
        }

        String::new()
    }
}

impl Serialize for Move {
    fn serialize<S>(&self, serializer: S) -> Result<S::Ok, S::Error>
    where 
        S: Serializer
    {
        serializer.serialize_u16(self.index)
    }
}

fn main() -> io::Result<()> {
    let mut pokemon = Pokemon::new();
    pokemon.nickname = get_nickname();

    println!("Say hi to {}!", pokemon.nickname);

    get_moves(&mut pokemon);
    println!("{}'s moves: ", pokemon.nickname);
    for i in 0..NUM_MOVES {
        println!("{}", pokemon.moves[i].name())
    }

    let pokemon_json = serde_json::to_string(&pokemon)?;
    //println!("{}", pokemon_json);
    join_battle(&pokemon_json);

    Ok(())
}

fn join_battle(data: &str) {
    let url = format!("{}{}", GAME_SERVER, "/joinson");

    match post(&url, data) {
        Ok(response) => {
            println!("{}", response);
        },
        Err(e) => println!("{}", e)
    }
}

fn get_nickname() -> String {
    //  ask for nickname of pokemon
    print!("Enter a nickname for {}: ", SPECIES);
    io::stdout().flush().unwrap();

    player_input().trim().to_string()
}

fn get_moves(pokemon: &mut Pokemon) {
    //  get species info from pokeapi
    let url = format!("https://pokeapi.co/api/v2/pokemon/{}", SPECIES);

    match get(&url) {
        Ok(response) => {
            pick_moves(response, pokemon);
            //pokemon.moves = pokemon_moves;

        },
        Err(e) => println!("{}", e)
    }

    //println!("{}'s moves: ", pokemon.nickname);
    //for m in pokemon.moves {
    //    println!("{}", m.name);
    //}
}

fn pick_moves(data: serde_json::Value, pokemon: &mut Pokemon) {
    let moves = &data["moves"].as_array().unwrap();

    let max = moves.len();
    let mut count = 0;

    while count < NUM_MOVES {
        // pick a random move index
        let index: u16 = rand::thread_rng()
            .gen_range(0, max)
            .try_into()
            .unwrap();

        // check index hasn't already been picked
        let mut ok = true;
        for i in 0..NUM_MOVES {
            if pokemon.moves[i].index == index {
                ok = false;
                break;
            }
        }

        // add to results
        if ok {
            pokemon.moves[count].index = index;
            count = count + 1;
        }
    }
}

fn get(url: &str) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let response: serde_json::Value = reqwest::get(url)?
        .json()?;

    Ok(response)
}

fn post(url: &str, data: &str) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    println!("{}", data);

    let client = reqwest::Client::new();
    let response: serde_json::Value = client.post(url)
        .json(data)
        .send()?
        .json()?;

    Ok(response)
}

fn player_input() -> String {
    let mut input = String::new();

    loop {
        match io::stdin().read_line(&mut input) {
            Ok(_) => return input,
            Err(e) => println!("{}", e)
        }
    }
}


