# import all these packages
import webbrowser
from tkinter import *
import playsound
from gtts import gTTS
import speech_recognition as sr
import time
import random
import os





R = sr.Recognizer() # From the speech_recognition class import Recognizer() and make a object


# Make a function to record Audio from Microphone
def record_audio(ask = False,txt_wid= None): # ask default value is False

    with sr.Microphone() as source: # Use Speech_recognition package and use microphone method to record audio
        if ask:
            Junaid_speak(ask, txt_wid)
        audio = R.listen(source) # The audio captured is stored in "audio" variable

        voicedata = '' # Initialize voicedata as empty

        try: # write code in try exception block
            voicedata = R.recognize_google(audio)
            '''this function takes audio as argument and recognize it and
                stores in "voicedata" variable'''

        except sr.UnknownValueError:
            Junaid_speak('Sorry, I Did Not Get That!',txt_wid)

        except sr.RequestError:
            Junaid_speak('Sorry, My Services Are Currently Down!',txt_wid)

        return voicedata # Returns "voicedata"



def Junaid_speak(audio_str,txt_wid): # Function to talk back to user, it take one argument

    tts = gTTS(text=audio_str,lang='en')
    '''gTTS function has two value "text=" this will read string and stores it in tts
        "lang="this means th language you want google to understand'''

    r = random.randint(1,5000) # generates number between 1-5000

    aud = 'audio' + str(r) + '.mp3' # this will generate random number to put in names
    tts.save(aud) # it will save the audio

    audio_file = os.path.join(f'E:\\Python\\Projects\\NXTECH-Speechrecognition\\{aud}')
    ''' this audio_file is a variable which holds the locatation of where the file is stored
        and it also joins the string as it has f-string'''
    tts.save(audio_file) # this will save the 'audio_file'

    playsound.playsound(audio_file) # playsound plays the audio

    os.remove(audio_file) # after playing the audio os.remove will remove the audio_file

     # Add the spoken text to the Text widget
    txt_wid.insert('end', audio_str + '\n')
    txt_wid.see('end')  # Scroll to the end to show the latest text




def respond(voicedata,txt_wid):
    '''This function is responsible to search string in voice data,
        if found it speak with Junaid_speak() function'''

    if 'hello' in voicedata:
        reply = ['Hey how can I help you',"Hey what's up",'I am listening','how can I help you','hello']
        rep = reply[random.randint(0,len(reply)-1)] # it will randomly pick any string in reply variable
        Junaid_speak(rep,txt_wid)

    elif 'what is your name' in voicedata:
        rep = 'Hey my name is junaid ahmed'
        Junaid_speak(rep,txt_wid)

    elif 'what time is it' in voicedata:
        Junaid_speak(time.ctime(),txt_wid)

    elif 'search' in voicedata:
        search = record_audio(ask= "What do you want me to search?",txt_wid=txt_wid) # ask in record_audio is True here
        url = 'http://google.com/search?q=' + search
        webbrowser.open(url) # this will open webbrowser
        Junaid_speak("Here Is What I Found For " + search,txt_wid)

    elif "location" in voicedata:
        location = record_audio(ask = "What's The Location You Want Me To Find!",txt_wid=txt_wid)
        url = "https://www.google.com/maps/place/" + location
        webbrowser.open(url)
        Junaid_speak("Here Is The Location You asked For "+ location,txt_wid)

    elif 'exit' in voicedata:
        Junaid_speak("Thank You",txt_wid) # before exiting it will say Thank You
        root.quit() # in-built function to quit the root/window

def listen_button_clicked(event=None): # this function will trigger when the button on the root is pressed!

    voicedata = record_audio(txt_wid=TXT)
    ''' when the listen_button_clicked function is triggered the record_audio function is triggered 
        and the recorded audio is stored in voice data variable'''

    respond(voicedata,TXT)
    '''respond function take voicedata as argument and inside the respond function it 
    check if the voice data matches to respond it will give response according to it.'''

def close_on_escape(event):
    root.quit()


root = Tk()
root.title('Speech Recognition')
root.geometry('450x350')
root.maxsize(450,350)
root.minsize(450,350)
root.config(bg= 'black')

label1 = Label(root,text='Welcome To My Application',bg='black',fg='white',font=('aerial',10,'bold')).grid(row= 0, column= 3)
TXT = Text(root,width=56,height=7)
TXT.grid(row= 1,column = 3)

label_cmd = Label(root,text='| Commands |',bg='black',fg='white',font=('aerial',10,'bold'))
label_cmd.grid(row= 3,column= 3)

more_cmd = Label(root,text='Hello\nwhat is your name\nwhat time is it\nsearch (give what to search)\nlocation (give what to search)\nexit'
                 ,bg='black',fg='white',font=('aerial',10,'bold'))
more_cmd.grid(row= 5,column=3)



btn_listen = Button(text='Listen',bg='white',fg='black',height=1,width=8,command=listen_button_clicked,font=('aerial',10,'bold'))
root.bind('<Return>',lambda event = None : listen_button_clicked())
btn_listen.grid(row= 7,column=3)

btn_quit = Button(text='Quit',bg='red',fg='white',height=1,width=8,command=root.quit,font=('aerial',10,'bold'))
root.bind("<Escape>",close_on_escape)
btn_quit.grid(row= 8,column= 3)

root.mainloop()
