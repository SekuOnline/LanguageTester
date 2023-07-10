import random, json
import PySimpleGUI as sg

def checkFlashcardAnswer(answer, userAnswer):
    userAnswer = userAnswer.lower()
    userAnswer = userAnswer.replace(" ", "")
    if(type(answer) is list):
        newAns = ''
        for i in range(len(answer)):
            newAns += answer[i]
            if (i != len(answer)-1):
                newAns += ' or '
        if userAnswer == 'skip':
            return (-1), "Question skipped.", newAns
        for ans in answer:
            ans = ans.lower()
            ans = ans.replace(" ", "")
            if ans == userAnswer:
                return 1, "Correct!", newAns
        
        
        return 0, "Incorrect. The correct answer was: ", newAns
            
        
    answer = answer.lower()
    formattedAnswer = answer
    answer = answer.replace(" ", "")
    if userAnswer == answer or userAnswer == answer + ")":
        print("correct answer")
        return 1, "Correct!", formattedAnswer
    
    elif userAnswer == 'skip':
        return (-1), "Question skipped.", formattedAnswer
    print("incorrect answer")
    return 0, "Incorrect. The correct answer was: ", formattedAnswer

def setupFlashcard(dataSet):
    questionsList = list(dataSet.keys())
    questionIndex = random.randint(0, len(questionsList)-1)
    question = questionsList[questionIndex]         
    answer = dataSet[question]
    #print("Answer = "+str(answer))
    return question, answer

    

            












   

