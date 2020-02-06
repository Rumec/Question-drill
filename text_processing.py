"""
This program is used for practicing questions for exams.
Author: Dominik Rumian
12-03-2019
"""


def readFile(nameOfFile):
    """
    Loads questions from a file (specified by the name given as parameter), it stores then questins with
    answers in a form of list
    :param nameOfFile: File to be loaded
    :return: List of tuples containing questions
    """
    file = open(nameOfFile, "r")
    questions = []
    tuple = ("", [0])
    for line in file:
        # Some lines doesn't contain relevant informations (the file is exported from pdf)
        if len(line) <= 3:
            continue
        l = line.strip().strip('\n')
        # Question
        if not (l.startswith('a)') or l.startswith('b)') or l.startswith('c)') or l.startswith('d)') or l.startswith(
                'e)')):
            questions.append(tuple)
            tuple = (l, [0])
        # Possibilities
        elif (l.startswith('a)') or l.startswith('b)') or l.startswith('c)') or l.startswith('d)') or l.startswith(
                'e)')):
            tuple[1].append(l)
            # Correct answer
            if '€' in l:
                tuple[1][0] = l[0]
    file.close()
    questions.pop(0)
    return questions


def questions_and_answers(questions):
    """
    Looping through questions and testing the user
    :param questions: List of tuple containing questions
    :return: void
    """
    while True:
        num_of_question = 1
        jump = 0
        for tuple in questions:
            if jump > 0:
                jump -= 1
                continue
            print("Otazka c.: ", num_of_question, ':\n', tuple[0])
            for i in range(1, len(tuple[1])):
                print(tuple[1][i].strip('€'))
            answer = input("Odpoved:\n")

            # Jumping 'jump' questions forward
            if answer[0] == ':':
                jump = int(answer.strip(':')) - 1
                num_of_question += jump + 1
                continue

            while answer not in ('a', 'b', 'c', 'd', 'e'):
                print("Neplatna volba! Zadej pismeno od 'a' do 'e'!!\n")
                answer = input("Odpoved:\n")
            if answer == tuple[1][0]:
                print("Spravne!!!\n\n\n")
                num_of_question += 1
                continue
            else:
                print("Spatne, spravna odpoved je: ", tuple[1][0], "\n\n\n")
            num_of_question += 1
        print("\n\n\nVsechny otazky byly projity, spusti se opet od zacatku\n\n\n")
        num_of_question = 1


questions_and_answers(readFile("otazky.txt"))
