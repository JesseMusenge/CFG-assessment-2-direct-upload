def isogram_check(word):
    word = word.lower()
    unique_letter = set()
    
    for letter in word:
        if letter in unique_letter:
            return False
        else:
            unique_letter.add(letter)
    return True


word = input("Please enter a word to check if it is an isogram :)\n ")
result = isogram_check(word)
print(result)


def test_isogram_check(): #all unit tests in one function
    #Test case 1: Checking for an inputted word with no repeated letters
    word = "isogram"
    #Explanation: since this word contains no repeated letters, it will return True.
    assert isogram_check(word) == True

    #Test case 2: checking for an inputted word with repeated letters
    word = "hello"
    #Explanation: This word contains the letter 'l' twice, so it will return False.
    assert isogram_check(word) == False

    #Test case 3: checking for an inputted word with repeated letters and different cases
    word = "Abcdefg"
    #Explanation: since this word contains the letter 'a' and 'A', it will return False.
    assert isogram_check(word) == False

#Running the unit tests
test_isogram_check()