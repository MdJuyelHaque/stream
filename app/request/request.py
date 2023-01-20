import requests
import json
from encrypt_sql import *
servername = server
user = username
password= password
database =database
url = connect
payload = json.dumps({
  "name": "Task",
  "config": {
    "connector.class": "io.debezium.connector.sqlserver.SqlServerConnector",
    "database.hostname": servername,
    "database.port": "1433",
    "database.user": user,
    "database.password": password,
    "database.names": database,
    "database.server.name": servername,
    "topic.prefix": "Test",
    "database.encrypt": False,
    "table.include.list":"dbo.Task",
    "schema.history.internal.kafka.bootstrap.servers": "kafka:29092",
    "schema.history.internal.kafka.topic": "schema-changes.inventory",
    "value.converter": "org.apache.kafka.connect.json.JsonConverter",
    "value.converter.schemas.enable": "false",
    "key.converter": "org.apache.kafka.connect.json.JsonConverter",
    "key.converter.schemas.enable": "false"
  }
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
