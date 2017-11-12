#!/usr/bin/env python
# coding: utf-8

# You may read https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript carefully before converting.

#################### read File ####################
inputFile = open('input.txt')
linesAsStringList = inputFile.readlines()
inputFile.close()

#################### edit File ####################
#declare flagVariables for keycombinations
lineNumber = 0
defaultDelayFlag = False
shiftFlag = False
altFlag = False
ctrlFlag = False
guiFlag = False

#check for pressed Option-Keys
def checkOptions(zeile):
	global shiftFlag 
	global altFlag 
	global ctrlFlag 
	global guiFlag 

	if (zeile[:5]=="SHIFT"):
		shiftFlag = True
		return checkOptions(zeile[6:])
	elif (zeile[:3]=="ALT"):
		altFlag = True
		return checkOptions(zeile[4:])
	elif (zeile[:4]=="CTRL"):
		ctrlFlag = True
		return checkOptions(zeile[5:])
	elif (zeile[:7]=="CONTROL"):
		ctrlFlag = True
		return checkOptions(zeile[8:])
	elif (zeile[:3]=="GUI"):
		guiFlag = True
		return checkOptions(zeile[4:])
	elif (zeile[:7]=="WINDOWS"):
		guiFlag = True
		return checkOptions(zeile[8:])
	else:
		return zeile


for line in linesAsStringList:
	#take Action
	linesAsStringList[lineNumber] = checkOptions(linesAsStringList[lineNumber])

	if (linesAsStringList[lineNumber][:3]=="REM"):
		linesAsStringList[lineNumber] = "//" + linesAsStringList[lineNumber][3:]
	elif (linesAsStringList[lineNumber][:6]=="STRING"):
		linesAsStringList[lineNumber] = linesAsStringList[lineNumber].replace("\\",r"\\")
		linesAsStringList[lineNumber] = linesAsStringList[lineNumber].replace("\"",r"\"")		
		linesAsStringList[lineNumber] = 'Keyboard.print("'+ linesAsStringList[lineNumber][7:-1]+'");\n'	
	elif (linesAsStringList[lineNumber][:5]=="DELAY"):
		linesAsStringList[lineNumber] = "delay(" + linesAsStringList[lineNumber][6:-1] + ");\n"
	elif (linesAsStringList[lineNumber][:12]=="DEFAULTDELAY"):
		defaultDelayFlag = True;
		defaultDelayTime=linesAsStringList[lineNumber][13:-1]
		linesAsStringList[lineNumber] = "\n"
	elif (linesAsStringList[lineNumber][:13]=="DEFAULT_DELAY"):
		defaultDelayFlag = True;
		defaultDelayTime = linesAsStringList[lineNumber][14:-1]
		linesAsStringList[lineNumber] = "\n"
	elif (linesAsStringList[lineNumber][:5]=="ENTER"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_RETURN); \nKeyboard.release(KEY_RETURN);\n'
	elif (linesAsStringList[lineNumber][:6]=="RETURN"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_RETURN); \nKeyboard.release(KEY_RETURN);\n'
	elif (linesAsStringList[lineNumber][:5]=="SPACE"):
		linesAsStringList[lineNumber] = 'Keyboard.print(" ");\n'
	elif ((linesAsStringList[lineNumber][:2]=="F1")and(linesAsStringList[lineNumber][:3]!=("F10"or"F11"or"F12"))):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F1); \nKeyboard.release(KEY_F1);\n'
	elif (linesAsStringList[lineNumber][:2]=="F2"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F2); \nKeyboard.release(KEY_F2);\n'
	elif (linesAsStringList[lineNumber][:2]=="F3"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F3); \nKeyboard.release(KEY_F3);\n'
	elif (linesAsStringList[lineNumber][:2]=="F4"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F4); \nKeyboard.release(KEY_F4);\n'
	elif (linesAsStringList[lineNumber][:2]=="F5"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F5); \nKeyboard.release(KEY_F5);\n'
	elif (linesAsStringList[lineNumber][:2]=="F6"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F6); \nKeyboard.release(KEY_F6);\n'
	elif (linesAsStringList[lineNumber][:2]=="F7"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F7); \nKeyboard.release(KEY_F7);\n'
	elif (linesAsStringList[lineNumber][:2]=="F8"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F8); \nKeyboard.release(KEY_F8);\n'
	elif (linesAsStringList[lineNumber][:2]=="F9"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F9); \nKeyboard.release(KEY_F9);\n'
	elif (linesAsStringList[lineNumber][:3]=="F10"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F10); \nKeyboard.release(KEY_F10);\n'
	elif (linesAsStringList[lineNumber][:3]=="F11"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F11); \nKeyboard.release(KEY_F11);\n'
	elif (linesAsStringList[lineNumber][:3]=="F12"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F12); \nKeyboard.release(KEY_F12);\n'
	elif (linesAsStringList[lineNumber][:4]=="LEFT"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_LEFT_ARROW); \nKeyboard.release(KEY_LEFT_ARROW);\n'
	elif (linesAsStringList[lineNumber][:2]=="UP"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_UP_ARROW); \nKeyboard.release(KEY_UP_ARROW);\n'
	elif (linesAsStringList[lineNumber][:5]=="RIGHT"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_RIGHT_ARROW); \nKeyboard.release(KEY_RIGHT_ARROW);\n'
	elif (linesAsStringList[lineNumber][:4]=="DOWN"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_DOWN_ARROW); \nKeyboard.release(KEY_DOWN_ARROW);\n'
	elif (linesAsStringList[lineNumber][:4]=="MENU"):
		shiftFlag = True
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F10); \nKeyboard.release(KEY_F10);\n'
	elif (linesAsStringList[lineNumber][:3]=="APP"):
		shiftFlag = True
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_F10); \nKeyboard.release(KEY_F10);\n'
	elif (linesAsStringList[lineNumber][:6]=="DELETE"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_DELETE); \nKeyboard.release(KEY_DELETE);\n'
	elif (linesAsStringList[lineNumber][:3]=="ESC"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_ESC); \nKeyboard.release(KEY_ESC);\n'
	elif (linesAsStringList[lineNumber][:3]=="TAB"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_TAB); \nKeyboard.release(KEY_TAB);\n'
	elif (linesAsStringList[lineNumber][:6]=="INSERT"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_INSERT); \nKeyboard.release(KEY_INSERT);\n'
	elif (linesAsStringList[lineNumber][:3]=="END"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_END); \nKeyboard.release(KEY_END);\n'
	elif (linesAsStringList[lineNumber][:4]=="HOME"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_HOME); \nKeyboard.release(KEY_HOME);\n'
	elif (linesAsStringList[lineNumber][:7]=="CAPSLOCK"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_CAPS_LOCK); \nKeyboard.release(KEY_CAPS_LOCK);\n'
	elif (linesAsStringList[lineNumber][:6]=="PAGEUP"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_PAGE_UP); \nKeyboard.release(KEY_PAGE_UP);\n'
	elif (linesAsStringList[lineNumber][:8]=="PAGEDOWN"):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_PAGE_DOWN); \nKeyboard.release(KEY_PAGE_DOWN);\n'
	elif (linesAsStringList[lineNumber][:6]=="REPLAY"):
		c = int(linesAsStringList[lineNumber][7:-1])
		linesAsStringList[lineNumber] = '//REPLAY ' + str(c) + ' Times\n'
		for x in range (c) :
			linesAsStringList[lineNumber] = linesAsStringList[lineNumber] + linesAsStringList[lineNumber-1]
	else:
		print "Something possibly went wrong!\nPlease check the code in output.ino in the marked lines (<<<<<!!!!! CHECK FOR ERRORS HERE !!!!!>>>>>)"
		linesAsStringList[lineNumber] = 'Keyboard.print("'+ linesAsStringList[lineNumber][0] + '");// <<<<<<<<<<<<<<<<!!!!! CHECK FOR ERRORS HERE !!!!!\n'

	#add pressed Key-Options
	if (defaultDelayFlag==True):
		linesAsStringList[lineNumber] = linesAsStringList[lineNumber] + "delay(" + defaultDelayTime + ");\n"
	if (shiftFlag==True):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_LEFT_SHIFT);\n'+ linesAsStringList[lineNumber] + 'Keyboard.release(KEY_LEFT_SHIFT);\n'
		shiftFlag = False
	if (altFlag==True):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_LEFT_ALT);\n'+ linesAsStringList[lineNumber] + 'Keyboard.release(KEY_LEFT_ALT);\n'
		altFlag = False
	if (ctrlFlag==True):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_LEFT_CTRL);\n'+ linesAsStringList[lineNumber] + 'Keyboard.release(KEY_LEFT_CTRL);\n'
		ctrlFlag = False
	if (guiFlag==True):
		linesAsStringList[lineNumber] = 'Keyboard.press(KEY_LEFT_GUI); \n' + linesAsStringList[lineNumber] + 'Keyboard.release(KEY_LEFT_GUI);\n'
		guiFlag = False
	lineNumber=lineNumber+1


#################### make an Output.ino out of the edited File ####################
linesAsStringList.insert(0,'#include "Keyboard.h"\n//Thank You for using BESOBERLINs ducky2arduino converter!\n\nvoid setup() {\nKeyboard.begin();\ndelay(3000);\n\n')
linesAsStringList.append("\n}\n\n\nvoid loop(){\n\n}")
outputFile = open('input.ino', 'w')
outputFile.writelines(linesAsStringList)
outputFile.close()

