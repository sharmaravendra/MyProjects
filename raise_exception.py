class Accident(Exception):
    def __init__(self,msg):
        self.msg= msg
    # def print_exception(self):
    #     print("User Defined Exception",self.msg)
    def handle(self):
        print("Acciende occured, please take detour")
try:
    raise Accident("Crash b/w two cars")
except Accident as e:
    # e.print_exception()
    e.handle()