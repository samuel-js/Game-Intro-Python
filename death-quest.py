# The Quest
from sys import exit


def mountains():
    print "Welcome to the mountains."


end_line = "\nBad Choice !!!!!!!!!"
game_over = "\nNice to see you die. Game Over !!"


def the_lake():
    print "\nYou have arrived to Big Lake."
    print "Would you like to swim or catch some sun?"
    print "(Enter '1' to swim, '2' to catch some sun)"

    next = raw_input("> ")

    if next == "1":
        print "The water is warm and deep, but... Something seems to be wrong..."
        go_on = raw_input("Press 'Enter' if you dare to continue > ")
        print
        print "You realize you don't know how to swim, remember!"
        print game_over
        print end_line
    elif next == "2":
        print "You burn to death. Remember the climate change?"
        print game_over
        print end_line
    else:
        print "You obvioulsy don't know how to write numbers. So..."
        print "You die!! "
        print game_over
        exit(0)


def the_old_tree():
    print "\nYou've come to the old tree."
    print "Are you sure you want to continue? ('yes' or 'no' )"
    next = raw_input("> ")

    if next == "no":
        print "You coward!"
        print game_over

def the_city():
    print "\nIt's great to be in the city. Right?"
    print "It's starting to rain."
    print "What do you wish to do?."
    print " Enter '1' to open the umbrella or '2' to start running"
    print

    next = raw_input("> ")

    if next == "1":
        print "It just stopped raining. Sorry :-) "
        print "Do you want to take a walk instead? (Type 'yes' or 'no' )"
        next = raw_input()

        if next == "yes":
            print " Sorry, It started raining again. Opps :-)"
            print " It rains a lot so you die!."
            print game_over
        elif next == "no":
            print "Are you tired?", "I thought so..."
            print "I'll take you to the Old Tree. It's not too far..."
            print " The wind takes you slowly to the Old Tree..."
            the_old_tree()
        else:
            print "Go to bed!"
            print game_over

    elif next == "2":
        print "You fall and you break a leg... and then you die."
        print game_over


def start():
    print "\nHow do you want to die?"
    print "Enter '1' to die in The Lake or '2' to die in The City. "

    next = raw_input("> ")

    if next == "1":
        the_lake()
    elif next == "2":
        the_city()
    else:
        print "Did you lear the numbers in school?"
        print "C'mon I know you can do it!!"
        print "Please try again", "Enter '1' or '2'"
        start()

        next = raw_input("> ")


def intro():
    print "\nWelcome to Death Quest!"
    print "At the moment there are only two different ways of dying!"


intro()

start()
