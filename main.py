from abc import ABC, abstractmethod
from fastapi import FastAPI

app = FastAPI()

class WarGame(ABC):
    def play(self):
        self.prepare_game()
        self.start_game()
        self.end_game()

    @abstractmethod
    def prepare_game(self):
        pass

    @abstractmethod
    def start_game(self):
        pass

    @abstractmethod
    def end_game(self):
        pass

class War(WarGame):
    def __init__(self, num_players):
        self.num_players = num_players

    def prepare_game(self):
        print("Preparando o jogo War com {} jogadores.".format(self.num_players))

    def start_game(self):
        self.set_attack_defense()

    def end_game(self):
        print("Jogo War terminado.")

    def set_attack_defense(self):
        attack_dice = max(1, self.num_players // 2)
        defense_dice = max(1, self.num_players // 3)
        print("Quantidade de dados de ataque: {}".format(attack_dice))
        print("Quantidade de dados de defesa: {}".format(defense_dice))
        return attack_dice, defense_dice

@app.post("/start_war_game/")
async def start_war_game(num_players: int):
    if num_players < 2:
        return {"error": "Número de jogadores deve ser no mínimo 2"}
    
    game = War(num_players)
    game.play()
    return {"message": "Jogo War iniciado com {} jogadores.".format(num_players)}

