print("Welcome to my computer quiz")

play = input("Do you want to play? ")

if play.lower() != "yes":
    quit()

print("Okay lets play: ")
score = 0

#question 1
answer = input("What does CPU satnd for? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

#question 2
answer = input("What does GPU satnd for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

#question 3
answer = input("What does RAM satnd for? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

#question 4
answer = input("What does PSU satnd for? ")
if answer.lower() == "power supply":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

#question 5
answer = input("What does HDD satnd for? ")
if answer.lower() == "hard disk drives":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

#question 6
answer = input("What does SSD satnd for? ")
if answer.lower() == "Solid state drives":
    print("Correct")
    score += 1
else: 
    print("Incorrect")

print("you got " + str(score) + " questions correct")
print("You got " + str((score / 6) * 100) + "%.")