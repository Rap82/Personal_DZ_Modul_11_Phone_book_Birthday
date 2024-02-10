from main import  Record , AddressBook

     # Створення нової адресної книги
book = AddressBook()

    # Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

john_record.birthday="01-02-2024"

    # Додавання запису John до адресної книги
book.add_record(john_record)
print(john_record)

print(john_record.birthday)

    # Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

jane1_record = Record("Jane12")
jane1_record.add_phone("9876543210")
book.add_record(jane1_record)
jane2_record = Record("Jane78")
jane2_record.add_phone("9876543210")
book.add_record(jane2_record)

jane4_record = Record("Jane78uiii")
jane4_record.add_phone("9876543210")
book.add_record(jane4_record)

jane6_record = Record("Jane7898")
jane6_record.add_phone("9876543210")
book.add_record(jane6_record)


rew_record = Record("REW")
rew_record.add_phone("9876543234")
book.add_record(rew_record)

    # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

    # Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")


print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#     # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}:{found_phone}")  # Виведення: 5555555555

#     # Видалення запису Jane
book.delete("Jane")