import reflex as rx
import random

caracters = ['@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

class MainClass(rx.State):
    pwd: str = ""
    c: int = 0
    numberChecked:bool=True
    caracterChecked:bool=True

    @rx.event
    def password(self):
        amount = int(self.c) if str(self.c).isdigit() else 0
        randomLetters = [random.choice(letters) for i in range(amount)]
        randomSpecialCharacters = [random.choice(caracters) for i in range(3)]
        randomNumbers = [random.choice(numbers) for i in range(3)]
        matriz = randomLetters + randomSpecialCharacters + randomNumbers
        random.shuffle(matriz)
        self.pwd = "".join(matriz)

    @rx.event
    def getAmount(self, c: int):
        self.c = c

    def validateMaxNumber(self,c:int):
        if self.c <=12:
            self.c=c
        else:
            return 0

    def passwordWithCheckbox(self):
        if self.numberChecked is True and self.caracterChecked is True:
            return self.password()
        else:
            if self.numberChecked is True and self.caracterChecked is False:
                amount = int(self.c) if str(self.c).isdigit() else 0
                randomLetters = [random.choice(letters) for i in range(amount)]
                randomNumbers = [random.choice(numbers) for i in range(3)]
                matriz = randomLetters+ randomNumbers
                random.shuffle(matriz)
                self.pwd = "".join(matriz)
            else:
                if self.numberChecked is False and self.caracterChecked is True:
                    amount = int(self.c) if str(self.c).isdigit() else 0
                    randomLetters = [random.choice(letters) for i in range(amount)]
                    randomSpecialCharacters = [random.choice(caracters) for i in range(3)]
                    matriz = randomLetters+ randomSpecialCharacters
                    random.shuffle(matriz)
                    self.pwd = "".join(matriz)
                else:
                    if self.numberChecked is False and self.caracterChecked is False:
                        amount = int(self.c) if str(self.c).isdigit() else 0
                        randomLetters = [random.choice(letters) for i in range(amount)]
                        matriz = randomLetters
                        random.shuffle(matriz)
                        self.pwd = "".join(matriz)