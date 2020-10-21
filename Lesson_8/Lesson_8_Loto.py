import random
import sys

class LotoCard:
    def __init__(self, player):
        self.player = player
        self.card = [['  ','  ','  ','  ','  ','  ','  ','  ','  '],
                     ['  ','  ','  ','  ','  ','  ','  ','  ','  '],
                     ['  ','  ','  ','  ','  ','  ','  ','  ','  ']]
        self.number_list = []

    def create_number(self):
        num_counter = 1
        while num_counter < 16:
            number = random.randint(1, 90)
            if number in self.number_list:
                continue
            self.number_list.append(number)
            for i in range(9):
                similar_num_counter = 0
                for item in self.number_list:
                    upper_boarder = (i + 1) * 10
                    if i == 8:
                        upper_boarder = 91
                    if i * 10 <= item < upper_boarder:
                        similar_num_counter += 1
                if similar_num_counter > 3:
                    self.number_list.pop()
            num_counter += 1
        self.number_list.sort()

    def fillout_card(self):
        for el in self.number_list:
            i = 0
            while i < 9:
                upper_boarder = (i + 1) * 10
                if i == 8:
                    upper_boarder = 91
                if i * 10 <= el < upper_boarder:
                    counter = [[], [], []]
                    for j, line in enumerate(self.card):
                        for item in self.card[j]:
                            if item != '  ':
                                counter[j].append(item)
                    if len(counter[0]) >= len(counter[1]):
                        if len(counter[1]) >= len(counter[2]):
                            if self.card[2][i] == '  ':
                                self.card[2][i] = el
                            else:
                                counter[2].append(0)
                                i -= 1
                                continue
                        else:
                            if self.card[1][i] == '  ':
                                self.card[1][i] = el
                            else:
                                counter[1].append(0)
                                i -= 1
                                continue
                    else:
                        if self.card[0][i] == '  ':
                            self.card[0][i] = el
                        else:
                            counter[0].append(0)
                            i -= 1
                            continue
                i += 1

    def draw_card(self):
        print('-'* 9 + self.player + '-'* 10)
        for i in self.card:
            for index, j in enumerate(i):
                if j != '  ' and j != '--' and int(j) < 10:
                    j = ' ' + str(j)
                print(j, end=' ')
                if index % 8 == 0 and index != 0:
                    print('\n'.strip())
        print('-' * 27)


class Game:
    def __init__(self, card1, card2):
        self.card1 = card1
        self.card2 = card2
        self.bag_num = []

    def start(self):
        card1.create_number()
        card1.fillout_card()
        card2.create_number()
        card2.fillout_card()
        self.start_game()


    def start_game(self):
        quit_game = 0
        while quit_game == 0:
            winner = 1
            for line in self.card1.card:
                for item in line:
                    if str(item).isnumeric():
                        winner = 0
            if winner == 1:
                print('You won!')
                break
            winner = 1
            for line in self.card2.card:
                for item in line:
                    if str(item).isnumeric():
                        winner = 0
            if winner == 1:
                print('Computer won!')
                break

            rand_bag_num = random.randint(1, 90)
            if rand_bag_num in self.bag_num:
                continue
            else:
                self.bag_num.append(rand_bag_num)
                print(f'The number is {rand_bag_num}')
                card1.draw_card()
                card2.draw_card()
                error_input = 0
                while True:
                    user_answer = input('Would you like to cross the number?(y/n)').strip()
                    for line_index, line in enumerate(self.card2.card):
                        for item_index, item in enumerate(line):
                            if rand_bag_num == item:
                                self.card2.card[line_index][item_index] = '--'
                    if user_answer == 'y':
                        for line_index, line in enumerate(self.card1.card):
                            for item_index, item in enumerate(line):
                                if rand_bag_num == item:
                                    self.card1.card[line_index][item_index] = '--'
                                    sys.stdout.flush()
                                    print('The choice is done correctly.\n', 27 * '*', '\n')
                                    error_input = 1
                        if error_input == 1:
                            break
                        print('Your choice is incorrect. You lost the game.')
                        quit_game = 1
                        break
                    elif user_answer == 'n':
                        for line_index, line in enumerate(self.card1.card):
                            for item_index, item in enumerate(line):
                                if rand_bag_num == item:
                                    print('The choice is done incorrectly. You lost the game.')
                                    quit_game = 1
                                    error_input = 1
                        if error_input == 1:
                            break
                        print('The choice is done correctly.\n', 27 * '*', '\n')
                        break
                    else:
                        print('Input is incorrect.')
                        continue






card1 = LotoCard('-Player-')
card2 = LotoCard('Computer')

game = Game(card1, card2)
game.start()
