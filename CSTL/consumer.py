# There are total of 2 sections you need to edit.
# Codes you need to edit are designated with 
# ### - START
# and
# ### - END

from influxdb import InfluxDBClient
from kafka import KafkaConsumer
import sys
#define information about kafka

### - START
bootstrap_servers = ['172.17.0.1:9092']
topicName = 'cstl'
STUDENT_NAME = "LIMMINTAEK"   # INPUT YOUR STUDENT NAME HERE

# IF YOU DO NOT INSERT YOUR NAME, YOU WILL GET NO CREDIT

### - END
consumer = KafkaConsumer(topicName, bootstrap_servers = bootstrap_servers)

# connect to InfluxDB 

client = InfluxDBClient(host='localhost', port=8086)   
client.create_database('cstl')
client.switch_database('cstl')

# database being used : cstl

try :
    for message in consumer:
        value = str(message.value)  # this is where the kafka consumer's value is saved as a string
        
        # EDIT THE CODES BELOW TO RETRIEVE destination IP address / source IP address / ICMP (request/reply)
        ### - START
        DST_IP = ''
        SRC_IP = ''
        ICMP_VALUE = ''

        names = value.split(' ')
        if (len(names)>7) :
            DST_IP = names[2]
            SRC_IP = names[4].replace(':','')
            ICMP_VALUE = names[7].replace(',','')
        # ICMP value means whether the packet is a (request or a reply)

        # You need to have the values printed

        print('dst_IP-' + DST_IP)
        print('src_ip-' + SRC_IP)
        print('icmp_value-' + ICMP_VALUE)

        # EDIT THE CODE BELOW TO SAVE VALUES IN THE DATABASEa

        ### - END
        data_to_be_saved = [
                {
                    'measurement': 'lmt',
                    'tags': {
                        'student' : STUDENT_NAME # DO NOT CHANGE THIS LINE
                        },
                    'fields': {
                        'dst_IP' : DST_IP,
                        'src_IP' : SRC_IP,
                        'value' : ICMP_VALUE
                        }                    
                    }
                ]



        client.write_points(data_to_be_saved) # this line of code saves what you put in the data_to_be_saved

except KeyboardInterrupt:
    sys.exit()
