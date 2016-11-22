from linkup import *

sms = LinkupSMS('larrygh' , 'venlgwymfz' , 'ldnjfwprgs')
response = sms.send_message('PYTHON' , '0540792532' , 'I love Python') 
print response.text
print response.status_code
