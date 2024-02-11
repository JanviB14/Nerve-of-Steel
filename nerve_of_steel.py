
from PIL import Image
import time
from random import randint
im = Image.open("display_last.jpg")
print("Players stand")
time.sleep(randint(5,25))
#print("Times up! Last to sit down wins")
im.show()

