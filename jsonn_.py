import json

a = 'Hello World!'
b = {key: value for key, value in enumerate(a)}

# Correct separators format
c = json.dumps(b, indent=3, separators=(',', '; '))
print(c)
