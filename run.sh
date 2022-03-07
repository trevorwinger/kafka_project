#install python package
pip3 install kafka-python

#create output dir
mkdir -p files

#remove old test files
rm ./files/*.txt

#get kafka stuff up and running
cd kafka_2.11-1.1.0 && \
  ./bin/zookeeper-server-start.sh config/zookeeper.properties & \
  ./bin/kafka-server-start.sh config/server.properties & \
  ./bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test & \
  ./bin/kafka-topics.sh --list --zookeeper localhost:2181 & \
  #run my test spinning up producers and consumers writing to files
  cd .. && python3 test.py

