import Question_class
import Answer_class

def test_func():
    print('Hello')


test_func()

q = Question_class.Question('Вопрос 1')
print(q.text)


a1 = Answer_class.Answer(q,'Ответ 1')
a2 = Answer_class.Answer(q,'Ответ 2')

print(q.voted, a1.voted)
a1.choose()

print(q.voted, a1.voted)
