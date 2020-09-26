#!/usr/bin/sh

if [[ ! -z "$1" ]]; then
    if [[ "$1" == "manager" ]]; then
        exec python3.8 -m manager.main
    fi
fi