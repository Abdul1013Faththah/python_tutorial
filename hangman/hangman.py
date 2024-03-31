import random
from word import words
from lives_visual import lives_visual_dict
import string

def getvalidwords(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)

    return word.upper()

def hangman(no_of_time):
    while no_of_time > 0:
        
        word=getvalidwords(words)
        word_letters=set(word)#the random choiced word is seperated to single letter as a list
        alphabet=set(string.ascii_uppercase)#bring the 26 letter of alphabet into a list
        used_letters=set()

        live = 5
        
        
        while len(word_letters) > 0 and live > 0:
            print("the letter that u have used", ' '.join(used_letters))
            word_list = [x if x in used_letters else '-' for x in word]
            print('current word:', ' '.join(word_list))
            
            
            
            user_letter=input("Guess a letter : ").upper()#upper means if u enter in simple it will be taken as capital
            if user_letter in alphabet:
                used_letters.add(user_letter)# the user in put is added in to used letter by function .add()
                if user_letter in word_letters:
                    word_letters.remove(user_letter)   
                else:
                    print(lives_visual_dict[live])
                    live = live - 1
                    print('ur down by one live. now u have ',live,'lives')
                    
            elif user_letter in used_letters:
                print("letter already used")
                
            else :
                print("invalid character")

        if live == 0 :
            print('you died!!  the word was',word)
        else:
            print('current word:', ' '.join(word_list))
            print("welldone!!!!!!!")

        no_of_time = no_of_time - 1


print("-------H A N G M A N-------")
print(lives_visual_dict[6])
no_of_time=int(input('enter how many word u need to guess : '))
hangman(no_of_time)

input(" if you want to stop press  any key : ")
