# S-DES Method Code README #

## Overview ##
This Python script implements the Simplified Data Encryption Standard (S-DES) algorithm for encryption and decryption of data. S-DES is a simplified version of the DES algorithm, designed for educational purposes.

## Functions ## 

```apply_table(inp, table)``` Applies an input permutation table to a given input.

```left_shift(data)``` Performs a left circular shift on the input data.

```xor(a, b)``` Performs a bitwise XOR operation between two binary strings.

```apply_sbox(s, data)``` Applies substitution box (S-box) transformation to the input data based on the S-box matrix provided.

## Usage ## 

Define the key and message binary strings in the ```__main__``` block.
Initialize permutation tables, S-box matrices, and other necessary variables.
Run the script to perform S-DES encryption on the input message using the specified key.

## Key Variables ## 

```key```: The binary key used for encryption.

```message```: The binary message to be encrypted.

```Tables``` and ```Matrices```:

- ```p8_table```, ```p10_table```, ```p4_table```: Permutation tables for key generation and permutation.
- ```IP```, ```IP_inv```: Initial and final permutation tables.
- ```expansion```: Expansion permutation table for S-DES function.
- ```s0```, ```s1```: S-box matrices for substitution.

## Execution ## 

The script generates two subkeys ```key1``` and ```key2``` from the initial key using permutation tables and left shifts.
It then encrypts the input message using the ```S-DES``` function with the generated subkeys.
The final ciphertext ```CT``` is obtained after performing the final permutation.
Note: This code is for educational purposes and demonstrates a simplified version of the Data Encryption Standard ```DES``` algorithm.
