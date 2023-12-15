from pprint import pprint
from random import randint, uniform

import numpy as np


class Qrl:

    def __init__(self) -> None:
        pass

    def setup(self):
        self.alpha = 0.1
        self.gamma = 0.6
        self.epsilon = 0.9

        # observation_space
        # 40 possiveis cartas na posição 1 da mão
        # 40 (39) possiveis cartas na posição 2 da mão
        # 40 (38) possiveis cartas na posição 3 da mão + ausente (por se aproximar do fim do jogo)
        # 40 (37) possiveis cartas na mesa + ausente (por ser o primeiro a jogar)
        # 40×40×41×41 = 2_689_600 com posições impossíveis (cartas repetidas) 
        # 40×39×39×38 = 2_311_920 sem posições impossíveis (mais custoso de trabalhar)
        self.observation_space_size = 2_689_600

        # action_space
        # escolher uma das 3 possíveis posições da mão
        self.action_space = [0, 1, 2]

        # reward
        # positiva a quantidade de pontos ganha pelo jogador no resultado da mão
        # negativa a quantidade de pontos ganha pelo oponente no resultado da mão
        # -100 por uma escolha inválida (uma posição da mão que está ausente)

        self.q_table = np.zeros([self.observation_space_size, len(self.action_space)])


    def get_action(self, state):
        if uniform(0, 1) < self.epsilon:
            return self.action_space_sample()  # Explore action space
        else:
            return np.argmax(self.q_table[state])  # Exploit learned values

    def run_episode(self):
        state, info = self.env.reset()
        self.init_steps()
        while not (self.done or self.truncated):
            action = self.get_action(state)
            (
                next_state,
                reward,
                self.done,
                self.truncated,
                info,
            ) = self.env.step(action)
            self.update_qtable(state, action, reward, next_state)
            state = next_state
            self.print_step()
            self.step += 1
        self.csv_write()
        self.end_print_step()
