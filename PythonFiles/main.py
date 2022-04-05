import string

cipher = {"a":"w", "b":"x", "c":"y", "d":"z", "e":"a", "f":"b", "g":"c", "h":"d", "i":"e", "j":"f", "k":"g", "l":"h", "m":"i", "n":"j", "o":"k", "p":"l", "q":"m", "r":"n", "s":"o", "t":"p", "u":"q", "v":"r", "w":"s", "x":"t", "y":"u", "z":"v"}

def encode(msg):  
    
    codedMessage = ""
    key = cipher
    for ch in msg:
        if (ch.isalpha() == False):
            codedMessage += ch
        elif (ch.isupper()):
            new_letter = cipher[ch.lower()]
            codedMessage += new_letter.capitalize()
        else:
            codedMessage += cipher[ch]
        
    return codedMessage
    
	
print(encode("I like code wheels!"))