#!/bin/bash

# Create the data directory
mkdir data 

# Create the test files
python3 generate_data.py

# Create the attempt files
cargo run -q

# Confirm the attempt files are the same
for i in {0..2}
do
    ftrue="./data/atmp_0$i.txt"
    fpred="./data/answ_0$i.txt"
    echo $ftrue
    echo $fpred
    
    cmp --silent $ftrue $fpred && echo '    ### SUCCESS: Files Are Identical! ###' || echo '    ### WARNING: Files Are Different! ###'
    
    echo
done

# Remove all the created files
rm -r data/*
rm -rf data

# clean up the compiled binaries 
cargo clean -q
