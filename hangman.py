import requests 

class Hangman():
    def __init__(self):
        pass

    def start_menu(self):
        print("HANGMAN".center(30, '-'))
        start = input("Press ENTER to Start: ")
        while start != "":
            print("\n>>> INVALID INPUT <<<")
            start = input("Press ENTER to Start: ")
        self.attempts = 7
        self.game()

    def game(self):
        self.hide_word()
        while self.attempts != 0:
            print(f'\n{"  ".join(self.hidden_word)}')
            print(f"GUESSES LEFT: {self.attempts}")
            self.guess = input("Guess a letter: ")
            self.guess = self.guess.lower()
            while self.guess.isdigit() or len(self.guess) > 1 or self.guess == "":
                print("\n>>> INVALID INPUT <<<")
                print("  ".join(self.hidden_word))
                print(f"GUESSES LEFT: {self.attempts}")
                self.guess = input("Guess a letter: ")
                self.guess = self.guess.lower()
            self.check_guess()
            win = True
            for letter in self.word_list:
                if letter != "":
                    win = False
                    break
            if win:
                self.won()
            elif self.attempts == 0:
                self.lost()
        
    def get_word(self):
        url = 'https://random-word-api.vercel.app/api?words=1'
        response = requests.get(url)
        if response.ok:
            data = response.json()
            random_word = data[0]
            return random_word
        else:
            print(f"ERROR: {response.status_code}")

    def hide_word(self):
        self.word = self.get_word()
        self.hidden_word = ["_" for char in self.word]
        self.word_list = list(self.word)

    def check_guess(self):
        if self.guess not in self.word_list:
            self.attempts -= 1
            print("\n>>> INCORRECT <<<")
        else:
            for letter in self.word_list:
                if letter == self.guess:
                    index = self.word_list.index(self.guess)
                    self.hidden_word[index] = self.word_list[index]
                    self.word_list[index] = ""
                else:
                    continue

    def won(self):
        print(f'\n{"  ".join(self.hidden_word)}')
        print("\n!! YOU WON !!")
        print(f"WORD: {self.word}")
        print(f"ATTEMPTS LEFT: {self.attempts}")
        self.attempts = 0
        self.play_again()

    def lost(self):
        print(f'\n{"  ".join(self.hidden_word)}')
        print("\n!! YOU LOST !!")
        print(f"WORD: {self.word}")
        print(f"GUESSES LEFT: {self.attempts}")
        self.play_again()

    def play_again(self):
        p_again = input("\nPlay Again? (Y/N): ")
        p_again = p_again.upper()
        while p_again not in {'Y', 'N'}:
            print("\n>>> INVALID INPUT <<<")
            p_again = input("Play Again? (Y/N): ")
            p_again = p_again.upper()
        if p_again == 'Y':
            self.start_menu()
        else:
            self.quit()

    def quit(self):
        print("\nThank you for playing!")
        
        
obj = Hangman()
obj.start_menu()