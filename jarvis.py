import pyttsx3  #for voice in device 
import datetime
import speech_recognition as sr  #to take audio as input
import wikipedia #to open wikipedia
import webbrowser #to open webbrowser
import os       #to open files
import smtplib  # to send mail
import random #to play random songs

engine = pyttsx3.init('sapi5')          
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)          

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


#wishMe() will greet user 
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour <12:
        speak("Good Morning")
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Jarvis Sir Please tell me how may i help You")

#it takes microphone user from user and return string output
def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"

    return  query

def sendEmail(to, content):  #for sending email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()


#_______________________________main______________________________

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        
        #logic for executing task base on query
        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir= "D:\\Professional\\College Related\\Projects\\Python Project\\Jarvis\\favsongs"
            songs=os.listdir(music_dir)
            x=len(songs)
            y=random.randint(0,x)
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[y]))

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir the time is {strTime}")
            
        elif "open code editor" in query:
            codePath="C:\\Users\\ronak\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif "play movie" in query:
            movie_dir="D:\\Professional\\College Related\\Projects\\Python Project\\Jarvis\\movie"
            movie=os.listdir(movie_dir)
            print(movie)
            os.startfile(os.path.join(movie_dir,movie[0]))



        elif "send email" in query:
            try:
                speak("What should I say")
                content = takeCommand()
                to = "rroonnaakk7@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry i am not able to send email")

        elif "goodbye" in query:
            speak("Bye Sir have a nice day!!")
            exit()