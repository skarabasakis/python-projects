#Subscription Manager
import sys
import time
import json
from datetime import date, datetime

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
MONTHS = [month[:3] for month in MONTHS] + MONTHS + [ int(a) for a in range(1, len(MONTHS) + 1)]

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
DAYS = [day[:3] for day in DAYS] + DAYS + [ int(a) for a in range(1, len(DAYS) + 1)]

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
            # print(subscriptions)
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

class List:

    def __init__(self): pass

    def execute(self):
        with open('subscriptions.json', 'r') as f:
            for element in json.load(f):
                # print(element)
                pass
                



if __name__ == "__main__":
    #parser

        #ADD command
        if len(sys.argv) == 7:
            if "to" in sys.argv:                        
                id = sys.argv[2]
                cost = sys.argv[4].partition("/")[0]
                frequency = sys.argv[4].partition("/")[-1] if sys.argv[4].partition("/")[-1][-1] in ['w', 'm', 'd', 'y'] else None
                if frequency == None:
                    print(sys.argv[4].partition("/")[-1] + ": Invalid frequency input.\nTry 'm', 'd', 'y' or 'w'.")
                    exit()
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

                new_command = List()
                new_command.execute()

        else:

            #alternative cancel method
            if len(sys.argv) == 3:
                id = sys.argv[2] #id is third arg
                ends_on = None #cancel Today
                new_command = Sub.Cancel(id, ends_on)
                new_command.cancel_subscription()

            else:
                # raise IndexError this should be an error/usage message
                pass


    #BUG: ends_on contains time instead of just date.
    #BUG: json.dump() doesn't work.
    #TODO: Check for lifetime or free subscriptions (haven't decided yet).
    #TODO: Tomorrow, next week, next month, next year should work with Add and Cancel.