# An encoder/decoder for our spies to secretly send messages.
encryption_option = input("Would you like to Encode or Decode? ") 


# Ask the user for their message and cipher number.
cipher_number = int(input("What is your cipher number? "))
user_message = input("What is your message? ")
length_of_message = len(user_message)
encoded_message = ""
decoded_message = ""
if encryption_option.lower() == "encode":
    # Your code here!
    for i in range(length_of_message):
        ascii = ord(user_message[i])

        if ascii >= 65 and ascii <= 90:
            
            if ascii + cipher_number <= 90:
                ascii = ascii + cipher_number    #when the encoded character doesn't come after Z

            else:    
                ascii = ascii - (26 - cipher_number) #when the encoded character comes after Z


        elif ascii >=97 and ascii <=122:
            if ascii + cipher_number <= 122:
                ascii = ascii + cipher_number #when encoded character doesn't come after Z

            else:  
                ascii = ascii - (26 - cipher_number)  #when encoded character comes after Z

        

        else:
            ascii = ascii               #for anything besides an alphabet
        
        encoded_message = encoded_message + chr(ascii)
    print (encoded_message)
        


elif encryption_option.lower() == "decode":
    for i in range(length_of_message):
        ascii = ord(user_message[i])

        if ascii >= 65 and ascii <= 90:
            
            if ascii - cipher_number >= 65:
                ascii = ascii - cipher_number    #when the decoded character doesn't come before A

            elif ascii - cipher_number <65:    
                ascii = ascii + (26 - cipher_number) #when the decoded character comes before A


        elif ascii >=97 and ascii <=122:
            if ascii - cipher_number >= 97:
                ascii = ascii - cipher_number #when decoded character doesn't come before a

            elif ascii - cipher_number < 97:    
                ascii = ascii + (26 - cipher_number)  #when decoded character comes before a

        
        else:
            ascii = ascii               #for anything besides an alphabet
        decoded_message = decoded_message + chr(ascii)
    print (decoded_message)
    # Your code here for extra credit
    # Focus on getting the code above to work first.
    #sdcscd
else:
    # Print a nice notice that we only support encrypt/decrypt
    print("Sorry, we only support encryption/decryption")
    # Your code here!

