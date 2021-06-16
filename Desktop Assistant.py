import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit as pt # for send message on whatsapp

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour<12):
        speak('Good Morning!')
    elif(hour >= 12 and hour <18):
        speak('Good Afternoon!')
    else:
        speak('Good Night, Have a good Day!')
    speak('I am your Desktop Manager, Please tell me how may I help you')

def takeCommand():
    #it takes microphone input from user and returns string output
    r = sr.Recognizer()
    #print((sr.Microphone.list_microphone_names()))
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source, duration = 1)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
   
    except Exception as e:
        print('Say that again Please...')
        return "None"

    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login(yourgmail,yourpassword)
    server.sendmail(yourgmail,to,content)
    server.close()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


if __name__ == '__main__':
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia....')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query,sentences=1)
            speak('According to wikipedia')
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open instagram' in query:
            webbrowser.open("instagram.com")
        elif 'open facebook' in query:
            webbrowser.open("facebook.com")
        elif 'open twitter' in query:
            webbrowser.open("twitter.com")
        elif 'open linkedin' in query:
            webbrowser.open("linkedin.com")
        elif 'open nit jalandhar' in query:
            webbrowser.open("nitj.ac.in")
        elif 'open nit jamshedpur' in query:
            webbrowser.open("nitjsr.ac.in")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = "D:\\SD Card\\audio"
            songs = os.listdir(music_dir)
            os.startfile(music_dir,songs[0])
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(strTime)
        elif 'open code' in query:
            codePath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak('what should I say?')
                content = takeCommand()
                to = "umadhamdaha1066@gmail.com"
                sendEmail(to,content)
                speak('Email has been sent !')
            except Exception as e:
                print(e)
                speak("sorry sir, I am not able to send this email at the moment")
         elif 'send message on whatsapp' in query:
            try:
                speak('What should I Say?')
                content = takeCommand()
                pt.sendwhatmsg('+919304550791',content,14,40)
                speak('Message has been sent!')
            except Exception as e:
                print(e)
                speak('Sorry sir, I am not able to send this message at the moment! ,Please try again')
        elif 'quit' in query:
            exit()            

        
