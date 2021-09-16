def greet(lang):
    if lang == "es":
        print ("Hola!")
    elif lang == "fr":
        print ("Bonjour!")
    elif lang == "ch":
        print ("Ni Hão!")
    else:
        print ("Hello!")

greet("es")
greet("fr")
greet("ch")
greet("en")


def welcome():
    return "Hello"

print (welcome())