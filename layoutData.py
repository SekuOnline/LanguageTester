import PySimpleGUI as sg





# sg.theme("PolishTheme")s

# #sg.Button("Quit", size=(8, 2),font=(urm, button_size))
# #[sg.Text("Question Description", key="-DESCRIPTION-", font=(urm, 18), text_color='#000000'), 

# mainMenuLayout =    [ 
#                 [sg.Text("Custom Polish Quiz Generator", font=(urb, header_size))],
#                 [sg.Text("", font=(urb, header_size))],
#                 #[sg.Button('Start Quiz')],
#                 [sg.Button("Flashcards", size=(10, 2),font=(urm, button_size))],
#                 # [sg.Button("Add Question Data")],
#                 [sg.Button("Quit", size=(10, 2),font=(urm, button_size))]
#             ]

# flashcardLayout =    [
#                 #Score
#                 [sg.Button('<', key='-BACK-', size=(4, 1), font=(urm, button_size)), sg.Text('', key='-EXPAND3-', pad=(0,0)), sg.Text('0/0', key="-SCORE-", font=(urb, score_size), text_color='#000000', justification='right')],     
                
#                 #Correct/Incorrect desc + Correct Answer text
#                 [sg.Text('', key='-FLASHCARD_RESULT-', font=(urm, quiz_header_size)), 
#                 sg.Text('', key='-CORRECT_ANSWER_TEXT-', font=(urb, quiz_header_size), text_color='#000000')],
                
#                 #Flashcard frame + Flashcard question + Filler(EXPAND)
#                 [sg.Frame('', [
#                     [sg.Text(key='-EXPAND-', pad=(0,0), background_color='#F7F7F7')],
#                     [sg.Text('', key='-FLASHCARD_QUESTION-', font=(urb, flashcard_question), background_color='#F7F7F7')],
#                     [sg.Text(key='-EXPAND2-', pad=(0,0), background_color='#F7F7F7')],
#                     ], size = (500,350), element_justification='c', vertical_alignment='center', background_color='#F7F7F7')
#                 ],
#                 #Answer Input + Submit button
#                 [sg.In(key='-FLASHCARD_ANSWER-', size=(28,2), font=(urm, question_header), enable_events=True), sg.Button(">", key='-SUBMIT-', size=(4, 1), font=(urm, button_size))],
                
#             ]