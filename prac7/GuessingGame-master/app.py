"""Keep Guessing! - The Kivy Game"""

from kivy.app import App
from kivy.lang import Builder

import random


def validate_guess(min_num, max_num):
    """Validate the numbers required for guessing"""
    try:
        min_num = int(min_num)
    except ValueError:
        # print("Value error in min")
        min_num = 1
    try:
        max_num = int(max_num)
    except ValueError:
        # print("Value error in max")
        max_num = 10
    if min_num >= max_num:
        max_num = min_num + 10
    return min_num, max_num


# def get_rand(min_num, max_num):
#     """Get a random number"""
#     rand_num = random.randint(min_num, max_num)
#     return rand_num


class GuessingGame(App):
    def build(self):
        self.title = "Guessing Game 0.0.1"
        self.root = Builder.load_file('gui.kv')
        self.root.size = (300, 500)
        self.handle_menu(1)
        self.handle_min_max(1, 10)
        return self.root

    def handle_menu(self, which):
        """Handle menu style on click"""
        if which == 0:
            self.root.ids.settings_game.background_color = (0, 0, 0, 1)
            self.root.ids.game_game.background_color = (0, 0, 1, 1)
            self.root.ids.about_game.background_color = (0, 0.6, 0, 1)
        elif which == 1:
            self.root.ids.game_game.background_color = (0, 0, 0, 1)
            self.root.ids.settings_game.background_color = (0.5, 0.5, 0.5, 1)
            self.root.ids.about_game.background_color = (0, 0.6, 0, 1)
        elif which == 2:
            self.root.ids.about_game.background_color = (0, 0, 0, 1)
            self.root.ids.settings_game.background_color = (0.5, 0.5, 0.5, 1)
            self.root.ids.game_game.background_color = (0, 0, 1, 1)

    def handle_valid_num(self, num_text):
        """Handle if minimum and maximum are not valid numbers"""
        if num_text != '':
            try:
                num = int(num_text)
            except ValueError:
                self.root.ids.enter_valid_num.text = "Invalid. Enter a valid number!"
                self.root.ids.enter_valid_num.color = 1, 0, 0, 1
            else:
                self.root.ids.enter_valid_num.color = 1, 0, 0, 1
                if num < 1:
                    self.root.ids.enter_valid_num.text = 'Minimum must be greater than or equal to 1.'
                else:
                    self.root.ids.enter_valid_num.text = ''
        else:
            self.root.ids.enter_valid_num.text = ''

    def handle_min_max(self, min_num, max_num):
        """Display min and max on kivy game screen"""
        min_num, max_num = validate_guess(min_num, max_num)
        self.root.ids.min_max.text = f"Numbers set for guess game   \n          Min={min_num}       Max={max_num}\n\n" \
                                     f"(can be changed in settings)"

    def guess_counter(self, guess_text, guess):
        """Count and display number of guesses on kivy"""
        count = 0
        try:
            guess = int(guess)
        except ValueError:
            pass
        else:
            if guess < 1:
                return
            if guess_text == '':
                count = count + 1
            else:
                guess_text = guess_text.split('= ')
                count = int(guess_text[1]) + 1
            self.root.ids.guess_count.text = f"Number of Guesses = {count}"
            if guess < 1:
                self.root.ids.guess_count.text = ''

    def empty_count(self):
        """Empty the label which give number of guesses"""
        self.root.ids.guess_count.text = ''
        self.root.ids.guess_info.text = ''
        self.root.ids.found_it.text = ''

    def handle_guess(self, count, guess, min_num, max_num, guess_answer):
        """Handle the guess thing- main part of the game"""
        min_num, max_num = validate_guess(min_num, max_num)
        if count != '':
            game_answer = int(guess_answer)
        else:
            game_answer = random.randint(min_num, max_num)
            self.root.ids.guess_answer.text = str(game_answer)
        print(game_answer, 'is game answer. Guess tried is', guess)
        try:
            guess = int(guess)
        except ValueError:
            # write on kivy invalid guess
            self.root.ids.guess_info.text = 'Invalid guess. Guess must be a number.'
        else:
            if guess < 1:
                self.root.ids.guess_info.text = 'Guess must be greater than or equal to 1.'
            elif guess > game_answer:
                self.root.ids.guess_info.text = 'Lower'
            elif guess < game_answer:
                self.root.ids.guess_info.text = 'Higher'
            else:
                self.root.ids.guess_info.text = 'Game over'
                self.root.ids.found_it.text = f"You found the answer! {game_answer} is the answer!"

    def handle_up_down(self, value, up_down):
        """handle when up or down is clicked in kivy app"""
        try:
            result = int(value) + up_down
            # self.root.ids.guess.text = str(result)
        except ValueError:
            value = 0
            result = int(value) + up_down
        if result < 1:
            result = 1
        self.root.ids.guess.text = str(result)

    def handle_new_game(self):
        """Handle new game"""
        self.root.clear_widgets()
        self.stop()
        GuessingGame().run()

    def handle_exit(self):
        """Handle exit game option"""
        self.root.ids.found_it.text = 'Bye!'
        GuessingGame().stop()


# create and start the App running
GuessingGame().run()

# Solution given

# from kivy.app import App
# from kivy.lang import Builder
#
# from Game import Game
#
#
# class ErrorOutsideLimit(Exception):
#     def __init__(self, value):
#         self.value = value
#
#     def __str__(self):
#         return repr(self.value)
#
#
# class GuessingGame(App):
#     def __init__(self):
#         super(GuessingGame, self).__init__()
#         self.game = Game()
#
#     def build(self):
#         self.title = "Guessing Game 0.0.1"
#         self.root = Builder.load_file('gui.kv')
#         self.root.size = (300, 500)
#         print(type(self.root.ids))
#         return self.root
#
#     def handle_new_game(self):
#         self.game = Game()
#
#     def handle_guess(self):
#         user_guess = self.root.ids.guess_input.text
#         try:
#             user_guess = int(user_guess)
#             if 0 <= user_guess <= 10:
#                 self.root.ids.game_info_text.text = "{}".format(self.game.guess(user_guess))
#                 self.root.ids.game_guess_number.text = "Guess Number = {}".format(self.game.add_move())
#             else:
#                 raise ErrorOutsideLimit("stoopid")
#
#         except (ValueError, TypeError, ErrorOutsideLimit):
#             self.root.ids.game_info_text.text = "please enter a number between 1 and 10"
#             print("please enter a number between 1 and 10")
#
#     def handle_menu(self, current_menu):
#         normal = [1, 1, 1, 1]
#         hilight = [0, 0, 1, 1]
#
#         menu_context_list = ['settings_screen', 'about_screen', 'game_screen']
#
#         for key in self.root.ids:
#             if key in menu_context_list:
#                 if key == current_menu:
#                     self.root.ids[key].background_color = hilight
#                 else:
#                     self.root.ids[key].background_color = normal
#
#
# # create and start the App running
# GuessingGame().run()
