"""
The Goal: Despite the name, the actual “hangman” part isn’t necessary. The main goal here is
to create a sort of “guess the word” game. The user needs to be able to input letter guesses.
A limit should also be set on how many guesses they can use. This means you’ll need a way to
grab a word to use for guessing. (This can be grabbed from a pre-made list.
No need to get too fancy.) You will also need functions to check if the user has actually
inputted a single letter, to check if the inputted letter is in the hidden word (and if it is,
how many times it appears), to print letters, and a counter variable to limit guesses.
"""

import random

movie_list=['the shawshank redemption','the godfather','the dark night',
'angry birds','schindlers list','pulp fiction' 'the good the bad the ugly', 'fight club',
'inception','shutter island']

vowel1=['a','e','i','o','u']



def display(vowel,movie):

    for i in movie :
        if i in vowel : print(i,end=' ')
        elif i==' ': print(' ',end=' ')
        else: print('_',end=' ')


def full_guess(movie) :
    #print(movie)
    word=input(" Enter movie name  ").lower().strip()

    if word==movie:
        print(" \n ")
        print( " Congratulations you have Won!! "  )
        quit()

    else:
        print('\n')
        print(" nope -> you are not ready yet.. guess one letter again ..  ")


def hangman(movie,t) :

    #print(movie)
    temp=movie
    print( " You have ", t , " Guesses"  )
    print('\n')

    vowel=['a','e','i','o','u']
    display(vowel,movie)

    x=0

    while(x<=t) :

        print('\n')
        print(" No. of Guesses left : ")
        print(t-x)
        print('\n')

        temp=list(filter((lambda x: x not in vowel and x!=' '),temp))
        print('\n')

        guess=input(" Enter your letter ").lower()

        if guess=='':
            if temp==[] :
                print( " Congratulations !! You Won! ")
                break
            else: print(" Not valid entry ")

        elif guess=='word':
            full_guess(movie)
            x+=1

        elif ord(guess)>=97 and ord(guess)<=122 :
            x=x+1
            if guess in movie : vowel.append(guess)
            display(vowel, movie)
            print("\n")

            if temp==[] :
                print( " Congratulations !! You Won! ")
                print('\n')
                print('\n')
                break


        elif guess=='leave' : quit()

        else: print(" letter not valid - type only a-z ")


    if x>t:
        print( " You are out of guesses.. ")
        print('\n')
        print(" the movie name was:   ", movie)



def instructions():

    print('\n')
    print('\n')
    print('......................................................................')
    print('......................................................................')
    print(" Instructions!!  ")
    print('\n')
    print(" This game is to guess the name of a movie  ")
    print('\n')
    print( ' all the vowels are diplayed -- guess the remaining letters ! ')
    print('\n')
    print(' type leave to quit the game ')
    print('\n')
    print(" if you think you got the name of the movie ")
    print('\n')
    print(" type -> word  to Guess the full name of the movie")
    print('.....................................................................')
    print('\n')


def guesses(x):

    t=input( " How many guesses to you want : "   )

    if t=='leave' : quit()

    try: t=int(t)

    except :
        print(" enter a numerical value only  ")
        t=input( " How many guesses to you want : "   )

#print(x)
    count=0
    for i in movie_list[x] :
        if i in vowel1: count+=1
        if i==' ': count-=1

    if t<len(movie_list[x])-count:
        print('\n')
        print('\n')
        print(" Number of guesses increased by system -> play ")
        t=len(movie_list[x])-count
    return t



instructions()
x=random.randint(0,len(movie_list)-1)
print('\n')
hangman(movie_list[x],guesses(x))
