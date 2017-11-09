import Question_class


class Answer:
    id = 0
    voted = 0

    def __init__(self, question, text):
        self.question = question
        self.text = text
        self.id = Answer.id
        Answer.id += 1

    def choose(self):
        self.voted += 1
        self.question.inc_voted()
