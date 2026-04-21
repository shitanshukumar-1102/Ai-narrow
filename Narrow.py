import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyttsx3

# -------- Text to Speech --------

engine = pyttsx3.init()

def speak(text):
    try:
        engine.stop()   # stop any previous speech
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass  # ignore loop error
    
# -------- Voice Recognition --------

print("jarvis started...")
def listen():
    print("Listening...")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)
        recognizer.energy_threshold = 300
        recognizer.pause_threshold = 0.8

        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)
            print("Recognizing...")

            command = recognizer.recognize_google(audio)
            print("You said:", command)

            return command.lower()

        except sr.WaitTimeoutError:
            print("Timeout, try again")
            return ""

        except sr.UnknownValueError:
            print("Didn't understand")
            return ""

        except sr.RequestError:
            print("Check internet connection")
            return ""
# -------- Command Processing --------
def process_command(command):
    command = command.lower()

    if "time" in command:
        time = datetime.datetime.now().strftime("%H:%M")
        return f"The time is {time}"

    elif "open youtube" in command:
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        webbrowser.open("https://google.com")
        return "Opening Google"
    elif "open wikipedia" in command:
        webbrowser.open("https://wikipedia.org")
        return "Opening Wikipedia"
    elif "open whatsapp" in command:
        webbrowser.open("https://web.whatsapp.com")
        return "Opening WhatsApp"
    elif "open facebook" in command:
        webbrowser.open("https://facebook.com")
        return "Opening Facebook"
    elif "open twitter" in command:
        webbrowser.open("https://twitter.com")
        return "Opening Twitter"
    elif "open instagram" in command:
        webbrowser.open("https://instagram.com")
        return "Opening Instagram"  
    elif "open github" in command:
        webbrowser.open("https://github.com")
        return "Opening GitHub"
    elif "open linkedin" in command:
        webbrowser.open("https://linkedin.com")
        return "Opening LinkedIn"
    elif"zomato" in command:
        webbrowser.open("https://www.zomato.com")
        return "Opening Zomato"
    elif"amazon" in command:
        webbrowser.open("https://www.amazon.in")
        return "Opening Amazon"
    elif"flipkart" in command:
        webbrowser.open("https://www.flipkart.com")
        return "Opening Flipkart"
    elif"spotify" in command:
        webbrowser.open("https://www.spotify.com")
        return "Opening Spotify"
    elif"netflix" in command:
        webbrowser.open("https://www.netflix.com")
        return "Opening Netflix"
    elif"gmail" in command:
        webbrowser.open("https://mail.google.com")
        return "Opening Gmail"
    elif"urban company" in command:
        webbrowser.open("https://www.urbancompany.com")
        return "Opening Urban Company"
    elif"quora" in command: 
        webbrowser.open("https://www.quora.com")
        return "Opening Quora"
    elif"swiggy" in command:
        webbrowser.open("https://www.swiggy.com")
        return "Opening Swiggy"
    elif"uber" in command:
        webbrowser.open("https://www.uber.com")
        return "Opening Uber"
    elif"ola" in command:
        webbrowser.open("https://www.olacabs.com")
        return "Opening Ola"
    elif"gemini" in command:
        webbrowser.open("https://gemini.google.com")
        return "Opening Gemini"
    elif"zoom" in command:
        webbrowser.open("https://zoom.us")
        return "Opening Zoom"
    elif"chatgpt" in command:
        webbrowser.open("https://chat.openai.com")
        return "Opening ChatGPT"

    elif "who is" in command:
        person = command.replace("who is", "")
        try:
            info = wikipedia.summary(person, sentences=2)
            return info
        except:
            return "Sorry, I couldn't find information."
        
    elif "what is" in command:
        person = command.replace("what is", "")
        try:
            info = wikipedia.summary(person, sentences=2)
            return info
        except:
            return "Sorry, I couldn't find information."    


    elif "exit" in command:
        return "exit"

    else:
        return "I didn't understand that."
        
