from telebot import types
import re
import Constants
from QuizPost import QuizPost
import os


class User:
    def __init__(self, id: int, first_name: str, last_name: str, username: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.__culture_post_cnt = 0
        self.__music_post_cnt = 0
        self.__aes_post_cnt = 0
        self.new_year_quiz_dict = {}
        self.character_quiz_dict = {}

    def get_cur_aes_post(self):
        if self.__aes_post_cnt == 0:
            num = -1
        elif self.__aes_post_cnt == len(Constants.AES_POSTS) - 1:
            num = 1
        else:
            num = 0
        return Constants.AES_POSTS[self.__aes_post_cnt], num

    def increase_aes_post_cnt(self):
        if self.__aes_post_cnt < len(Constants.AES_POSTS) - 1:
            self.__aes_post_cnt += 1

    def decrease_aes_post_cnt(self):
        if self.__aes_post_cnt > 0:
            self.__aes_post_cnt -= 1

    def get_cur_music_post(self):
        if self.__music_post_cnt == 0:
            num = -1
        elif self.__music_post_cnt == len(Constants.MUSIC_POSTS) - 1:
            num = 1
        else:
            num = 0
        if 0 <= self.__music_post_cnt <= len(Constants.MUSIC_POSTS):
            return Constants.MUSIC_POSTS[self.__music_post_cnt], num

    def increase_music_post_cnt(self):
        if self.__music_post_cnt < len(Constants.MUSIC_POSTS) - 1:
            self.__music_post_cnt += 1

    def decrease_music_post_cnt(self):
        if self.__music_post_cnt > 0:
            self.__music_post_cnt -= 1

    def get_cur_culture_post(self):
        if self.__culture_post_cnt == 0:
            num = -1
        elif self.__culture_post_cnt == len(Constants.CULTURE_POSTS) - 1:
            num = 1
        else:
            num = 0
        return Constants.CULTURE_POSTS[self.__culture_post_cnt], num

    def increase_culture_post_cnt(self):
        if self.__culture_post_cnt < len(Constants.CULTURE_POSTS) - 1:
            self.__culture_post_cnt += 1

    def decrease_culture_post_cnt(self):
        if self.__culture_post_cnt > 0:
            self.__culture_post_cnt -= 1

    def add_new_year_quiz(self, id: int):
        self.new_year_quiz_dict[id] = QuizPost(id, 13)

    def get_new_year_quiz(self, message: types.Message):
        # return self.new_year_quiz_dict[message.message_id]
        try:
            return self.new_year_quiz_dict[message.message_id]
        except KeyError:
            quiz = QuizPost(message.message_id, 13)
            res = re.findall(r'Верно \d', message.text)[0].split()[1]
            for i in range(int(res)):
                quiz.score[i] = 1
            self.new_year_quiz_dict[message.message_id] = quiz
            return quiz

    def delete_new_year_quiz(self, id: int):
        self.new_year_quiz_dict.pop(id)

    def add_character_quiz(self, message_id: int):
        file = open(f"metadata/character_quiz_metadata/{self.id}-{message_id}.txt", "w")
        file.write(" ".join(['0' for _ in range(Constants.CHARACTER_QUIZ_LENGTH)]))
        file.close()
        self.character_quiz_dict[message_id] = QuizPost(self.id, Constants.CHARACTER_QUIZ_LENGTH)

    def get_character_quiz(self, message: types.Message):
        try:
            return self.character_quiz_dict[message.message_id]
        except KeyError:
            quiz = QuizPost(self.id, Constants.CHARACTER_QUIZ_LENGTH)
            file = open(f"metadata/character_quiz_metadata/{self.id}-{message.message_id}.txt", "r")
            quiz.score = list(map(int, file.read().split()))
            file.close()
            self.character_quiz_dict[message.message_id] = quiz
            return quiz

    def update_character_quiz_score(self, message: types.Message, answer_num: int):
        cur_quiz = self.get_character_quiz(message)
        cur_quiz.score[
            (Constants.CHARACTER_QUIZ_LENGTH - cur_quiz.score.count(0)) % Constants.CHARACTER_QUIZ_LENGTH] = answer_num
        file = open(f"metadata/character_quiz_metadata/{self.id}-{message.message_id}.txt", "w")
        file.write(" ".join(map(str, cur_quiz.score)))
        file.close()
        return Constants.CHARACTER_QUIZ_LENGTH - cur_quiz.score.count(0)

    def delete_character_quiz(self, message_id: int):
        try:
            os.remove(f"metadata/character_quiz_metadata/{self.id}-{message_id}.txt")
            self.character_quiz_dict.pop(message_id)
        except Exception:
            pass

    def toString(self):
        return "id: " + str(self.id) + "\nfirst_name: " + str(self.first_name) + "\nlast_name: " + str(
            self.last_name) + "\nusername: " + str(self.username)
