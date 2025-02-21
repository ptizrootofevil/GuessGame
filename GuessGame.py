import colorama as col
import random
import sys

class GuessGame:
    def __init__(self) -> None:
        self.word = random.choice(['chair', 'weave', 'eagle', 'angle', 'snack', 'guard', 'tired', 'sweat', 'crime', \
                    'witch', 'debut', 'jelly', 'flesh', 'stamp', 'liver', 'skate'])
        
        self.letters = {}
        for i in self.word:
            self.letters.setdefault(i, 0)
            self.letters[i] += 1

    def guess_word(self, guess: str) -> bool:
        letters = self.letters.copy()
        sys.stdout.write("\033[F")  # Move cursor up one line
        sys.stdout.write("\033[K")  # Clear the line
        for i in range(len(guess)):
            if self.word[i] == guess[i]:
                print(col.Fore.GREEN + guess[i], end='')
                letters[guess[i]] -= 1
            elif guess[i] in letters.keys() and letters[guess[i]] > 0:
                print(col.Fore.YELLOW + guess[i], end='')
                letters[guess[i]] -= 1
            else:
                print(col.Fore.WHITE + guess[i], end='')
        if self.word == guess:
            print(col.Fore.GREEN + '\nCongratulation! You`ve won!' + col.Fore.WHITE)
            return True
        print(col.Fore.WHITE)
        return False

        
def main():
    a = GuessGame()

    print('Welcome to a game of guess \nGuess an english word with 5 letters')
    print('Green - right letter in right place \nYellow - right letter in wrong place \nWhite - wrong letter')

    tmp = input('Please insert a word with 5 letters\n')

    for i in range(5):
        while len(tmp) != 5:
            tmp = input('Please insert a word with 5 letters\n')
        if a.guess_word(tmp):
            break
        elif i != 4:
            tmp = input()
    else:
        print(col.Fore.WHITE + 'The attempts are over \nYou can run programm again to try again')

if __name__ == '__main__':
    main()
