#Subscription Manager
import sys
import time
import json
from datetime import date, datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

class Sub:

    global subscriptions 
    subscriptions = {}

    class Add:

        def __init__(self, id, cost, frequency, starts_on, ends_on):
            self.id = id
            self.cost = cost
            self.frequency = frequency
            self.starts_on = starts_on
            self.ends_on = ends_on

        def record_subscription(self):
            subscriptions[id] = [cost,frequency,date.today(),ends_on]
            print(subscriptions)
            with open('subscriptions.json', 'w') as f:
                json.dump(subscriptions[id], f, default=str, indent=6)

    class Cancel:

        def __init__(self, id, ends_on):
            self.id = id
            self.ends_on = ends_on

        def cancel_subscription(self):
            del subscriptions[id]
            with open('subscriptions.json', 'w') as f:
                for element in json.load('subscriptions.json'): 
                    del element[id]

    def list(self):
        with open('subscriptions.json', 'r') as f:
            for element in json.load(f):
                # print(element)
                pass
                    



if __name__ == "__main__":
    #parser
    try:

        #ADD command
        if len(sys.argv) == 7:
            if "to" in sys.argv:                        
                id = sys.argv[2]
                cost = sys.argv[4].partition("/")[0]
                frequency = sys.argv[4].partition("/")[-1]
                if sys.argv[-1] in MONTHS:
                    if date.today().month > time.strptime(sys.argv[-1],'%B').tm_mon:
                        ends_on = (datetime(date.today().year+1, time.strptime(sys.argv[-1],'%B').tm_mon, date.today().day))
                    else:
                        ends_on = (datetime(date.today().year, time.strptime(sys.argv[-1],'%B').tm_mon, date.today().day))

                elif sys.argv[-1] in DAYS:
                    try:
                        ends_on = (datetime(date.today().year, date.today().month, time.strptime(sys.argv[-1],'%A').tm_wday))
                    except ValueError:
                        ends_on = (datetime(date.today().year, date.today().month, time.strptime(sys.argv[-1],'%A').tm_wday+7))


                new_command = Sub.Add(id, cost, frequency, date.today(), ends_on)
                new_command.record_subscription()
            
            else:
                print("Invalid input.")
                exit()

        #CANCEL command
        elif len(sys.argv) == 5:
            if "cancel" in sys.argv:
                if "on" in sys.argv: #look for a date
                    if sys.argv[-1] in MONTHS:
                        if date.today().month > time.strptime(sys.argv[-1],'%B').tm_mon:
                            ends_on = (datetime(date.today().year+1, time.strptime(sys.argv[-1],'%B').tm_mon, date.today().day))
                        else:
                            ends_on = (datetime(date.today().year, time.strptime(sys.argv[-1],'%B').tm_mon, date.today().day))
                    else:
                        if sys.argv[-1] in DAYS:
                            try:
                                ends_on = (datetime(date.today().year, date.today().month, time.strptime(sys.argv[-1],'%A').tm_wday))
                            except ValueError:
                                ends_on = (datetime(date.today().year, date.today().month, time.strptime(sys.argv[-1],'%A').tm_wday+7))
                        else:
                            print("Invalid input.")
                            exit()

                id = sys.argv[2]

                new_command = Sub.Cancel(id, ends_on)
                new_command.cancel_subscription()

        elif len(sys.argv) == 2:
            if sys.argv[1] == "list":

                new_command = Sub()
                new_command.list()

        else:

            #alternative cancel method
            if len(sys.argv) == 3:
                id = sys.argv[2] #id is third arg
                ends_on = None #cancel Today
                new_command = Sub.Cancel(id, ends_on)
                new_command.cancel_subscription()

            else:
                raise IndexError

    except IndexError:

        while True:
            prompt = input("sub> ").split(" ")

            #ADD command
            if len(prompt) == 6: #doesn't contain "sub" for running the program, it's already running.
                if "to" in prompt:        
                    id = prompt[1]
                    cost = prompt[3].partition("/")[0]
                    frequency = prompt[3].partition("/")[-1]

                if prompt[-1] in MONTHS:
                    if date.today().month > time.strptime(prompt[-1],'%B').tm_mon:
                        ends_on = (datetime(date.today().year+1, time.strptime(prompt[-1],'%B').tm_mon, date.today().day))
                    else:
                        ends_on = (datetime(date.today().year, time.strptime(prompt[-1],'%B').tm_mon, date.today().day))

                elif prompt[-1] in DAYS:
                    try:
                        ends_on = (datetime(date.today().year, date.today().month, time.strptime(prompt[-1],'%A').tm_wday))
                    except ValueError:
                        ends_on = (datetime(date.today().year, date.today().month, time.strptime(prompt[-1],'%A').tm_wday+7))

                new_command = Sub.Add(id, cost, frequency, date.today(), ends_on)
                new_command.record_subscription()

            #CANCEL command
            elif len(prompt) == 4:
                if "cancel" in prompt:
                    if "on" in prompt: #look for a date
                        if prompt[-1] in MONTHS:
                            if date.today().month > time.strptime(prompt[-1],'%B').tm_mon:
                                ends_on = (datetime(date.today().year+1, time.strptime(prompt[-1],'%B').tm_mon, date.today().day))
                            else:
                                ends_on = (datetime(date.today().year, time.strptime(prompt[-1],'%B').tm_mon, date.today().day))
                        else:
                            if prompt[-1] in DAYS:
                                try:
                                    ends_on = (datetime(date.today().year, date.today().month, time.strptime(prompt[-1],'%A').tm_wday))
                                except ValueError:
                                    ends_on = (datetime(date.today().year, date.today().month, time.strptime(prompt[-1],'%A').tm_wday+7))
                            else:
                                print("Invalid input.")
                                exit()

                    id = prompt[1]

                    new_command = Sub.Cancel(id, ends_on)
                    new_command.cancel_subscription()

            elif prompt[0] == "list":
                
                new_command = Sub()
                new_command.list()

            else:

                #alternative cancel method
                if len(prompt) == 2:
                    id = prompt[1] #id is second arg
                    ends_on = None
                    new_command = Sub.Cancel(id, ends_on)
                    new_command.cancel_subscription()
                    
                else:
                    print("Invalid input.")
                    exit(2)


    #BUG: ends_on contains time instead of just date.
    #BUG: json.dump() doesn't work.
    #TODO: Check for next weekly and daily frequency
    #TODO: Check for lifetime or free subscriptions (haven't decided yet)