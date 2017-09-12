def happy_birthday(name, age):
    
    i = input("Hello, is it your birthday today?")
    if i == "yes":
        return "HAPPY BIRTHDAY {}! {} AIN'T THAT OLD.".format(name, age)
    else:
        print("Sorry, you ain't getting no presents.")
        
def hbd(age):
    
    i = input("Hello, is it your birthday today?")
    if i == "yes":
        print("{} years ago, on this very day, something special happened.".format(age))
        i1 = input("Do you want to know what?")
        if i1 == 'yes':
            return "No I don't think so."
        else:
            return "Too bad, but don't worry it wasn't you."
    else:
        return "Oops, my bad."

def jkjk(name):
    
    i = input("Knock knock, who's there?")
    if i == name:
        return "I'm sad {}, you were supposed to be a funny one.".format(name)
    else:
        return "I know who you are! I know where you live! Be afraid! Very afraid!"
    
