from django.shortcuts import redirect, render
import speech_recognition as sr
import pyttsx3
from .models import chats ,online
# Create your views here.
def index(request):
    talk = pyttsx3.init()
    talk.say("Tap on the microphone and speak the magic word")
    talk.setProperty('rate',30)
    talk.runAndWait()

    return render(request,'index.html')

def home(request):
    fetch_data = chats.objects.all()

    fetch_online = online.objects.all()
    # r = sr.Recognizer()

    # with sr.Microphone() as source:
    #     print('Speak Anything:')
    #     audio = r.listen(source)

    #     text = r.recognize_google(audio)
    #     reply = print("you said :{}".format(text))

                             # Store chat in database
   
    return render(request,'home.html',{'all':fetch_data,'members':fetch_online})

        

def welcome(request):
    name = request.POST.get('name',None)
    message = request.POST.get('text',None)
    insert = chats(chat_id=23,name=name,message=message)
    insert.save()
    return redirect('/home')


def personal(request):
    user_id = request.POST['id']
    user_message = chats.objects.filter(user_id=user_id)
    return render(request,'personal.html')