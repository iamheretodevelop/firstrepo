user_message = "Hello, World"
cipher_number = 4
length_of_message = len(user_message)
encoded_message = ""
for i in range(length_of_message):
        ascii = ord(user_message[i])
        if ascii>= 65 and ascii < 87:
            ascii = ascii + cipher_number

        elif ascii>=87 and ascii <= 90:    
            ascii = ascii - (26 - cipher_number) 

        elif ascii>= 97 and ascii < 119:
            ascii = ascii + cipher_number

        elif ascii>=119 and ascii <= 122:    
            ascii = ascii - (26 - cipher_number) 

        else: 
            ascii = ascii 
        encoded_message = encoded_message + chr(ascii)
print (encoded_message)