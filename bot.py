from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer #Allows a chat bot to be trained using a list of strings where the list represents a conversation
from tkinter import *
from chatterbot.trainers import ChatterBotCorpusTrainer #Allows the chat bot to be trained using data from the ChatterBot dialog corpus.
import pyttsx3 as pp
import speech_recognition as s
import threading

#pushkargole1996@gmail.com
engine = pp.init()

voices = engine.getProperty('voices')
print(voices)

engine.setProperty('voice', voices[1].id)


def speak(word):
    engine.say(word)
    engine.runAndWait()


# pyttsx3
bot = ChatBot("My Bot")

convo = [
    'hello',
    'hi there !',
    'what is your name ?',
    'My name is Pepper , i am a chatbot',
    'how are you ?',
    'I am doing great these days',
    'who is your father?'
    'my father is Atulya Mehra'
    'am i cute?'
    'yes, you are very cute.'
    'thank you',
    'In which city you live ?',
    'I live in Delhi',
    'In which language you talk?',
    'I mostly talk in english and hindi'
]

trainer = ListTrainer(bot)

# now training the bot with the help of trainer

trainer.train(convo)

trainer= ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")
trainer.train("chatterbot.corpus.hindi")



# answer = bot.get_response("what is your name?")
# print(answer)

# print("Talk to bot ")
# while True:
#     query = input()
#     if query == 'exit':
#         break
#     answer = bot.get_response(query)
#     print("bot : ", answer)

main = Tk()

main.geometry("500x650")

main.title("SmartBot")
img = PhotoImage(file="bot1.png")

photoL = Label(main, image=img)

photoL.pack(pady=5)


# takey query : it takes audio as input from user and convert it to string..

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold = 1
    print("your bot is listening try to speak")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
        except Exception as e:
            print(e)
            print("not recognized")


def ask_from_bot():
    query = textF.get()
    answer_from_bot = bot.get_response(query)
    msgs.insert(END, "you : " + query)
    print(type(answer_from_bot))
    msgs.insert(END, "bot : " + str(answer_from_bot))
    speak(answer_from_bot)
    textF.delete(0, END)
    msgs.yview(END)


frame = Frame(main)

sc = Scrollbar(frame)
msgs = Listbox(frame, width=80, height=20, yscrollcommand=sc.set)

sc.pack(side=RIGHT, fill=Y)

msgs.pack(side=LEFT, fill=BOTH, pady=10)

frame.pack()

# creating text field

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)

btn = Button(main, text="ENTER", font=("Verdana", 20), command=ask_from_bot)
btn.pack()


# creating a function
def enter_function(event):
    btn.invoke()


# going to bind main window with enter key...

main.bind('<Return>', enter_function)


def repeatL():
    while True:
        takeQuery()


t = threading.Thread(target=repeatL)

t.start()

main.mainloop()