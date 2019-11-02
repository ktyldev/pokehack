package main

import (
    "log"
    "net/http"
    "fmt"
)

func main() {
    if !Config.Exists() {
        Config.Create()
    }

    port := Config.Read(CFG_PORT)
    log.Printf(
        "Starting PokeServer v%s on port %s\n",
        Config.Version(),
        port)

    port = fmt.Sprintf(":%s", port)
    log.Fatal(http.ListenAndServe(port, NewRouter()))
}

