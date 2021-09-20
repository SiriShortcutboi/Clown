#Holden Anderson
#Alarm Clock
#9-21

#imports
import winsound
import time

#timezones

MIT = -11
HST = -10
AST = -9
PST = -8
MST = -7
CST = -6
EST =-5
PRT = -4
CNT = -3
CAT =-2
GMT = 0
ECT = 1
EET = 2
ART = 3
NET = 4
PLT = 5
BST = 6
VST = 7
CTT = 8
CST = 9
aet =10
sst = 11
nst = 12
dls = 1





#defining  variables
def gmtimenow(timeZone,dls):
    seconds = Calendar.timegm(time.gmtime)
    current_second = seconds%60
    minutes = seconds//60
    current_min = minutes % 60
    hours = minutes // 60
    current_hour = hours % 24
    #set time zone
    if current_hour>=12:
        tag = " PM"
    else:
        tag = " AM"
    if current_hour > 12:
        current_hour -= 12
    print(str(current_hour)+":"+str(current_min)+":"+str(current_second)+tag)
    
                             


while True:
    gmtimenow(MST,dls)
littlesleep = time.sleep(0.3)
soundlowD = winsound.Beep(77,500)
soundlowA = winsound.Beep(116,500)
soundhighlowA = winsound.Beep(233,500)

###winsound.Beep(750,2000)
##winsound.Beep(155,500)
###littlesleep
##winsound.Beep(155,500)
##winsound.Beep(233,500)
##winsound.Beep(233,1000)

def funny():
    soundlowD
    soundlowD
    soundlowA
    

    
