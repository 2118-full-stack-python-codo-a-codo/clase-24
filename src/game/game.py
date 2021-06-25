from game.player import *
from random import random

class Game:
    
    def __init__(self) -> None:
        """
        Solo el constructor
        """
        self.__player1 = None
        self.__player2 = None
    
    @property
    def player1(self):
        return self.__player1

    @player1.setter
    def player1(self, player1):
        self.__player1 = player1

    def __str__(self) -> str:
        return f"Esto es el objeto Game"
    
    def start(self) -> bool:
        pass

    def end(self) -> bool:
        pass
    
    def update(self) -> bool:
        self.player2.score = random() * 10
        self.player1.score = random() * 10
        return False