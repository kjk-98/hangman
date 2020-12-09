from random import seed
from random import randint

mywords = ['apple', 'banana', 'orange', 'strawberry', 'potato']
selection = randint(0, 4)
size = len(mywords[selection])
myword = mywords[selection]
chance = 6
progress = 0
flag = True

while flag:
    status = progress
    print("your remain chance: ", chance)
    guess = input("say your guess!\n")

    for j in range(size):
        if guess == myword[j]:
            progress = progress + 1

    if status == progress:
        chance = chance - 1

    if chance == 0 or progress == size:
        flag = False

############################################
if progress == size:
    print("you win!\n the selected word was: ", myword)
else:
    print("you lose!\n the selected word was: ", myword)
