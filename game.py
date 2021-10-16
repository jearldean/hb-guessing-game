"""A number-guessing game."""

# Put your code here
#let's make a random number selection

import random
randomizer = random.randrange(1, 100)
#print(randomizer)

#let's greet the player
name = input('Hello, what is your name? ')
print(name + ", I'm thinking of a number between 1 and 100. \n Try to guess my number.")

#let's loop through the game
guess = input("Your guess?")
while randomizer != guess:
    guess_as_int = int(guess)
    #if  guess is more than the value of randomizer, then
    #we should print "too high", and ask to guess again
    if guess_as_int > randomizer:
        print("Your guess is too high, try again.")
        guess = input("Your guess?")
    #elif, print "too low"
    elif guess_as_int < randomizer:
        print("Your guess is too low, try again.")
        guess = input("Your guess?")
    #else, we congradulate the player and stop the loop
    else:
        print("Well done," + name + "!")
        break
