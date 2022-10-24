#Team: Robson & Nicola, Pair 1
#Write a program that will display a joke and display the punchline after the enter key
import colorama
from colorama import init, Fore, Back, Style
#initialise colorama
colorama.init(autoreset=True)

print("Why do polar bears and penguins not get on?")
(input("Press the enter key to laugh!"))
print(Back.WHITE + Fore.BLUE + "Because they are polar opposites!")


