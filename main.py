import random
#---------------------------------------------------------------------
#Global Variables | Ease of use changing of important test numbers
#---------------------------------------------------------------------

quizSize = 15
#---------------------------------------------------------------------
#Data sets (Will be moved to files later for better storage)
#---------------------------------------------------------------------


#Type 1 data (MC)
#Dictionary 1 : 4
adj_conj_data = {
    "This test is very difficult\nTen test jest bardzo [______]" : ["trudny", "trudnego", "trudna", "trudno"],
    "I want a new jacket.\nChcę [_____]  kurtkę.":["nową","nowy","nowa","nowe"]
}

#Type 2 data (FITB)
#Dictionary 1 : 1
sentance_translation_data = {
    "She is very sweet." : "Ona jest bardzo słodka."
}

#Type 3 data (FITB)
#Dictionary 1 : 1
pluralization_data = {
    "Paczka" : "Paczki"
}

#Type 3/2 data (FITB)
#Dictionary 1 : 1
locative_grammar_data = {
    "Dom" : "Domu"
}

#Type 5 DATA (MC / FITB)
#Dictionary 1 : 1
mc_eng_pol_data = {
    "Easy" : "łatwy",
    "Difficult" : "trudny",
    "Hard" : "twardy",
    "Heavy" : "ciężki",
    "Scarf" : "szalik",
    "Wide" : "szeroki",
}

#Type 6 Data (FITB)
#Dictionary 1 : 2
correct_case_ending_data = {
    "I see (Widzę)" : ["They see [_____]", "Widzą"],
}



#---------------------------------------------------------------------
#Helper Functions:
#---------------------------------------------------------------------

#Takes a FITB question, presents it, and returns the validity of the answer
#Used to do work for multiple types of FITB questions.
#All params should be strings.
def fillInTheBlanks(question, answer, description):
    print(description + "\n" + question)
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


def checkAnswer(answer, userAnswer):
    if userAnswer == answer or userAnswer == answer + ")":
        print("Correct!")
        return 1
    elif userAnswer == 'q' or userAnswer == 'quit':
        return -1
    print("Incorrect.\n The correct answer was: "+ answer + ".")
    return 0

def FITB(dataSet, description):
    questionsList = list(dataSet.keys())
    questionIndex = random.randint(0, len(questionsList)-1)
    question = questionsList[questionIndex]         
    answer = dataSet[question]
    print("Answer = "+str(answer))
    return fillInTheBlanks(question, answer, description)


#---------------------------------------------------------------------
#Question Functions 
#---------------------------------------------------------------------

#adjective conjugation, MC
def adjConj():
    keys = list(adj_conj.keys())
    values = list(adj_conj.values())
    q_index = random.randint(0, len(keys)-1)
    answer = values[q_index][0]
    print(answer)
    answerList = random.sample(range(0,4), 4)
    print(answerList)
    print(values)
    print("Place the correct word to finish the sentence:\n"+keys[q_index])
    for x in range(4):
        answerList[x] = values[q_index][answerList[x]]
        print(str(x+1) + ") "+ str(answerList[x]))
        if answerList[x] == answer:
            answer = str(x+1)  #set the answer index
            
    return(checkAnswer(answer, input()))


def multipleChoice(): #mc_eng_pol
    #Decide whether the question is polish or english answer (50/50)

    if (random.randint(0,2) == 0):  #English Question, Polish answer
        questions = list(mc_eng_pol.keys())
        answers = list(mc_eng_pol.values())
    else:
        questions = list(mc_eng_pol.values())  #Polish Question, English Answer
        answers = list(mc_eng_pol.keys())

    indexes = random.sample(range(0, len(mc_eng_pol)), 4)
    
    #Select an answer 
    answerIndex = random.randint(0,3)

    print("What is the correct translation of "+questions[indexes[answerIndex]]+"?")
    count = 1
    print(answerIndex+1)
    for i in indexes:
        print(str(count)+") "+answers[i])
        count+=1
    userAnswer = input()
    return checkAnswer(str(answerIndex+1), str(userAnswer).lower())

# def sentanceFITB():
#     questionsList = list(fitb.keys())
#     questionIndex = random.randint(0, len(questionsList)-1)
#     translation = questionsList[questionIndex]
#     question = fitb[translation][0]
#     answer = fitb[translation][1]
#     return fillInTheBlanks(question, answer, "", "Translate the sentance:")

# def pluralizeWord():
#     questionsList = list(fitb.keys())
#     questionIndex = random.randint(0, len(questionsList)-1)
#     translation = questionsList[questionIndex]
#     question = fitb[translation][0]
#     answer = fitb[translation][1]
#     return fillInTheBlanks(question, answer, "", "Translate the sentance:")



#---------------------------------------------------------------------
#Main Functions
#---------------------------------------------------------------------

def chooseQuestion(quizType):
    # if 0 <= quizType <= 66:   #Fill in the blanks
    #     return(multipleChoice())
    # elif quizType <=100:
    #     return(fillInTheBlanks())

    #return(multipleChoice())
    #return adjConj()
    #return adj_conj()                                                                       #Type 1
    return FITB(sentance_translation_data, "Translate the sentance into Polish:")                                #Type 2
    #return FITB(fitb, "Correctly pluralize the noun:")                                      #Type 3
    #Type 4: Requires both FITB and MC, unique
    return FITB(fitb, "Translate the following word: ")                                     #Type 5
    return FITB(fitb, "Use the locative case for the following noun:")                      #Type 3.5
    return FITB(fitb, "Conjugate the word to describe the person in the given example:")    #Type 6
    



def startQuiz():
    submit = ""
    totalCorrect = 0
    totalQuestion = 1
    while (submit != "Quit" or submit != "Q" or submit != "quit"):
        print("-----------------------------------------\nQuestion "+str(totalQuestion)+":")
        questionResult = chooseQuestion(random.randint(0,100))
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