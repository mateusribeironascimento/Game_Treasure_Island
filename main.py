print("\033[1m----- Welcome to Treasure Island -----\033[0m")
print("- Your mission is to find the treasure.")

question1 = "You're at a cross road. Where do you want to go? Type \033[1m'left' or 'right'.\033[0m "
question2 = "You come to a lake. There is an island in the middle of the lake. Type \033[1m'wait'\033[0m to wait for a boat or type \033[1m'swim'\033[0m to swim across. "
question3 = "You arrive at the island unharmed. There is a house with 3 doors. One \033[1mred\033[0m, one \033[1myellow\033[0m and one \033[1mblue\033[0m. Which colour do you choose? "

correct1 = 'left'
correct2 = 'wait'
correct3 = 'yellow'

answer1 = input(question1)
if answer1 == correct1:
    answer2 = input(question2)
    if answer2 == correct2:
        answer3 = input(question3)
        if answer3 == correct3:
            print('Congratulations! You found the treasure!')
        else:
            print('Game over!')
    else:
        print('Game over!')
else:
    print('Game over!')

