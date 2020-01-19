import requests
import time
import sys
import threading
import random 
import names
from random_username.generate import generate_username
import omlet_bot
from threading import Thread



######################
### SELENOID SERVERS :->
servers=[
"35.245.123.216",
"104.196.232.76",

"35.227.177.187", ### NOT WORKING
"34.94.145.176", ### NOT WORKING
"34.73.218.30", ### NOT WORKING
"35.245.216.139", ### NOT WORKING

"35.245.213.142",
"35.231.44.169",
"35.202.142.197",

"35.196.231.162",
"34.83.203.177",

# "35.230.6.83", ### NOT WORKING
]
#########################
thread_count= len(servers)

# thread_count = 4

like_="https://omlet.gg/photo/eyJhIjoiT1NPVDAwNFBUNkRBMUxWSkVQTzYiLCJpZCI6IlhobGJrWUpvWU0yUVZCRlkiLCJ0IjoiU2NyZWVuU2hvdCJ9"
report_="https://omlet.gg/video/eyJhIjoiUU1FVEJXSVFHWENaVVhOQ1BYSFciLCJpZCI6IlhnL2pjVW9nY0lMdnkwcGUiLCJ0IjoiVmlkZW8ifQ"
follow_="https://omlet.gg/profile/attila11"
watch_="https://omlet.gg/stream/bigdaddy_4123"

def Gen():
    # fake = generate_username(1)
    # fake = fake[0]
    fake = names.get_last_name().lower()
    return fake



def Register_Bot(ip):
    link=watch_
    ip = ip
    name=Gen()
    bonus = Gen()
    name = name + bonus
    name = name + random.choice(["_", "_g", "3", ".o", "_4"])
    bonus = name + "_a" + random.choice(["__", ".gg", "123", "_pro", "_123"])
    try:
        
        a = omlet_bot.Bot('NO_LOGIN',"bugmenot",bonus,ip,link)
        
        # a.Browser_Register()
        
        a.Browser_Start()
        
        # a.Browser_Login()
        # a.Browser_Like()
        time.sleep(10)
        # a.driver.get(report_)
        # a.Browser_Report_Post()
        # time.sleep(2)
        # a.driver.get(follow_)
        # a.Browser_Follow()
        # time.sleep(2)
        # a.driver.get(watch_)
        a.Browser_Watch()
        # a.Browser_Quit()
        # a.Browser_NoLoginWatch()
        
    except:
        print("Session Failed/Ended")
        pass
    while True:
        try:
            name=Gen()
            bonus = Gen()
            name = name + bonus
            name = name + random.choice(["_", "_g", "3", ".o", "_4"])
            bonus = name + "_a" + random.choice(["__", ".gg", "123", "_pro", "_123"])
            a = omlet_bot.Bot('NO_LOGIN',"bugmenot",bonus,ip,link)
            # a.Browser_Register()
            a.Browser_Start()
            # a.Browser_Login()
            # a.Browser_Like()
            time.sleep(10)
            # a.driver.get(report_)
            # a.Browser_Report_Post()
            # time.sleep(2)
            # a.driver.get(follow_)
            # a.Browser_Follow()
            # time.sleep(2)
            # a.driver.get(watch_)
            a.Browser_Watch()
            # a.Browser_Quit()
            # a.Browser_NoLoginWatch()
        except:
            print("Session Failed/Ended")
            pass

def Start(ip):
    threads_ = []
    for i in range(0,5):
        threads_.append(Thread(target=Register_Bot,args=(ip,)))
    for thread in threads_:
        time.sleep(2)
        thread.start()
    '''
    ip = ip
    t0 = threading.Thread(target=Register_Bot, args=(ip,))
    time.sleep(1)
    t1 = threading.Thread(target=Register_Bot, args=(ip,))
    time.sleep(1)
    t2 = threading.Thread(target=Register_Bot, args=(ip,))
    time.sleep(1)
    t3 = threading.Thread(target=Register_Bot, args=(ip,))
    time.sleep(1)
    t4 = threading.Thread(target=Register_Bot, args=(ip,))
    time.sleep(1)

    t0.start()
    time.sleep(1)
    t1.start()
    time.sleep(1)
    t2.start()
    time.sleep(1)
    t3.start()
    time.sleep(1)
    t4.start()

    t0.join()
    time.sleep(1)
    t1.join()
    time.sleep(1)
    t2.join()
    time.sleep(1)
    t3.join()
    time.sleep(1)
    t4.join()
    '''



threads = []
for i in range(0,thread_count):
    threads.append(Thread(target=Start,args=(servers[i],)))
for thread in threads:
    time.sleep(2)
    thread.start()

# data=generate_username(60)
'''
t0 = threading.Thread(target=Start, args=([data[0],data[1],data[2],data[3],data[4]],"35.245.123.216",))
time.sleep(1)
t1 = threading.Thread(target=Start, args=([data[5],data[6],data[7],data[8],data[9]],"104.196.232.76",))
time.sleep(1)
t2 = threading.Thread(target=Start, args=([data[10],data[11],data[12],data[13],data[14]],"35.227.177.187",))
time.sleep(1)
t3 = threading.Thread(target=Start, args=([data[15],data[16],data[17],data[18],data[19]],"34.94.145.176",))
time.sleep(1)
t4 = threading.Thread(target=Start, args=([data[20],data[21],data[22],data[23],data[24]],"34.73.218.30",)) 
time.sleep(1)
t5 = threading.Thread(target=Start, args=([data[25],data[26],data[27],data[28],data[29]],"35.245.216.139",)) 
time.sleep(1)
t6 = threading.Thread(target=Start, args=([data[30],data[31],data[32],data[33],data[34]],"35.245.213.142",)) 
time.sleep(1)
t7 = threading.Thread(target=Start, args=([data[35],data[36],data[37],data[38],data[39]],"35.231.44.169",)) 
time.sleep(1)
t8 = threading.Thread(target=Start, args=([data[40],data[41],data[42],data[43],data[44]],"35.202.142.197",)) 
time.sleep(1)
t9 = threading.Thread(target=Start, args=([data[45],data[46],data[47],data[48],data[49]],"35.230.6.83",)) 
time.sleep(1)
t10 = threading.Thread(target=Start, args=([data[50],data[51],data[52],data[53],data[54]],"35.196.231.162",)) 
time.sleep(1)
t11 = threading.Thread(target=Start, args=([data[55],data[56],data[57],data[58],data[59]],"34.83.203.177",)) 
time.sleep(1)


t0.start()
time.sleep(1)
t1.start()
time.sleep(1)
t2.start()
time.sleep(1)
t3.start()
time.sleep(1)
t4.start()
time.sleep(1)
t5.start()
time.sleep(1)
t6.start()
time.sleep(1)
t7.start()
time.sleep(1)
t8.start()
time.sleep(1)
t9.start()
time.sleep(1)
t10.start()
time.sleep(1)
t11.start()
time.sleep(1)

t0.join()
time.sleep(0.5)
t1.join()
time.sleep(0.5)
t2.join()
time.sleep(0.5)
t3.join()
time.sleep(0.5)
t4.join()
time.sleep(0.5)
t5.join()
time.sleep(0.5)
t6.join()
time.sleep(0.5)
t7.join()
time.sleep(0.5)
t8.join()
time.sleep(1)
t9.join()
time.sleep(1)
t10.join()
time.sleep(1)
t11.join()
'''