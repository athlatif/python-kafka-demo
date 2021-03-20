from kafka import KafkaConsumer
import json
from pymongo import MongoClient


client =MongoClient("mongodb+srv://pydatademo:pydatademo@cluster0.2dcmv.mongodb.net/?retryWrites=true&w=majority")
db = client.websitelogs



def passToMongoDB(messagejson):
    
    mycol = db["kafka_logs"]
    
    x = mycol.insert_one(messagejson)
    
    output = ['#156','#1768']
    return output

consumer = KafkaConsumer('heartbeatlogs',
                         group_id='mongoDB_C',
                         bootstrap_servers=['localhost:9092'],
                         enable_auto_commit=True,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))
for message in consumer:
    passToMongoDB(message.value)
    

