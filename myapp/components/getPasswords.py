import reflex as rx
import random

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
caracters = ['@', '#', '$', '%', '^', '&', '*', '(', ')']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
uppercaseLetters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K','L', 'M', 'N', 'O', 'P', 'R', 'S', 'T', 'U', 'V','W','X','Y','Z']

class MainClass(rx.State):
    pwd: str = ""
    c: int = 0
    numberChecked:bool
    caracterChecked:bool
    lettersChecked:bool
    UppercaseLetterChecked:bool

    @rx.event
    def getAmount(self, c: int):
        self.c = c

    def passwordWithCheckbox(self):
        getRandom = []
        result = " "
        amount = int(self.c) if str(self.c).isdigit() else 0

        if amount>12:
            self.pwd="No puede ser mayor a 12 digitos"
        else:
            if amount>4 and self.numberChecked is False and self.caracterChecked is False and self.lettersChecked is False and self.UppercaseLetterChecked is False:
                #amount<4 or amount==0
                self.pwd="Debe marcar almenos una opción"
            else:
                if amount=="" or amount==0:
                #amount>4 and self.numberChecked is False and self.caracterChecked is False and self.lettersChecked is False and self.UppercaseLetterChecked is False
                    self.pwd="Debe ingresar una cantidad y marcar almenos una opción"
                else:
                    if self.numberChecked and self.caracterChecked and self.lettersChecked is False and self.UppercaseLetterChecked is False:
                        getRandom.extend([random.choice(numbers),random.choice(caracters)])
                        for i in range(amount-len(getRandom)):
                            if getRandom in numbers:
                                getRandom.append(random.choice(numbers))
                            if getRandom not in caracters:
                                getRandom.append(random.choice(caracters))
                                random.shuffle(getRandom)
                                result="".join(getRandom)
                            self.pwd=result
                    else:
                        if self.numberChecked and self.lettersChecked and self.caracterChecked is False and self.UppercaseLetterChecked is False:
                            getRandom.extend([random.choice(numbers),random.choice(letters)])
                            for i in range(amount-len(getRandom)):
                                if getRandom in numbers:
                                    getRandom.append(random.choice(numbers))
                                if getRandom not in letters:
                                    getRandom.append(random.choice(letters))
                                    random.shuffle(getRandom)
                                    result="".join(getRandom)
                                self.pwd=result
                        else:
                            if self.numberChecked and self.lettersChecked and self.UppercaseLetterChecked and self.caracterChecked is False:
                                getRandom.extend([random.choice(numbers),random.choice(letters),random.choice(uppercaseLetters)])
                                for i in range(amount-len(getRandom)):
                                    result=random.choice(getRandom)
                                    if getRandom in numbers:
                                        getRandom.append(random.choice(numbers))
                                    else:
                                        if getRandom not in letters:
                                            getRandom.append(random.choice(letters))
                                        else:
                                            if getRandom not in uppercaseLetters:
                                                getRandom.append(random.choice(uppercaseLetters))
                                    random.shuffle(getRandom)
                                self.pwd=getRandom
                            else:
                                if self.numberChecked and self.caracterChecked and self.lettersChecked is False and self.UppercaseLetterChecked:
                                    getRandom.extend([random.choice(numbers),random.choice(caracters),random.choice(uppercaseLetters)])
                                    for i in range(amount-len(getRandom)):
                                        result=random.choice(getRandom)
                                        if getRandom in numbers:
                                            getRandom.append(random.choice(numbers))
                                        else:
                                            if getRandom not in caracters:
                                                getRandom.append(random.choice(caracters))
                                            else:
                                                if getRandom not in uppercaseLetters:
                                                    getRandom.append(random.choice(uppercaseLetters))
                                        random.shuffle(getRandom)
                                    self.pwd=getRandom
                                else:
                                    if self.numberChecked and self.UppercaseLetterChecked and self.caracterChecked is False and self.lettersChecked is False:
                                        getRandom.extend([random.choice(numbers), random.choice(uppercaseLetters)])
                                        for i in range(amount-len(getRandom)):
                                            if getRandom in numbers:
                                                getRandom.append(random.choice(numbers))
                                            if getRandom not in uppercaseLetters:
                                                getRandom.append(random.choice(uppercaseLetters))
                                                random.shuffle(getRandom)
                                                result="".join(getRandom)
                                            self.pwd=result
                                    else:
                                        if self.numberChecked and self.caracterChecked and self.lettersChecked and self.UppercaseLetterChecked is False:
                                            getRandom.extend([random.choice(numbers), random.choice(caracters), random.choice(letters)])
                                            for i in range(amount-len(getRandom)):
                                                if getRandom in numbers:
                                                    getRandom.append(random.choice(numbers))
                                                if getRandom in caracters:
                                                    getRandom.append(random.choice(caracters))        
                                                if getRandom not in letters:
                                                    getRandom.append(random.choice(letters))
                                                    random.shuffle(getRandom)
                                                    result="".join(getRandom)
                                                self.pwd=result
                                        else:
                                            if self.numberChecked and self.caracterChecked and self.lettersChecked and self.UppercaseLetterChecked:
                                                getRandom.extend([random.choice(numbers), random.choice(caracters), random.choice(letters),random.choice(uppercaseLetters)])
                                                for i in range(amount-len(getRandom)):
                                                    result=random.choice(getRandom)
                                                    if getRandom in numbers:
                                                        getRandom.append(random.choice(numbers))
                                                    else:
                                                        if getRandom not in caracters:
                                                            getRandom.append(random.choice(caracters))
                                                        else:
                                                            if getRandom not in letters:
                                                                getRandom.append(random.choice(letters))
                                                            else:
                                                                if getRandom not in uppercaseLetters:
                                                                    getRandom.append(random.choice(uppercaseLetters))
                                                    random.shuffle(getRandom)
                                                self.pwd=getRandom
                                            else:
                                                if self.numberChecked:
                                                    getRandom.append(random.choice(random.choice(numbers)))
                                                    for i in range(amount-len(getRandom)):
                                                        result=random.choice(getRandom)
                                                        if getRandom not in numbers:
                                                            getRandom.append(random.choice(numbers))
                                                        random.shuffle(getRandom)
                                                    self.pwd=getRandom
                                                else:
                                                    if self.caracterChecked and self.lettersChecked and self.UppercaseLetterChecked is False:
                                                        getRandom.extend([random.choice(caracters),random.choice(letters)])
                                                        for i in range(amount-len(getRandom)):
                                                            result=random.choice(getRandom)
                                                            if getRandom in caracters:
                                                                getRandom.append(random.choice(caracters))
                                                            if getRandom not in letters:
                                                                getRandom.append(random.choice(letters))
                                                            random.shuffle(getRandom)
                                                        self.pwd=getRandom
                                                    else:
                                                        if self.caracterChecked and self.UppercaseLetterChecked and self.lettersChecked is False:
                                                            getRandom.extend([random.choice(caracters),random.choice(uppercaseLetters)])
                                                            for i in range(amount-len(getRandom)):
                                                                result=random.choice(getRandom)
                                                                if getRandom in caracters:
                                                                    getRandom.append(random.choice(caracters))
                                                                if getRandom not in uppercaseLetters:
                                                                    getRandom.append(random.choice(uppercaseLetters))
                                                                random.shuffle(getRandom)
                                                            self.pwd=getRandom
                                                        else:
                                                            if self.caracterChecked and self.lettersChecked and self.UppercaseLetterChecked and self.numberChecked is False:
                                                                getRandom.extend([random.choice(caracters),random.choice(letters),random.choice(uppercaseLetters)])
                                                                for i in range(amount-len(getRandom)):
                                                                    result=random.choice(getRandom)
                                                                    if getRandom in caracters:
                                                                        getRandom.append(random.choice(caracters))
                                                                    else:   
                                                                        if getRandom not in letters:
                                                                            getRandom.append(random.choice(letters))
                                                                        else:
                                                                            if getRandom not in uppercaseLetters:
                                                                                getRandom.append(random.choice(uppercaseLetters))
                                                                    random.shuffle(getRandom)
                                                                self.pwd=getRandom
                                                            else:
                                                                if self.caracterChecked:
                                                                    getRandom.append(random.choice(random.choice(caracters)))
                                                                    for i in range(amount-len(getRandom)):
                                                                        result=random.choice(getRandom)
                                                                        if getRandom not in numbers:
                                                                            getRandom.append(random.choice(caracters))
                                                                        random.shuffle(getRandom)
                                                                    self.pwd=getRandom
                                                                else:
                                                                    if self.lettersChecked and self.UppercaseLetterChecked:
                                                                        getRandom.extend([random.choice(letters),random.choice(uppercaseLetters)])
                                                                        for i in range(amount-len(getRandom)):
                                                                            result=random.choice(getRandom)
                                                                            if getRandom not in letters:
                                                                                getRandom.append(random.choice(letters))
                                                                            if getRandom in uppercaseLetters:
                                                                                getRandom.append(random.choice(uppercaseLetters))
                                                                            random.shuffle(getRandom)
                                                                        self.pwd=getRandom
                                                                    else:
                                                                        if self.UppercaseLetterChecked:
                                                                            getRandom.append([random.choice(uppercaseLetters)])
                                                                            for i in range(amount-len(getRandom)):
                                                                                result=random.choice(getRandom)
                                                                                if getRandom not in uppercaseLetters:
                                                                                    getRandom.append(random.choice(uppercaseLetters))
                                                                                random.shuffle(getRandom)
                                                                            self.pwd=getRandom
                                                                        else:
                                                                            if self.lettersChecked:
                                                                                getRandom.append(random.choice(letters))
                                                                                for i in range(amount-len(getRandom)):
                                                                                    result=random.choice(getRandom)
                                                                                    if getRandom not in letters:
                                                                                        getRandom.append(random.choice(letters))
                                                                                    random.shuffle(getRandom)
                                                                                self.pwd=getRandom
                                                                            else:
                                                                                if self.numberChecked is False and self.caracterChecked is False and self.lettersChecked is False and self.UppercaseLetterChecked is False:
                                                                                    self.pwd="Debe marcar una opción"
                                                                                       