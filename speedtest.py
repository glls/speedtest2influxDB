import json
import subprocess
from influxdb import InfluxDBClient

#command = 'speedtest-cli --server 2105 --json'
#response = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read().decode('utf-8')

# load sample
with open('data/sample.json') as f:
    data = json.load(f)

# cleanup/restructure data
for field in data['server']:
    data['server_' + str(field)] = data['server'][field]

for field in data['client']:
    data['client_' + str(field)] = data['client'][field]

data['server'] = ''
data['client'] = ''

d = [{
    "measurement": "internet_speed",
    "fields": data
}]

# send to influxDB
client = InfluxDBClient(host='192.168.3.11', port=8086, database='speedtest')
client.write_points(d)
