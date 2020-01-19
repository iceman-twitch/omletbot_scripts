import time
import requests
import random 
import string
import re

import sys
import os, platform

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from random_user_agent.user_agent import UserAgent
from random_user_agent.params import SoftwareName, OperatingSystem

capabilities = {
    "browserName": "chrome",
    "version": "78.0",
    "enableVNC": True,
    "enableVideo": False
}

def randomStringDigits(stringLength=6):
    """Generate a random string of letters and digits """
    lettersAndDigits = string.ascii_letters + string.digits
    return str(''.join(random.choice(lettersAndDigits) for i in range(stringLength)))

def check_proxy(proxy):
    code=404
    try:
        proxydict = {
            'http': proxy
        }
        r =requests.get("https://idp.omlet.me/auth",proxies=proxydict)
        
        # print(r.status_code)
        code=r.status_code
    except Exception as e:
        print("ERROR:" + str(e))
    return code

def get_proxy():
    cwd = os.path.dirname(os.path.realpath(__file__))
    with open( cwd + "\proxy4777.txt" ) as file_in:
        lines = []
        for line in file_in:
            lines.append(line)
    
        
    return lines[random.randint(0,len(lines)-2)]

# print(get_proxy())

class Bot:
    def __init__( self, a, b, c, d,l ):
        self.a = a
        self.b = randomStringDigits(12)
        self.d = c
        self.host = d
        self.s=requests.Session()
        #self.s=requests.Session()
        self.success=False
        self.driver=0
        self.private=False
        self.stream=l
        self.proxy=get_proxy()
        self.like="https://omlet.gg/photo/eyJhIjoiWlY4VUtMTVZFVVFYSVRVUTJNMU8iLCJpZCI6IlhndVJacVgrNlpEeFFNOTUiLCJ0IjoiU2NyZWVuU2hvdCJ9"
        software_names = [SoftwareName.CHROME.value]
        operating_systems = [OperatingSystem.WINDOWS.value, OperatingSystem.LINUX.value]   

        self.user_agent_rotator = UserAgent(software_names=software_names, operating_systems=operating_systems, limit=100)
        self.user_agent = self.user_agent_rotator.get_random_user_agent()
    def get_id( self, get_url ):
        url = get_url
        cut1 = url
        cut2=cut1.split('k=')
        cut3=cut2[1].split('&')
        return cut3[0]
    def Browser_Quit( self ):
        time.sleep(3)
        self.driver.close()
        exit()

    def Browser_Register( self ):
        tries = 0
        self.error= 404
        while self.error == 404:
            
            self.proxy=get_proxy()
            self.error=check_proxy(self.proxy)
            tries=tries+1
            if tries>100:
                print("No Good Proxy")
                exit()
        data= {
            "cpass": self.b,
            "email": "",
            "omid": self.a,
            "pass": self.b
        }
        proxydict = {
            'http': self.proxy
        }
        url = self.s.get("https://idp.omlet.me/auth")

        url = url.url
        r = self.s.post(url,data=data,proxies=proxydict)
        
        print( "SIGNED UP ( "+ self.a +" )")

    def Browser_Chat( self ):
        ## text area codes
        xpath1 = '//*[@id="root"]/div/div[3]/div/div[2]/div/div/div[2]/textarea'
        xpath2= '/html/body/div/div/div[3]/div/div[2]/div/div/div[2]/textarea'
        classname='textarea__chat__Wz1nT'
        chat = random.choice(["Min tolod??"," ","háj", " ","heo","szijja","Mizujs? helló"," "," "," ","Olah"," ", "helló", "Csá", "Cső"," ", "Csumi", "Hi All", "Csatizhatok?", "Jöhetek?"])
        time.sleep(2)
        try:
            value = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, classname)))  
            value.clear()
            time.sleep(1)
            value.send_keys(chat)
            time.sleep(1)
            value.send_keys(Keys.RETURN)

        except:
            try:
                value = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath1)))
                value.clear()
                time.sleep(1)
                value.send_keys(chat)
                time.sleep(1)
                value.send_keys(Keys.RETURN)
            except:
                try:
                    value = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, xpath2)))
                    value.clear()
                    time.sleep(1)
                    value.send_keys(chat)
                    time.sleep(1)
                    value.send_keys(Keys.RETURN)
                except:
                    print("CHATTING FAILED")
    def Browser_NoLoginWatch( self ):
        time.sleep(5)
        # self.driver.execute_script("window.open('"+ "https://127.0.0.1"+"', '_blank');") 
        # time.sleep(3)
        # windows = self.driver.window_handles

        # time.sleep(2)
        # self.driver.switch_to.window(windows[1])
        # time.sleep(2)
        
        i=0
        while True:
            i=i+1
            if i==5000:
                print("WATCH STREAM ( "+ "NO LOGIN" +" )")
                time.sleep(4)
                
                # windows = self.driver.window_handles
                # self.driver.switch_to.window(windows[1])
                # self.driver.refresh()
                
                # windows = self.driver.window_handles
                # self.driver.switch_to.window(windows[0])
                i=0

    def Browser_StartHeadless( self ):
        chrome_options = Options()
        # chrome_options.add_argument(f'--proxy-server={self.proxy}')
        chrome_options.add_argument("--headless") 
        self.driver = webdriver.Remote(
            command_executor="http://"+ self.host +":4444/wd/hub",
            desired_capabilities=capabilities,
            options=chrome_options
            )
        
        self.driver.implicitly_wait(55)
        self.driver.set_page_load_timeout(55)
        self.driver.get(self.stream)
    def Browser_StartHeadless_Local( self ):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        if platform.system() == 'Windows':
            chromepath = BASE_DIR + r'\chromedriver.exe'
            chromepath = chromepath.replace("\\","/")
        # print("1")
        options = Options()
        # print("2")
        # options.add_argument(f'proxy-server={ self.proxy }')
        # print("3")
        options.add_argument('--headless')
        # print("4")
        options.add_argument('--disable-gpu')
        # print("5")
        options.add_argument('--lang=en')
        options.add_argument("user-agent="+self.user_agent+"")
        # print("6")
        # self.driver = webdriver.Remote(
        #     command_executor="http://"+ self.host +":4444/wd/hub",
        #     desired_capabilities=capabilities,
        #     chrome_options=options
        #     )
        self.driver = webdriver.Chrome(executable_path=chromepath, options=options)
        # print("7")
        self.driver.implicitly_wait(55)
        # print("8")
        self.driver.set_page_load_timeout(55)
        # print("9")
        self.driver.get(self.stream)
        print("BROWSER STARTED")

    def Browser_Start( self ):
        chrome_options = Options()
        # options.add_argument(f'--proxy-server={self.proxy}')
        chrome_options.add_argument("user-agent="+self.user_agent+"")
        self.driver = webdriver.Remote(
            command_executor="http://"+ self.host +":4444/wd/hub",
            desired_capabilities=capabilities,
            options=chrome_options
            )
        
        self.driver.implicitly_wait(55)
        self.driver.set_page_load_timeout(55)
        self.driver.get(self.stream)
        print("BROWSER STARTED")
    def Browser_Start_Local( self ):
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        if platform.system() == 'Windows':
            chromepath = BASE_DIR + r'\chromedriver.exe'
            chromepath = chromepath.replace("\\","/")
        options = Options()
        options.add_argument(f'--proxy-server={self.proxy}')
        options.add_argument("user-agent="+self.user_agent+"")
        self.driver = webdriver.Chrome(executable_path=chromepath, 
        # options=options
        )
        
        self.driver.implicitly_wait(55)
        self.driver.set_page_load_timeout(55)
        self.driver.get(self.stream)
    def Browser_Login( self ):
        

        
        time.sleep(5)
        #WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='omlet-bar']/div[2]/div[2]")
        #centre = self.driver.find_element_by_xpath("//*[@id='omlet-bar']/div[2]/div[2]")
        #hover = ActionChains(self.driver).move_to_element(centre)
        #hover.perform()
        #centre.click()
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[1]/div/div[2]/div[2]"))).click()

        time.sleep(5)
        
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/a/button"))).click()
        
        self.driver.execute_script(f'var element = document.getElementById("omid"); element.value = "{self.a}";')
        
        if self.private == True:
            self.driver.execute_script(f'var element = document.getElementById("omid"); element.value = "{self.d}";')
        self.driver.execute_script(f'var element = document.getElementById("pass"); element.value = "{self.b}";')
        
        time.sleep(2)
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/form/button"))).click()
        # login = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/button")
        # login = self.driver.find_element_by_xpath("/html/body/div/div[2]/form/button")
        # login.click()
        time.sleep(5)
        if self.driver.current_url==self.stream:
            print("SIGNED IN: ( "+ self.a + " )")
        else:
            print("FAILED TO SIGNED IN: ( "+ self.a + " )")
            time.sleep(2)
            self.Browser_Quit()
            return
        
        # self.Browser_Watch()

    def Browser_Report_Post( self ):
        # self.driver.get("https://omlet.gg/video/eyJhIjoiUU1FVEJXSVFHWENaVVhOQ1BYSFciLCJpZCI6IlhnL2pjVW9nY0lMdnkwcGUiLCJ0IjoiVmlkZW8ifQ")

        time.sleep(5)
        try:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[3]/div/div[1]/div[2]/div[1]/div[3]"))).click()
        except:
            WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div[2]/div[1]/div[3]"))).click()
        time.sleep(3)
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='menu_report_post']"))).click()
        except:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/div/div/div/div"))).click()
        time.sleep(1)
        self.check_report = False
        try:
            WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='root']/div/div[3]/div/div[1]/div[2]/div[1]/span/div/div/div/div[3]/span[2]/div"))).click()
            #WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[1]/span/div/div/div/div[3]/span[3]/div'))).click()
            self.check_report = True
        except:
            self.check_report = False
            try:
                WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[1]/div[2]/div[1]/span/div/div/div/div[3]/span[2]/div"))).click()
                #WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div/div[3]/div/div[1]/div[2]/div[1]/span/div/div/div/div[3]/span[3]/div'))).click()
                self.check_report = True
            except:
                self.check_report= False
        
        
        # #root > div > div.page-container > div > div.left-col > div.content-wrapper.post-container > div.post-user-info-bar > span > div > div > div > div.ask-options-options > span:nth-child(2) > div
        # document.querySelector("#root > div > div.page-container > div > div.left-col > div.content-wrapper.post-container > div.post-user-info-bar > span > div > div > div > div.ask-options-options > span:nth-child(2) > div")
        
        if self.check_report:
            print("FINISHED REPORT ( "+ self.a +" )")
        else:
            print("FAILED TO REPORT ( "+ self.a +" )")
        time.sleep(1)
        # self.Browser_Quit()
    def Browser_Follow( self ):
        # self.driver.get("https://omlet.gg/profile/bigdaddy_4123")
        time.sleep(3)
        followed=False
        try:
            follow = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="user-profile"]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]')))
            follow.click()
            followed=True

        except:
            followed=False

            try:
                follow = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div[2]/div[1]")))
                follow.click()
                followed=True
            except:
                followed=False

        if followed:
            print("PROFILE FOLLOWED ( "+ self.a +" )")
        else:
            print("FAILED TO FOLLOW ( "+ self.a +" )")
        time.sleep(2)
        # self.Browser_Quit()
    def Browser_Like( self ):

        # check = self.driver.find_element_by_xpath('//*[@id="omlet-bar"]/div[2]/div[5]')        
        # self.driver.get(self.like)
        time.sleep(3)
        # try:
        #     element = WebDriverWait(self.driver, 10).until(
        #         EC.presence_of_element_located((By.ID, "myDynamicElement"))
        #     )
            
        # finally:
        #     print("Failed to Like")
        # like = self.driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[6]/div[2]/div[1]')
        # like.click()

        class_name1="like-action"
        class_name2="omlet-white-heart"
        classs_name3="like-description "
        classs_name4="like-description"
        classnames=[class_name1,class_name2,classs_name3,classs_name4]
        
        xpath1 = '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[5]/div[2]/div[1]'
        xpath2 = '/html/body/div/div/div[3]/div/div[1]/div[2]/div[5]/div[2]/div[1]'

        xpath3 = '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[5]/div[2]/div[1]/div'
        xpath4 = '/html/body/div/div/div[3]/div/div[1]/div[2]/div[5]/div[2]/div[1]/div'

        xpath5 = '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[5]/div[2]/div[1]/span'
        xpath6 = '/html/body/div/div/div[3]/div/div[1]/div[2]/div[5]/div[2]/div[1]/span'
        xpath7 = '//*[@id="root"]/div/div[3]/div/div[1]/div[2]/div[6]/div[2]/div[1]'
        xpaths=[xpath1,xpath2,xpath3,xpath4,xpath5,xpath6,xpath7]
        check=False
        timeout=2
        try:
            for i in range(0,4):
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, classnames[i]))).click()
                check=True
        except:
            check=False
            try:
                for i in range(0,7):
                    WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpaths[i]))).click()
                    check=True
            except:
                check=False

        if check:
            print("POST LIKED ( "+ self.a +" )")
        else:
            print("FAILED TO LIKE ( "+ self.a +" )")
        
        # self.Browser_Quit()
        # self.Browser_Watch()

    def Browser_NewTab( self ):
        self.driver.execute_script("window.open('https://www.croxyproxy.com/', '_blank');") 

        time.sleep(1) 
        windows = self.driver.window_handles

        time.sleep(2)
        self.driver.switch_to.window(windows[1])
        time.sleep(2)
        self.private = True
        url= self.stream
        self.driver.execute_script(f'var element = document.getElementById("url"); element.value = "{ url }";')
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="requestSubmit"]' ))).click() 
        time.sleep(10)
        self.Browser_Login()

        time.sleep(5)
        #print("Watch Stream")
        i=0
        while True:
            i=i+1
            if i==1000:
                time.sleep(15)
                self.driver.refresh()
                i=0

    def Browser_Watch( self ):
        # time.sleep(5)
        # self.driver.get(self.stream)

        time.sleep(5)
        self.driver.execute_script("window.open('"+ "https://127.0.0.1"+"', '_blank');") 
        time.sleep(3)
        windows = self.driver.window_handles

        time.sleep(2)
        self.driver.switch_to.window(windows[1])
        time.sleep(2)
        
        i=0
        while True:
            i=i+1
            if i==5000:
                print("WATCH STREAM ( "+ self.a +" )")
                time.sleep(4)
                
                windows = self.driver.window_handles
                self.driver.switch_to.window(windows[1])
                self.driver.refresh()
                
                windows = self.driver.window_handles
                self.driver.switch_to.window(windows[0])
                i=0

        
        # self.driver.get("https://idp.omlet.me/auth")
        # url = self.driver.current_url
        # id = self.get_id( url )
        # url = url.replace('register', 'login')

        # self.driver.get(url)
        # self.driver.execute_script(f'var element = document.getElementById("omid"); element.value = "{self.a}";')
        # self.driver.execute_script(f'var element = document.getElementById("pass"); element.value = "{self.b}";')

# print(get_proxy())
# cwd = os.path.realpath(os.path.dirname(__file__))
# print(cwd)
# print(os.path.dirname(os.path.realpath(__file__)))