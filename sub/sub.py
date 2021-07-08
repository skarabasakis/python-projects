#Subscription Manager
import dateparser #make sure to install this module with "pip install dateparser"
import sys
import time
from datetime import date, datetime

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
            

if __name__ == "__main__":
    #parser
    try:

        #ADD command
        if len(sys.argv) == 7:
            if "to" in sys.argv:                        
                id = sys.argv[2]
                cost = sys.argv[4].partition("/")[0]
                frequency = sys.argv[4].partition("/")[-1]
                if date.today().month > time.strptime(sys.argv[-1],'%B').tm_mon:
                    ends_on = (datetime(date.today().year+1, time.strptime(sys.argv[-1],'%B').tm_mon, date.today().day))
                else:
                    ends_on = (datetime(date.today().year, time.strptime(sys.argv[-1],'%B').tm_mon, date.today().day))

                new_command = Sub.Add(id, cost, frequency, date.today(), ends_on)
                new_command.record_subscription()
            
            else:
                print("Invalid input.")
                exit()
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
                    if date.today().month > time.strptime(prompt[-1],'%B').tm_mon:
                        ends_on = (datetime(date.today().year+1, time.strptime(prompt[-1],'%B').tm_mon, date.today().day))
                    else:
                        ends_on = (datetime(date.today().year, time.strptime(prompt[-1],'%B').tm_mon, date.today().day))
            
                new_command = Sub.Add(id, cost, frequency, date.today(), ends_on)
                new_command.record_subscription()
            
            else:
                print("Invalid input.")
                exit()

    #BUG: ends_on contains time instead of just date.
    #TODO: save subscriptions in a text file instead of a dictionary.