import speech_recognition as sr

import gtts as gt 
import os  


r = sr.Recognizer()
with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            r.adjust_for_ambient_noise(source,duration = 1)

            print("Please say something")
            audio = r.listen(source)
            print("Recognizing Now .... ")
            
            try:
                print("You have said \n" + r.recognize_google(audio, language="ta-IN"))
               
            except Exception as e:
                print("Error :  " + str(e))

 
TamilText="வணக்கம்.அறம் செய விரும்பு, ஆறுவது சினம், இயல்வது கரவேல், ஈவது விலக்கேல், உடையது விளம்பேல். நன்றி!"
tts = gt.gTTS(text=TamilText, lang='ta')
