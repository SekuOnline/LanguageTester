import random

eng_pol = {
    "I'm sorry / Excuse me" : "Przepraszam",
    "Calendar" : "Kalendarz",
    "Blue" : "Niebieski",
    "abby" : "john",
}

def startQuiz():
    submit = ""
    totalCorrect = 0
    totalQuestion = 1
    while (submit != "Quit" or submit != "Q" or submit != "quit"):
        print("-----------------------------------------\nQuestion "+str(totalQuestion)+":")
        questionResult = makeQuestion(random.randint(0,2))
        if (questionResult == 1):
            totalCorrect+=1
        elif( questionResult == -1):
            print("Final Score: "+str(totalCorrect)+"/"+str(totalQuestion-1))
            exit()
        print("Score: "+str(totalCorrect)+"/"+str(totalQuestion))
        
        totalQuestion+=1


        

def makeQuestion(quizType):
    if quizType == 0:   #Polish answer
        x = list(eng_pol.values())
        y = list(eng_pol.keys())
    else:
        x = list(eng_pol.keys())
        y = list(eng_pol.values())
    #print(x)
    #print(y)
    #choose a random item to be the subject of the question
    questionIndex = random.randint(0, len(x)-1)
    question = x[questionIndex]
    answer = y[questionIndex]
   
    print("What is the translation of "+x[questionIndex]+"?")
    for count in range (len(x)):
        print (str(count+1) + ") "+y[count])
    userAnswer = input()
    if (userAnswer == str(questionIndex+1) or userAnswer == str(questionIndex+1)+')'):
        print("Correct!")
        return 1
    
    elif (userAnswer.lower() == 'q' or userAnswer.lower == 'quit'):
        return -1

    else:
        print("Incorrect\n the correct translation of "+x[questionIndex]+" is: "+str(questionIndex+1) + ") " +y[questionIndex])
        return 0
    
    
    

    


def main():
    menu = 0
    while (menu != -1):
        print('''Select an option and press enter:
1. Polish Quiz
2. Quit''')
        menu = input()
        if (menu == '1'):
            startQuiz()
        elif (menu == '2'):
            print("Quitting")
            exit()
        else:
            print('Invalid option selected, try again.\n')

main()