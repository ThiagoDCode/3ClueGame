import json
from random import choice
from operator import itemgetter


with open("word_list.json", mode="r", encoding="UTF-8") as file:
    words = json.load(file)


class Game_Solo:
    def __init__(self):
        self.words_played = 0           # número de palavras jogadas
        self.score = 0                  # pontuação total do jogador
        self.total_words = len(words)   # total de palavras secretas do game

    def play_word(self):
        if words:
            self.word_selected, self.tips_word = choice(list(words.items()))
            self.words_played += 1
            words.pop(self.word_selected)
            
            return self.word_selected, self.tips_word
        else:
            return False
