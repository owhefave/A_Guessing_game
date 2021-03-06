#A guessing game using the class function
import random
user_range= int(input("Please input the range of numbers you want to make a guess: "))
computer_guess=random.randint(0,user_range)
class Guessing_Game():
    def __init__(self):
        self.user_guess=0
        self.computer_guess=0
        self.user_range=0
    def start_game(self,user_range):
        print(f"You are about to guess a number between 0 to {self.user_range}")
    def game_algorithm(self):
        trial=1
        while trial<4:
            user_guess= int(input("\nPlease guess the lucky number: "))
            prompt= "You have made {} attempt: ".format(trial)
            print(prompt)
            if user_guess == computer_guess:
                print("\nCongratulation, you have won the lottery")
                break
            elif user_guess< computer_guess:
                print("Hint:The lucky number is less than the number you entered")
            elif user_guess>computer_guess:
                print("Hint:The lucky number is greater than the number you entered")
            trial+=1
        else:
            print("\nTry again next time")
            print("The Lucky number is: ", computer_guess)      
my_guess= Guessing_Game()
my_guess.start_game(user_range)
my_guess.game_algorithm()
