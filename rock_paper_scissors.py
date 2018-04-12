# Create Rock, Paper, Scissors
# Use all of your knowledge of Conditional Statements, While Loops, and For Loops
# to make a 2 player Rock, Paper, Scissors game. Here are the game requirements:
#
# - At least 2 players need to be able to enter their names.
# - Each Player should be able to select an option.
# - Players should not see each other's answers. Hint: research "\n".
# - The specific Player that wins should get a congratulations message. Tied
#   players should also receive a special message.
# - After each round the players should be able to choose to restart the game.
# - Your project should use at least one If Statement, While Loop, and For Loop.
#   Don't forget about Else If and Else Statements.
# - Rock beats Scissors. Paper beats Rock. Scissors beats Paper. Any more rules
#   are up to you!


print("\nWeclome to Rock, Paper, Scissors!\n")

# Getting the names for each player:
# raw_input is a function that takes a string, prints it to the console, and
# then waits for you to type something in and hit Enter. Whatever you typed it
# will get made into a string, and the variable declared before the `=` will
# get that string as its value
#
# source: http://www.pythonforbeginners.com/basics/getting-user-input-from-the-keyboard
player1_name = raw_input("Please enter player 1's name: ")
player2_name = raw_input("Please enter player 2's name: ")


# Start the game loop
# We're doing `while True` because we want the loop to keep going forever until
# something within the loop's code actually tells it to exit the loop by calling
# the `break` command
while True:
    # Just to add some space in the console
    print("\n")
    # Again, using the raw_input function to get input from the players
    player1_choice = raw_input(player1_name + ", rock, paper, or scissors? ")
    # This loop will run 100 times, and each time is just printing a "\n" to the
    # console, so that the other player won't see what they typed after they hit
    # enter
    for x in range(0, 100):
        print("\n")

    # Same thing for player 2
    player2_choice = raw_input(player2_name + ", rock, paper, or scissors? ")
    for x in range(0, 100):
        print("\n")

    # This just checks each possible outcome and prints the corresponding message
    #
    # This part of the code can be made much smaller and more simple, and that
    # could be a good challenge for the kids
    if player1_choice == player2_choice:
        print("Oh my goodness, you both tied!")
        print("You both chose " + player1_choice + "!\n")
    elif player1_choice == "paper" and player2_choice == "rock":
        print("Good call " + player1_name + ", you win!")
        print(player1_choice + " beats " + player2_choice)
    elif player1_choice == "rock" and player2_choice == "scissors":
        print("Good call " + player1_name + ", you win!")
        print(player1_choice + " beats " + player2_choice)
    elif player1_choice == "scissors" and player2_choice == "paper":
        print("Good call " + player1_name + ", you win!")
        print(player1_choice + " beats " + player2_choice)
    elif player1_choice == "paper" and player2_choice == "scissors":
        print("Good call " + player2_name + ", you win!")
        print(player2_choice + " beats " + player1_choice)
    elif player1_choice == "rock" and player2_choice == "paper":
        print("Good call " + player2_name + ", you win!")
        print(player2_choice + " beats " + player1_choice)
    elif player1_choice == "scissors" and player2_choice == "rock":
        print("Good call " + player2_name + ", you win!")
        print(player2_choice + " beats " + player1_choice)
    else:
        print("Oops! Someone didn't pick a rock, paper, or scissors")
        print(player1_name + " picked " + player1_choice)
        print(player2_name + " picked " + player2_choice)

    play_again = raw_input("\nWant to play again? (yes/no): ")

    if play_again != "yes":
        print("\nThanks for playing!\n")
        break
