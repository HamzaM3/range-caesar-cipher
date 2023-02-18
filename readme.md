# Range Caesar Substitution

We propose a fix for the Caesar substitution method that prevents frequency analysis.

We associate to each letter an amount of values proportional to their respective frequency and we substitute each character with a random value in its range.

The key is the seed of the random function used while creating the ranges. So that the whole key json is not exchanged (the key can deterministically be calculated on each side of the conversation).

## Test it !

You can test this by doing this (after adding your message to `message.txt`):

```sh
python3 generate_key.py \<seed\>
python3 range_caesar_encrypt.py
```

The encrypted message is in `encrypted_message.json`

To decrypt the message do:

```sh
python3 range_caesar_decrypt.py
```

<small>(A statistical analysis should be performed and an in depth thought on the possible attacks as well)</small>
