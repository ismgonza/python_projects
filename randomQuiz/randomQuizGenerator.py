#! oython3
# randomQuiz Generator.py  - creates an Anti-Cheating method for nasty students by randomizing the order of questions and options and saves the answer into a file

import random
# Quiz data
capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois': 'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas': 'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine': 'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan': 'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri': 'Jefferson City',
            'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada': 'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico': 'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh', 'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City', 'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence', 'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee': 'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont': 'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia': 'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

# Generate the 35 quizes (imagine there are 35 diferent students)

for quizNum in range(5):
    # TODO: Create the quiz and answer key files
    quizFile = open('capitalsQuiz{}.txt'.format(quizNum + 1), 'w')
    answerFile = open('answerCapitalsQuiz{}.txt'.format(quizNum + 1), 'w')

    # TODO: Write out the header for the quiz
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write('State Capitals Quiz (Form {})'.format(quizNum + 1))
    quizFile.write('\n\n')

    # TODO: Shuffle the order of states
    states = list(capitals.keys())
    random.shuffle(states)

    # TODO: Loop through all 50 states, making a question for each
    for questionNum in range(50):
        # get the right answer, returns the capital for the selected state
        correctAnswer = capitals[states[questionNum]]
        # get the wrong answer, returns all the capitals in the original list
        wrongAnswer = list(capitals.values())
        # remove the right answer from the list in wrong answer
        del wrongAnswer[wrongAnswer.index(correctAnswer)]
        # randomly get 3 capitals from wrong answers to use them as options
        wrongAnswer = random.sample(wrongAnswer, 3)
        # Concat all answer options
        answerOptions = wrongAnswer + [correctAnswer]
        # Shuffle the answer Options
        random.shuffle(answerOptions)

        # TODO: write the question and answers options to the quiz file
        quizFile.write('{}. What is the Capital of {}:\n'.format(
            questionNum + 1, states[questionNum]))
        for answer in range(len(answerOptions)):
            quizFile.write('   {}. {}\n'.format(
                'ABCD'[answer], answerOptions[answer]))
        quizFile.write('\n')

        # TODO: write the answer key to a file.
        answerFile.write('{}. {}\n'.format(
            questionNum + 1, 'ABCD'[answerOptions.index(correctAnswer)]))
    quizFile.close()
    answerFile.close()
