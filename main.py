import funcData
import PySimpleGUI as sg
import json, random

#----------------------------------------------------------------------------------------------------------------
#Global Variables:
#----------------------------------------------------------------------------------------------------------------

#UI elements:
window_width = 800
window_height = 600
header_size = 32
button_size = 18
quiz_header_size = 18
question_header = 16
flashcard_question = 30
flashcard_question_small = 20
score_size = 24
expanded_score_size = 24

urb = 'Urbane Rounded Bold'
urm = 'Urbane Rounded Medium'

PolishTheme = {
    'BACKGROUND': '#FFFFFF',
    'TEXT': '#998675',
    'INPUT': '#F7F7F7',
    'TEXT_INPUT': '#404040',
    'SCROLL': '#99CC99',
    'BUTTON': ('#66605D', '#CEC8C2'),    #Text, then background
    'PROGRESS': ('#D1826B', '#CC8019'),
    'BORDER': 1, 'SLIDER_DEPTH': 0, 
    'PROGRESS_DEPTH': 0, 
}

#Program Variables
#quizSize = 5



#----------------------------------------------------------------------------------------------------------------
#Making Window Functions (Neccessary as functions since layouts cannot be re-used.)
#----------------------------------------------------------------------------------------------------------------
def makeFlashcardWindow():
    flashcardLayout =    [ 

                #Score
                [sg.Button('<', key='-BACK-', size=(4, 1), font=(urm, button_size)), sg.Text('', key='-EXPAND3-', pad=(0,0)), sg.Text('0/0', key="-SCORE-", font=(urb, score_size), text_color='#000000', justification='right')],     
                
                #Correct/Incorrect desc + Correct Answer text
                [sg.Text('', key='-FLASHCARD_RESULT-', font=(urm, quiz_header_size))], 
                [sg.Text('', key='-CORRECT_ANSWER_TEXT-', font=(urb, quiz_header_size), text_color='#000000')],
                
                #Flashcard frame + Flashcard question + Filler(EXPAND)
                [sg.Frame('', [
                    [sg.Text(key='-EXPAND-', pad=(0,0), background_color='#F7F7F7')],
                    [sg.Text('', key='-FLASHCARD_QUESTION-', font=(urb, flashcard_question), background_color='#F7F7F7')],
                    [sg.Text(key='-EXPAND2-', pad=(0,0), background_color='#F7F7F7')],
                    ], size = (500,350), element_justification='c', vertical_alignment='center', background_color='#F7F7F7')
                ],
                #Answer Input + Submit button
                [sg.In(key='-FLASHCARD_ANSWER-', size=(28,2), font=(urm, question_header), enable_events=True), sg.Button(">", key='-SKIP-', size=(4, 1), font=(urm, button_size))],
                [sg.Button('Submit', key='-SUBMIT-', size=(8, 1), font=(urm, button_size))]
                
            ]
    return sg.Window("Flashcards", flashcardLayout, finalize=True, size=(window_width, window_height), element_justification='c')

def makeMainWindow():
    mainMenuLayout =    [ 
                [sg.Text('', font=(urb, 45))],
                [sg.Text("Custom Polish Quiz Generator", font=(urb, header_size))],
                [sg.Text("", font=(urb, header_size))],
                #[sg.Button('Start Quiz')],
                [sg.Button("Flashcards", size=(10, 2),font=(urm, button_size))],
                # [sg.Button("Add Question Data")],
                [sg.Button("Quit", size=(10, 2),font=(urm, button_size))]
    ]
    return sg.Window("Polish_Quiz", mainMenuLayout, size=(window_width, window_height), element_justification='c')

def makeQuizSelectWindow():
    layout = [
        [sg.Text("What would you like to practice? ", font=(urm, header_size))],
        [sg.Text('')],
        [sg.Button('Adjectives', key='-PRACTICE_ADJECTIVES-', font=(urm, button_size), size=(10, 2))],
        [sg.Button('Nouns', key='-PRACTICE_NOUNS-', font=(urm, button_size), size=(10, 2))],
        [sg.Button('Verbs', key='-PRACTICE_VERBS-', font=(urm, button_size), size=(10, 2))],
        [sg.Button('All', key='-PRACTICE_ALL-', font=(urm, button_size), size=(10, 2))],
    ]
    return sg.Window("Flashcard Quiz Select", layout, element_justification='c', size=(window_width, window_height))

def makeScoreWindow():
    layout = [
        [sg.Button('<', key='-BACK-', size=(4, 1), font=(urm, button_size)), sg.Text('', key='-EXPAND-', pad=(0,0))],
        [sg.Text('')],
        [sg.Frame('', [
                    [sg.Text('Final Score:', font=(urm, header_size),background_color='#F7F7F7'), sg.Text('', key='-FINAL_SCORE-', font=(urb, header_size),background_color='#F7F7F7')],
                    [sg.Text('', key='-SCORE_PERCENTAGE-', font=(urb, 40),background_color='#F7F7F7')],
                    [sg.Text('')],
                    [sg.Text('', key='-SCORE_MESSAGE-', font=(urm, 20),background_color='#F7F7F7')]
                    ], size = (500,350), element_justification='c', vertical_alignment='center', background_color='#F7F7F7')
                ],
        
        
    ]
     
    return sg.Window("Results", layout, element_justification='c', size=(window_width, window_height), finalize=True)

#----------------------------------------------------------------------------------------------------------------
#Window Functionality
#----------------------------------------------------------------------------------------------------------------
def flashcardWindow(data, setType):
    #print("Entered flashcard window")

    window = makeFlashcardWindow()
    window['-EXPAND-'].expand(True, True, True)
    window['-EXPAND2-'].expand(True, False, True)
    window['-EXPAND3-'].expand(True, False, False)
    window.bind("<Return>", "_Enter")
    window.bind("<Tab>", "_Tab")
        
    
    print(type(data), len(data))
    if (setType == 'all'):
        dataSet = {}
        dataSet.update(data["adjective_set"])
        dataSet.update(data["noun_set"])
        dataSet.update(data["verb_set"])
        print(dataSet)
        
    else:
        dataSet = data[setType]
    
    #Prevent looping 
    usedTerms = {}

    score = 0
    questionCount = 0
    event, values = '', ''
    while True:
        window['-SCORE-'].update(str(score)+'/' + str(questionCount))


        #----------------------
        #Code to stop the quiz at a certain quiz size. Quiz size global variable available above
        # print(questionCount, quizSize, window['-SCORE-'].get())
        # if (questionCount == quizSize):
        #     window.close()
        #     scoreWindow(data, window['-SCORE-'].get())
        #     break
            
            
           

        if (event != '-FLASHCARD_ANSWER-'):
            while True:
                if len(usedTerms) == len(dataSet):
                    window.close()
                    scoreWindow(data, window['-SCORE-'].get())
                    break
                question, answer = funcData.setupFlashcard(dataSet)
                if (question in usedTerms) == False:
                    usedTerms[question] = answer
                    break
                
            print(usedTerms)
            #Randomizing whether the question is polish->english or english->polish

            window['-FLASHCARD_QUESTION-'].update(font=(urm, flashcard_question))
            if (random.randint(0,1) == 0):
                if type(answer) is list:
                    newQuestion = ''
                    for i in range(len(answer)):
                        newQuestion += answer[i]
                        if (i != len(answer)-1):
                            newQuestion += " or "
                    window['-FLASHCARD_QUESTION-'].update(font=(urm, flashcard_question_small))
                else:
                    newQuestion = answer
                    
                answer = question
                question = newQuestion 
            window['-FLASHCARD_ANSWER-'].update('')
       
        #Populating/Updating the layout with the current question
        window['-FLASHCARD_QUESTION-'].update(question)
        
        #---------------------------------
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Quit':
            window.close()
            break 
        elif event == '-BACK-':
            #add popup here
            window.close()
            mainMenuWindow(data)
        
        elif event == '-SUBMIT-' or event == '_Enter' or event == '-SKIP-' or event == '_Tab':
            #print(values['-FLASHCARD_ANSWER-'])
            if event == "-SKIP-" or event == '_Tab':
                checkResult, resultDescription, correctAnswer = (-1), 'Question skipped.', ''
            else:
                checkResult, resultDescription, correctAnswer = funcData.checkFlashcardAnswer(answer,values['-FLASHCARD_ANSWER-'])
            if (checkResult == 1):
                score+=1
                window['-FLASHCARD_RESULT-'].update(text_color='#3EFF00')
                window['-CORRECT_ANSWER_TEXT-'].update(correctAnswer)
            elif checkResult == (-1):
                print('skipped')
                window['-FLASHCARD_RESULT-'].update(text_color='#000000')
                window['-CORRECT_ANSWER_TEXT-'].update(correctAnswer)
                questionCount-=1
            else:
                #print('wrong' + str(correctAnswer))
                window['-FLASHCARD_RESULT-'].update(text_color='#FF0000')
                window['-CORRECT_ANSWER_TEXT-'].update(correctAnswer)
            

            questionCount+=1
            
            window['-FLASHCARD_RESULT-'].update(resultDescription)
            
def scoreWindow(data, score):
    
    
    window = makeScoreWindow()
    window['-EXPAND-'].expand(True, False, False)
    window['-FINAL_SCORE-'].update(score)
    scoreValues = score.split('/')
    scorePercent = round((int(scoreValues[0]) / int(scoreValues[1])) * 100 )
   
    print("score%" +str(scorePercent))
    window['-SCORE_PERCENTAGE-'].update(str(scorePercent)+ '%')
    #Changes dependent on score thresholds:
    if (scorePercent >= 80):
        window['-SCORE_PERCENTAGE-'].update(text_color='#3EFF00')
        window['-SCORE_MESSAGE-'].update("Great work! You're a genius!")
    elif (scorePercent >= 60):
        window['-SCORE_PERCENTAGE-'].update(text_color='#FFE883')
        window['-SCORE_MESSAGE-'].update("Good job, keep practicing!")
    else:
        window['-SCORE_MESSAGE-'].update("I love you, keep working hard!")

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == '':
            window.close()
            break 
        elif event == '-BACK-':
            window.close()
            mainMenuWindow(data)

def mainMenuWindow(data):
    #print("Entered main window")

    window = makeMainWindow()
   
    while True:
        event, values = window.read()
        #print(event, values)
        if event == sg.WIN_CLOSED or event == 'Quit':
            window.close()
            break 
        elif event == 'Flashcards':
            window.close()
            quizSelectWindow(data)

def quizSelectWindow(data):
    window = makeQuizSelectWindow()

    while True:
        event, values = window.read()
        #print(event, values)
        if event == sg.WIN_CLOSED or event == '':
            window.close()
            break 
        elif event == '-PRACTICE_ADJECTIVES-':
            window.close()
            flashcardWindow(data, 'adjective_set')
        elif event == '-PRACTICE_NOUNS-':
            window.close()
            flashcardWindow(data, 'noun_set')
        elif event == '-PRACTICE_VERBS-':
            window.close()
            flashcardWindow(data, 'verb_set')
        elif event == '-PRACTICE_ALL-':
            window.close()
            flashcardWindow(data, 'all')

def main():
    sg.LOOK_AND_FEEL_TABLE['PolishTheme'] = PolishTheme
    sg.theme('PolishTheme')
    with open('data.json', 'r', encoding='utf-8') as json_file:
        #data = json.dumps(json.load(json_file), ensure_ascii=False)
        data = json.load(json_file)
        #print(data)
    #print("Entered main")
    mainMenuWindow(data)
    
main()
