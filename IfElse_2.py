name = input("Enter your Name : ")

# Logical Operator = and, or, not
# Membership Operator = in, not in
# Identity Operator = is, not is

chat = True
while chat:
    msg = input("Enter your message: ")
    if msg == "hello" or msg == "hi" or msg == "hey" or msg == "hi there":
        print(f"Hi {name}...")
    elif msg == "bye":
        print("Bye User...")
        chat = False
    else:
        print("I don't understand")
