

class Smartphone:
  
    # construct a new Smartphone
    def __init__(self, capacity, name):

        #attributes
        self.capacity = capacity
        self.space = 0

        #name = input("Smartphone name: ")
        self.name = name

        #keep track of all apps
        self.apps = {}
       
 
    # add a new app
    def add_app(self, appname, appsize):
        #appname = input("App name to add: ")
        #appsize = int(input("App size in GB: "))
        if int(self.space) + int(appsize)  <= int(self.capacity):
            self.apps[appname] = appsize
            self.space = sum(self.apps.values())
            return self.apps
        else:
            print("Cannot install app, no available space")
            return self.apps
  
    # removes an app from the phone
    def remove_app(self, appname):
        if appname in self.apps:
            self.apps.pop(appname)
            self.space = sum(self.apps.values())
            return self.apps
            
        if appname not in self.apps:
            print("Invalid demand. App does not exist")

        
        print(self.apps)
    # checks to see if an app is installed based on appname (string)
    # returns True if the app is installed, False if it is not
    def has_app(self, appname):
        if appname in self.apps.keys():
            return True
        if appname not in self.apps.keys():
            return False
  
    # returns the current space available on the phone (integer)
    def get_available_space(self):
        available = int(self.capacity)-self.space
        return available 
  
    # prints a detailed report that describes the following: name, space capacity, apps
    def report(self):
        print("Name: ", self.name+"'s Iphone")
        print("Capacity: ", self.space, "out of", self.capacity, "GB")
        print("Available Space: ", self.get_available_space())
        print("Apps installed: ", len(self.apps))
        for x,y in self.apps.items():
            print("* ",x, "is using",y, "GB")
        print()
        return




#ask user for size of phone
capacity = int(input("Size of your new smartphone (32, 64 or 128 GB): "))
#validate GB choice
while capacity != 32 and capacity != 64 and capacity != 128:
    print("Invalid choice")
    capacity = int(input("Size of your new smartphone (32, 64 or 128 GB): "))
name = input("Smartphone name: ")
phone = Smartphone(capacity, name)
phone.report()


#user's choice in features
f = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")

#validate menu choice 
while f.lower() != "q" and f.lower() != "r" and f.lower() != "a" and f.lower() != "e":
    print("Invalid Choice")
    f = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")


while f.lower() != "q":
    #report
    if f.lower() == "r":
        phone.report()
        print()
        f = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")



    #add app
    if f.lower() == "a":
        appname = input("App name to add: ")
        appsize = int(input("App size in GB: "))
        phone.add_app(appname, appsize)
        print()
        f = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")
  

    #remove app
    if f.lower() == "e":
        appname = input("App name to remove: ")
        print("App removed: ", appname)
        phone.remove_app(appname)
        print()
        f = input("(r)eport, (a)dd app, r(e)move app or (q)uit: ")



# quit
if f.lower() == "q":
    print("Bye")









