def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
    return True

if __name__ == '__main__':
    print ('I am testing these phone numbers as well as writing a main method')
    print ('Is this a phone number 111-222-3333: ' + str(isPhoneNumber('111-222-3333')))
    print ('Is this a phone number moshi moshi: ' + str(isPhoneNumber('moshi moshi')))
    
