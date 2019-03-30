import webbrowser

name = input("Enter your Name : ")

helloIntent = ['hi','hello','hey','hey there','hi there','hello there','hola']

chat = True
while chat:
    msg = input("Enter your message: ")
    if msg in helloIntent:
        print(f"Hi {name}...")
    elif msg.startswith("open"):
        web = msg.split()[-1]
        webbrowser.open(web+'.com')
    elif msg == "bye":
        print(f"Bye {name}...")
        chat = False
    else:
        print("I don't understand")
