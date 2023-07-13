from admin import administration
class Data:
    def Question_bank(question_number: int, question: str, answer: str, difficulty: str):
        ref = administration.reference()
        ref.child(str(question_number)).set({
            'question_number': question_number,
            'question': question,
            'answer': answer,
            'difficulty': difficulty
        })