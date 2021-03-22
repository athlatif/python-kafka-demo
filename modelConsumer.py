from kafka import KafkaConsumer
import json


# sudo AI Engine function
def passTomodel(product_number,userID):
    
    output = ['#156','#1768']
    return output

# init consumer with group ID
consumer = KafkaConsumer('heartbeatlogs',
                         group_id='CConsumerlogs',
                         bootstrap_servers=['localhost:9092'],
                         enable_auto_commit=True,
                         value_deserializer=lambda m: json.loads(m.decode('ascii')))
# loop over events 
for message in consumer:
    print(message.value)
    # send only product page logs
    if(message.value['page'] == 'product page'):
        print(passTomodel(message.value['product_number'], message.value['userID']))
