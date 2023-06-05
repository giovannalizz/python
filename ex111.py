def display_regular(message):
    print(message)

def display_up(message):
    up = message.upper()
    print(up)

def display_low(message):
    low = message.lower()
    print(low)

user_message = input("Enter a message: ")

display_regular(user_message)
display_up(user_message)
display_low(user_message)