#This is a python program which takes input from the user which it encrypts with a dynamic key wordwise and copies it to the user's clipboard(works only on windows) then is decrypted later.

#******************************************************************************
import platform #Importing paltform module to check for the user's device platform as pyperclip only works for windows
user_system = platform.system() #Storing the user's device platform name
if user_system == 'Windows': #Checking if the user's device is Windows
    import pyperclip as pc #Importing pyperclip module to automaticaly copy the encrypted result to the user's clipboard(works only on windows)

#Encryption block
user_string = input('Enter the string : ') #Asking the user to enter a string to encrypt
masterkey = int(input('Enter a number key: ')) #Dynamic key for better encryption

character_result = ''  #Defining variable for a character
space=' ' #Defining variable for empty space
encrypted_result = '' #Defining variable for final encrypted string for printing                

if user_string[len(user_string)-2:len(user_string)] != '#@': #If the string ends in #@ then it will decrypt it instead of encryption
#User wants to encrypt    
    for word in user_string.split(): #Spliting the user string into words
        encryption_key = masterkey #Creating a new variable encryption key so that masterkey value does not change
        word_result = '' #Defing variable for the encrypted word
        string_final_result = '' #Defining variable for the encrypted string 
        for character in range(0,len(word)): #Travesing the word
            if word[character].isupper() == True:
                character_result = chr(((ord(word[character]))-65+encryption_key)%26+65) #Result when character is a capital
            elif word[character].islower() == True:
                character_result = chr(((ord(word[character]))-97+encryption_key)%26+97) #Result when character is a capital
            elif word[character].isdigit() == True:
                character_result = chr(((ord(word[character]))-48+encryption_key)%10+48) #Result when character is a digit
            elif word[character] == ' ':
                character_result = space #Result when character is a space
            else:
                character_result = word[character] #Result when character is a special character
        
            word_result += character_result #Concatenating the encrypted characters of a word together to form the encrypted word
            encryption_key+=13 #Dynamic key changes the value of the key for every character of a word for more security
        string_final_result += space + word_result #Concatenating the encrypted words of a string together to form the encrypted string
        encrypted_result += string_final_result #Concatenating the encrypted strings of the user input together to form the encrypted result
    
    if user_system == 'Windows': #Checking if the user's device is Windows
        pc.copy(encrypted_result) #Copying the the encrypted result to user's clipboard for more convience(works only on windows) 

    print('') #To leave an empty line
    print('') #To leave an empty line
    print('>e> ',encrypted_result,' <e<') #Displaying the encrypted result
    print('') #To leave an empty line
#------------------------------------------------------------------------------    
    
    #Decrytion block
    character_result = '' #defining encoded result variable for each character
    string_final_result = '' #Defining variable for the encrypted string
    decrypted_result = '' #Defining variable for final decrypted string for printing 

    for word in encrypted_result.split(): #Spliting the encrypted result into words
        decryption_key = masterkey #Creating a new variable decryption key so that masterkey value does not change
        word_result = '' #Defing variable for the encrypted word
        string_final_result = '' #Defining variable for the encrypted string
        for character in range(0,len(word)): #Travesing the word
            if word[character].isupper() == True:
                character_result = chr(((ord(word[character]))-65-decryption_key)%26+65) #Result when character is a capital
            elif word[character].islower() == True:
                character_result = chr(((ord(word[character]))-97-decryption_key)%26+97) #Result when character is a capital
            elif word[character].isdigit() == True:
                character_result = chr(((ord(word[character]))-48-decryption_key)%10+48) #Result when character is a digit
            elif word[character] == ' ':
                character_result = space #Result when character is a space
            else:
                character_result = word[character] #Result when character is a special character
            
            word_result += character_result #Concatenating the encrypted characters of a word together to form the encrypted word
            decryption_key+=13  #Dynamic key changes the value of the key for every character of a word for more security
        string_final_result += space + word_result #Concatenating the encrypted words of a string together to form the encrypted string
        decrypted_result += string_final_result #Concatenating the encrypted strings of the user encrypted result together to form the decrypted result
    print('') #To leave an empty line
    print('>d> ',decrypted_result,' <d<') #Decryption of the encrypted message is over
    print('') #To leave an empty line
    print('Program finished')

#******************************************************************************
#******************************************************************************
else: #User wants to decrypt
    character_result = '' #defining encoded result variable for each character
    string_final_result = '' #Defining variable for the encrypted string
    decrypted_result = '' #Defining variable for final decrypted string for printing 
    space=' ' #Defining variable for empty space
    encrypted_result = user_string #Defining the encrypted string
    for word in encrypted_result.split(): #Spliting the encrypted result into words
        decryption_key = masterkey #Creating a new variable decryption key so that masterkey value does not change
        word_result = '' #Defing variable for the encrypted word
        string_final_result = '' #Defining variable for the encrypted string
        for character in range(0,len(word)): #Travesing the word
            if word[character].isupper() == True:
                character_result = chr(((ord(word[character]))-65-decryption_key)%26+65) #Result when character is a capital
            elif word[character].islower() == True:
                character_result = chr(((ord(word[character]))-97-decryption_key)%26+97) #Result when character is a capital
            elif word[character].isdigit() == True:
                character_result = chr(((ord(word[character]))-48-decryption_key)%10+48) #Result when character is a digit
            elif word[character] == ' ':
                character_result = space #Result when character is a space
            else:
                character_result = word[character] #Result when character is a special character
            
            word_result += character_result #Concatenating the encrypted characters of a word together to form the encrypted word
            decryption_key+=13  #Dynamic key changes the value of the key for every character of a word for more security
        string_final_result += space + word_result #Concatenating the encrypted words of a string together to form the encrypted string
        decrypted_result += string_final_result #Concatenating the encrypted strings of the user encrypted result together to form the decrypted result
        decrypted_result = decrypted_result.replace('#@','') #Removing the #@ at the end of the string
    print('') #To leave an empty line
    print('>d> ',decrypted_result,' <d<') #Decryption of the encrypted message is over
    print('') #To leave an empty line
    print('Program finished')
