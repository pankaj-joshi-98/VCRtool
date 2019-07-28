import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)  # Checking the inbuild voices in the system.
engine.setProperty('voice', voices[0].id)

# getting the default speech rate
# rate = engine.getProperty('rate')
# print(rate)
 
engine.setProperty('rate', 150) # slowing down the speech rate


def speak(audio):
    """ This function converts the string input into voice output."""
    engine.say(audio)
    engine.runAndWait()


def wishUser():
    """This function wishes the user according to the time of the day, then asks for the command from the user."""
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am VCR, a voice command recognition tool. Please tell me how can I help you?")  


def takeCommands():
    """This function takes microphone input from the user and returns string output."""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        r.adjust_for_ambient_noise(source, duration=5)   # environment noise supression.

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishUser()
    while True:
    # if 1:
        query = takeCommands().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
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


        elif 'play music' in query:
            music_dir = 'Path of directory containing music files.'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "Path of Code.exe file." #Visual Studio Code.
            os.startfile(codePath)

        elif 'email to <receiver>' in query:
            try:
                speak("What should I say?")
                content = takeCommands()
                to = "receiverEmail@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry, I am not able to send this email.")

        elif 'quit' in query:
            speak("VCR quitting. Thank you for your time.")
            exit()

        else:
            speak("No input. VCR quitting. Thank you for your time.")
            exit()


                                               # -- End of code -- #