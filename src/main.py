import random
import qs
import importlib
importlib.reload(qs)


class PySkillTester:
    def __init__(self):
        self.questions = [getattr(qs, f'q{i}') for i in range(1, 4)]
        
        repo_link = 'https://github.com/cywei23/PySkillTester/src/ans/ans'
        
        self.answers = [repo_link + str(i) + '.py' for i in range(1, 4)]

    def pick_random_question(self):
        index = random.randrange(len(self.questions))
        return index, self.questions[index]

    def pick_specific_question(self, question_number):
        index = question_number - 1
        return index, self.questions[index]

    def display_question(self, question_number=None):
        if question_number is not None:
            index, question = self.pick_specific_question(question_number)
        else:
            index, question = self.pick_random_question()
        
        self.current_index = index
        print(question)

    def display_answer(self):
        answer = self.answers[self.current_index]
        print(answer)



