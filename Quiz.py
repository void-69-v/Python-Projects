import csv
import random

count = 0
c_w = 0
c_w2 = 0
c_w3 = 0
list = []
flag = None
q = ''
q2 = ''
q3 = ''
rec = {}
scoreR1 = 0
scoreR2 = 0
scoreR3 = 0
scoreT = 0

d_Q = {
    1: 'What is the largest lake in India..?',
    2: 'Which Country has the world’s best education system..?',
    3: 'Which is the world’s largest ocean..? ',
    4: 'What is the Full form of ISRO..?',
    5: 'Which is the largest continent in the world..?',
    6: 'Which bird is the national symbol of the United States..?',
    7: 'What does DNA stand for..?',
    8: 'Which country is known as the Land of the Rising Sun..?',
    9: 'Who was the first President of the United States..?',
    10: 'Who wrote the play "Romeo and Juliet"..?',
    11: 'In which year did the Titanic sink..?',
    12: 'Which is the longest river in the world..?',
    13: 'In which year did World War II end..?',
    14: "What is the most abundant gas in the Earth's atmosphere..?",
    15: 'In which year did World War I begin..?',
    16: 'What is the currency of the United Kingdom..?',
    17: 'Who discovered penicillin..?',
    18: 'What is the smallest unit of life..?',
    19: 'What is the most common blood type in humans..?',
    20: 'What is the capital city of Canada?',
    21: 'Who invented the light bulb?',
    22:
    'which of the element called the king of the metal in periodic table..?',
    23:
    'which of the element called the king of the element in periodic table..?',
    24: 'What is the main language spoken in Brazil..?',
    25: 'Which chemical element has the symbol "Au"..?',
    26: 'Which is the smallest ocean in the world..?',
    27: 'Which vitamin is produced by the body when exposed to sunlight..?',
    28: 'Who invented the telephone..?',
    29: 'What is the capital of Russia..?',
    30: 'Who was the first woman to win a Nobel Prize?',
}
d_A = {
    1: 'Loktak Lake',
    2: 'United State',
    3: 'Pacific ocean',
    4: 'Indian Space Research Organisation',
    5: 'Asia',
    6: 'Bald Eagle',
    7: 'deoxyribonucleic acid',
    8: 'Japan',
    9: 'George Washington',
    10: 'William Shakespeare',
    11: '1912',
    12: 'Nile River',
    13: '1945',
    14: 'Nitrogen',
    15: '1914',
    16: 'Pound Sterling',
    17: 'Alexander Fleming',
    18: 'Cell',
    19: 'O',
    20: 'Ottawa',
    21: 'Thomas Edison',
    22: 'Gold (Au)',
    23: 'Carbon',
    24: 'Portuguese',
    25: 'Gold',
    26: 'Arctic Ocean',
    27: 'Vitamin D',
    28: 'Alexander Graham Bell',
    29: 'Moscow',
    30: 'Marie Curie',
}
Q1 = d_Q[1]
Q2 = d_Q[2]
Q3 = d_Q[3]
Q4 = d_Q[4]
Q5 = d_Q[5]
Q6 = d_Q[6]
Q7 = d_Q[7]
Q8 = d_Q[8]
Q9 = d_Q[9]
Q10 = d_Q[10]
Q11 = d_Q[11]
Q12 = d_Q[12]
Q13 = d_Q[13]
Q14 = d_Q[14]
Q15 = d_Q[15]
Q16 = d_Q[16]
Q17 = d_Q[17]
Q18 = d_Q[18]
Q19 = d_Q[19]
Q20 = d_Q[20]
Q21 = d_Q[21]
Q22 = d_Q[22]
Q23 = d_Q[23]
Q24 = d_Q[24]
Q25 = d_Q[25]
Q26 = d_Q[26]
Q27 = d_Q[27]
Q28 = d_Q[28]
Q29 = d_Q[29]
Q30 = d_Q[30]

A1 = d_A[1]
A2 = d_A[2]
A3 = d_A[3]
A4 = d_A[4]
A5 = d_A[5]
A6 = d_A[6]
A7 = d_A[7]
A8 = d_A[8]
A9 = d_A[9]
A10 = d_A[10]
A11 = d_A[11]
A12 = d_A[12]
A13 = d_A[13]
A14 = d_A[14]
A15 = d_A[15]
A16 = d_A[16]
A17 = d_A[17]
A18 = d_A[18]
A19 = d_A[19]
A20 = d_A[20]
A21 = d_A[21]
A22 = d_A[22]
A23 = d_A[23]
A24 = d_A[24]
A25 = d_A[25]
A26 = d_A[26]
A27 = d_A[27]
A28 = d_A[28]
A29 = d_A[29]
A30 = d_A[30]
# yeh switch me sare question ke sare answer ha or yeh dictionary data type me ha
switch = {
    Q1: A1,
    Q2: A2,
    Q3: A3,
    Q4: A4,
    Q5: A5,
    Q6: A6,
    Q7: A7,
    Q8: A8,
    Q9: A9,
    Q10: A10,
    Q11: A11,
    Q12: A12,
    Q13: A13,
    Q14: A14,
    Q15: A15,
    Q16: A16,
    Q17: A17,
    Q18: A18,
    Q19: A19,
    Q20: A20,
    Q21: A21,
    Q22: A22,
    Q23: A23,
    Q24: A24,
    Q25: A25,
    Q26: A26,
    Q27: A27,
    Q28: A28,
    Q29: A29,
    Q30: A30
}
Q_n = [
    Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11, Q12, Q13, Q14, Q15, Q16, Q17,
    Q18, Q19, Q20, Q21, Q22, Q23, Q24, Q25, Q26, Q27, Q28, Q29, Q30
]
A_n = [
    A1, A2, A3, A4, A5, A6, A7, A8, A9, A10, A11, A12, A13, A14, A15, A16, A17,
    A18, A19, A20, A21, A22, A23, A24, A25, A26, A27, A28, A29, A30
]


def rules():  # rules wala part
    print()
    print("\t ''''Rules of the Game''''")
    print()
    print(
        "\n\t There will be a total of 3 matches here \n\t\vif you think i don't want to  continue more then after it you can leave after that match whenever you want..."
    )
    print(
        '\n\t In each match You will be asked a series of different types of 10 questions.'
    )
    print('\n\t Each right answer will be awarded 2 points.')
    print('\n\t Each wrong answer will be awarded -1 points.')
    print('\n\t You will be given 4 options to choose from.')
    print(
        '\n\t If you made a mistake then the quiz automatically restart to the first question asked before.'
    )
    print('\n\t You will be given a score at the end of the game.')
    print('\n\t \t\t""""Hope you understand ,Have fun..!!!""""')
    print()


# **** Round1 begin*****
def round1():

    global flag
    global switch
    global q
    global count
    global c_w

    global c_w3
    global scoreR1
    print('\n\t\tHelllo', f'{User_name} and welcome to the Quiz')
    print()
    try:
        print('Question 1:-\n\n\t', Q1)
        print('\nOptions are\n\n\t\t', '1', ':', 'Suraj Tal Lake', '\n\t\t',
              '2', ':', 'Loktak Lake', '\n\t\t', '3', ':', 'Prashar Lake',
              '\n\t\t', '4', ':', 'Sattal Lake')
        ans = int(input('\n\nEnter the option number of your answer : '))
        d_user = {
            1: 'Suraj Tal Lake',
            2: 'Loktak Lake',
            3: 'Prashar Lake',
            4: 'Sattal Lake'
        }
        user_ans = d_user[ans]

        if user_ans == A1:
            flag = True
            list.append(flag)

            print()
            scoreR1 = scoreR1 + 2

        else:
            list.append(flag)
            c_w += 1
            flag = False
            scoreR1 = scoreR1 - 1
            q = q + Q1 + '\n'

            print()
        print('Question 2 :-\n\n\t', Q2)
        print('\nOptions are\n\n\t\t', '1', ':', 'United State', '\n\t\t', '2',
              ':', 'India', '\n\t\t', '3', ':', 'New Zealand', '\n\t\t', '4',
              ':', 'Australlia')
        ans2 = int(input('\n\nEnter the option number of your answer : '))
        d_user2 = {
            1: 'United State',
            2: 'India',
            3: 'New Zealand',
            4: 'Australlia'
        }
        user_ans2 = d_user2[ans2]
        if user_ans2 == A2:
            list.append(flag)
            flag = True
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q2 + '\n'

            print()
        print('Question 3 :-\n\n\t', Q3)
        print('\nOptions are\n\n\t\t', '1', ':', 'Atlantic ocean', '\n\t\t',
              '2', ':', 'Indian ocean', '\n\t\t', '3', ':', 'Arctic Ocean',
              '\n\t\t', '4', ':', 'Pacific ocean')
        ans3 = int(input('\n\nEnter the option number of your answer : '))
        d_user3 = {
            1: 'Atlantic ocean',
            2: 'Indian ocean',
            3: 'Arctic Ocean',
            4: 'Pacific ocean'
        }
        user_ans3 = d_user3[ans3]
        if user_ans3 == A3:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:

            flag = False
            scoreR1 = scoreR1 - 1
            list.append(flag)
            c_w += 1
            q = q + Q3 + '\n'
            print()
        print('Question 4 :-\n\n\t', Q4)
        print('\nOptions are\n\n\t\t', '1', ':',
              'Indian Scientific Research Organisation', '\n\t\t', '2', ':',
              'International Sports Research Organisation', '\n\t\t', '3', ':',
              'Indian Space Research Organisation', '\n\t\t', '4', ':',
              'International Speech Reaseach Organisation')
        ans4 = int(input('\n\nEnter the option number of your answer : '))
        d_user4 = {
            1: 'Indian Scientific Research Organisation',
            2: 'International Sports Research Organisation',
            3: 'Indian Space Research Organisation',
            4: 'International Speech Reaseach Organisation'
        }
        user_ans4 = d_user4[ans4]
        if user_ans4 == A4:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            q = q + Q4 + '\n'
            c_w += 1
            print()
        print('Question 5 :-\n\n\t', Q5)

        print('\nOptions are\n\n\t\t', '1', ':', 'Asia', '\n\t\t', '2', ':',
              'Australlia', '\n\t\t', '3', ':', 'Africa', '\n\t\t', '4', ':',
              'Europe')
        ans5 = int(input('\n\nEnter the option number of your answer : '))
        d_user5 = {1: 'Asia', 2: 'Australlia', 3: 'Africa', 4: 'Europe'}
        user_ans5 = d_user5[ans5]
        if user_ans5 == A5:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q5 + '\n'
            print()
        print()
        print('Question 6 :-\n\n\t', Q6)
        print('\nOptions are\n\n\t\t', '1', ':', 'Crow', '\n\t\t', '2', ':',
              'Ostrich', '\n\t\t', '3', ':', 'Peacock', '\n\t\t', '4', ':',
              'Bald Eagle')
        ans6 = int(input('\n\nEnter the option number of your answer : '))
        d_user6 = {1: 'Crow', 2: 'Ostrich', 3: 'Peacock', 4: 'Bald Eagle'}
        user_ans6 = d_user6[ans6]
        if user_ans6 == A6:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q6 + '\n'
            print()
        print('Question 7 :-\n\n\t', Q7)
        print('\nOptions are\n\n\t\t', '1', ':', 'deoxyribeneutral acid',
              '\n\t\t', '2', ':', 'dyoxyenucleic acid', '\n\t\t', '3', ':',
              'deoxyribonucleic acid', '\n\t\t', '4', ':', 'deltanucleic acid')
        ans7 = int(input('\n\nEnter the option number of your answer : '))
        d_user7 = {
            1: 'deoxyribeneutral acid',
            2: 'dyoxyenucleic acid',
            3: 'deoxyribonucleic acid',
            4: 'deltanucleic acid'
        }
        user_ans7 = d_user7[ans7]
        if user_ans7 == A7:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q7 + '\n'
            print()
        print('Question 8 :-\n\n\t', Q8)
        print('\nOptions are\n\n\t\t', '1', ':', 'China', '\n\t\t', '2', ':',
              'Japan', '\n\t\t', '3', ':', 'India', '\n\t\t', '4', ':',
              'United States')
        ans8 = int(input('\n\nEnter the option number of your answer : '))
        d_user8 = {1: 'China', 2: 'Japan', 3: 'India', 4: 'United States'}
        user_ans8 = d_user8[ans8]
        if user_ans8 == A8:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q8 + '\n'
            print()
        print('Question 9 :-\n\n\t', Q9)
        print('\nOptions are\n\n\t\t', '1', ':', 'George Washington', '\n\t\t',
              '2', ':', 'Abraham Lincoln', '\n\t\t', '3', ':',
              'Thomas Jefferson', '\n\t\t', '4', ':', 'John Adams')
        ans9 = int(input('\n\nEnter the option number of your answer : '))
        d_user9 = {
            1: 'George Washington',
            2: 'Abraham Lincoln',
            3: 'Thomas Jefferson',
            4: 'John Adams'
        }
        user_ans9 = d_user9[ans9]
        if user_ans9 == A9:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q9 + '\n'
            print()
        print('Question 10 :-\n\n\t', Q10)
        print('\nOptions are\n\n\t\t', '1', ':', 'Charles Dickens', '\n\t\t',
              '2', ':', 'William Shakespeare', '\n\t\t', '3', ':',
              'George Orwell', '\n\t\t', '4', ':', 'Jane Austen')
        ans10 = int(input('\n\nEnter the option number of your answer : '))
        d_user10 = {
            1: 'Charles Dickens',
            2: 'William Shakespeare',
            3: 'George Orwell',
            4: 'Jane Austen'
        }
        user_ans10 = d_user10[ans10]
        if user_ans10 == A10:
            flag = True
            list.append(flag)
            print()
            scoreR1 = scoreR1 + 2
        else:
            scoreR1 = scoreR1 - 1
            flag = False
            list.append(flag)
            c_w += 1
            q = q + Q10 + '\n'
            print()

        #print('Your score is :', scoreR1)
        print()
    except ValueError:
        print()
        q=''
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('\n\tThis is your puniment you have to play again')
        print()
        round1()
    except IndexError:
        print()
        q = ''
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round1()
    except KeyError:
        print()
        q = ''
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round1()
    else:
        print(f'Your score is : {scoreR1} out of 20')
        print()


# **** Round 2 begin ****
def round2():

    global scoreR2
    global q2
    global c_w2

    print('\n\t\tHelllo',
          f'{User_name} and welcome again  to the Quiz next round')
    print()
    try:

        print('Question 11 :-\n\n\t', Q11)
        print('\nOptions are\n\n\t\t', '1', ':', '1912', '\n\t\t', '2', ':',
              '1905', '\n\t\t', '3', ':', '1914', '\n\t\t', '4', ':', '1920')
        ans11 = int(input('\n\nEnter the option number of your answer : '))
        d_user11 = {1: '1912', 2: '1905', 3: '1914', 4: '1920'}
        user_ans11 = d_user11[ans11]
        if user_ans11 == A11:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            scoreR2 = scoreR2 - 1
            flag = False
            list.append(flag)
            c_w2 += 1
            q2 = q2 + Q11 + '\n'
            print()
        print('Question 12:-\n\n\t', Q12)
        print('\nOptions are\n\n\t\t', '1', ':', 'Amazon River', '\n\t\t', '2',
              ':', 'Nile River', '\n\t\t', '3', ':', 'Mississippi River',
              '\n\t\t', '4', ':', 'Yangtze River')
        ans12 = int(input('\n\nEnter the option number of your answer : '))
        d_user12 = {
            1: 'Amazon River',
            2: 'Nile River',
            3: 'Mississippi River',
            4: 'Yangtze River'
        }
        user_ans12 = d_user12[ans12]
        if user_ans12 == A12:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            list.append(flag)
            c_w2 += 1
            scoreR2 = scoreR2 - 1
            q2 = q2 + Q12 + '\n'
            print()
        print('Question 13 :-\n\n\t', Q13)
        print('\nOptions are\n\n\t\t', '1', ':', '1945', '\n\t\t', '2', ':',
              '1914', '\n\t\t', '3', ':', '1939', '\n\t\t', '4', ':', '1920')
        ans13 = int(input('\n\nEnter the option number of your answer : '))
        d_user13 = {1: '1945', 2: '1914', 3: '1939', 4: '1920'}
        user_ans13 = d_user13[ans13]
        if user_ans13 == A13:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            scoreR2 = scoreR2 - 1
            list.append(flag)
            c_w2 += 1
            q2 = q2 + Q13 + '\n'
            print()
        print('Question 14 :-\n\n\t', Q14)
        print('\nOptions are\n\n\t\t', '1', ':', 'Oxygen', '\n\t\t', '2', ':',
              'Hydrogen', '\n\t\t', '3', ':', 'Carbon', '\n\t\t', '4', ':',
              'Nitrogen')
        ans14 = int(input('\n\nEnter the option number of your answer : '))
        d_user14 = {1: 'Oxygen', 2: 'Hydrogen', 3: 'Carbon', 4: 'Nitrogen'}
        user_ans14 = d_user14[ans14]
        if user_ans14 == A14:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            list.append(flag)
            scoreR2 = scoreR2 - 1
            c_w2 += 1
            q2 = q2 + Q14 + '\n'
            print()
        print('Question 15 :-\n\n\t', Q15)
        print('\nOptions are\n\n\t\t', '1', ':', '1945', '\n\t\t', '2', ':',
              '1914', '\n\t\t', '3', ':', '1939', '\n\t\t', '4', ':', '1920')
        ans15 = int(input('\n\nEnter the option number of your answer : '))
        d_user15 = {1: '1945', 2: '1914', 3: '1939', 4: '1920'}
        user_ans15 = d_user15[ans15]
        if user_ans15 == A15:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            list.append(flag)
            scoreR2 = scoreR2 - 1
            c_w2 += 1
            q2 = q2 + Q15 + '\n'
            print()
        print('Question 16 :-\n\n\t', Q16)
        print('\nOptions are\n\n\t\t', '1', ':', 'Pound Sterling', '\n\t\t',
              '2', ':', 'Euro', '\n\t\t', '3', ':', 'Dollar', '\n\t\t', '4',
              ':', 'Yen')
        ans16 = int(input('\n\nEnter the option number of your answer : '))
        d_user16 = {1: 'Pound Sterling', 2: 'Euro', 3: 'Dollar', 4: 'Yen'}

        user_ans16 = d_user16[ans16]
        if user_ans16 == A16:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            list.append(flag)
            c_w2 += 1
            scoreR2 = scoreR2 - 1
            q2 = q2 + Q16 + '\n'
            print()
        print('Question 17 :-\n\n\t', Q17)
        print('\nOptions are\n\n\t\t', '1', ':', 'Gregor Mendel', '\n\t\t',
              '2', ':', 'Albert Einstein', '\n\t\t', '3', ':', 'Isaac Newton',
              '\n\t\t', '4', ':', 'Alexander Fleming')
        ans17 = int(input('\n\nEnter the option number of your answer : '))
        d_user17 = {
            1: 'Gregor Mendel',
            2: 'Albert Einstein',
            3: 'Isaac Newton',
            4: 'Alexander Fleming'
        }
        user_ans17 = d_user17[ans17]
        if user_ans17 == A17:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            scoreR2 = scoreR2 - 1
            flag = False
            list.append(flag)
            c_w2 += 1
            q2 = q2 + Q17 + '\n'
            print()
        print('Question 18 :-\n\n\t', Q18)
        print('\nOptions are\n\n\t\t', '1', ':', 'Organ', '\n\t\t', '2', ':',
              'Tissue', '\n\t\t', '3', ':', 'Cell', '\n\t\t', '4', ':', 'Atom')
        ans18 = int(input('\n\nEnter the option number of your answer : '))
        d_user18 = {1: 'Organ', 2: 'Tissue', 3: 'Cell', 4: 'Atom'}
        user_ans18 = d_user18[ans18]
        if user_ans18 == A18:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            scoreR2 = scoreR2 - 1
            list.append(flag)
            c_w2 += 1
            q2 = q2 + Q18 + '\n'
            print()
        print('Question 19 :-\n\n\t', Q19)
        print('\nOptions are\n\n\t\t', '1', ':', 'A+', '\n\t\t', '2', ':',
              'B-', '\n\t\t', '3', ':', 'O', '\n\t\t', '4', ':', 'AB')
        ans19 = int(input('\n\nEnter the option number of your answer : '))
        d_user19 = {1: 'A+', 2: 'B-', 3: 'O', 4: 'AB'}
        user_ans19 = d_user19[ans19]
        if user_ans19 == A19:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            scoreR2 = scoreR2 - 1
            list.append(flag)
            c_w2 += 1
            q2 = q2 + Q19 + '\n'
            print()
        print('Question 20 :-\n\n\t', Q20)
        print('\nOptions are\n\n\t\t', '1', ':', 'Toronto', '\n\t\t', '2', ':',
              'Vancouver', '\n\t\t', '3', ':', 'Montreal', '\n\t\t', '4', ':',
              'Ottawa')
        ans20 = int(input('\n\nEnter the option number of your answer : '))
        d_user20 = {1: 'Toronto', 2: 'Vancouver', 3: 'Montreal', 4: 'Ottawa'}
        user_ans20 = d_user20[ans20]
        if user_ans20 == A20:
            flag = True
            list.append(flag)
            print()
            scoreR2 = scoreR2 + 2
        else:
            flag = False
            list.append(flag)
            scoreR2 = scoreR2 - 1
            c_w2 += 1
            q2 = q2 + Q20 + '\n'
            print()
        #print('Your score is :', scoreR2)
        print()
    except ValueError:
        q2 =''
        print()
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round2()
    except IndexError:
        q2 =''
        print()
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round2()
    except KeyError:
        q2=''
        print()
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round2()
    else:

        print(f'Your score is : {scoreR2} out of 20')
        print()


# **** Round 3 begin ****
def round3():

    global scoreR3
    global q3
    global c_w3
    print('\n\t\tHelllo', f'{User_name} and welcome to the Quiz next round')
    print()
    try:
        print('Question 21 :-\n\n\t', Q21)
        print('\nOptions are\n\n\t\t', '1', ':', 'Thomas Edison', '\n\t\t',
              '2', ':', 'Albert Einstein', '\n\t\t', '3', ':', 'Isaac Newton',
              '\n\t\t', '4', ':', 'Alexander Fleming')
        ans21 = int(input('\n\nEnter the option number of your answer : '))
        d_user21 = {
            1: 'Thomas Edison',
            2: 'Albert Einstein',
            3: 'Isaac Newton',
            4: 'Alexander Fleming'
        }
        user_ans21 = d_user21[ans21]
        if user_ans21 == A21:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            scoreR3 = scoreR3 - 1
            list.append(flag)
            c_w3 += 1
            q3 = q3 + Q21 + '\n'
            print()
        print('Question 22 :-\n\n\t', Q22)
        print('\nOptions are\n\n\t\t', '1', ':', 'Silver', '\n\t\t', '2', ':',
              'Gold (Au)', '\n\t\t', '3', ':', 'Carbon', '\n\t\t', '4', ':',
              'Platanium')
        ans22 = int(input('\n\nEnter the option number of your answer : '))
        d_user22 = {1: 'Silver', 2: 'Gold (Au)', 3: 'Carbon', 4: 'Platanium'}
        user_ans22 = d_user22[ans22]
        if user_ans22 == A22:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            scoreR3 = scoreR3 - 1
            list.append(flag)
            c_w3 += 1
            q3 = q3 + Q22 + '\n'
            print()
        print('Question 23 :-\n\n\t', Q23)
        print('\nOptions are\n\n\t\t', '1', ':', 'Carbon', '\n\t\t', '2', ':',
              'Oxygen', '\n\t\t', '3', ':', 'Nitrogen', '\n\t\t', '4', ':',
              'Hydrogen')
        ans23 = int(input('\n\nEnter the option number of your answer : '))
        d_user23 = {1: 'Carbon', 2: 'Oxygen', 3: 'Nitrogen', 4: 'Hydrogen'}
        user_ans23 = d_user23[ans23]
        if user_ans23 == A23:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            list.append(flag)
            scoreR3 = scoreR3 - 1
            c_w3 += 1
            q3 = q3 + Q23 + '\n'
            print()
        print('Question 24 :-\n\n\t', Q24)
        print('\nOptions are\n\n\t\t', '1', ':', 'Brazilian', '\n\t\t', '2',
              ':', 'American', '\n\t\t', '3', ':', 'Canadian', '\n\t\t', '4',
              ':', 'Portuguese')
        ans24 = int(input('\n\nEnter the option number of your answer : '))
        d_user24 = {
            1: 'Brazilian',
            2: 'American',
            3: 'Canadian',
            4: 'Portuguese'
        }
        user_ans24 = d_user24[ans24]
        if user_ans24 == A24:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            list.append(flag)
            scoreR3 = scoreR3 - 1
            c_w3 += 1
            q3 = q3 + Q24 + '\n'
            print()
        print('Question 25 :-\n\n\t', Q25)
        print('\nOptions are\n\n\t\t', '1', ':', 'Gold', '\n\t\t', '2', ':',
              'Silver', '\n\t\t', '3', ':', 'Copper', '\n\t\t', '4', ':',
              'Platinum')
        ans25 = int(input('\n\nEnter the option number of your answer : '))
        d_user25 = {1: 'Gold', 2: 'Silver', 3: 'Copper', 4: 'Platinum'}
        user_ans25 = d_user25[ans25]
        if user_ans25 == A25:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            list.append(flag)
            scoreR3 = scoreR3 - 1
            c_w3 += 1
            q3 = q3 + Q25 + '\n'
            print()
        print('Question 26 :-\n\n\t', Q26)
        print('\nOptions are\n\n\t\t', '1', ':', 'Arctic Ocean', '\n\t\t', '2',
              ':', 'Atlantic Ocean', '\n\t\t', '3', ':', 'Indian Ocean',
              '\n\t\t', '4', ':', 'Pacific Ocean')
        ans26 = int(input('\n\nEnter the option number of your answer : '))
        d_user26 = {
            1: 'Arctic Ocean',
            2: 'Atlantic Ocean',
            3: 'Indian Ocean',
            4: 'Pacific Ocean'
        }
        user_ans26 = d_user26[ans26]
        if user_ans26 == A26:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            scoreR3 = scoreR3 - 1
            flag = False
            list.append(flag)
            c_w3 += 1
            q3 = q3 + Q26 + '\n'
            print()
        print('Question 27 :-\n\n\t', Q27)
        print('\nOptions are\n\n\t\t', '1', ':', 'Vitamin B12', '\n\t\t', '2',
              ':', 'Vitamin D', '\n\t\t', '3', ':', 'Vitamin B6', '\n\t\t',
              '4', ':', 'Vitamin B9')
        ans27 = int(input('\n\nEnter the option number of your answer : '))
        d_user27 = {
            1: 'Vitamin B12',
            2: 'Vitamin D',
            3: 'Vitamin B6',
            4: 'Vitamin B9'
        }
        user_ans27 = d_user27[ans27]
        if user_ans27 == A27:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            list.append(flag)
            scoreR3 = scoreR3 - 1
            c_w3 += 1
            q3 = q3 + Q27 + '\n'
            print()
        print('Question 28 :-\n\n\t', Q28)
        print('\nOptions are\n\n\t\t', '1', ':', 'Alexander Graham Bell',
              '\n\t\t', '2', ':', 'Thomas Edison', '\n\t\t', '3', ':',
              'Isaac Newton', '\n\t\t', '4', ':', 'Alexander Fleming')
        ans28 = int(input('\n\nEnter the option number of your answer : '))
        d_user28 = {
            1: 'Alexander Graham Bell',
            2: 'Thomas Edison',
            3: 'Isaac Newton',
            4: 'Alexander Fleming'
        }
        user_ans28 = d_user28[ans28]
        if user_ans28 == A28:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            scoreR3 = scoreR3 - 1
            list.append(flag)
            c_w3 += 1
            q3 = q3 + Q28 + '\n'
            print()
        print('Question 29 :-\n\n\t', Q29)
        print('\nOptions are\n\n\t\t', '1', ':', 'Moscow', '\n\t\t', '2', ':',
              'Paris', '\n\t\t', '3', ':', 'Rome', '\n\t\t', '4', ':',
              'London')
        ans29 = int(input('\n\nEnter the option number of your answer : '))
        d_user29 = {1: 'Moscow', 2: 'Paris', 3: 'Rome', 4: 'London'}
        user_ans29 = d_user29[ans29]
        if user_ans29 == A29:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            flag = False
            list.append(flag)
            scoreR3 = scoreR3 - 1
            c_w3 += 1
            q3 = q3 + Q29 + '\n'
            print()
        print('Question 30 :-\n\n\t', Q30)
        print('\nOptions are\n\n\t\t', '1', ':', 'Rosalind Franklin', '\n\t\t',
              '2', ':', 'Newton', '\n\t\t', '3', ':', 'Marie Curie', '\n\t\t',
              '4', ':', 'Jane Austen')
        ans30 = int(input('\n\nEnter the option number of your answer : '))
        d_user30 = {
            1: 'Rosalind Franklin',
            2: 'Newton',
            3: 'Marie Curie',
            4: 'Jane Austen'
        }
        user_ans30 = d_user30[ans30]
        if user_ans30 == A30:
            flag = True
            list.append(flag)
            print()
            scoreR3 = scoreR3 + 2
        else:
            scoreR3 = scoreR3 - 1
            flag = False
            list.append(flag)
            c_w3 += 1
            q3 = q3 + Q30 + '\n'
            print()
        #print('Your score is :', scoreR3)
    except ValueError:
        q3=''
        print()
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round3()
    except KeyError:
        q3=''
        print()
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round3()
    except IndexError:
        q3 =''
        print()
        print('\t\tWarning...!!')
        print('\n\tPlease enter the correct option number')
        print('This is your puniment you have to play again')
        print()
        round3()
    else:
        print(f'Your score is : {scoreR3}')
        print()


def Quiz():
    global Q_n
    global A_n
    global scoreT
    print()

    print()
    f = open('quiz.txt', 'w')
    if count == 0:
        round1()
        temp = q.split('\n')

        for i in temp:
            if i != '':
                f.write(f'Question :- {i}')
                f.write('\n')
                f.write(f'Answer :- \t\t{switch[i]}\n')

        print(f'The number of questions are wrong :{c_w} which are:-')

    elif count == 1:
        round2()
        temp = q2.split('\n')
        for i in temp:
            if i != '':
                f.write(f'Question :- {i}')
                f.write('\n')
                f.write(f'Answer :- \t\t{switch[i]}\n')
        print(f'The number of questions are wrong :{c_w2} which are:-')
    elif count == 2:
        round3()
        temp = q3.split('\n')
        for i in temp:
            if i != '':
                f.write(f'Question :- {i}')
                f.write('\n')
                f.write(f'Answer :- \t\t{switch[i]}\n')
        print(f'The number of questions are wrong :{c_w3} which are:-')
    elif count > 2:
        print('You have completed the quiz')
        print()
        scoreT = scoreR1 + scoreR2 + scoreR3
        print('Your Total score is :', scoreT)
        exit()
    f.close()

    f1 = open('quiz.csv', 'a', newline='')
    data = [User_name, scoreT]
    data1 = csv.writer(f1)

    data1.writerow(data)
    f1.close()

    print()
    f.close()
    f = open('quiz.txt', 'r')
    print()
    c_w_net = c_w + c_w2 + c_w3
    #print(f'The number of questions are wrong :{c_w_net} which are:-')
    r = f.readlines()
    print()
    for i in r:
        print(i)
    print()


def user():

    global count
    print('''Choices are :-
                 1 : Start the quiz
                 2 : You want to know the rules again
                 3 : Previous users score data
                 4 : Exit 
                 ''')
    print('What do you want to do...')
    while True:
        print()
        user_input = input('Enter the number of operation you want to do : ')
        if user_input == '1':
            Quiz()
            count += 1
            print('Thanks for playing the quiz')
            break
        elif user_input == '2':
            rules()
            print()
            print()
            print('''Choices are :-
                    1: Start the quiz
                    2: Exit''')
            print('What do you want to do...')
            print()
            user_input2 = input(
                'Enter the number of operation you want to do : ')
            if user_input2 == '1':
                Quiz()
                count += 1
                print()
                print('\tThank for playing the Quiz')
                break
            elif user_input2 == '2':
                print()
                print('''\tAre you sure don't you have to play again :-
                             1 : Yes
                             2 : No''')
                print()
                user_input4 = input(
                    'Enter the number of operation you want to do : ')
                if user_input4 == '1':
                    print()
                    print('')
                    print('\tThanks for coming...!!!')
                    exit()
                elif user_input4 == '2':
                    print()
                    user()
                else:
                    print('Invalid Input')

                break
            else:
                print('\tInvalid input')
        elif user_input == '3':
            f2 = open('quiz.csv', 'r')
            data2 = csv.reader(f2)
            
            print('\nSome previous users data is :-')
            print()
            for i in data2:
                print('\t', i[0], ':- ', i[1])
            f2.close()
            print()
            print()
            print('''Choices are :-
                    1: Start the quiz
                    2: Exit''')
            print('What do you want to do...')
            print()
            user_input3 = input(
                'Enter the number of operation you want to do : ')
            if user_input3 == '1':
                Quiz()
                count += 1
                print()
                print('\tThanks for playing the quiz')
                break
            elif user_input3 == '2':
                print()
                print()
                print('''\tAre you sure don't you have to play again :-
                             1 : Yes
                             2 : No''')
                print()
                user_input4 = input(
                    'Enter the number of operation you want to do : ')
                if user_input4 == '1':
                    print()
                    print('')
                    print('\tThanks for coming...!!!')
                    exit()
                elif user_input4 == '2':
                    print()
                    user()
                else:
                    print('Invalid Input')

                break
            else:
                print()
                print('\tInvalid input')
        elif user_input == '4':
            print()
            print('\tThank for playing')
            exit()
        else:
            print()
            print('\tInvalid input')

    print()
    restart()


def restart():
    print()
    print('''Do you wanna to play again :-
                 1 : Yes
                 2 : No''')
    print()
    user_input4 = input('Enter the number of operation you want to do : ')
    if user_input4 == '1':
        print()
        user()
    else:
        print()
        print()
        print('''\tAre you sure don't you have to play again :-
                     1 : Yes
                     2 : No''')
        print()
        user_input4 = input('Enter the number of operation you want to do : ')
        if user_input4 == '1':
            print()
            print('')
            print('\tThanks for coming...!!!')
            exit()
        elif user_input4 == '2':
            print()
            user()
        else:
            print('Invalid Input')


print('\n\t\t\tWelcome to the quiz')
User_name = input('\nEnter your good name: ')
print(
    '\n\nFirst you have to know about the rules of the quiz which is mandatory'
)
print()
rules()
print()
user()
