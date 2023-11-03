# write 'hello world' to the console   
print('hello world')

# player select rock, paper, or scissors
player = input('rock (r), paper (p), or scissors (s)?')

# computer select rock, paper, or scissors
# import random module
import random

# create a list of play options
options = ['r', 'p', 's']

# assign a random play to the computer
computer = random.choice(options)


# print out the player and computer selections
print('player:', player, 'vs', 'computer:', computer)

# determine who wins
# rock beats scissors
# paper beats rock
# scissors beats paper
if player == computer:
    print('tie')
elif player == 'r' and computer == 's':
    print('player wins')
elif player == 'r' and computer == 'p':
    print('computer wins')
elif player == 'p' and computer == 'r':
    print('player wins')
elif player == 'p' and computer == 's':
    print('computer wins')
elif player == 's' and computer == 'p':
    print('player wins')
elif player == 's' and computer == 'r':
    print('computer wins')
else:
    print('something went wrong')

 






