
# **NUMBER GUESSING GAME - DAY 12**

# %%
print("""
                                   _   _                                  _               _ _ _ 
                            | | | |                                | |             | | | |
  __ _ _   _  ___  ___ ___  | |_| |__   ___   _ __  _   _ _ __ ___ | |__   ___ _ __| | | |
 / _` | | | |/ _ \/ __/ __| | __| '_ \ / _ \ | '_ \| | | | '_ ` _ \| '_ \ / _ \ '__| | | |
| (_| | |_| |  __/\__ \__ \ | |_| | | |  __/ | | | | |_| | | | | | | |_) |  __/ |  |_|_|_|
 \__, |\__,_|\___||___/___/  \__|_| |_|\___| |_| |_|\__,_|_| |_| |_|_.__/ \___|_|  (_|_|_)
  __/ |                                                                                   
 |___/                                                                                    
      """)
print("""welcome to number guessing game!
!'m thinking of a number betwen 1 and 100

""")

#global constants
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def set_difficulty():
   diff_level=input("choose a difficulty type:easy or hard:")
   if diff_level.lower() == "easy":
       return EASY_LEVEL_TURNS
   else:
      return HARD_LEVEL_TURNS


from random import randint
number_to_be_guessed = randint(1,100)

def get_guess(): 
   try :
      guess=int(input("Make a guess:"))
   except ValueError as e:
      print(f'valueerror : {e}')
   return guess


chances=set_difficulty()
for chance in range(chances):
    print(f"you have {chances-chance} number of guesses remaining:")
    guess=get_guess()
    if guess > number_to_be_guessed:
        print("too high")        
    elif guess < number_to_be_guessed:
        print("too low")
    else:
        print("you have guess the correct value!! you won!!!")
        break
    if chance+1==chances:
       print("you have run out of guesses") 
    else:
        print("guess_again")



