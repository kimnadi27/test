import pyautogui
import time
from random import randint

a = 100000
b = int()
o = int()
line = int()
c = str()
o = 10

print("До старта")

for i in range(10):
	print(o)
	o -= 1
	time.sleep(1)

#time.sleep(5)
print("Начинаю")
while b <= 6:
	a = randint(100000, 999999)
	print(a)
	#print(len(str(a)))
	b = len(str(a))
	#print(c)
	#print(a.count('a'))

	pyautogui.typewrite(str(a))
	pyautogui.press("enter")
	for i in range(6):
		pyautogui.press("backspace")
	time.sleep(3)