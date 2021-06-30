#!/usr/bin/env python
# coding: utf-8

# In[18]:


#importing the necessary packages
import random
from IPython.display import clear_output


# In[19]:


#game_display_board_format
def display_board(board):
    print("|" + board[1] + "|" +board[2] + "|" + board[3])
    print("-------")
    print("|" + board[4] + "|" +board[5] + "|" + board[6])
    print("-------")
    print("|" + board[7] + "|" +board[8] + "|" + board[9])


# In[20]:


#showing the player's selected value in the screen in display_board
def assign_value_to_list(value,player):
    realboard[value]=player


# In[21]:


# computer choosing a random player to start the game
def rd():
    a=random.randint(0,1)
    if a==0:
        return pl1
    else:
        return pl2


# In[22]:


#logic to check the game_win
def game_win_check(vi,vs):
    if (realboard[1]==vs and realboard[2]==vs and realboard[3]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[4]==vs and realboard[5]==vs and realboard[6]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[7]==vs and realboard[8]==vs and realboard[9]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[1]==vs and realboard[4]==vs and realboard[7]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[2]==vs and realboard[5]==vs and realboard[8]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[3]==vs and realboard[6]==vs and realboard[9]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[1]==vs and realboard[5]==vs and realboard[9]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover
    elif (realboard[3]==vs and realboard[5]==vs and realboard[7]==vs):
        print("Congratulations!!! {0}, You have won this match".format(vi))
        Gameover=True
        return Gameover


# In[23]:


#logic to check game_cant_win
def game_cant_win_check(realboard):
    j=0
    for x in realboard:
        if x=="x" or x=="o":
            j=j+1
    if j==9:
        print("The game cannot be continued further. It has no result")
        Gameover=True
        return Gameover


# In[24]:


#game_logic
while True:
    clear_output()
    print("Welcome to Tic Tac Toe game!!!\n")
    available_values=[1,2,3,4,5,6,7,8,9]
    testboard=["#","1","2","3","4","5","6","7","8","9"]
    realboard=["-","-","-","-","-","-","-","-","-","-"]
    
    pl1="player1"
    player1="x"
    player2="o"
    pl2="player2"
    print("player1, your marker is \"x\"\n ")
    print("player2, your marker is \"o\"\n ")
    print("players,please look into the below playboard\n")
    print("You have to choose a number to mark your value\n")
    print("in the playboard as per the format below\n")
    display_board(testboard)
    print("\n")
    Gameover=False
    random_choice=rd()
    print(random_choice, "You shall be starting the game\n")
    
    while pl1 or pl2:
        
        if random_choice==pl1:
            vi=pl1
            vs=player1
            
        else:
            vi=pl2
            vs=player2
            
        print(vi, "......Enter the position where you want to insert the symbol from the available choices\n", available_values)
        
        try:
            value=int(input())
            available_values.remove(value)
            print("You have choosen", value)
        except:
            print("\n please select from the available values", available_values)
            while value not in available_values:
                value=int(input())
                
            available_values.remove(value)
            print("You have choosen", value)
        assign_value_to_list(value,vs)
        print("                     ")
        display_board(realboard)
        print("                     ")
        game_won=game_win_check(vi,vs)
        
        if game_won:
            break
        else:
            pass
        
        game_not_won=game_cant_win_check(realboard)
        
        
        if game_not_won:
            break
        else:
            pass
        
        if vi==pl2:
            random_choice=pl1
        elif vi==pl1:
            random_choice=pl2
            
          
    print("Do you want to play again?\n")
    print("If yes, please press \"y\" \n")
    print("If no, please press \"n\" \n")
    
    try:
        result=str(input())
    except:
        print("Please press \"y\" or \"n\" \n")
        while result not in ["y", "n"]:
            result=str(input())
            clear_output()
            
    if result=="n":
        clear_output()
        break
    
        
    


# In[ ]:




