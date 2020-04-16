
#USERMANUAL
#1. Hi, this is the code of the Battleship Game.
#2. Firstly, to play this game , you must input the username and password at the welcome page of the game.
#3. If you do not input the correct username and password , you will not be able to log in to the game. Hence, the game will not give you access
#4. Once you have input the username and password, the board will appear.
#5. After printing the board, you must input your difficulty level. There are 3 difficulties which are Beginner , Intermediate or Advance. If you input an invalid difficulty. You will have to restart the game.
#6. The difficulty Beginner has 80 ships in the game , Intermediate has 50 ships in the game and Advance has 20 ships in the game
#7. After you have input your difficulty level , you will be given the choice to choose whether you want the ships to be shown or not
#8. Depending on whether you choose to show or not to show the locations, you will be able to start the game
#9. Then, you will have to enter the locations to boom in the format of (row,column). Once you have entered, the location you have chosen will be displayed on the board.
#10. If (row<0 or row>20) and (column<0 or column>60) or (row<0 or row>20) or (column<0 or column>60) : , then the location you input will be invalid and you lose 1 boom and 1 attemp.
#11. If (board[row-1][column-1])=='O': or (board[row-1][column-1])=='':, means you guessed that one already or you may have missed the location.
#12.  If [row, column] in shipCoord: , means you have guessed the location of the ship. Else: you missed the location of it.
#13. Lastly, if you destroy 5 ships and still have > 0 booms, you win the game depending on how many attemps you have done. However, if you destroy < 5 ships and have no more booms , you will lose the game.
#14. Depending on whether you win or lose the game , the game will exit once it is over.
#15. This is the end of the usermanual.


#to create new page in c windows  
import os
os.system("cls")                                        

print("\t ########################################################")
print("\t 																	")
print("\t 																	") 
print("\t 		WELCOME TO GROUP 2 BATTLESHIP GAME											")
print("\tTHE USERNAME IS THE COURSENAME WHILE THE PASSWORD IS THE COURSEID                                                                                                                                                   ")
print("\t 																	") 
print("\t 							                                                                                ")
print("\t ########################################################")



username = input("\t\t\t\tUsername  : ")
password = input("\t\t\t\tPassword  : ")

# This is the username and password
username1 = "programmingprinciple"              
password1 = "csc1024"

if username == username1 and password == password1: 
        print(" You are logged into the game\n\n ")
        os.system("cls")
        
# Exit the system if username or password is incorrect
if username1 != username and password1 != password:
        print("Sorry ! No Access!")
        exit()                                                                          



#creating board
board = [['#']*60 for x in range(20)]                           


#print numbers on top of board
def display_board(board):
    print(' ' * 12 + '1', 2, 3, 4, 5, 6, sep = ' ' * 9)                                                 
    print(' ' * 3 + '1234567890' * 6)                                                           

    
    for rowNum, row in enumerate(board, start = 1):
        if rowNum < 10:                                                                                                 
            print(' ',rowNum,' ',''.join(row), sep = '')
        else:
            print(rowNum, ''.join(row))

#starting the game and printing the board
print ("Let's play Battleship!")
display_board(board)




print("Please choose a difficulty")                                                                                                     


difficulty = str(input("Beginner / Intermediate / Advance : "))                                 



if difficulty == "Beginner":
        
        import random

        shipNum = 0
        shipCoord = []
        temp = []
        shipPos = [[] for x in range(20)]

         #prepare 80 random ships
        while shipNum <= 79:
            row = random.randint(1, 20)
            column = random.randint(1, 56)

            while [row, column] in shipCoord or [row, column + 4] in shipCoord:
                    column = random.randint(1, 56)
                    
            #Ship maximum length 5
            for x in range(5):
                shipCoord.append([row, column + x])
                temp.append(column + x)
             #20 rows
            for x in range(20):
                if row == x + 1:
                    shipPos[x].append(temp)
                    break

            temp = []
            shipNum += 1

        #For reference of ship location
        print("\nDo you want us to show you where the ships are?")
        choose = str(input( "\nAnswer with (Show) or enter with other keys to not show : "))
        if choose =='Show':
                print('Ship is in: ')
                for row_number, ship_location in enumerate(shipPos, start = 1):
                        print(row_number, ship_location)
        else:
                print("\nYou have decided to not show the locations\n")
                

        
        
        
    
elif difficulty =="Intermediate":
        

        import random

        shipNum = 0
        shipCoord = []
        temp = []
        shipPos = [[] for x in range(20)]

         #prepare 50 random ships
        while shipNum <= 49:
            row = random.randint(1, 20)
            column = random.randint(1, 56)

            while [row, column] in shipCoord or [row, column + 4] in shipCoord:
                    column = random.randint(1, 56)
    
            for x in range(5):                                                  
                shipCoord.append([row, column + x])
                temp.append(column + x)

            for x in range(20):                                                 
                if row == x + 1:
                    shipPos[x].append(temp)
                    break

            temp = []
            shipNum += 1

        #For reference of ship location
        print("\nDo you want us to show you where the ships are?")
        choose = str(input( "\nAnswer with (Show) or enter with other keys to not show : "))
        if choose =='Show':
                print('Ship is in: ')
                for row_number, ship_location in enumerate(shipPos, start = 1):
                        print(row_number, ship_location)
        else:
                print("\nYou have decided to not show the locations\n")
    

elif difficulty == "Advance":
       

        import random

        shipNum = 0
        shipCoord = []
        temp = []
        shipPos = [[] for x in range(20)]

         #prepare 20 random ships
        while shipNum <= 19:
            row = random.randint(1, 20)
            column = random.randint(1, 56)

            while [row, column] in shipCoord or [row, column + 4] in shipCoord:
                    column = random.randint(1, 56)
    
            for x in range(5):                                                                  
                shipCoord.append([row, column + x])
                temp.append(column + x)

            for x in range(20):                                                                 
                if row == x + 1:
                    shipPos[x].append(temp)
                    break

            temp = []
            shipNum += 1

        #For reference of ship location
        print("\nDo you want us to show you where the ships are?")
        choose = str(input( "\nAnswer with (Show) or enter with other keys to not show : "))
        if choose =='Show':
                print('Ship is in: ')
                for row_number, ship_location in enumerate(shipPos, start = 1):
                        print(row_number, ship_location)
        else:
                print("\nYou have decided to not show the locations\n")
    
else:
        print("\nInvalid Input")                                                                       
        print("Please Restart The Game")
        print(input("Press any key and enter to continue / just press enter"))
        exit()




#For tracing
shipDestroyed = 0    
boom = 15
attemp = 0
while boom > 0:
        #User input the location of ships
        temp = input("Enter location to boom (row, column): ")
        
        #To check if user enter the row and column in correct format, example: 2,4
        if ',' in temp:
                row, column = map(int, temp.split(','))

                #To check if user input a location inside the range of the board
                if (row<0 or row>20) and (column<0 or column>60) or (row<0 or row>20) or (column<0 or column>60) :
                        print("Opps, thats not even in the ocean")
                        attemp = attemp+1
                        boom -=1
                        print("You now left "+ str(boom)+" boom")
                #To check if the user guessed the same ship 
                elif (board[row-1][column-1])=='O':
                        print("You gueesed that one already")
                        attemp = attemp+1
                        print("You now left "+ str(boom)+" boom")
                #To check if the user guessed the same location
                elif (board[row-1][column-1])==' ':
                        print("You gueesed that one already")
                        attemp = attemp+1
                        print("You now left "+ str(boom)+" boom")
                
                #To check if user guessed the ship
                elif [row, column] in shipCoord:
                        print("You guessed the ship")
                        shipDestroyed = shipDestroyed +1
                        print("You now destroyed "+str(shipDestroyed)+" ship")
                        boom -=1
                        print("You now left "+ str(boom)+" boom")
                        attemp = attemp+1

                        for ship in shipPos[row - 1]:
                                if column in ship:
                                        shipCol = ship
                                        break
                        #Print the ship on the board
                        for x in shipCol:
                                board[row - 1][x - 1] = 'O'
                                
                else:
                        #Print blank if user did not guess the ship
                        board[row - 1][column - 1] = ' '                                                                
                        print("You missed my battleship!")
                
                        boom -= 1
                        print("You now left "+ str(boom)+" boom")
                        attemp = attemp +1
                                           
                display_board(board)
                #To check if the user destroyed 5 ships without using all boom       
                if shipDestroyed==5 and boom>0:
                        print("Game over,you won!")
                        
                        #check the total attempt between 13 - 15
                        if attemp >=13 and attemp <=15:                                                         
                                print("You are a novice\n")
                                print("Total Attempts : " ,  attemp , "\n")                             
                                print(input("Press any key to exit"))
                                exit()
                        #check the total attempt between 10 - 12
                        elif attemp >= 10 and attemp <=12:                                                        
                                print("Not too bad\n")
                                print("Total Attempts : " ,  attemp , "\n")                                      
                                print(input("Press any key to exit"))
                                exit()
                        #check if the total attempt less than 10
                        elif attemp <10:                                                                                                 
                                print("You have the talent!\n")
                                print("Total Attempts : " ,  attemp , "\n")                                                     
                                print(input("Press any key to exit"))
                                exit()
                        break
                #User lose if used all the boom and destoyed less than 5 ships
                if boom ==0  and shipDestroyed <5:                                                                                      
                        print("You've no luck today, try again\n")
                        print("You Lose\n")
                        print("Total Attempts : " ,  attemp , "\n")                                              
                        print(input("Press any key to exit"))
                        exit()

                
        else:
                print("Invalid Location..Please use correct format (row,column) or do not use string values!")
                print("One boom will be deducted as punishment!")
                boom -= 1
                attemp = attemp+1
                print("You now left "+ str(boom)+" boom")
                display_board(board)
                #End the game if user used up all boom and destroyed less than 5 ships
                if boom ==0  and shipDestroyed <5:                                                                              
                        print("You've no luck today, try again")
                        print("You Lose\n")
                        print("Total Attempts : " ,  attemp , "\n")
                        exit()
                


        
        




