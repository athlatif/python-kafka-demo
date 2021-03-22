# python-kafka-demo

1- Clone repo
> git clone https://github.com/athlatif/python-kafka-demo.git

2- Clone docker image
> git clone https://github.com/confluentinc/cp-all-in-one

3- Run docker image
> cd C:\your_dir\cp-all-in-one\cp-all-in-one
> docker-compose up -d

2- create a topic
> docker-compose exec broker kafka-topics --create --bootstrap-server localhost:9092 --replication-factor 1  --partitions 1 --topic topicname

3- Run logs simulator code
python3 producer.py

4- Run consumers
python3 mongodbconsumer.py
python3 modelConsumer.py

