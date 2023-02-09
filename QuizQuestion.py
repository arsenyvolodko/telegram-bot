class NewYearQuizQuestion:

    def __init__(self, question: str, options: list, answer_num: int, options_callbacks: list):
        self.question = question
        self.options = options
        self.answer_num = answer_num
        self.options_callbacks = options_callbacks
