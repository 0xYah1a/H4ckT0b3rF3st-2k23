

def encrypt_caeser(text,k):
    result= ""
    #plaintext -> ciphertext
    for char in text:
        if(char.isalpha()):
            #uppercase
            if (char.isupper()):
                result += chr((ord(char) + k - 65) % 26 + 65 )
            #lowercase
            else :
                result += chr((ord(char) + k - 97 ) % 26 + 97 )
        else :
            result += " "
    return result 

