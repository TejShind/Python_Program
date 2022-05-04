
"""
@Author: Tejaswini Shinde
@Date: 2022-05-02 23:20
@Last Modified by: Tejaswini Shinde
@Last Modified time: No
@Title : Write program of Tik_Tak_Toe Game.

"""
import random

print("Hurry!Welcome to the TIK_TAC_TOE Game!")

"""This class is about tic tac toe game. Where this game will played between computer and human"""
class TicTacToe:

    def __init__(self):
        self.computer_option = None
        self.player_option = None
        self.board = [0] * 10
        self.turn_check = None
        self.game_board = [[' ', '|', ' ', '|', ' '], ['_', '+', '_', '+', '_'], [' ', '|', ' ', '|', ' '],
                           ['_', '+', '_', '+', '_'], [' ', '|', ' ', '|', ' ']]
        self.player_positions = {10}
        self.computer_positions = {10}

    @property
    def initialize(self):
        for i in range(len(self.board)):
            self.board[i] = " "

    @property
    def input_option(self):
        option = input("Enter the option X or O :")
        if option == "X":
            self.player_option = "X"
            self.computer_option = "O"
        else:
            self.player_option = "O"
            self.computer_option = "X"

        print(f"The player option : {self.player_option} & The computer option : {self.computer_option}")

    @property
    def show_board(self):

        for row in self.game_board:
            for grid in row:
                print(grid, end=" ")
            print()

    def check_free_space(self, position):
        if self.board[position] == " ":
            return 1
        return 0

    @property
    def toss(self):
        prediction = input("Predict head or tail :")
        predict_set = ["head", "tail"]
        index_generate = random.randint(0, 1)
        if prediction == predict_set[index_generate]:
            print(f" It's {prediction}. Player won the toss")
            self.turn_check = 0
        else:
            print(f"It's {predict_set[index_generate]}. Player lose the toss")
            self.turn_check = 1

    @property
    def start(self):
        if self.turn_check == 0:
            print("Player's Turn")
            response = int(input("Enter the number from 1 to 9 :"))
            result = self.check_free_space(response)
            if result == 0:
                print("Space is not free.Fill another index")
                return self.start
            else:
                self.place_position(response, self.player_option, self.player_positions)
                self.turn_check = 1

        else:
            print("Computer's Turn")
            response = random.randint(1, 9)
            result = self.check_free_space(response)
            if result == 0:
                print("Space is not free.Fill another index")
                return self.start
            else:
                self.place_position(response, self.computer_option, self.computer_positions)
                self.turn_check = 0

    def place_position(self, place, option, positions):
        if place == 1:
            self.board[place] = option
            self.game_board[0][0] = option
            positions.add(place)
        elif place == 2:
            self.board[place] = option
            self.game_board[0][2] = option
            positions.add(place)
        elif place == 3:
            self.board[place] = option
            self.game_board[0][4] = option
            positions.add(place)
        elif place == 4:
            self.board[place] = option
            self.game_board[2][0] = option
            positions.add(place)
        elif place == 5:
            self.board[place] = option
            self.game_board[2][2] = option
            positions.add(place)
        elif place == 6:
            self.board[place] = option
            self.game_board[2][4] = option
            positions.add(place)
        elif place == 7:
            self.board[place] = option
            self.game_board[4][0] = option
            positions.add(place)
        elif place == 8:
            self.board[place] = option
            self.game_board[4][2] = option
            positions.add(place)
        else:
            self.board[place] = option
            self.game_board[4][4] = option
            positions.add(place)

    @property
    def check_winner(self):
        matched_pairs_list = [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}, {1, 5, 9}, {3, 5, 7}]
        for pair in matched_pairs_list:
            if pair.intersection(self.player_positions) == pair:
                return 1
            elif pair.intersection(self.computer_positions) == pair:
                return 2
        return 0

if __name__ == "__main__":
    game = TicTacToe()
    game.initialize
    game.show_board
    game.input_option
    game.toss
    while True:
        game.start
        game.show_board
        result = game.check_winner
        if result == 1:
            print("Player won ")
            break
        elif result == 2:
            print("Computer won")
            break