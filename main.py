from random import randint


# creating 3 slots
slot_1 = ["Apple","7","Orange"]
slot_2 = ["Apple","7","Orange"]
slot_3 = ["Apple","7","Orange"]

point = 200 #providing points to the player at the start of the game

print("Welcome to SLOT MACHINE! AS YOU ARE A FIRST TIMER YOU GET 200 COINS FOR FREE.")

run = True

while run:
    bet_value = int(input("Enter the amount of coin you want to bet: ")) # will add code later so that player must choose possible amount

    s1_value = randint(0,2)
    s2_value = randint(0,2)
    s3_value = randint(0,2)



    if slot_1[s1_value] == slot_2[s2_value] == slot_3[s3_value] == '7': #checks if each slot got 7 in the center row
        print(f"YOU GOT {slot_1[s1_value]} {slot_2[s2_value]} {slot_3[s3_value]} IN THE CENTER")
        point = point + (bet_value*3)
        print(f"you win {bet_value*3} coins.")
    elif slot_1[s1_value] == slot_2[s2_value] == slot_3[s3_value] == "Apple": #checks if each slot got 7 in the lower row
        print(f"YOU GOT 7 7 7 IN THE LOWER ROW")
        point = point + (bet_value*2)
        print(f"you win {bet_value*2} coins.")
    elif slot_1[s1_value] == slot_2[s2_value] == slot_3[s3_value] == "Orange": #checks if each slot got 7 in the upper row
        print(f"YOU GOT 7 7 7 IN THE UPPER ROW")
        point = point + (bet_value*2)
        print(f"you win {bet_value*2} coins.")
    elif (s1_value == 0 and s2_value == 1 and s3_value == 2) or (s1_value == 2 and s2_value == 1 and s3_value == 0): #checks if player got 7s diagonally
        print(f"YOU GOT 7 7 7 IN THE DIAGONALS")
        point += bet_value
        print(f"you win {bet_value} coins.")
    else:
        print(f"YOU DIDN'T GET 7 7 7 AT ALL")
        print(f"you lose {bet_value} coins.")
        point -= bet_value
    
    if (point > 0):
        print(f"after the round your got {point} coins.")
        play_again = input("Press Y/y if you want to play again  or press N/n if you want to quit: ") #need to update in future so player must choos either Y/y or N/n
        if (play_again == 'n' or play_again == "N"):
            print(f"You got in total {point} coins. GOOD BYE. HOPE TO SEE YOU AGAIN")
            run = False
    else:
        print(f"after the round your got 0 coins.")
        run = False

