import random, json
#---------------------------------------------------------------------
#Global Variables | Ease of use changing of important test numbers
#---------------------------------------------------------------------

quizSize = 15

#---------------------------------------------------------------------
#Helper Functions:
#---------------------------------------------------------------------


def checkAnswer(answer, userAnswer):
    userAnswer = userAnswer.lower()
    answer = answer.lower()
    if userAnswer == answer or userAnswer == answer + ")":
        print("Correct!")
        return 1
    elif userAnswer == 'q' or userAnswer == 'quit':
        return -1
    print("Incorrect.\n The correct answer was: "+ answer + ".")
    return 0

def setupFITB(dataSet, description):
    questionsList = list(dataSet.keys())
    questionIndex = random.randint(0, len(questionsList)-1)
    question = questionsList[questionIndex]         
    answer = dataSet[question]
    print("Answer = "+str(answer))
    return fillInTheBlanks(question, answer, description)


#---------------------------------------------------------------------
#Question Functions 
#---------------------------------------------------------------------

def fillInTheBlanks(question, answer, description):
    print(description + "\n" + question)
    if (type(answer) is list):
        print(answer[0])
        answer = answer[1]
    
    print("(Press enter to skip)")
    userAnswer = input()
    if userAnswer == '':
        return 2
    elif userAnswer.lower() == answer.lower():
        print("Correct!")
        return 1
    else:
        print("Incorrect.\nThe correct answer was:\n" + answer)
        return 0
    

def multipleChoice(dataset, description):
    keys = list(dataset.keys())
    values = list(dataset.values())
    q_index = random.randint(0, len(keys)-1)
    answer = values[q_index]
    #check whether the dataset has pre-built answers, or should randomize it
    if (type(answer) is list):          #Type is list, MC options are built in
        answer = values[q_index][0]
        answerList = random.sample(range(0,4), 4)
        # print(answerList)
        # print(values)
        print(description+"\n"+keys[q_index])
        for x in range(len(answerList)):
            answerList[x] = values[q_index][answerList[x]]
            print(str(x+1) + ") "+ str(answerList[x]))
            if answerList[x] == answer:
                answer = str(x+1)  #set the answer index
    else:                               #Type is string containing only the answer, randomize other options.

        indexes = random.sample(range(0, len(values)), 4)
        answerIndex = random.randint(0,3)
        print("What is the correct translation of "+keys[indexes[answerIndex]]+"?")
        print(answerIndex+1)
        count = 1
        for i in indexes:
            print(str(count)+") "+values[i])
            count+=1
           
        return checkAnswer(str(answerIndex+1), input())


        
        
    return checkAnswer(answer, input())


def typeFour(dataset):
    keys = list(dataset.keys())
    values = list(dataset.values())
    questionIndex = random.randint(0, len(values)-1)
    if (multipleChoice({keys[questionIndex] : values[questionIndex][0]}, "Choose the correct adjective:")):
        
        return fillInTheBlanks(values[questionIndex][1], values[questionIndex][2], "Now pluralize the adjective and noun pairing:")
    
    else:
        return 0


#---------------------------------------------------------------------
#Main Functions
#---------------------------------------------------------------------

def chooseQuestion(data):

    questionSelect = random.randint(0,7)
    print("(Question type " + str(questionSelect+1)+")")

    if questionSelect == 0:
        return multipleChoice(data["adj_conj_data"], "Place the correct word to finish the sentence:")
    elif questionSelect == 1:
        return setupFITB(data["sentence_translation_data"], "Translate the sentance into Polish:")
    elif questionSelect == 2:
        return setupFITB(data("pluralization_data"), "Correctly pluralize the noun:")
    elif questionSelect == 3:
        return typeFour(data("follow_up_data"))
    elif questionSelect == 4:
        return multipleChoice(data("mc_eng_pol_data"), "Translate the following word:")
    elif questionSelect == 5:
        return setupFITB(data("locative_grammar_data"), "Use the locative case for the following noun:")
    elif questionSelect == 6:
        return setupFITB(data("correct_case_ending_data"), "Testing")
        
def addData(data):
    data["testing"] = "bleh"
    with open("data.json", 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))
        print("Wrote to file.")
        return

def startQuiz(data):
    submit = ""
    totalCorrect = 0
    totalQuestion = 1
    while (submit != "Quit" or submit != "Q" or submit != "quit"):
        print("-----------------------------------------\nQuestion "+str(totalQuestion)+":")
        questionResult = chooseQuestion(data)
        #Scoring system: 1 is a correct answer, -1 is exit quiz
        
        if (questionResult == 1):
            totalCorrect+=1
        elif( questionResult == -1):
            print("Final Score: "+str(totalCorrect)+"/"+str(totalQuestion-1))
            exit()
        elif questionResult == 2: #skipped
            totalQuestion-=1
       
        
        if (totalQuestion == quizSize):
            print("Your final score was: "+str(totalCorrect)+"/"+str(totalQuestion))
            exit()
        
         
        print("Score: "+str(totalCorrect)+"/"+str(totalQuestion)+"\nPress enter to continue:")
        input()
        totalQuestion+=1  


def main():
    with open('data.json') as json_file:
        data = json.load(json_file)
    
    menu = 0
    while (menu != -1):
        print('''Select an option and press enter:
1. Polish Quiz
2. Quit
3. Add data''')
        menu = input()
        if (menu == '1'):
            startQuiz(data)
        elif (menu == '2'):
            print("Quitting")
            exit()
        elif (menu == '3'):
            addData(data)
        else:
            print('Invalid option selected, try again.\n')

main()