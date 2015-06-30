import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    dict = {}
    for i in range(len(secretWord)):
        if secretWord[i] in dict:
            dict[secretWord[i]] += 1
        else:
            dict[secretWord[i]] = 1
    c = 0
    for key in dict.keys():
        if key in lettersGuessed:
            c = c + dict[key]
        else:
            return False
    if (c == len(secretWord)):
        return True
    else:
        return False

def getGuessedWord(secretWord, lettersGuessed):
    l = len(secretWord)
    res = []
    for i in range(l):
        if secretWord[i] in lettersGuessed:
            res.append(secretWord[i])
        else:
            res.append('_ ')
    return str(''.join(res))

def getAvailableLetters(lettersGuessed):
    alpha = {} 
    import string
    all = string.ascii_lowercase
    for i in range(len(all)):
        alpha[all[i]] = 1
    for l in lettersGuessed:
        if l in alpha.keys():
            alpha[l] = 0
    return ''.join(sorted([key for key,value in alpha.items() if alpha[key] == 1]))
    
def hangman(secretWord):
    print ('Welcome to the game, Hangman!')
    print ('I am thinking of a word that is '+str(len(secretWord))+' letters long.')
    counter = 8
    entry_list = []
    miss_list = []
    while (counter > 0):
        print ('-'*13)
        print ('You have '+str(counter)+' guesses left.')
        print ('Available letters: '+ getAvailableLetters(entry_list+miss_list))
        while True:
            entry = raw_input('Please guess a letter: ').lower()
            if len(entry) == 1:
                break
            print 'Please enter only one character from available letters.'

        if entry in entry_list:
            print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord,entry_list))
            continue
        if entry in miss_list:
            print ("Oops! You've already guessed that letter: "+getGuessedWord(secretWord,entry_list))
            continue

        if entry in secretWord:
            entry_list.append(entry)
            print ('Good guess: '+getGuessedWord(secretWord,entry_list))
        else:
            miss_list.append(entry)
            print ('Oops! That letter is not in my word: '+getGuessedWord(secretWord,entry_list))
            counter -= 1

        if (isWordGuessed(secretWord, entry_list)):
            print ('-'*13)
            print('Congratulations, you won!')
            break
        else:
            continue
    if (counter == 0):
        print ('-'*13)
        print('Sorry, you ran out of guesses. The word was ' +secretWord+'.')

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
