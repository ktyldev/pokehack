#   PokéHack

Made for Hack:Brunel hackathon

Networked Pokémon game using the [PokéAPI](https://pokeapi.co/), for fun!

Write clients to consume or provide 

## TODO

*   Replace title of readme with ASCII art
*   Define `/battle` get route
*   License

*   Turn all these points into issues on the repo

##  API Reference

### Battle

####    **POST** */move*

```json
{
    "name": "billybob",
    "i":    22
}
```

```
name:   player name  
i:      move id      
```

Sends a move to be processed in the next turn.

####    **POST** */joinson*

```json
{
    "name":     "billybob",
    "dent":     4,
    "moves":    [ 517, 14, 257, 44 ],
    "level":    1
}
```

```
name:   player name
dent:   pokedex id
moves:  move ids
level:  pokemon level
```

Join battle.

####    **GET** */battle*

TODO

Get battle state.
