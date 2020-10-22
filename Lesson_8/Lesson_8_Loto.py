import random


class LotoCard:
    def __init__(self, player):
        self.player = player
        self.card = [['  ','  ','  ','  ','  ','  ','  ','  ','  '],
                     ['  ','  ','  ','  ','  ','  ','  ','  ','  '],
                     ['  ','  ','  ','  ','  ','  ','  ','  ','  ']]
        self.number_list = []

    def create_number(self):
        '''
        The method creates numbers for a card.
        '''
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
        '''
        The method fills out a card with the numbers created by the 'create_number' method.
        '''
        self.create_number()
        for self.el in self.number_list:
            self.row = 0
            while self.row < 9:
                upper_boarder = (self.row + 1) * 10
                if self.row == 8:
                    upper_boarder = 91
                if self.row * 10 <= self.el < upper_boarder:
                    self.counter = [[], [], []]
                    for j, line in enumerate(self.card):
                        for item in self.card[j]:
                            if item != '  ':
                                self.counter[j].append(item)
                    if len(self.counter[0]) >= len(self.counter[1]):
                        if len(self.counter[1]) >= len(self.counter[2]):
                            self.row_add_element(2)
                        else:
                            self.row_add_element(1)
                    else:
                        self.row_add_element(0)
                self.row += 1

    def row_add_element(self, card_row):
        '''
        The method adds an element into a card.
        :param card_row: the number of the list(card's row) where the element is being added.
        '''
        if self.card[card_row][self.row] == '  ':
            self.card[card_row][self.row] = self.el
        else:
            self.counter[card_row].append(0)
            self.row -= 1

    def draw_card(self):
        '''
        The method draws a card.
        '''
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
        self.quit_game = 0
        self.error_input = 0

    def start(self):
        '''
        The main method of the game.
        '''
        card1.fillout_card()
        card2.fillout_card()
        while self.quit_game == 0:
            self.rand_bag_num = random.randint(1, 90)
            if self.rand_bag_num in self.bag_num:
                continue
            else:
                self.bag_num.append(self.rand_bag_num)
                print(f'The number is {self.rand_bag_num}')
                card1.draw_card()
                card2.draw_card()
                self.error_input = 0
                while self.error_input == 0:
                    user_answer = input('Would you like to cross the number?(y/n)').strip()
                    self.computer_answer_check()
                    self.player_answer_check(user_answer)
            self.check_winner(self.card1)
            self.check_winner(self.card2)

    def computer_answer_check(self):
        '''
        The method checks the computer's answer.
        '''
        for line_index, line in enumerate(self.card2.card):
            for item_index, item in enumerate(line):
                if self.rand_bag_num == item:
                    self.card2.card[line_index][item_index] = '--'

    def player_answer_check(self, user_answer):
        '''
        The method checks the user's answer.
        :param user_answer: the exact answer that the user has given.
        '''
        for line_index, line in enumerate(self.card1.card):
            for item_index, item in enumerate(line):
                if self.rand_bag_num == item:
                    if user_answer == 'y':
                        self.card1.card[line_index][item_index] = '--'
                        print('The choice is done correctly.\n', 27 * '*', '\n')
                        self.error_input = 1
                        return
                    elif user_answer == 'n':
                        print('The choice is done incorrectly. You lost the game.')
                        self.error_input = 1
                        self.quit_game = 1
                        return
                    else:
                        print('Input is incorrect.')
        if user_answer == 'y':
            print('The choice is done incorrectly. You lost the game.')
            self.error_input = 1
            self.quit_game = 1
        elif user_answer == 'n':
            print('The choice is done correctly.\n', 27 * '*', '\n')
            self.error_input = 1
        else:
            print('Input is incorrect.')

    def check_winner(self, participant):
        '''
        The method check whether a user or a computer has won.
        :param participant: class instance.
        '''
        winner = 1
        for line in participant.card:
            for item in line:
                if str(item).isnumeric():
                    winner = 0
        if winner == 1:
            print(f'{participant.player} won!')
            self.quit_game = 1


card1 = LotoCard('-Player-')
card2 = LotoCard('Computer')
game = Game(card1, card2)
game.start()
