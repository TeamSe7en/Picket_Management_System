class Question:
    id = 0
    voted = 0

    def __init__(self, text, no_option):
        self.text = text
        self.no_option = no_option
        self.id = Question.id
        Question.id += 1
        #self.voted = 0

    def inc_voted(self):
        self.voted+=1

        



