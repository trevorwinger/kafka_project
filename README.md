# Kafka Bonus Project
## CSCI 5751
## University of Minnesota 
### Trevor Winger

#### 0. Installs 
You do not have to install any of these the shell file will install necessary pip files and git repo contains the kafka files from apache. 

##### 0.1 Kafka from apache site -- included in repo from: https://www.apache.org/dyn/closer.cgi?path=/kafka/1.1.0/kafka_2.11-1.1.0.tgz
##### 0.2 kafka-python from: https://kafka-python.readthedocs.io/en/master/install.html


#### 1. Running
You will have to move to the directory you installed the git files and run: `sh run.sh` \n
This will do several things: \n
* install pip dependcies
* make output directory called 'files' 
* remove previous output files in 'files'
* start running the necessary kafka servers 
* start the `test.py` which will spin up the consumer and producer
    

#### 2. What is happening in python? 
##### `test.py` generates messages for our producer, I have it set to 100 messages not to eat up too much time, but this could be set to any arbitraty number. The messages are pretty simple, 'test message' plus an appended number representing the count in our entire message list. Once all of the messages are created our producer takes the list of messages and sends them to our consumer with the designated topic. Our consumer is taking each produced message reading it and writing an file for each message. This simple operation is just meant to show that you could do something here like write to a db. 