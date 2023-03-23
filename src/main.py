import random
import os
import importlib

import src.qs as qs
importlib.reload(qs)


class PySkillTester:
    def __init__(self):
        self.folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ans")
        self.num_files = self.count_py_files()
        
        self.questions = [getattr(qs, f'q{i}') for i in range(1, self.num_files)]
        
        repo_link = 'https://github.com/cywei23/PySkillTester/blob/main/src/ans/ans'
        
        self.answers = [repo_link + str(i) + '.py' for i in range(1, self.num_files)]

    def count_py_files(self):
        return sum(1 for file in os.listdir(self.folder_path) if file.endswith('.py'))

    def pick_random_question(self):
        index = random.randrange(len(self.questions))
        return index, self.questions[index]

    def pick_specific_question(self, question_number):
        index = question_number - 1
        print(index)
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
        print('\n', 'Answer link:', answer)