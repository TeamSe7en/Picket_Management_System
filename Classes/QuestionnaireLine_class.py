class QuestionnaireLine:
    id = 0

    def __init__(self, questionnaire, question, answer):
        self.questionnaire = questionnaire
        self.question = question
        self.answer = answer
        self.id = QuestionnaireLine.id
        QuestionnaireLine.id += 1