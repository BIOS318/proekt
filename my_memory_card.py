
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QRadioButton, QPushButton, QLabel, QButtonGroup
from random import shuffle, randint

class QuestionClass():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

app = QApplication([])

main_win = QWidget()
main_win.setWindowTitle('Memory Card')

lineH1 = QHBoxLayout()
lineV1 = QVBoxLayout()
lineV2 = QVBoxLayout()

RadioGroupBox = QGroupBox('Варианты ответов')

b1 = QRadioButton('Вариант 1')
b2 = QRadioButton('Вариант 2')
b3 = QRadioButton('Вариант 3')
b4 = QRadioButton('Вариант 4')

lineV1.addWidget(b1, alignment=Qt.AlignCenter)
lineV1.addWidget(b2, alignment=Qt.AlignCenter)
lineV2.addWidget(b3, alignment=Qt.AlignCenter)
lineV2.addWidget(b4, alignment=Qt.AlignCenter)

lineH1.addLayout(lineV1)
lineH1.addLayout(lineV2)

RadioGroupBox.setLayout(lineH1)

mLineH1 = QHBoxLayout()
mLineH2 = QHBoxLayout()
mLineH3 = QHBoxLayout()

question = QLabel('САМЫЙ ХАРД ВОПРОС!')
ansButton = QPushButton('Ответить!')

mLineH1.addWidget(question, alignment=Qt.AlignCenter)
mLineH2.addWidget(RadioGroupBox, alignment=Qt.AlignCenter)
mLineH3.addWidget(ansButton, alignment=Qt.AlignCenter)

#RadioGroupBox.hide()

AnsBox = QGroupBox('Результат!')
YesNoLabel = QLabel('тут будет верно/неверно')
CorrectAns = QLabel('тут верный ответ')

lineVAnsBox = QVBoxLayout()
lineVAnsBox.addWidget(YesNoLabel)
lineVAnsBox.addWidget(CorrectAns)
AnsBox.setLayout(lineVAnsBox)

mLineH2.addWidget(AnsBox)

mLineV = QVBoxLayout()

mLineV.addLayout(mLineH1)
mLineV.addLayout(mLineH2)
mLineV.addLayout(mLineH3)

main_win.setLayout(mLineV)

RadioGroup = QButtonGroup()
RadioGroup.addButton(b1)
RadioGroup.addButton(b2)
RadioGroup.addButton(b3)
RadioGroup.addButton(b4)

AnsBox.hide()

def show_results():
    RadioGroupBox.hide()
    AnsBox.show()
    ansButton.setText('Го некст')

def show_question():
    AnsBox.hide()
    RadioGroupBox.show()
    ansButton.setText('Ответить!')

    RadioGroup.setExclusive(False)
    b1.setChecked(False)
    b2.setChecked(False)
    b3.setChecked(False)
    b4.setChecked(False)
    RadioGroup.setExclusive(True)

# def TEST():
#     if 'Ответить!' == ansButton.text():
#         show_results()
#     else:
#         show_question()

answers = [b1, b2, b3, b4]

def ask(q: QuestionClass):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    CorrectAns.setText(q.right_answer)
    show_question()
    
def show_correct(result):
    YesNoLabel.setText(result)
    show_results()

def check():
    if answers[0].isChecked():
        show_correct('Верно!')
        main_win.score += 1
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
           show_correct('Неверно!')
    print('Рейтинг:', main_win.score/main_win.total*100, '%')

question_list = []

question_list.append(QuestionClass('Кто лох?', 'ты', 'автор', 'он', 'она'))
question_list.append(QuestionClass('2+2?', '4', '5', '666', '228'))
question_list.append(QuestionClass('44+100', '144', '322', '14//88', '777'))
question_list.append(QuestionClass('Когда началась WW2', '1939', '1731', '1914', '1941'))
question_list.append(QuestionClass('ТЫ ГЕЙ?', 'да', 'нет', 'неа', 'я животное'))
question_list.append(QuestionClass('ВОПРОС НА МИЛЛИОН!!!: Что тыделал вчера вечером', 'играл', 'гулял', 'я эксковатор', 'ок'))
question_list.append(QuestionClass('ТЫ КТО', 'Человек', 'абу-бандит', 'ностя мир', 'она'))
question_list.append(QuestionClass('Никита крутой?', 'да', 'нет', 'вообще даже не рядом', 'хз'))
question_list.append(QuestionClass('Какие камни есть в речке', 'Драгоценные', 'мокрые', 'Влажные', 'сухие'))
question_list.append(QuestionClass('Что не вместится даже в самую большую кастрюлю', 'ЖОПА 300КГ ТЁТКИ', 'крышка банки', 'да', 'хз'))
question_list.append(QuestionClass('Какая гора самая высокая в мире от подножия до вершины?', 'АРАРАТ', 'ЭВЕРЕСТ', 'ПИДАН', 'ПИСЯ'))
question_list.append(QuestionClass('Два человека родились одновременно, но у них разные даты рождения. Как такое может быть?', 'Родились в разны часовые пояса', 'Уэтой загадки нет ответа', 'типо хс', 'пук'))
question_list.append(QuestionClass('У кого зубы в желудке', 'краб', 'лягушка', 'орёл', 'улитка ахатины'))
question_list.append(QuestionClass('что лучше 1660 TI или 2060', '2060', '1660 Ti', 'хз', 'Я не шарю в компах'))
# main_win.cur_question = -1
main_win.total = 0
main_win.score = 0


def next_question():
    main_win.total += 1
    print('К/Д:', main_win.total, '- Всего вопросовю Верно:', main_win.score)
    # main_win.cur_question += 1

    # if main_win.cur_question >= len(question_list):
    #     main_win.cur_question = 0

    cur_question = randint(0, len(question_list)-1)
    q = question_list[cur_question]
    ask(q)

def click_Ok():
    if 'Ответить!' == ansButton.text():
        check()
    else:
        next_question()

ansButton.clicked.connect(click_Ok)

next_question()
main_win.show()
app.exec_()