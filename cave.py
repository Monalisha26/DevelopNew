import random
import time
def intro():
    print("You are in a forest full of ghosts.In front of you,you will see two caves.In one cave, there is a ghost gaurding the treasure who is friendly and will share his treasure with you. In other cave there is a ghost is dangerous and will eat you on sight.")
def choosecave():
    cave=''
    while cave!='1' and cave!='2':
        print("which cave will you go into?(1 or 2)")
        cave=input()
    return cave
def checkcave(chosecave):
    print('you approach the cave....')
    time.sleep(2)
    print('it is dark and spooky..')
    time.sleep(2)
    print('a ghost jumps infront of you and......')
    time.sleep(2)
    friendlycave=random.randint(1,2)
    if chosecave==str(friendlycave):
          print('gives u treasure!')
    else:
          print('gobbles u down in one bite!')
playagain='yes'
while playagain=='yes' or playagain=='y':
          intro()
          cavenumber=choosecave()
          checkcave(cavenumber)
          print('Do u want to play again?(yes or no)')
          playagain=input()
