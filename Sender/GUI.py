from dearpygui import core,simple
from Sender import Sender
from XSSFilterBypass.PayloadCrafter import PayloadCrafter

class SenderGUI: 
    def __init__(self):
        with simple.window("Sender"):
            core.add_text("Welcome to the payload injector.")
            core.add_input_text("Select a target", source="target")
            core.add_input_text("Set data", source="data")
            core.add_input_text("Set vulnerable field", source="field")
            core.add_input_text("Set payload", source="payload")            
            
            core.add_button("Select payload", callback=self.listPayloads)
            
            core.add_button("Send", callback=self.send)
    
    def listPayloads(self, *args):
        pc = PayloadCrafter()
        payloads = pc.get_payloads()
        with simple.window("Select a payload"):
            core.add_table("Payloads", ["Payloads"])
            for payload in payloads:
                core.add_row("Payloads", [payload])
            
    def send(self, *args):
        target = core.get_value('target')
        data = core.get_value('data')
        field = core.get_value('field')
        payload = core.get_value('payload')
        
        sender = Sender(url=target, data=data, field=field)
        sender.send(payload)
        