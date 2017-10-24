class Questionnaire:
    id = 0

    def __init__(self, person_name, phone, email):
        self.person_name = person_name
        self.phone = phone
        self.email = email
        self.id = Questionnaire.id
        Questionnaire.id += 1
