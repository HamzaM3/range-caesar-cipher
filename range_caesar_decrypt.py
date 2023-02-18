import json

def getLetter(key, i):
  for letter in key:
    if i in key[letter]:
      return letter

  raise 'Wrong index'

encrypted_json = open('encrypted_message.json', 'r')
encrypted = json.load(encrypted_json)
key_json = open('key.json', 'r')
key = json.load(key_json)

decrypted = ''
for i in encrypted:
  decrypted += getLetter(key, i)

print(decrypted)
