import random
min_val = 1
max_val = 6

roll_again = 'yes'

#Loop
while roll_again == 'yes' or roll_again == 'y':
    print("Rolling the dices...")
    print('The values are: ')
    
    print(random.randint(min_val, max_val))
    print(random.randint(min_val, max_val))
    
    roll_again = input('Do you wish to roll again? ')