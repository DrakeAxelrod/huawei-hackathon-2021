import json

def read_file(filename="./src/sample.json"):
  with open(filename) as f:
    file = json.load(f)
    f.close()
  return file
  
def read_data():
  data = read_file()
  return data

f = read_data()
print(f)
