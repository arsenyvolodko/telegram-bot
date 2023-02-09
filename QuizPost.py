class QuizPost:

    def __init__(self, id: int, question_list_size: int):
        self.id = id
        self.score = [0 for _ in range(question_list_size)]
