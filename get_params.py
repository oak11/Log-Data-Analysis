from sklearn.preprocessing import OneHotEncoder
from numpy import array
from sklearn import preprocessing
import json


enc = OneHotEncoder()
data = []
with open('data.json') as f:
    for line in f:
        data.append(json.loads(line))
l = []
temp_request_path = []
s = ''

#finding unique features for request_path

for i in range (0,1955):
	k = str(data[i]['metadata']['request_path'])	
	if k != s and (k not in temp_request_path):
		temp_request_path.append(k)
		s = k
#finding unique features for request_lb_ip

temp_request_lb_ip = []
s = ''

for i in range (0,1955):
	k = str(data[i]['metadata']['request_lb_ip'])	
	if k != s and (k not in temp_request_lb_ip):
		temp_request_lb_ip.append(k)
		s = k

#finding unique features for host
			
temp_host = []
s = ''

for i in range (0,1955):
	k = str(data[i]['metadata']['host'])	
	if k != s and (k not in temp_host):
		temp_host.append(k)
		s = k
'''
print (temp_request_path)
print (temp_host)
print (temp_request_lb_ip)
'''
#creating a new list with values of fields as indices of above unique values
labels = []
processed_data = []
for i in range (0,1955):
	labels.append(float(data[i]['metadata']['request_time']))
	processed_data.append( 
		[temp_request_path.index(str(data[i]['metadata']['request_path']))]
		+ [temp_request_lb_ip.index(str(data[i]['metadata']['request_lb_ip']))]
		+ [temp_host.index(str(data[i]['metadata']['host']))]
		)

#print (processed_data) 

#performing one hot encoding
#print (processed_data)

enc.fit(processed_data)
pre_processed_data = enc.transform(processed_data).toarray()  #TODO reshaping of data 

#print (enc.transform(processed_data[1]).toarray())  #example of encoded field
#print (pre_processed_data)