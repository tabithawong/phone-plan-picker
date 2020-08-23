#a test program that helps users find a phone plan that suits them, so far no prepaid services
#improvements to make: fix errors on mb/gb function, make an option to go to the previous question if you make a mistake or an easy way to restart program
#made on July 6, 2020
#Tabitha Wong

#creating the "Plan" class
class Plan:
    def __init__(self, carrier, cost, data, minutes, text):
        self.carrier = carrier
        self.cost = cost
        self.data = data
        self.minute = minutes
        self.text = text

    def printplan(self):
        print("")
        print("SUMMARY OF PLAN:")
        print("Carrier: "+ self.carrier)
        #finish this
        
plan1 = Plan("Public", 13, "250 MB", 100, "unlimited")

#function that retrieves information from user
def getinfo():
    global b,pc,d,af,i,j,q,TelusList,RogersList,BellList,found,dstring,e,vstring,vnum,vin,FreedomList,end
    placeholders()
    getbudget()
    if end == False:
        getcarrier()
        if end == False:
            getdata()
            if end == False:
                getcalls()
    
#makes placeholder values
def placeholders():
    global TelusList,RogersList,BellList,pc,d,i,j,q,found,dstring,FreedomList,k,end
    i = 0
    j = 0
    q = 0
    k = 0
    dstring = ""
    pc = ""
    d = False
    found = False
    end = False
    TelusList = ["Telus", "telus", "TELUS", "Koodo", "Koodo Mobile", "KOODO MOBILE", "koodo mobile", "KOODO", "koodo", "Public", "PUBLIC", "public", "Public Mobile", "PM", "pm", "public mobile", "PUBLIC MOBILE","Pm"]
    RogersList = ["Rogers", "rogers", "ROGERS", "Chatr", "Chatr Mobile", "CHATR MOBILE", "chatr mobile", "CHATR", "chatr", "FIDO", "FIDO MOBILE", "Fido Mobile", "fido mobile", "Fido", "fido"]
    BellList = ["Bell", "bell", "BELL", "Virgin", "virgin", "VIRGIN", "virgin mobile", "Virgin Mobile", "VIRGIN MOBILE", "lucky", "LUCKY","Lucky", "Lucky Mobile", "lucky mobile", "LUCKY MOBILE", "lm", "LM"]
    FreedomList = ["Freedom", "FREEDOM", "freedom", "Freedom Mobile", "FREEDOM MOBILE", "freedom mobile"]
    
#getting user's budget
def getbudget():
    global b
    b = int(input("What is your budget (tax excluded)? $"))

#probing for preferred carrier
def getcarrier():
    global c,pc,i,j,q,k,end
    #probing for preferred carrier
    c = input("Do you have a preferred carrier? If so, type it in. If not, type in no or hit the enter key: ")
    #assigning user's input of preferred carrier
    if c == "" or c == "no" or  c == "NO" or c == "No":
        pc = "none"
    #attempting to match user-inputted carrier with carriers in arrays
    else:
        checklists()

#probing for data needs
def getdata():
    global din, d, a, af, dstring,end
    din = input("Do you need data in your plan? Please only type yes or no: ")
    #user needs data
    if din == "yes" or din == "YES" or din == "Yes":
        a = input("How much data do you need? Please enter please type in GB and MB next to your answer (eg. 1.45 GB or 250 MB). If you need unlimited data, Type in the word unlimited: ")
        getdataamt()
    elif din == "no" or din == "NO" or din == "No":
        dstring = "None"
    #user unknown
    else:
        print("Sorry, you can only answer with yes or no. Please run the program again. ")
        end = True
        return
        
#dealing with the amount of data the user needs
def getdataamt():
    global a, af, dstring,xstring
    if a == "unlimited":
        dstring = "Unlimited"
    else:
        convertdataamt(a)
        if xstring[1] == "gb" or xstring[1] == "Gb":
            dstring = xstring[0]+" GB"
        elif xstring[1] == "mb" or xstring[1] == "Mb":
            dstring = xstring[0]+" MB"
        print(af)

#converts user-inputted data amount as GB or MB
def convertdataamt(x):
    global af, xstring, dstring
    xstring = x.split(" ")
    if xstring[1] == "GB" or xstring[1] == "gb" or xstring[1] == "Gb":
        af = float(xstring[0])*1024
    elif xstring[1] == "MB" or xstring[1] == "mb" or xstring[1] == "Mb":
        af = float(xstring[0])

#checks carrier lists
def checklists():
    global pc,i,q,j,c,found,RogersList,TelusList,BellList,FreedomList,k,end
    while (i < len(TelusList)):
        if c == TelusList[i]:
            pc = TelusList[0]
            found = True
            break
        i+=1
    if (found == False):
        while (j < len(RogersList)):
            if c == RogersList[j]:
                pc = RogersList[0]
                found = True
                break
            j+=1
    if (found == False):
        while (k < len(FreedomList)):
            if c == FreedomList[k]:
                pc = FreedomList[0]
                found = True
                break
            k+=1
    if (found == False):
        while (q < len(BellList)):
            if c == BellList[q]:
                pc = BellList[0]
                found = True
                break
            q+=1
        if q == len(BellList):
            print("Sorry, we were unable to recognize this carrier. Please run the program again. ")
            end = True
            return

#probing for user's voice call needs part 1
#rework this so it follows the same format as unlimited data
def getcalls():
    global m, vstring,vnum,end
    m = input("Do you need voice call minutes? Please only type yes or no: ")
    if m == "yes" or m == "YES" or m == "Yes":
        getcallamt()
    elif m == "no" or m == "NO" or m == "No":
        #default to data only plans
        vnum = 0
        vstring = "None"
    else:
        print("Sorry, you can only answer with yes or no. Please run the program again. ")
        end = True
        return

#probing for user's voice call needs part 2
def getcallamt():
    global e,vstring,vnum, m
    e = input("How many minutes do you need? If you need unlimited minutes, type in the word unlimited: ")
    if e == "unlimited" or e == "Unlimited" or e == "UNLIMITED":
        vstring = "Unlimited"
    else:
        vnum = int(e)
        vstring = str(e) + " minutes"
        
#prints a summary of info collected from user
def printinfo():
    global vstring, dstring, pc, b
    print("")
    print("SUMMARY OF INFO:")
    print("Budget: $" + str(b))
    print("Preferred Carrier: " + pc)
    print("Data Needed: " + dstring)
    print("Minutes Needed: " + vstring)
    print("All plans will include unlimited texting as long as they include calling minutes.")
    
    
#run program
def runprogram():
    getinfo()
    if end == False:
        printinfo()

runprogram()
     
