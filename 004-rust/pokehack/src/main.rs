extern crate reqwest;

extern crate serde;
extern crate serde_json;

use std::io;
use std::io::Write;
use std::convert::TryInto;

use serde::{Serialize, Serializer};
use serde_json::json;

use rand::Rng;

const SPECIES: &str = "charmander";
const GAME_SERVER: &str = "192.168.69.1:42069";
const NUM_MOVES: usize = 4;

#[derive(Clone, Serialize)]
struct Pokemon <'a> {
    pokemon_id: u16,
    nickname: String,
    moves: &'a Vec<Move>
}

#[derive(Clone)]
struct Move {
    name: String,
    index: u16
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
    let mut pokemon = Pokemon{
        pokemon_id:0, 
        nickname:"".to_string(),
        moves: &mut vec![Move{
            name: "".to_string(),
            index: 0
        }; 4]
    };

    pokemon.nickname = get_nickname();
    println!("Say hi to {}!", pokemon.nickname);

    //  get species info from pokeapi
    let url = format!("https://pokeapi.co/api/v2/pokemon/{}", SPECIES);
    match request(&url) {
        Ok(response) => {
            let pokemon_moves = &mut vec![Move{
                name: "".to_string(),
                index: 0
            }; 4];

            pick_moves(response, pokemon_moves);
            pokemon.moves = pokemon_moves;

            println!("{}'s moves: ", pokemon.nickname);
            for m in pokemon.moves {
                println!("{}", m.name);
            }

            let pokemon_json = serde_json::to_string_pretty(&pokemon)?;
            println!("{}", pokemon_json);
        },
        Err(e) => println!("Error: {}", e)
    }

    //  send join request to game server

    Ok(())
}

fn get_nickname() -> String {
    //  ask for species and nickname of pokemon
    print!("Enter a nickname for {}: ", SPECIES);
    io::stdout().flush().unwrap();

    player_input().trim().to_string()
}

fn pick_moves(data: serde_json::Value, pokemon_moves: &mut Vec<Move>) {
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
            if pokemon_moves[i].index == index {
                ok = false;
                break;
            }
        }

        // add to results
        if ok {
            pokemon_moves[count].index = index;

            let move_name = &moves[index as usize]["move"]["name"];
            pokemon_moves[count].name = move_name
                .to_string()
                .replace("\"", "");

            count = count + 1;
        }
    }
}

fn request(url: &str) -> Result<serde_json::Value, Box<dyn std::error::Error>> {
    let response: serde_json::Value = reqwest::get(url)?
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


