import requests
import pyttsx3 
import pickle
import psutil
import requests, json
import speech_recognition as sr
from pygame import *   
import time
import glob
import datetime
import smtplib
import keyboard as k
from datetime import datetime
import pyaudio

import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

now = datetime.now()
current_time = now.strftime("%H %M")
print("Current Time =", current_time)


def listen(say):
    r = sr.Recognizer()
    with sr.Microphone() as source:
             r.adjust_for_ambient_noise(source)
             r.adjust_for_ambient_noise(source,duration = 1)

             print("Please say something")
             speak(say)
             audio = r.listen(source)
             print("Recognizing Now .... ")
             
             try:
                 print("You have said \n" + r.recognize_google(audio))
                 return(r.recognize_google(audio))

             except Exception as e:
                 print("Error :  " + str(e))

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


engine = pyttsx3.init('sapi5')
voices=engine.getProperty("voices")

def voice():
    engine.setProperty("voice", voices[0].id)
    speak('Do you want to proceed with the male voice')
    engine.setProperty("voice", voices[1].id)
    speak('or do you want to proceed with the female voice')

    v=listen("say your choice")
    if v=="mail" or v=="Mail" or v=="male" or v=="Mail":
        engine.setProperty("voice", voices[0].id)
        print("Male voice")
        inst()
    else:
        engine.setProperty("voice", voices[1].id)
        print("Female  voice")
        inst()

def inst():
    inp=listen("do you want me to read the instructions for input")
    if inp=="yes" or inp=="s":
        speak("INSTRUCTIONS")
        speak("Use the up and down arrow keys to navigate in the home menu")
        speak("use the right arrow key to get inside any sub menu")
        speak("Inside the song menu, use the right arrow key for next song.")
        speak("Up arrow key for pausing the song")
        speak("Down arrow key for playing the paused song")
        speak("and left arrow key to come back to main menu")
        speak("Inside the send mail menu, use the up arrow key to select the email from favourites ")
        speak("and down arrow key to add a new email")
        speak("When asked for a voice input, make sure you pronounce it clearly")
        speak("You are ready to roll")
        home()
    else:
        home()



def home():
    
     hour = int(datetime.now().hour)
     if hour>=0 and hour<12:
         speak("Good Morning! ")

     elif hour>=12 and hour<17:
         speak("Good Afternoon! ")

     elif hour>=17 and hour<19 :
         speak("Good Evening! ")

     else:
         speak("Good Evening! ")
         
    
     speak("The time is"+current_time) 

     speak("I am your  Virtual  Assistant Vision.")
     speak("I am here to give you vision.")

     speak("You are in home menu")
     
     main(0)

def choose(o):
     if o==1:
         oute()

     elif o==2:
         songe()

     elif o==3:
         maile()

     elif o==4:
         bate()

     elif o==5:
         newse()
     
     elif o==6:
         readme()
     
     elif o==7:
        timere()

     elif o==8:
         app()
 
def main(i):

    while True:

         if k.is_pressed('up'):       
             print("up is pressed")
             i+=1
             time.sleep(1) # Sleep for 1 seconds
             print(i)
             choose(i)

         elif k.is_pressed('down'):  
             print("down is pressed")
             i-=1
             time.sleep(1) 
             print(i)
             choose(i)

def newse():
    speak("Do you want me to read the news for you, ")

    while True:
        if k.is_pressed('right'):
            print("Pressed right key")
            news()       
        elif k.is_pressed('up'):
            print("Pressed up key")
            main(5)  
        elif k.is_pressed('down'):
             print("Pressed down key")
             main(5)
def news():
    url = ('http://newsapi.org/v2/top-headlines?'
        'sources=bbc-news&'
        'apiKey=322f71466b8c42608b12bb360c14c665')
    response = requests.get(url)
    d=response.json()
    D=(d['articles'])
    for i in D:
        print(i['title'])
        speak(i['title'])
        if k.is_pressed('up'):    
                main(5)
                time.sleep(1)  
    main(5)

def songe():
     speak("Do you want to play a song? ")
    
     
     while True:
         if k.is_pressed('right'):
             print("Pressed right key")
             song()       
         elif k.is_pressed('up'):
             print("Pressed up key")
             main(2)     
         elif k.is_pressed('down'):
             print("Pressed down key")
             main(2)              
def song():
    
    d=(glob.glob("F:\Cs project\msc\*.mp3"))
    print(d)
    for i in range(len(d)):

        print(i)
        mixer.init()
        mixer.music.load(d[i])
        mixer.music.play()
        X=True
        while X:       
            
            if k.is_pressed('up'):    
                mixer.music.pause() 
                time.sleep(1)     

            elif k.is_pressed('down'):    
                mixer.music.unpause()
                time.sleep(1)
                    

            elif k.is_pressed('left'):    
                mixer.music.stop()   
                main(2)

               

            elif k.is_pressed('right'):
                time.sleep(1)
                if len(d)==i+1:
                    mixer.music.stop()
                    speak("Songs Exhausted. Going back to main menu.")
                    main(2)
                else:
                    mixer.music.stop()
                    X=False

def maile():
     speak("Do you want to send a mail? ")
       
     
     while True:
         if k.is_pressed('right'):
             print("Pressed right key")
             mail()       
         elif k.is_pressed('up'):
             print("Pressed up key")
             main(3)
         elif k.is_pressed('down'):
             print("Pressed down key")
             main(3)
def mail():
     speak("Select from favourites or add a new mail")

     while True:
         if k.is_pressed('up'):
             print("Pressed up key")
             fav()       

         elif k.is_pressed('down'):
             print("Pressed down key")
             newm()
def fav():

    f=open(r"F:\Cs project\data\fav.dat","rb")
    data=pickle.load(f)
    print(data)
   

    for b in data:
        print(b[0])
        print(b[1])
        speak(b[0])
        speak(b[1])
    
    l =listen("Say the option")
    
    if l=="Tu":
        print("2")
        ld='2'
    else:
        ld=l


    for b in data:
        if ld==b[0]:
            rm=b[2]
            print(rm)
  
    con=listen("Be ready to say the content. Recording in 3 2 1")
    print(con)
    sendm(rm,con)
def newm():
    f=open(r"F:\Cs project\data\fav.dat","rb")
    data=pickle.load(f)
    f.close()
    print(data)
    L=[]
    l=len(data)+1

      
    m=listen("Say the mail without the domain")
    M=m.replace(" ", "")
    
    speak("Select the domain.")
    domlist="""1 gmail
               2 yahoo
               3 reddifmail"""
    do=listen(domlist)
    if do=="Tu":
        dom=2
    else:
        dom=do
    if int(dom)==1:
        print(M+'@gmail.com')
        mm=M+'@gmail.com'
    
    elif int(dom)==2:
        print(M+"@yahoo.com")
        mm=M+"@yahoo.com"

    elif int(dom)==3:
        print(M+'@reddifmail.com')
        mm=M+'@reddifmail.com'

    i=str(l)
    L.append(i)
    L.append(M)
    L.append(mm)

    print(L)
    data.append(L)
    print(data)

    f=open(r"F:\Cs project\data\fav.dat","wb")
    pickle.dump(data,f)
    f.close()

    con=listen("Be ready to say the content. Recording in 3 2 1")
    sendm(mm,con)
def sendm(to,c):
     server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
     server.login('sendermail2020@gmail.com', 'imsending')
     server.sendmail('sendermail2020@gmail.com',to,c)
     server.quit()
     speak("mail sent successfully")
     main(3) 

def oute():
    speak("Do you want to know how is it around you?")

    while True:
        if k.is_pressed('right'):
            print("Pressed right key")
            out()       
        elif k.is_pressed('up'):
            print("Pressed up key")
            main(1)                
def out():
    
    url = 'https://api.openweathermap.org/data/2.5/weather?q=Coimbatore&appid=60cfacc8c34b5d1c6d6869b5960744c6'
    json_data = requests.get(url).json()
    tem = json_data['main']['temp']
    speak("the time is "+str(current_time))
    speak('The temperature is '+str(tem)+'degree farenheit at coimbatore')

    main(1)

def bate():
    speak("DO you want to check battery percentage, and know whether the charger is plugged in ")
    while True:
            if k.is_pressed('right'):
                print("Pressed right key")
                bat()       
            elif k.is_pressed('up'):
                print("Pressed up key")
                main(4) 

            elif k.is_pressed('down'):
             print("Pressed down key")
             main(4)
def bat():
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)
    plugged = "Plugged In" if plugged else "Not Plugged In"
    print(percent+'% | '+plugged)
    speak("You have "+str(percent)+'percentage'+"remaining and the charger is "+plugged )
    main(4)

def readme():
    speak("To read your emails, ")
    while True:
            if k.is_pressed('right'):
                print("Pressed right key")
                readm()       
            elif k.is_pressed('up'):
                print("Pressed up key")
                main(6)

            elif k.is_pressed('down'):
             print("Pressed down key")
             main(6)
def readm():

    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None

    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    results= service.users().messages().list(userId='me',labelIds=['INBOX']).execute()
    messages=results.get('messages',[])
    
    mc=listen("How many messages do you want to see?")
    message_count=int(mc)

    if not messages:
        print('No messages found.')
        speak("No messages found")
        main(6)

    else:
        print('Messages:')
        for message in messages[:message_count]:
            msg=service.users().messages().get(userId='me',id=message['id']).execute()
            print(msg['snippet'])
            speak(msg['snippet'])
            print("\n")

            main(6)

def timere():
    speak("Do you want to set a timer?")
    while True:
            if k.is_pressed('right'):
                print("Pressed right key")
                timer1()       
            elif k.is_pressed('up'):
                print("Pressed up key")
                main(7)

            elif k.is_pressed('down'):
             print("Pressed down key")
             main(7)
def timer1():
    mi=(listen("How many minutes do you want to set the timer?"))
    if mi=='Tu' or mi=='tu':
        min=2
    else:
        min=int(mi)
    se=int(listen("How many seconds do you want to set the timer?"))
    if se=='Tu' or se=='tu':
        sec=2
    else:
        sec=int(se)
    sec_m=mi*60
    ts=sec_m+sec
    print(ts)
    countdown(int(ts))
def countdown(t): 
	
	while t: 
		mins, secs = divmod(t, 60) 
		timer = '{:02d}:{:02d}'.format(mins, secs) 
		print(timer, end="\r") 
		time.sleep(1) 
		t -= 1
	
	timer3()
def timer3():
    
    speak("Your Time is up. Please wake up")
    mixer.init()
    soundObj = mixer.Sound('F:\Cs project\msc\Alarm-Fast-High-Pitch-A3-Ring-Tone-www.fesliyanstudios.com.mp3')
    soundObj.play()

    while True:       
            
            if k.is_pressed('up'):    
                soundObj.stop() 
                main(7)  

            elif k.is_pressed('down'):    
                soundObj.stop() 
                main(7)
                    

            elif k.is_pressed('left'):    
                soundObj.stop()   
                main(7)

               

            elif k.is_pressed('right'):
                soundObj.stop()
                main(7)
                
def app():
    speak("You are amazing. I am glad to help you as an assistant.")
    main(0)


voice()
