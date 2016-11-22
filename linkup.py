import requests

class FailedResponse:
    """
    A class that defines a response to be returned
    in case there is an error in transmitting the
    request.

    The status code for this kind of response is None
    so a check for it can tell whether the request
    was submitted or not
    """
    def __init__(self , status , text):
        self.status_code = status
        self.text = text
        
        
class LinkupSMS:
    """
    Wrapper class that calls the LinkUp SMS api to send
    sms text messages
    """
    def __init__(self , username , client_id , client_key):
        self.username   = username.upper()
        self.client_id  = client_id
        self.client_key = client_key
        self.opt = 'sendSMS'

    def send_message(self , source , number , message):
        url = "https://purgren.com/linkup/api/sendsms.php"

        data = { 'From': source,
                 'To' : number,
                 'Message' : message,
                 'Username' : self.username,
                 'ClientId' : self.client_id,
                 'ClientKey' : self.client_key,
                 'opt' : self.opt
               }

        try:
            response = requests.post(url , data)
            return response
        except:
            return FailedResponse(None , "Error sending message")
        



