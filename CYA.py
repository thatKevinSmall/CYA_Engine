import os
import sys
import time

class Chapter:
    def __init__(self, chapterText, isEnding):
        self.chapterText = chapterText
        self.choices = []
        self.choicesIndex = []
        self.isEnding = isEnding
    
    def addChoice(self, choice):
        self.choices.append(choice)

    def printChapter(self):
        os.system("cls")
        delayPrint(self.chapterText)
        delayPrint("Your choices are:\n")
        index = 1
        for choice in self.choices:
            delayPrint(f"{index} : {choice.text}")
            index += 1
            
    def validateChoice(self, idx):
        try:
            if self.choices[idx - 1]:
                return self.choices[idx - 1].goto
        except:
            return None
        
class Choice:
    def __init__(self, choiceText, goToChapter):
        self.text = choiceText
        self.goto = goToChapter

def delayPrint(someText):
    for character in someText:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(.05)

def isInteger(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

#create chapters passing chapter text and true or false is it an ending
chapter1 = Chapter("You are in a clearing.\nYou are all alone.\n", False)
chapter2 = Chapter("You are back home.\nYou climb into bed.\n", True)
chapter3 = Chapter("You scroung around for wood to make a fire.\nYou come accross a snake.\n", False)
chapter4 = Chapter("You swing a stick at the snake.\n  It bites you and it was poisonous.\nYou die.", True)

#create choices passing in the choice text and the chpater it goes to
ChoiceGoHome = Choice("You can run back home.\n", chapter2)
ChoiceMakeAFire = Choice("You can look for firewood.\n", chapter3)
choiceAttackSnake = Choice("You can grab a log and smash the snake.\n", chapter4)

#add choices to the chapter 
chapter1.addChoice(ChoiceGoHome)
chapter1.addChoice(ChoiceMakeAFire)
chapter3.addChoice(ChoiceGoHome)
chapter3.addChoice(choiceAttackSnake)

gameContinue = True
currentChapter = chapter1

while gameContinue:
    if not currentChapter.isEnding:
        currentChapter.printChapter()
        userInput = input("Enter the number of your choice.\n")
        #verify the choice is a number
        if isInteger(userInput):
            response = currentChapter.validateChoice(int(userInput))
            #verify the choice is in this chapter
            if response:
                    currentChapter = response
            else:
                delayPrint(f"{userInput} is invalid choice.\n")
                
        else:
            delayPrint(f"{userInput} is invalid choice.\n")

    else:
        delayPrint(currentChapter.chapterText)
        delayPrint("Game is over.\nWould you like to try again?\n")
        userInput = input("Y or N")
        if userInput.lower() == "y":
            currentChapter = chapter1
        elif userInput.lower() == "n":
            gameContinue = False
        else:
            delayPrint(f"{userInput} is invalid choice.\n")
