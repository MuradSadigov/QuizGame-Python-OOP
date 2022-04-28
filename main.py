from question_model import Question
from Data import question_data
from quiz_brain import QuizBrain


question_bank = []
for data in question_data:
    d_text = data["question"]
    d_answer = data["correct_answer"]
    question_bank.append(Question(d_text, d_answer))


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()


print(f"You've completed the quiz.\nYour final score was: {quiz.score}/{len(question_bank)}")
