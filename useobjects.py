"""Документ со всеми обьектами с которыми может взаимодействовать персонаж, но которые не являются НПС.
Сундуки, двери, знаки и так далее"""

import pygame
import os
from constants import *


class UseObject:
    """Базовый класс для используеммых вещей"""
    def __init__(self):
        """Грузит изображение и получает его размеры"""
        self.image = pygame.Surface([25, 25]).convert()
        self.rect = self.image.get_rect()

    def use(self):
        """Описывает что случится, когда игрок провзаимодействует с предметом"""
        pass


class Gateway(UseObject):
    """Класс прохода. По сути это невидимый тригер который можно ставить на коней, двери, лестницы и т.п.
     и он будет переводить персонажа на новый уровень."""

    def __init__(self, level_name):
        """Создаем невидимый квадрат и передаем его для получения размеров,
        а так же записываем номер уровня куда эта дверь ведет"""
        self.lead_to_level = level_name
        super().__init__()


    def use(self, game):
        """Сообщаем игре что текущий уровень поменялся. А она уже сама с этим разберется"""
        game.level_number = self.lead_to_level


class NewSceneTrigger(UseObject):
    """Такс такс такс, тут по идее будет класс который запускаем новую сессию,
    то есть передает экран и время другой прожке. Это ставит игру на паузу и вызывает меню,диалоги и т.д."""
    def __init__(self, scene):
        self.scene = scene
        super().__init__()

    def use(self, screen, clock):
        """Эта функция передает какому то другому элементу управление над экранном и временем"""
        self.scene.player_control(screen, clock)