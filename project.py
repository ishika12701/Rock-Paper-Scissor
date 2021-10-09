import random




def computer(CHOICES,user_score,computer_score,user_name):
    while True:

        user_choice = input(" Choose (rock or paper or scissor) :  ")
        


        if user_choice in CHOICES:
            

            computer_choice = random.choice(CHOICES)
            
            print(f" You choose {user_choice} and computer choose {computer_choice} ")
            if user_choice == "rock":
                if computer_choice == "scissor":
                    
                    print(f" {user_name} win !")
                    user_score += 1

                elif computer_choice == "paper":
                    print(" computer win!")
                    computer_score += 1
                    
                else :
                    print(" match is draw")
            
            elif user_choice == "paper":
                if computer_choice == "rock":
                    print(f" {user_name} win! ")
                    user_score += 1
                    
                elif computer_choice == "scissor":
                    print(" computer win!")
                    computer_score += 1
                    
                else:
                    print("match is draw ")

            elif user_choice == "scissor":
                if computer_choice == "paper":
                    print(f" {user_name} win!")
                    user_score += 1
                    
                elif computer_choice == "rock":
                    print("computer win!")
                    computer_score += 1
                    
                else:
                    print("match is draw") 
                
            
            
            
            

        else:
            print(f" You typed {user_choice}. which is not a valid throw. ")

        again = input( " Play again (y/n)? ")

        if again.lower() == 'n':
            break
        

    print(f" {user_name} score {user_score} and computer score {computer_score} ")
    


def opponent(CHOICES,user_score,computer_score,user_name,opponent_name):
    
    while True:

        user_choice = input(f"{user_name} Choose (rock or paper or scissor) :  ")
        computer_choice = input(f"{opponent_name} Choose (rock or paper or scissor): ")
         


        if user_choice and computer_choice in CHOICES:
                        
            
            print(f" You choose {user_choice} and {opponent_name} choose {computer_choice} ")
            if user_choice == "rock":
                if computer_choice == "scissor":
                    
                    print(f" {user_name} win !")
                    user_score += 1

                elif computer_choice == "paper":
                    print(f" {opponent_name} win!")
                    computer_score += 1
                    
                else :
                    print(" match is draw")
            
            elif user_choice == "paper":
                if computer_choice == "rock":
                    print(f" {user_name} win! ")
                    user_score += 1
                    
                elif computer_choice == "scissor":
                    print(f" {opponent_name} win!")
                    computer_score += 1
                    
                else:
                    print("match is draw ")

            elif user_choice == "scissor":
                if computer_choice == "paper":
                    print(f" {user_name} win!")
                    user_score += 1
                    
                elif computer_choice == "rock":
                    print(f" {opponent_name} win!")
                    computer_score += 1
                    
                else:
                    print("match is draw") 
                
            
            
            
            

        else:
            print(f" You typed {user_choice} and {computer_choice}. which is not a valid throw. ")

        again = input( " Play again (y/n)? ")

        if again.lower() == 'n':
            break
        

    print(f" {user_name} score {user_score} and {opponent_name} score {computer_score} ")



if __name__=="__main__":


    CHOICES = ["rock","paper","scissor"]
    user_score = 0
    computer_score = 0
    print(" Hello welcome ")
    user_name = input( " Enter your name.... ")
    
    player = input(" Two player or One player?")
    
    if player.lower() == "one player":

        computer(CHOICES,user_score,computer_score,user_name)
    
    elif player.lower() == "two player":
        opponent_name = input("Enter player 2 name......")

        opponent(CHOICES,user_score,computer_score,user_name ,opponent_name)

    
    print("Thank you for playing....  ")