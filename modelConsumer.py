from kafka import KafkaConsumer
import json



def passTomodel(product_number,userID):
    
    
    
    output = ['#156','#1768']
    return output

consumer = KafkaConsumer('heartbeatlogs',
                         group_id='CConsumerlogs',
                         bootstrap_servers=['localhost:9092'],
                         enable_auto_commit=True,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))
for message in consumer:

    print(message.value)
    if(message.value['page'] == 'product page'):
        print(passTomodel(message.value['product_number'], message.value['userID']))