import time
import random

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

def intro(item, option1, option2):
    print_pause("You and Mia went to Hawaii for your honeymoon. You "
                "booked a luxury villa, with a beautiful view of the "
                "beach.")
    print_pause("You both decided to go " + option1 +" at night.")
    print_pause("\n*Timeskip to 10:00pm*\n")
    print_pause("You awaken in your room with a heavy head.")
    print_pause("You looked around for Mia, but she wasn't there.")
    print_pause("Suddenly your phone started ringing. You picked up "
                "the call.")
    print_pause("The person on the other side told you that they have"
                " Mia, but you need to do a job for them, to get Mia"
                " back.")
    print_pause("The job is to collect a package from a person with "
                " " + option2 +" at Oahu beach.")
    print_pause("Also, if you try to get police involved, they will "
                "kill Mia.")

def Oahu_Beach(item, option2):
    print_pause("You rushed to the Oahu beach.")
    print_pause("You looked around for the person with " + option2 + ".")
    print_pause("You finally located him!")
    if "package" not in item:
        print_pause("You feel nervous. You have never done such things.")
        while True:
            choice = input("Would you like to (1) approach him or (2) "
                            "run away?")
            if choice == '1':
                if "package" in item:
                    print_pause("You have already collected the package.")
                    print_pause("There is nothing more to do here.")
                    print_pause("You call the kidnapper and let them know "
                    "that you have the package.")
                    break
                else:
                    print_pause("You approach the person with " + option2 +".")
                    print_pause("\n*code* Do you also feel the MagicInAir! "
                                "*code*\n")
                    print_pause("The person gives you the package and leaves.")
                    print_pause("You called the kidnapper and let them know "
                                "that you have the package.")
                    print_pause("They asked you to leave the package under "
                                "the nearest palm tree. And in return they "
                                "will send Mia home.")
                    print_pause("You reached your villa and found Mia sitting"
                                " at the front porch!")
                    item.append("package")
                play_again()
                break
            if choice == '2':
                print_pause("You ran back to your room.")
                make_choice(item, option2)
                break


def Call_Police(item, option2):
    print_pause("You're very scared. You don't know what to do.")
    print_pause("You finally decided to inform the police.")
    if "package" in item:
        print_pause("You called the police and handed over the package "
                    "and the phone number from which you received the "
                    "call.")
        print_pause("They traced them back and saved Mia.")
    else:
        print_pause("You called the police and told them the whole story "
                    "and gave them the number which you received call from.")
        print_pause("Police asked you to meet the person with " + option2 + ","
                    " so that they can arrest whoever is involved.")
        print_pause("You went to the beach as planned, but the kidnapper "
                    "saw police following you.")
        print_pause("They discarded their phone, and nobody knew what "
                    "happened to Mia after that... ")
    make_choice(item, option2)
    play_again()

def make_choice(item, option2):
    print_pause("\nEnter 1 to Go to the beach.")
    print_pause("Enter 2 to Call police.\n")
    print_pause("What would you like to do?\n")
    while True:
        choice1 = input("(Please enter 1 or 2.)\n")
        if choice1 == "1":
            Oahu_Beach(item, option2)
            break
        elif choice1 == "2":
            Call_Police(item, option2)
            break

def play_again():
    again = input("\nWould you like to play again? (y/n)\n").lower()
    if again == "y":
        print_pause("\n\nExcellent! Restarting the game ...\n\n")
        play_game()
    elif again == "n":
        print_pause("\n\nThanks for playing! See you next time!\n\n")

def play_game():
    item = []
    option1 = random.choice(["clubbing", "for a fancy dinner",
                            "for a long walk on the beach"])
    option2 = random.choice(["red hat", "brown bag"])
    intro(item, option1, option2)
    make_choice(item, option2)

play_game()
