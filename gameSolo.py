import json
from random import choice

words = {}

def restart_game():
    global words
    
    print("CHAMOU NEW_GAME")
    with open("word_list.json", mode="r", encoding="UTF-8") as file_list:
        words = json.load(file_list)

    with open("word_list_copy.json", mode="w", encoding="UTF-8") as save_list:
        save_list.write(json.dumps(words, ensure_ascii=False, indent=4))
        
    with open("user_data.json", mode="r", encoding="UTF-8") as file_score:
        score = json.load(file_score)
    score["words_win"] = 0
    score["score"] = 0
    score["record"] = 0
    
    with open("user_data.json", mode="w", encoding="UTF-8") as save_score:
        save_score.write(json.dumps(score, ensure_ascii=False, indent=4))


class GameSolo:
    def __init__(self):
        self.total_words = len(words)
        self.words_played = 0
        self.score = 0
        
        
        with open("word_list_copy.json", mode="r", encoding="UTF-8") as file:
            self.words = json.load(file)
        
        self.word_selected, self.tips_word = choice(list(self.words.items()))
        
        print("CHAMOU GAME-SOLO")
        print(self.total_words)
        print(self.word_selected)
        print(self.tips_word)
        
        self.words.pop(self.word_selected)
        with open("word_list_copy.json", mode="w", encoding="UTF-8") as save:
            save.write(json.dumps(self.words, ensure_ascii=False, indent=4))
    
    def score_win(self, score_win):
        with open("user_data.json", mode="r", encoding="UTF-8") as file_score:
            score = json.load(file_score)
        
        score["words_win"] += 1
        score["score"] += score_win
        score["record"] = 0
        
        with open("user_data.json", mode="w", encoding="UTF-8") as save_score:
            save_score.write(json.dumps(score, ensure_ascii=False, indent=4))
    