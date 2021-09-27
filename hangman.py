import os
import time
from random import randrange
"""
Shitty code by
    !Goncalo
    *goncalo.horacarvalho@gmail.com
    27/09/2021

ASCII art made using https://patorjk.com/software/taag/#p=display&h=3&v=2&f=Big%20Money-sw&t=GAME%0AOVER
Change var @name and place the same string without spaces in var @dummy_name - should work.
"""
def choose_rand_name():
    names = ["feline van aagten", "jip maijers"]
    return names[randrange(len(names))]
    
name = choose_rand_name()
hangman_top = "                   __/\                    "
hangman_head = "                   | (;-;)                 "
hangman_torso = "                   | /|\                   "
hangman_legs = "                   | / \                   "
hangman_bottom = "                   |_                      "
hangman = [hangman_bottom, hangman_legs, hangman_torso, hangman_head, hangman_top]

def print_hangman():
    print(hangman_top)
    print(hangman_head)
    print(hangman_torso)
    print(hangman_legs)
    print(hangman_bottom)

def print_hangman_title():
    print("  ______   ______  __     __ ________ _______ ")                     
    print(" /      \ /      \/  |   /  /        /       \ ")                     
    print("/$$$$$$  /$$$$$$  $$ |   $$ $$$$$$$$/$$$$$$$  |")                     
    print("$$ |  $$/$$ |  $$ $$ |   $$ $$ |__   $$ |__$$ |")                     
    print("$$ |     $$ |  $$ $$  \ /$$/$$    |  $$    $$< ")                     
    print("$$ |   __$$ |  $$ |$$  /$$/ $$$$$/   $$$$$$$  |")                     
    print("$$ \__/  $$ \__$$ | $$ $$/  $$ |_____$$ |  $$ |")                     
    print("$$    $$/$$    $$/   $$$/   $$       $$ |  $$ |")                     
    print(" $$$$$$/  $$$$$$/     $/    $$$$$$$$/$$/   $$/ ")                     
    print(" __    __  ______  __    __  ______  __       __  ______  __    __ ") 
    print("/  |  /  |/      \/  \  /  |/      \/  \     /  |/      \/  \  /  |") 
    print("$$ |  $$ /$$$$$$  $$  \ $$ /$$$$$$  $$  \   /$$ /$$$$$$  $$  \ $$ |") 
    print("$$ |__$$ $$ |__$$ $$$  \$$ $$ | _$$/$$$  \ /$$$ $$ |__$$ $$$  \$$ |") 
    print("$$    $$ $$    $$ $$$$  $$ $$ |/    $$$$  /$$$$ $$    $$ $$$$  $$ |") 
    print("$$$$$$$$ $$$$$$$$ $$ $$ $$ $$ |$$$$ $$ $$ $$/$$ $$$$$$$$ $$ $$ $$ |") 
    print("$$ |  $$ $$ |  $$ $$ |$$$$ $$ \__$$ $$ |$$$/ $$ $$ |  $$ $$ |$$$$ |") 
    print("$$ |  $$ $$ |  $$ $$ | $$$ $$    $$/$$ | $/  $$ $$ |  $$ $$ | $$$ |") 
    print("$$/   $$/$$/   $$/$$/   $$/ $$$$$$/ $$/      $$/$$/   $$/$$/   $$/ ") 
    print("")
    print("")
    print("")

def name_tag_printer():
    name_tag = []
    for c in range(0, len(name)):
        if name[c] == " ":
            name_tag.append(" ")
        else:
            name_tag.append("_")
        
    print(name_tag)
    return name_tag

def main():
    os.system("clear")
    dummy_name = name.replace(" ", "")
    name_tag_letters = name
    hangman = [hangman_bottom, hangman_legs, hangman_torso, hangman_head, hangman_top]

    print_hangman_title()
    print_hangman()
    print("")
    print("             {0} WORDS, {1} LETTERS".format(name.count(' ')+1, len(name)-1))
    name_tag = name_tag_printer()
    print("")
    print("")
    popping_flag = 1
    hang_output = []

    while True:
        if dummy_name == "":
            os.system("clear")
            print(" __       __ ______ __    __ __    __ ________ _______")  
            print("/  |  _  /  /      /  \  /  /  \  /  /        /       \ ")
            print("$$ | / \ $$ $$$$$$/$$  \ $$ $$  \ $$ $$$$$$$$/$$$$$$$  |")
            print("$$ |/$  \$$ | $$ | $$$  \$$ $$$  \$$ $$ |__   $$ |__$$ |")
            print("$$ /$$$  $$ | $$ | $$$$  $$ $$$$  $$ $$    |  $$    $$< ")
            print("$$ $$/$$ $$ | $$ | $$ $$ $$ $$ $$ $$ $$$$$/   $$$$$$$  |")
            print("$$$$/  $$$$ |_$$ |_$$ |$$$$ $$ |$$$$ $$ |_____$$ |  $$ |")
            print("$$$/    $$$ / $$   $$ | $$$ $$ | $$$ $$       $$ |  $$ |")
            print("$$/      $$/$$$$$$/$$/   $$/$$/   $$/$$$$$$$$/$$/   $$/ ")
            print("                __       __       __                    ")
            print("              _/  |_   _/  |_   _/  |_                  ")
            print("             / $$   \ / $$   \ / $$   \                 ")
            print("            /$$$$$$  /$$$$$$  /$$$$$$  |                ")
            print("            $$ \__$$/$$ \__$$/$$ \__$$/                 ")
            print("            $$      \$$      \$$      \                 ")
            print("             $$$$$$  |$$$$$$  |$$$$$$  |                ")
            print("            /  \__$$ /  \__$$ /  \__$$ |                ")
            print("            $$    $$/$$    $$/$$    $$/                 ")
            print("             $$$$$$/  $$$$$$/  $$$$$$/                  ")
            print("               $$/      $$/      $$/                    ")
            time.sleep(2)
            os.system("clear")
            print("             Here's the key...")
            print("")
            print("             .---.")
            print("            /    |\________________")
            print("           |  ()  | ________   _   _)")
            print("            \    |/        |_| |_|")
            print("             `---'           |_|")
            print("")
            print("Message will self destruct in 3 seconds")
            print("1")
            time.sleep(1)
            print("2")
            time.sleep(1)
            print("3")
            time.sleep(1)
            os.system("clear")
            exit()
        letter = input("Input: ")
        i = 0
        for l in range(0, len(dummy_name)):
            if letter == dummy_name[l]:
                # os.system("clear")
                print("Yes.")
                dummy_name = dummy_name.replace(letter,"",1)
                popping_flag = 0
                for i in range(0, len(name_tag_letters)):
                    if name_tag_letters[i] == letter:
                        name_tag[i] = name_tag_letters[i]
                        name_tag_letters = name_tag_letters.replace(letter," ",1)
                        break
                break

        if not hangman:
            os.system("clear")
            print("  ______   ______  __       __ ________ ")
            print(" /      \ /      \/  \     /  /        |")
            print("/$$$$$$  /$$$$$$  $$  \   /$$ $$$$$$$$/ ")
            print("$$ | _$$/$$ |__$$ $$$  \ /$$$ $$ |__    ")
            print("$$ |/    $$    $$ $$$$  /$$$$ $$    |   ")
            print("$$ |$$$$ $$$$$$$$ $$ $$ $$/$$ $$$$$/    ")
            print("$$ \__$$ $$ |  $$ $$ |$$$/ $$ $$ |_____ ")
            print("$$    $$/$$ |  $$ $$ | $/  $$ $$       |")
            print(" $$$$$$/ $$/   $$/$$/      $$/$$$$$$$$/ ")
            print("  ______  __     __ ________ _______    ")
            print(" /      \/  |   /  /        /       \   ")
            print("/$$$$$$  $$ |   $$ $$$$$$$$/$$$$$$$  |  ")
            print("$$ |  $$ $$ |   $$ $$ |__   $$ |__$$ |  ")
            print("$$ |  $$ $$  \ /$$/$$    |  $$    $$<   ")
            print("$$ |  $$ |$$  /$$/ $$$$$/   $$$$$$$  |  ")
            print("$$ \__$$ | $$ $$/  $$ |_____$$ |  $$ |  ")
            print("$$    $$/   $$$/   $$       $$ |  $$ |  ")
            print(" $$$$$$/     $/    $$$$$$$$/$$/   $$/   ")
            print("")
            print("")
            print_hangman()
            time.sleep(2)
            os.system("clear")
            main()
            break
        elif popping_flag == 1:
            hang_output.append(hangman.pop())
        popping_flag = 1

        os.system("clear")
        print_hangman_title()
        print(name_tag)
        for h in hang_output:
            print(h)
        
if __name__ == '__main__':
    main()