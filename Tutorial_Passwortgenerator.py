from random import randrange
import time
import os

os.popen("title Tutorial_Passwortgenerator")

print("Dies ist ein Passwortgenerator!")
time.sleep(4)

rdm_1 = randrange(3, 6)
rdm_2 = randrange(10)
rdm_3 = randrange(2, 7)

input_name = input("Gib hier deinen Namen ein: ")

soz_1 = "!"
soz_2 = "*"
soz_3 = "$"

print(str(rdm_2) + soz_1 + str(rdm_1) + str(len(input_name)) + soz_3 + str(rdm_3) + soz_2)
time.sleep(999)
