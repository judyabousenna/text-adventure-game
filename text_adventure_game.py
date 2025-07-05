# Setup
import random , time
boss = ["witch" , "demon" , "vampire" , "ogre" , "ghoul"]

def print_pause(string) :
    print(string)
    time.sleep(0.2)
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]
points = 0
reward_loss = 10
continue_in_the_game = 'y'
# Introduction
print_pause("You wake up to find yourself all alone in a dark forest, hearing the voices of wild animals around you.")
print_pause("you:where am i?")
print_pause("unfamiliar voice:(laughs) Welcome, hero. The kingdom has brought you here to save us all…")
name = input("What is your name, adventurer?\n")
print_pause("Greetings, " + name + ". Let us go on a quest!")
print_pause("you: what am i supposed to do?")
print_pause("unfamiliar voice: you will find out soon.")
print_pause("you were brought here on a mission, to save us from the darkness that lurks in the shadows. One that seeks to destroy everything we hold dear…")
while continue_in_the_game == 'y' :
# Start of game
    i = random.randint(0, 4)
    print_pause("you get up and follow the guy deeper into the forest until you find a village ,\nthe bakers selling their pastries and the greengrocers screaming their unique prices \nyou find yourself feeling like you’re back at your home.")
    print_pause("A sense of intimacy and nostalgia came rushing over you as you walk and watch kids running around. As you walk you find yourself alone again.")
    print_pause(" You suddenly bump into someone and they fall to the ground, you look down to see a woman that looks different than the other NPCs,\nshe looked at you with a grin")
    print_pause("the woman: (laughs) You’re finally here, “hero”  I’ve been waiting for you…")
    print_pause("The woman starts floating in the air, her clothes burning and a black dress shown beneath them.\nher hair starts burning up as she looks at you with an evil look")
    print_pause("The woman: I would love having the pleasure to end you with this kingdom…")
    print_pause("you start thinking what to do as you get two ideas\n")
    print_pause("Enter 1 to start fighting the " + boss[i]+"  for the kingdom’s sake.\n" )
    print_pause("Enter 2 run away  before she catches you.\n")
    option1 = input()
    if option1 == '1':
        points =points + reward_loss
        print_pause( "you get a sword in your hand and the ability to fly. You fly and face her with your sword, she casts spells putting you into illusions.")
        print_pause("Enter 1 to start killing all the illusions.")
        print_pause("Enter 2 to burst to the first one risking it to be the real one.")
        option2 = input()

        if option2 == '1':
            print_pause("you start killing the illusions successfully when you think you are going to win you find something to hit in your chest…just to be killed by the sword of the "+ boss[i])
            print_pause("GAME OVER")
            continue_in_the_game = input("Would you like to play again (y/n) ")
        else:
            print_pause("you flash into her like a wrecking ball cutting her throat. you get down with her head to find everyone cheering. \nYou realize you have saved the kingdom. “our mighty hero”.")
            print_pause("You wake up in your bed again thinking you were just dreaming. But as you get up you see the same sword you were fighting with, \nyou smile as you put it in your drawer")
            print_pause("THE END")
            print_pause ("points = " + str(points))
            continue_in_the_game = input("Would you like to play again (y/n) ")
    else:
        points = points - reward_loss
        print_pause("she starts running after you, only to catch you after a few seconds and kill you")
        print_pause ("points = " +  str(points))   
        print_pause("GAME OVER")
        continue_in_the_game = input("Would you like to play again (y/n) ")