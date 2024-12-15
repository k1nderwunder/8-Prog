import random
import string

class PalindromeFinder:
    def __init__(self):
        self.text = ""
        self.palindromes = []
        self.algorithm_executed = False

    def main(self):
        while True:
            print("Меню:")
            print("1. Ввод исходных данных")
            print("2. Выполнение алгоритма")
            print("3. Вывод результата")
            print("4. Завершение работы программы")
            choice = input("Выберите пункт меню: ")

            if choice == '1':
                self.text = self.input_data()
                self.palindromes = []
                self.algorithm_executed = False
            elif choice == '2':
                if self.text:
                    self.palindromes = self.find_palindromes(self.text)
                    self.algorithm_executed = True
                else:
                    print("Сначала введите данные.")
            elif choice == '3':
                if self.algorithm_executed:
                    if self.palindromes:
                        self.print_palindromes(self.palindromes)
                    else:
                        print("Палиндромы не найдены.")
                else:
                    print("Сначала выполните алгоритм.")
            elif choice == '4':
                self.exit_program()
            else:
                print("Неверный выбор. Попробуйте снова.")

    def input_data(self):
        print("Выберите способ ввода данных:")
        print("1. Ввести данные вручную")
        print("2. Сгенерировать данные случайным образом")
        choice = input("Выберите пункт меню: ")

        if choice == '1':
            text = input("Введите текст: ")
        elif choice == '2':
            text = self.generate_random_text()
        else:
            print("Неверный выбор. Попробуйте снова.")
            return self.input_data()

        return text

    def generate_random_text(self):
        words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 7))) for _ in range(20)]
        return ' '.join(words)

    def find_palindromes(self, text):
        words = ''.join(char if char.isalnum() else ' ' for char in text).split()
        palindromes = [word for word in words if word == word[::-1]]
        return palindromes

    def print_palindromes(self, palindromes):
        print("Найденные палиндромы:")
        for palindrome in palindromes:
            print(palindrome)

    def exit_program(self):
        print("Программа завершена.")
        exit()

if __name__ == "__main__":
    finder = PalindromeFinder()
    finder.main()