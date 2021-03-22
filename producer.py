from kafka import KafkaProducer
import json


# Producer function
def sendToproducer(data):
    # send [ data ] to broker at [ localhost:9092 ]
    # parse json -> bytes
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
               value_serializer=lambda m: json.dumps(m).encode('ascii'))
    # define topic to send data to
    producer.send('heartbeatlogs',data)
    producer.flush()
    producer.close()
    
    
    # messages to be sent
m = [{'level': 'error', 'message' : 'error in login', 'page': 'login page'},
     {'level': 'info', 'message' : 'user clicked on homepage', 'page': 'homepage'},
     {'level': 'info', 'message' : 'user clicked on info page', 'page': 'info page'},
     {'level': 'error', 'message' : 'error in processing image', 'page': 'profile page'},
     {'level': 'info', 'message' : 'user clicked on product #12234', 'page': 'product page', 'product_number': '12234', 
      'userID': '10008'
      },
     {'level': 'info', 'message' : 'user clicked on product #12234', 'page': 'product page', 'product_number': '12234', 
      'userID': '10008'
      },
     {'level': 'info', 'message' : 'user clicked on product #12235', 'page': 'product page', 'product_number': '12235', 
      'userID': '10008'
      },
     {'level': 'info', 'message' : 'user clicked on product #12236', 'page': 'product page', 'product_number': '12236', 
      'userID': '10008'
      },
     {'level': 'info', 'message' : 'user clicked on product #12237', 'page': 'product page', 'product_number': '12237', 
      'userID': '10008'
      },
     {'level': 'info', 'message' : 'user clicked on product #12238', 'page': 'product page', 'product_number': '12238', 
      'userID': '10008'
      }
     
     
     ]
     
# infinite loop to send data  
while(True):     
    for i in range(len(m)):
        sendToproducer(m[i])
    
    
