import webbrowser
from datetime import datetime

name = input("Enter your Name : ")

helloIntent = ['hi','hello','hey','hey there','hi there','hello there','hola']
dateIntent = ["tell me date","today's date","what's the date today","date","date please"]
timeIntent = ["tell me time","current time","what's the time","time","time please"]

chat = True
while chat:
    msg = input("Enter your message: ")
    msg = msg.lower()
    if msg in helloIntent:
        print(f"Hi {name}...")
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg in dateIntent:
        d = datetime.now().date()
        print(d.strftime("%d/%m/%y, %a"))
    elif msg in timeIntent:
        t = datetime.now().time()
        print(t.strftime("%H:%M:%S, %p"))
    elif msg == "bye":
        print(f"Bye {name}...")
        chat = False
    else:
        print("I don't understand")
