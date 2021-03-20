from kafka import KafkaProducer
import json



# Simple example https://pypi.org/project/kafka-python/

def sendToproducer(data):
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
               value_serializer=lambda m: json.dumps(m).encode('ascii'))
    producer.send('heartbeatlogs',data)
    producer.flush()
    producer.close()
    
    
    
    
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
     
while(True):     
    for i in range(len(m)):
        sendToproducer(m[i])
    
    