import random

#set the top above 10
top_of_range = input("Set top of the range: ")

#checking validation of input
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 10:
        print('Please type a number larger than 10 next time.')
        quit()
else:
    print('Please type a number next time.')
    quit()

#setting range of the guess
random_number = random.randint(0, top_of_range)
guesses = 0

#how to find the number
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number next time.')
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("You were above the number!")
    else:
        print("You were below the number!")

print("You got it in", guesses, "guesses")