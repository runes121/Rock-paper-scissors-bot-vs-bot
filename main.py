# Rock Paper Scissors bot
import random

if __name__ == "__main__":
    bot1Point = 0
    bot2Point = 0

    x = 0
    prevPc = 0
    totalRuns = int(input("What should the total amount of runs be?\n"))

    while x < totalRuns:
        x = x + 1
        if prevPc != int((x/totalRuns) * 100):
            prevPc = int((x/totalRuns) * 100)
            print(str(prevPc) + "%")

        botChoicePreProcess: int = random.randint(1, 3)
        botChoice: str = ""

        userChoice = ""
        userChoiceRand = random.randint(0, 3)

        if userChoiceRand == 1:
            userChoice = "rock"
        elif userChoiceRand == 2:
            userChoice = "paper"
        else:
            userChoice = "scissors"

        userChoice.lower()

        if botChoicePreProcess == 1:
            botChoice = "rock"
        elif botChoicePreProcess == 2:
            botChoice = "paper"
        else:
            botChoice = "scissors"

        if userChoice == "rock" and botChoice == "scissors":
            bot1Point = bot1Point + 1
        elif userChoice == "scissors" and botChoice == "rock":
            bot2Point = bot2Point + 1
        elif userChoice == "paper" and botChoice == "rock":
            bot1Point = bot1Point + 1
        elif userChoice == "rock" and botChoice == "paper":
            bot2Point = bot2Point + 1
        elif userChoice == "scissors" and botChoice == "paper":
            bot1Point = bot1Point + 1
        elif userChoice == "paper" and botChoice == "scissors":
            bot2Point = bot2Point + 1

    print("Bot 1 points:" + str(bot1Point))
    print("Bot 2 points:" + str(bot2Point))

    if bot1Point > bot2Point:
        print("Bot 1 won!!")
    elif bot2Point > bot1Point:
        print("Bot 2 won!!")

    print("Total draws: " + str(totalRuns - (bot1Point + bot2Point)))

    input("Press enter to close.")
