import time
import random
from urllib import response


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def intro():
    print_pause("You wake up and open your eyes.")
    print_pause("You feel a stinging pain and "
                "feel your clothes are damp near your stomach.")
    print_pause("Around you is what looks to be a cave like structure"
                " with a tunnel showing the way forward. "
                "Above is the hole that you imagine is "
                "what caused you to be down here.")
    print_pause("Your trusty pack lies nearby with some everyday "
                "tools scattered about that"
                " had falled out upon your landing.")
    print_pause("Basic medical supplies, some food, and your canteen "
                "of water. Your belt still has your sword strapped in.\n")
    print_pause("You feel like you have lost some blood and need "
                "some medical attention.")
    print_pause("You should be able to check your kit and find "
                "some bandages even if it takes some time.")
    print_pause("However time is of the essence and you need to get "
                "out of here and patch yourself up after.\n")


def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower()
        if option1 == response:
            break
        if option2 == response:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def next_step():
    print_pause("What would you like to do next?")


def injury():
    response = valid_input("Do you take the time to patch yourself up now or "
                           "wait until later?",
                           "now", "later")
    if "now" in response.lower():
        print_pause("You feel much better and the bleeding has stopped."
                    " This should hold until you reach the village. "
                    "Now time to face the tunnel!")
    if "later" in response.lower():
        print_pause("You were never good with"
                    " medical stuff and decided you "
                    "need to get back home right away and find the doc."
                    " Now time to face the tunnel!")


def entrance():
    print_pause("The entrance with the rocky walls are in front of you."
                "The hole in the ceiling showing where"
                " you came in and a small bit "
                "of blood on the ground from your wounds.")
    print_pause("There is nothing for you to do in this room as the "
                "walls are too high to climb in your condition.")


def tunnel_unexplored():
    explore = valid_input("Would you like to move forward?", "yes", "no")
    if explore == "yes":
        print_pause("This tunnel holds just enough light from the "
                    "entrance hole to allow you to see.")
        print_pause("After walking for a few minutes, you spot the "
                    "faint light of a fire ahead.")
    if explore == "no":
        print_pause("You can't expect someone to come rescue you now, "
                    "you are down a large hole!")
        print_pause("This tunnel holds just enough light from the "
                    "entrance hole to allow you to see.")
        print_pause("After walking for a few minutes, you spot "
                    "the faint light of a fire ahead.")


def tunnel_exit():
    print_pause("You take your hard fought loot along with the "
                "rest of your items and head towards the new tunnel.")
    print_pause("As you get closer you start to feel the fresh "
                "air outside and soon enough you feel the"
                " warm sun on your skin.")
    print_pause("You get your bearings and begin to head home but while "
                "walking you think about how you handled"
                " that goblin and how maybe "
                "just maybe this could be the start"
                " of something new for you.")
    print_pause("The birth of a new adventurer!")
    player_death()


def goblin_horde():
    horde = ["gauntlet", "gold bar", "helmet", "belt"]
    horde_loot = random.choice(horde)
    print_pause("Congratulations you found a " + horde_loot +
                " inside of the goblin's lair!")


def goblin_startled():
    print_pause("The goblin takes out a dagger and leaps at you "
                "while you are surprised by their hideous visage.")
    print_pause("The goblin is heavier than you thought and as he "
                "attacks you are not able to react fast"
                " enough with your current "
                "wounds and your vision goes black!")
    player_death()


def goblin_surprise():
    print_pause("You sneak up towards the goblin, your sword drawn "
                "as carefuly and quietly as you can.")
    fight = valid_input("Do you take out the"
                        " goblin in front of you?", "yes", "no")
    if fight == "yes":
        print_pause("Your sword cuts through the goblin like "
                    "butter and he falls to the ground.")
        print_pause("Nearby you see some supplies that must "
                    "have belonged to him as well as"
                    " another tunnel leading elsewhere.")
        goblin_horde()
        tunnel_exit()
    if fight == "no":
        print_pause("You hesitate to swing, would this creature harm "
                    "me if I were to show them mercy?")
        print_pause("While contemplating if you should continue to swing,"
                    "the goblin turns and sees your"
                    " outline with the sword drawn.")
        print_pause("Any doubts you had about mercy are quickly snuffed "
                    "as the goblin jumps at you"
                    " claws and teeth lashing out.")
        print_pause("You do your best to hold him off but he is too "
                    "much for you and your vision goes dark!")
        player_death()


def goblin_area():
    print_pause("As you move closer to the fire and the light source"
                "the figure of a small humanoid"
                " creature comes out of the light "
                "with its back turned towards you.")
    sneak = valid_input("Would you like to"
                        " sneak up on the creature silently?", "yes", "no")
    if sneak == "yes":
        print_pause("You are able to see the creature is a goblin "
                    "typically known to be dangerous"
                    " and should be dealt with "
                    "swiftly. The goblin is surprised!")
        goblin_surprise()
    if sneak == "no":
        print_pause("It would be quite rude to sneak up on someone "
                    "that may help you out so you decide to shout 'Hello!'")
        print_pause("The creature whips around and you can now see "
                    "this has been a goblin all along known"
                    " to be dangerous! You "
                    "no longer have the element of surprise!")
        goblin_startled()


def player_death():
    dead = valid_input("Would you like to play again?", "yes", "no")
    if dead == "yes":
        adventure_game()
    if dead == "no":
        print_pause("Thank you for playing!")
        exit()


def adventure_game():
    intro()
    injury()
    tunnel_unexplored()
    goblin_area()
    tunnel_exit()


adventure_game()
