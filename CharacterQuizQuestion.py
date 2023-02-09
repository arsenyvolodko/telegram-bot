class CharacterQuizQuestion:

    def __init__(self, question_num: int, options_list: list):
        self.question_num = question_num
        self.picture = f"media/CharacterQuizPics/{question_num}.png"
        self.options_list = options_list
