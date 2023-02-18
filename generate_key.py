from math import ceil
from random import randint, seed
import json
import sys
 
secret_key = sys.argv[1]

freq = {
  "E": 56.88,
  "M": 15.36,
  "A": 43.31,
  "H": 15.31,
  "R": 38.64,
  "G": 12.59,
  "I": 38.45,
  "B": 10.56,
  "O": 36.51,
  "F": 9.24,
  "T": 35.43,
  "Y": 9.06,
  "N": 33.92,
  "W": 6.57,
  "S": 29.23,
  "K": 5.61,
  "L": 27.98,
  "V": 5.13,
  "C": 23.13,
  "X": 1.48,
  "U": 18.51,
  "Z": 1.39,
  "D": 17.25,
  "J": 1.00,
  "P": 16.14,
  "Q": 1
}

for letter in freq:
  freq[letter] = ceil(freq[letter])

s = 0

for letter in freq:
  s += freq[letter]

alphabet = list(range(s))

ranges = dict()
for letter in freq:
  ranges[letter] = []


seed(secret_key)
for letter in ranges:
  for i in range(freq[letter]):
    j = randint(0, len(alphabet)-1)
    ranges[letter].append(alphabet[j])
    del alphabet[j]
for letter in freq:
  print(letter, len(ranges[letter]))

key_file = open('key.json', 'w')
json.dump(ranges, key_file)