extern crate reqwest;

extern crate serde;
extern crate serde_json;

use std::io;
use std::io::Write;
use std::convert::TryInto;

use serde::{Serialize, Serializer};

use rand::Rng;

const SPECIES:      &str    = "charmander";
const POKE_API:     &str    = "https://pokeapi.co/api/v2";
const GAME_SERVER:  &str    = "http://192.168.69.1:42069";
const NUM_MOVES:    usize   = 4;

#[derive(Clone, Serialize)]
struct Pokemon {
    pkmn:       u16,
    name:       String,
    moves:      [Move; NUM_MOVES],
    level:      u32
}

impl Pokemon {
    fn new() -> Self {
        Pokemon {
            pkmn:   u16::max_value(),
            name:   String::new(),
            moves:  [Move::new(); NUM_MOVES],
            level:  1
        }
    }

    fn load(self: &mut Pokemon) {
        let url = format!("{}/pokemon/{}", POKE_API, SPECIES);

        match get(&url) {
            Ok(response) => {

                self.load_id(&response);
                self.load_moves(&response);
            },
            Err(e) => println!("{}", e)
        }
    }

    fn load_id(self: &mut Pokemon, data: &serde_json::Value) {
        self.pkmn = data["id"].as_u64().unwrap() as u16;
    }

    fn load_moves(self: &mut Pokemon, data: &serde_json::Value) {
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
                if self.moves[i].index == index {
                    ok = false;
                    break;
                }
            }

            // add to results
            if ok {
                self.moves[count].index = index;
                count += 1;
            }
        }
    }

    // TODO: replace bool with battle state
    fn make_move(self: &mut Pokemon, move_names: &Vec<String>) -> bool {
        // show available moves
        for i in 0..NUM_MOVES {
            println!("[{}]\t{}", i + 1, move_names[i]);
        }

        // player choose move
        let choice = get_player_move_choice();    

        println!("{}! use {}!", self.name, move_names[choice as usize]);

        // send move to server

        // handle response from round of battle

        true
    }
}


#[derive(Copy, Clone)]
struct Move {
    index:  u16,
}

impl Move {
    fn new() -> Self {
        Move {
            index:  u16::max_value()
        }
    }

    // TODO: should prolly be a Result lol
    fn name(self: &Move) -> String {
        let url = format!("{}/move/{}", POKE_API, self.index);
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
    pokemon.name = get_nickname();

    println!("Say hi to {}!", pokemon.name);

    pokemon.load();
    println!("{}'s moves: ", pokemon.name);
    for i in 0..NUM_MOVES {
        println!("{}", pokemon.moves[i].name())
    }

    let pokemon_json = serde_json::to_string(&pokemon)?;

    // try to join battle on the server
    let mut in_battle = join_battle(&pokemon_json);
    if !in_battle {
        std::process::exit(1);
    }
    // start battle
    
    // load move names
    let mut move_names = Vec::new();
    for i in 0..NUM_MOVES {
        let move_name = pokemon.moves[i].name();
        move_names.push(move_name);
    }

    while in_battle {
        in_battle = pokemon.make_move(&move_names);
    }

    println!("Game Over!");
    Ok(())
}


fn join_battle(data: &str) -> bool {
    let url = format!("{}{}", GAME_SERVER, "/joinson");

    match post(&url, data) {
        Ok(response) => {
            println!("{}", response);

        },
        Err(e) => println!("{}", e)
    }

    true
}

fn get_nickname() -> String {
    //  ask for nickname of pokemon
    print!("Enter a nickname for {}: ", SPECIES);
    io::stdout().flush().unwrap();

    player_input().trim().to_string()
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

fn get_player_move_choice() -> u8 {
    loop {
        match player_input().trim().parse::<i32>() {
            Ok(i) => {
                if i > 0 && i < NUM_MOVES as i32 {
                    break i as u8;
                }

                println!("{} is out of bounds", i);
            },
            _ => println!("Could not parse input")
        }
    }
}

