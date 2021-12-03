# IF YOUR GOING TO MODIFY OR PUBLISH THIS TOOL PLEASE CREDIT ME
# PLEASE DO NOT SELL OR USE THIS FOR WRONG PURPOSES
# I WILL MAKE MORE PROJECTS SOON STAY TUNED ;)


import time
import random





game_name = '''
 ██▓ ███▄ ▄███▓  ▄████  █    ██  ██▀███       █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███  
▓██▒▓██▒▀█▀ ██▒ ██▒ ▀█▒ ██  ▓██▒▓██ ▒ ██▒   ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
▒██▒▓██    ▓██░▒██░▄▄▄░▓██  ▒██░▓██ ░▄█ ▒   ▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
░██░▒██    ▒██ ░▓█  ██▓▓▓█  ░██░▒██▀▀█▄     ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄  
░██░▒██▒   ░██▒░▒▓███▀▒▒▒█████▓ ░██▓ ▒██▒   ░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
░▓  ░ ▒░   ░  ░ ░▒   ▒ ░▒▓▒ ▒ ▒ ░ ▒▓ ░▒▓░    ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
 ▒ ░░  ░      ░  ░   ░ ░░▒░ ░ ░   ░▒ ░ ▒░    ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
 ▒ ░░      ░   ░ ░   ░  ░░░ ░ ░   ░░   ░     ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░ 
 ░         ░         ░    ░        ░                ░           ░    ░       ░  ░   ░     
                                                                   ░                      Made by - zloonga#0001'''

print(game_name)
print("[1] Get a Random Imgur Image")
print("[2] Exit")

user_input = input()


if user_input == "1":
    def lookForImages(length):
            letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
            numbers = '1234567890'
            imgurBase = 'http://i.imgur.com/'

            result = imgurBase + ''.join((random.choice(str(letters) + str(numbers))) for x in range(length))
            print("Your random image/video is:", result)

                
            print("Do you want to search for another Image/Video again? [Y/N]:")

            again = input().upper()
            if again == "Y":
                lookForImages(5)
            elif again == 'N':
                print("Ok GoodBye <3 - zloonga#0001")
                time.sleep(3)
            else:
                print("THATS NOT A VALID ANSWER YOU NIGNOG!")
                time.sleep(4)

elif user_input == "2":

    print("Ok GoodBye <3 - zloonga#0001")
    time.sleep(4)


else:

    print("THATS NOT A VALID ANSWER YOU NIGNOG!")
    time.sleep(4)


lookForImages(5)



        



