# Databricks notebook source
import requests
import json
from datetime import date, datetime, timezone, timedelta

# COMMAND ----------

def save_json(path, fileName, data):
    filePath = path + fileName
    with open(filePath, 'w') as fp:
        json.dump(data, fp)
    fp.close()

# COMMAND ----------

url = 'https://api.chucknorris.io/jokes/random'

response = requests.get(url)
json_response = response.json()

# COMMAND ----------

path = '/dbfs/mnt/blobstorage/chuck_norris_api/raw/'

zone = timezone(timedelta(hours=-3))
datetime_string = datetime.now().astimezone(zone).strftime("%Y%m%d_%H%M%S")

fileName = f'api_chuck_norris_{datetime_string}.json'
dbutils.fs.mkdirs(path)
save_json(path, fileName, json_response)


# COMMAND ----------


