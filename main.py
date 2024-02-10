"""Імпортуємо *UserDict(клас словників) з бібліотеки *collections
який буде батьківським для нашого *class AddressBook
   Імпортуємо *datetime з бібліотеки *datetime - для роботи з датою"""
from collections import UserDict
from datetime import datetime


class Field:
    """Клас є батьківським для всіх полів, у ньому реалізується логіка,
    загальна для всіх полів."""

    def __init__(self, value):
        if not self.is_valide(value):
            raise ValueError("Invalid value")
        self.__value = value

   
    
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, new_value):
        if self.is_valide(new_value):
            self.__value = new_value
        else:
            raise ValueError("Invalid value")
    
    def is_valide(self, _):
        """Метод перевіряє дані з конструктора *__init__(self, value)
        на валідність(чи вони відповідають умовам завдання).
        В батьківському *class Field, повертаємо всім аргументам *True.
        В субкласах для яких *class Field - буде батьківським - цей метод будемо модифікувати
        в залежності від вимог до даних субкаласу."""

        return True
    
    def __str__(self):
        return str(self.__value)


class Name(Field):
    """Клас --- обов'язкове поле з ім'ям."""


class Phone(Field):
    """Клас немає власного конструкора, наслідує поля і методи від *class Field"""

    def is_valide(self, value):
        return len(value) == 10 and value.isdigit()

    def __eq__(self, other):
        return isinstance(other, Phone) and self.value == other.value

class Birthday(Field):
    '''Класс - небоязкове поле дати народження'''


    def is_valid(self, value):
        try:
            datetime.strptime(value, '%Y-%m-%d')
            return True
        except ValueError:
            return False


class Record:
    """Клас відповідає за логіку додавання/видалення/редагування
    необов'язкових полів та зберігання обов'язкового поля Name."""

    def __init__(self, name, birthday=None):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(birthday) if birthday else None

    def add_phone(self, phone):
        """Метод додає телефон в поле рекорд class Record"""

        self.phone = Phone(phone)
        self.phones.append(self.phone)

    def remove_phone(self, del_phone: Phone):
        """Метод видаляє збережений телефон з поля рекорд class Record"""

        del_phone = Phone(del_phone)
        self.phones.remove(del_phone)

    def edit_phone(self, old_phone: Phone, new_phone: Phone):
        """Метод змінює збережений телефон з поля рекорд *class Record.
        Якщо такого телефона не має повертає згенерованну нами помилку *raise ValueError
        """
        old_phone = Phone(old_phone)
        new_phone = Phone(new_phone)
        record = False

        for i, _ in enumerate(self.phones):
            if self.phones[i] == old_phone:
                self.phones[i] = new_phone
                return self.phones[i]

        if not record:
            raise ValueError
        

    def find_phone(self, numbre_phone):
        """Мотод пошуку телефону в полі рекорд *class Record"""

        numbre_phone = Phone(numbre_phone)

        for i, _ in enumerate(self.phones):
            if self.phones[i] == numbre_phone:
                return self.phones[i]

        return None
    
    def days_to_birthday(self):
        '''Метод неприймає аргументів
        Повертає кількість днів до вказаної дати народження, якщо вона зазначенна '''
        
        if not self.birthday:
            return None
        
        today = datetime.now().date()
            
        birthday_data = datetime.strptime(self.birthday.value, "%d-%m-%Y")
        next_birthday_data = birthday_data.replace(year=today.year)
        if today > next_birthday_data:
                
            next_birthday_data = birthday_data.replace(year=today.year+1)
            return (next_birthday_data - today).days
      
  
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    """Субклас для батьтківського *UserDict,  де реалізовано логіку роботи з адресоною книжкою,
    Додавати записи, видаляти записи, шукати записи за іменем."""

    def add_record(self, record):
        """Метод додає запис(рекорд) в адресну книжку *class AddressBook"""

        self.data[record.name.value] = record

    def delete(self, name):
        """Метод видаляє запис(рекорд) в адресну книжку *class AddressBook"""

        for key_name in self.data.keys():
            return self.data.pop(key_name, None)
        
    def find(self, name):
        """Метод шукає запис(рекорд) за іменем в адресній книжці *class AddressBook"""
       
        return self.data.get(name, None)
    
    def iterator(self, display_records=10):
        '''Ітератор - виводить по 10 записів з нашої записної книжки'''
        records = list(self.data.keys())
       
        for i in range(0, len(records), display_records):
            yield [self.data[key] for key in records[i:i + display_records]]

    def __str__(self):
        return '\n'.join(str(r) for r in self.data.values())



