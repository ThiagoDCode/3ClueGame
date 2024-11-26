import json
from random import choice
import os

words = {}

dir_app = os.path.dirname(__file__)


def restart_game():
    global words
    
    # RESET LISTA DE PALAVRAS
    with open(dir_app + "/word_list.json", mode="r", encoding="UTF-8") as file_list:
        words = json.load(file_list)

    if not os.path.exists(dir_app + "/word_list_copy.json"):
        with open("word_list_copy.json", mode="a"):...

    with open(dir_app + "/word_list_copy.json", mode="w", encoding="UTF-8") as save_list:
        save_list.write(json.dumps(words, ensure_ascii=False, indent=4))
    
    # RESET PONTUAÇÃO USUÁRIO
    with open(dir_app + "/user_data.json", mode="r", encoding="UTF-8") as file_score:
        score = json.load(file_score)
    score["words_played"] = [len(words), 1, 0]
    score["score"] = 0
    score["record"] = [0, 0]
    
    with open(dir_app + "/user_data.json", mode="w", encoding="UTF-8") as save_score:
        save_score.write(json.dumps(score, ensure_ascii=False, indent=4))


class GameSolo:
    def __init__(self):
        
        with open(dir_app + "/user_data.json", mode="r", encoding="UTF-8") as file_score:
            score_user = json.load(file_score)
        
        self.total_words_played = score_user["words_played"][1]
        self.total_words = score_user["words_played"][0]
        
        with open(dir_app + "/word_list_copy.json", mode="r", encoding="UTF-8") as file:
            self.words = json.load(file)
        
        self.word_selected, self.tips_word = choice(list(self.words.items()))
        self.words.pop(self.word_selected)
        
    def result_game(self, record=True, score_win=0):

        with open(dir_app + "/word_list_copy.json", mode="w", encoding="UTF-8") as save:
            save.write(json.dumps(self.words, ensure_ascii=False, indent=4))
        
        with open(dir_app + "/user_data.json", mode="r", encoding="UTF-8") as file_score:
            score_user = json.load(file_score)
        
        if record and score_win:
            score_user["words_played"][2] += 1   # contador de palavras descobertas
            score_user["score"] += score_win
            score_user["record"][0] += 1         # contador de palavras descobertas sequencialmente
        else:
            score_user["record"][0] = 0
        
        score_user["words_played"][1] += 1   # contador de palavras jogadas
        score_user["record"][1] = max(score_user["record"])   # salva o record máximo de palavras descobertas
        
        with open(dir_app + "/user_data.json", mode="w", encoding="UTF-8") as save_score:
            save_score.write(json.dumps(score_user, ensure_ascii=False, indent=4))
