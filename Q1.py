from time import *
import random as r


def mistake(text,user_text):
    error=0
    for i in range(len(text)):
        try:
            if text[i] != user_text[i]:
                error = error+1
        except:
            error=error+1
    return error                


def speed_time(time_s,time_e,userinput):
    time_delay =time_e-time_s
    time_R=round(time_delay,2)
    speed=len(userinput)/time_R
    return round(speed)


test=["OM NAMAH PARVATI PATEY HAR HAR MAHADEV","OM SHREE SHIVAY NAMASTOBHYAM","OM HUM JUM SAH OM BHUR BHUVAH SWAHA OM TRAYAMBAKAM YAJAMAHE SUGANDHIM PUSHTIVARDHANAM URVA RUKMIVA BANDHANAN MRITYOR MOKSHIYAMRITAT OM HUM JUM SAH OM BHUR BUHAVAH SWAHA","OM BHUR BHUVAH SWAHA TAT SAVITUR VARENYAM BHARGODEVASYADHIMAHI DHIYO YONAH PRACHODAYAT"]


test1 = r.choice(test)
print("TYPING SPEED")
print(test1)
print()
print()
time_before=time()
testinput=input("ENTER text : ")
time_after=time()

print("speed:", speed_time(time_before,time_after,testinput),"w/sec")
print("error: ",mistake(test1,testinput))
print("dhanyawad!!")