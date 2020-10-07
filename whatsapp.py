from twilio.rest import Client
import sys
import os
import time
import urllib
import pip
import socket

timeout = 1
socket.setdefaulttimeout(timeout)

os.system('clear')
os.system('git pull')

name = """\033[1;32;40m
\t /$$$$$$$                  /$$ /$$   /$$             /$$
\t| $$__  $$                | $$| $$$ | $$            | $$ 
\t| $$  \ $$  /$$$$$$   /$$$$$$$| $$$$| $$  /$$$$$$  /$$$$$$ 
\t| $$$$$$$/ /$$__  $$ /$$__  $$| $$ $$ $$ /$$__  $$|_  $$_/
\t| $$__  $$| $$$$$$$$| $$  | $$| $$  $$$$| $$$$$$$$  | $$ 
\t| $$  \ $$| $$_____/| $$  | $$| $$\  $$$| $$_____/  | $$ /$$ 
\t| $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$|  $$$$$$$  |  $$$$/ 
\t|__/  |__/ \_______/ \_______/|__/  \__/ \_______/   \___/

\t [¤] Termux Whatsapp Spam
\t [¤] Versions : 2.3.0
\t [¤] Coded By Shehan Lahiru
  """

print(name, "")

try:
    f = open("spam.js", "r")
    spam = f.read()
    f.close
except:
    f = open("spam.js", "w")
    f.write(wr)
    f.close
    f = open("spam.js", "r")
    spam = f.read()
    f.close
try:
    f = open("sid.js", "r")
    sid = f.read()
    f.close
except:
    f = open("sid.js", "w")
    f.write(wr)
    f.close
    f = open("sid.js", "r")
    sid = f.read()
    f.close

try:
    f = open("token.js", "r")
    f = open("token.js", "r")
    token = f.read()
    f.close
except:
    f = open("token.js", "w")
    f.write(wr)
    f.close
    f = open("token.js", "r")
    token = f.read()
    f.close
try:
    import pip


except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    os.system('clear')
    os.system('pip3 install twilio')
    os.system('clear')
    os.system('pip3 install matplotlib')
    os.system('clear')
    print('%s Requests has been installed.')
    os.system('clear')
    import pip
    
    print("\033[0;36m "" ░P░A░N░D░O░R░A░")
    print("\033[0;36m "" ")
    print("\033[0;36m "" ωнαтsαρρ sραм")
    print("")
    print("\033[0;36m "" ")
t = input("Enter send message: ")
sr = input("Enter a number: ")
def main():
    os.system("clear")
    print(name,"\n")
    irc_input = sid
    irc_joinig = token
    print_input = sid
    print_output = token
    client = Client(print_input, print_output)
    
    message = client.messages \
                    .create(
                         from_='whatsapp:+14155238886',
                         body= t,
                         to=sr
                 )
    
    
    ss = 0
    while 1 > ss:
        os.system("clear")
        print(name)
        size = 0
        ss+=1
        for i in range(180):

            pr = i/180*100
            print("\033[1;36;40m\n>>> [+]",str(int(pr)) +"% ",end="")
            time.sleep(0.006)
            sys.stdout.write("\033[F")

    os.system('')
    main()

def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
