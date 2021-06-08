def match(word, allowed_letters):
    """checks if a given word can be built from the allowed letters exclusivly. Each allowed letter may only occur once"""

    
    allowed_letters = [letter.lower() for letter in allowed_letters]
    word = [letter.lower() for letter in word]
    for letter in word:
        if letter not in allowed_letters:
            return False

    for letter in word:
        if letter not in allowed_letters:
            return False
        else:
            index = allowed_letters.index(letter)
            allowed_letters = allowed_letters[:index] + allowed_letters[index+1:]
    return True
            

if __name__=='__main__':
    match("oboo", "bobby")
