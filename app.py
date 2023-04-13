import json

SensitiveData="config.json"

with open(SensitiveData) as user_file:
  
  API_KEY = json.load(user_file)

  print(API_KEY["api_key"])