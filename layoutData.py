import PySimpleGUI as sg
mainMenuLayout =    [ 
                [sg.Text("Custom Polish Quiz Generator")],
                #[sg.Button('Start Quiz')],
                [sg.Button("Flashcards")],
                # [sg.Button("Add Question Data")],
                [sg.Button("Quit")]
            ]
flashcardLayout =    [ 
                [sg.Text("Question Description", key="-DESCRIPTION-"), sg.Text('0/0', key="-SCORE-")],
                [sg.Text('', key='-FLASHCARD_QUESTION-')],
                [sg.In(key='-FLASHCARD_ANSWER-', size=(30,1))],
                [sg.Text('', key='-FLASHCARD_RESULT-')],
                [sg.Button("Submit Answer", size=(8, 2)), sg.Button("Quit", size=(8, 2))],
                
            ]