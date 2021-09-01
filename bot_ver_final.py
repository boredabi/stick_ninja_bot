
# max points - 76


from pyautogui import pixelMatchesColor, mouseDown, mouseUp
from time import sleep

while 1:
	starting_points = []
	for i in range(793,811):
		if pixelMatchesColor(i,679,(0,0,0)):
			starting_points.append(i)
	for n in range(820,1215,10): # finding the red point
		if pixelMatchesColor(n,679,(253,10,1)):
			break
	y = (679-((n-2)-(starting_points[-1]))) #added -3 to compensate for the extra(10) shifiting
	x = starting_points[-1]
	mouseDown()
	while 1:
		if pixelMatchesColor(x,y,(0,0,0)):
			mouseUp()
			break
	if n <=860:
		sleep(1.7)
	elif n <=920:
		sleep(1.8)
	elif n <= 940: #aDD 880 conditon and sleep for 1.8 seconds if it doenst work
		sleep(1.9)
	elif n <= 1000:
		sleep(2)
	elif n <= 1060:
		sleep(2.1)
	elif n <= 1120:
		sleep(2.2)
	elif n <= 1180:
		sleep(2.3)
	else:
		sleep(2.4)