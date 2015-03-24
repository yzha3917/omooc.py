import random
import math
import simplegui

minimum = 0;
maximum = 100;
picked = 0;
guessed = 0;
n = 0;
m = 0;

def new_game():
    print "A new game has started! "
    print "Choose the range you wanna play,"
    print "and then, you guess an integer from this range."
    
    
def lowest(low):
    global minimum 
    minimum = float(low)
    print "You just input",int(minimum), "as the lower boundary"
    return

def highest(high):
    global maximum
    global n
    global m
    maximum = float(high)
    if minimum >= maximum:
        print "Don't....Can't you play this game normally..."
        print "Now input a new highest number"
        return
    else:
        print "and",int(maximum), "as the higher boundary of the range"
        n = math.log(maximum-minimum+1,2)
        n = math.ceil(n)
        n = int(n)
        m = n
        print "Therefore, you can try",n,"times at most."
        return

def arange():
    global picked
    picked = random.randrange(minimum,maximum)
    #print picked
    return 

def input_guess(guessed):
    global n
    global m
    print "You just guessed",guessed
    
    while (n > 1):
   
        if float(guessed) < minimum or float(guessed) >= maximum:
            print "What, You just set the range yourself..."
            print "Now guess it again, and this time, do it right"
            return
        elif float(guessed) == float(picked) == 42:
            print "OMG, 42 it is, What's the odds!"
            return
        elif float(guessed) == float(picked):
            # Beginner's luck
            if n == m:
                print "Unbelieveble! You got it right first time."
                print "Well, maybe it's just beginner's luck."
                print "Dare you play it one more time?"
            else:
                print "Now we are talking."
            new_game()
            return
        elif float(guessed) == 42:
            n -= 1
            print "Seriously? 42? You are SO predictable."
            print "Now you can still try", n, "times."
            return
        elif float(guessed) < float(picked):
            n -= 1
            print "You might want to pump it up."
            print "Now you can still try", n, "times."
            return
        elif float(guessed) > float(picked):
            n -= 1
            print "But man, it's too high."
            print "Now you can still try", n, "times."
            return

        else:
            print "I don't know what you're talking about..."
            return
    else:
        print "Wrong again??"
        print "You are really not supposed to see this line of string, if you play it right.."
        print "Now dummy, this game will start over. And this time, you entry the average of the two extreme values of the correct range."
        print "Can you do it?"
        new_game()
    
frame = simplegui.create_frame('Testing', 200, 200)

frame.add_input("Lowest number", lowest,100)
frame.add_input("Highest number", highest,100)
frame.add_button('Its Showtime!',arange,100)
frame.add_input("Do you have that luck?", input_guess,100)

new_game()
