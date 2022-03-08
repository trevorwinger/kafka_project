#install python package
echo "install python package"
pip3 install kafka-python
echo "install python package done"


#remove old test files
echo "remove old output files"
rm -rf ./files/
echo "remove old output files done"

#create output dir
echo "create output dir"
mkdir -p files
echo "create output dir done"

#get kafka stuff up and running
echo "start kafka"
#start zookeeper server
cd kafka_2.11-1.1.0
pwd 
bin/zookeeper-server-start.sh config/zookeeper.properties & 
#start kafka server
bin/kafka-server-start.sh config/server.properties & 
#create kafka topic
bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test &
#this will list all of the topics
bin/kafka-topics.sh --list --zookeeper localhost:2181 & 

#run my test spinning up producers and consumers writing to files
cd ../
python3 test.py
echo "kafka done"

