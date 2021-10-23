import random


#start text
print("██╗  ██╗███████╗██╗   ██╗     ██████╗ ███████╗███╗   ██╗███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ ")
print("██║ ██╔╝██╔════╝╚██╗ ██╔╝    ██╔════╝ ██╔════╝████╗  ██║██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗")
print("█████╔╝ █████╗   ╚████╔╝     ██║  ███╗█████╗  ██╔██╗ ██║█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝")
print("██╔═██╗ ██╔══╝    ╚██╔╝      ██║   ██║██╔══╝  ██║╚██╗██║██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗")
print("██║  ██╗███████╗   ██║       ╚██████╔╝███████╗██║ ╚████║███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║")
print("╚═╝  ╚═╝╚══════╝   ╚═╝        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝")
print("  by floppy ^~^                                                                                           ")
print("                                                                                                          ")
print("                                                                                                          ")
print("                                                                                                          ")


#for creating password
def generate():
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    symbol = "[]@\<>#()*;/,_-"
    

    all = lower + upper + number + symbol


    length = int(input("What lenght: "))
    password = "".join(random.sample(all, length))
    print (password)


#generate or no
agreement = input("Do you want to generate a password (Y or N): ")

if agreement == "Y":
    generate()
elif agreement == "N":
    exit()
else:
    print("I ASKED, YES OR NO, NOT SOME RANDOM SHIT ")

#new or close
close_or_new = input("Press 'N' for another password or any other key to close the script: ")
if close_or_new == "N":
    generate()
else:
    exit()

#close
input("To close press any key: ")
