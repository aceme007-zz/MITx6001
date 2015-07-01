from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    
    tot = 0
    bestWord = 'None'
    for w in wordList:
        if (isValidWord(w,hand,wordList)):
            s = getWordScore(w,n)
            if (s > tot):
                tot = s
                bestWord = w
            else:
                continue
        else:
            continue
    return bestWord



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score = 0
    while (calculateHandlen(hand) != 0):
        print("Current Hand: "),
        displayHand(hand)
        #entry = raw_input('Enter word, or a \".\" to indicate that you are finished: ')
        entry = compChooseWord(hand, wordList, n)
        if (entry == 'None'):
            print ('Goodbye! Total score: ' + str(score) + ' points.')
            print
            break
        else:
            if not (isValidWord(entry, hand, wordList)):
                print('Invalid word, please try again.')
                print ('')
                continue
            else:
                score = score + getWordScore(entry,n)
                print('\"'+str(entry)+'\" earned '+str(getWordScore(entry,n))+' points. Total: '+str(score)+' points')
                print ('')
                hand = updateHand(hand, entry)
    if (calculateHandlen(hand) == 0):
        print('Run out of letters. Total score: '+str(score)+' points.')
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    handDealt = 0
    while (1):
        userEntry = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ').lower()
        
        if (userEntry == 'n'):
            print
            while(1):
                mode = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
                if (mode == 'u'):
                    print
                    hand = dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    handDealt = 1
                    break
                elif (mode == 'c'):
                    print
                    hand = dealHand(HAND_SIZE)
                    compPlayHand(hand,wordList,HAND_SIZE)
                    handDealt = 1
                    break
                else:
                    print('Invalid command.')
                    print
                    continue

        elif (userEntry == 'e'):
            print
            break
        
        elif (userEntry == 'r'):
            if (handDealt == 0):
                print ('You have not played a hand yet. Please play a new hand first!')
                continue
            else:
                while(1):
                    print
                    mode = raw_input('Enter u to have yourself play, c to have the computer play: ').lower()
                    if (mode == 'u'):
                        print
                        playHand(hand, wordList, HAND_SIZE)
                        break
                    elif (mode == 'c'):
                        print
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
                    else:
                        print('Invalid command.')
                        continue
        else:
            print('Invalid command.')
            continue

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    # compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
    # compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
    # compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
    # compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12)


