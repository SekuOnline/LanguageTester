import layoutData, funcData
import PySimpleGUI as sg
import json, random

#----------------------------
#Global Variables:
window_width = 800
window_height = 600
#----------------------------

def flashcardWindow(data):
    #print("Entered flashcard window")
    window = sg.Window("Flashcards", layoutData.flashcardLayout, finalize=True, size=(window_width, window_height), element_justification='c')
    dataSet = data["mc_eng_pol_data"]
    score = 0
    questionCount = 0
    while True:
        question, answer = funcData.setupFlashcard(dataSet)
        #Randomizing whether the question is polish->english or english->polish
        if (random.randint(0,1) == 0):
            newQuestion = answer
            answer = question
            question = newQuestion
            window['-DESCRIPTION-'].update('Translate the word to English')
        else:
            window['-DESCRIPTION-'].update('Translate the word to Polish')
        #Populating/Updating the layout with the current question
        
        window['-FLASHCARD_QUESTION-'].update(question)
        window['-FLASHCARD_ANSWER-'].update('')
        window['-SCORE-'].update(str(score)+' / ' + str(questionCount))
        
        #---------------------------------
        event, values = window.read()
        #print(event, values)
        if event == sg.WIN_CLOSED or event == 'Quit':
            window.close()
            break 
        elif event == 'Submit Answer':
            #print(values['-FLASHCARD_ANSWER-'])
            checkResult, resultDescription = funcData.checkFlashcardAnswer(answer,values['-FLASHCARD_ANSWER-'])
            if (checkResult):
                score+=1
            elif checkResult == -1:
                questionCount-=1
            questionCount+=1
            window['-FLASHCARD_RESULT-'].update(resultDescription)

def mainMenuWindow(data):
    #print("Entered main window")
    window = sg.Window("Polish Quiz", layoutData.mainMenuLayout, size=(window_width, window_height), element_justification='c')
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break 
        elif event == 'Flashcards':
            window.close()
            flashcardWindow(data)

def main():
    with open('data.json', 'r', encoding='utf-8') as json_file:
        #data = json.dumps(json.load(json_file), ensure_ascii=False)
        data = json.load(json_file)
        #print(data)
    #print("Entered main")
    mainMenuWindow(data)
    
main()
