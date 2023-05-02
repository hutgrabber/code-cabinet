#!/bin/bash

spin_states=(- \\ \| /)

function spin {
    echo -n "Working...  "
    for ((i=0; i<$1; i++))
    do
        state=$((i % ${#spin_states[@]}))
        echo -ne "\b${spin_states[state]}"
        sleep .1 # A "real" script would probably do something useful here
    done
    echo
}

spin 100

