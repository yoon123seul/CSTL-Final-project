from kafka import KafkaProducer
from kafka.errors import KafkaError
import subprocess as sub

### - START

INTERFACE_NAME = 'eno1' # INPUT NETWORK INTERFCAE THAT YOU WISH TO MONITOR
IP_ADDRESS = '192.168.100.1' # INPUT SOURCE NETWORK IP ADDRESS

# Connect kafka producer here
producer = KafkaProducer(bootstrap_servers=['172.17.0.1:9092'],
                                            value_serializer=lambda m: m.encode('utf-8'))

### - END
topicName = 'cstl'

def transmit_kafka():
    p = sub.Popen(('tcpdump','-i',INTERFACE_NAME,'-l'), stdout=sub.PIPE)

    for line in iter(p.stdout.readline, b''):
        content = str(line)
        if (content.find(IP_ADDRESS)) != -1 and content.find('ICMP') != -1 :
            print(content)
            producer.send(topicName, content)

# transmit_kafka()

transmit_kafka()
