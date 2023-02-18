import json
from random  import choice

key_json = open('key.json', 'r')
key = json.load(key_json)

message_file=open('message.txt', 'r')
message = message_file.read()
message = ''.join(message.split()).upper()
message = [*message]

res = []
for c in message:
  res.append(choice(key[c]))

encrypted = open('encrypted_message.json', 'w')
json.dump(res, encrypted)
