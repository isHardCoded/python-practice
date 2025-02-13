class Subscriber:
    def __init__(self, full_name, home_phone, work_phone, mobile_phone, additional_info):
        self.full_name = full_name
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.additional_info = additional_info

    def __str__(self):
        return (f"ФИО: {self.full_name}\n"
                f"Домашний телефон: {self.home_phone}\n"
                f"Рабочий телефон: {self.work_phone}\n"
                f"Мобильный телефон: {self.mobile_phone}\n"
                f"Дополнительная информация: {self.additional_info}")
    
class PhoneBook:
    def __init__(self):
        self.subscribers = []

    def add_sub(self, subscriber):
        self.subscribers.append(subscriber)

    def delete_sub(self, name_subscriber):
        for subscriber in self.subscribers:
            if subscriber.full_name == name_subscriber:
                self.subscribers.remove(subscriber)
                print(f"{name_subscriber} удален.")
                return
        print(f"{name_subscriber} не найден.")

    def find_sub(self, name_subscriber):
        for subscriber in self.subscribers:
            if subscriber.full_name == name_subscriber:
                print(name_subscriber)
                return
        print(f"{name_subscriber} не найден.")

    def display_subs(self):
        for sub in self.subscribers:
            print(sub)

phone_book = PhoneBook()

while True:
    print()
    print(f"1. Показать абонентов\n"
          f"2. Добавить абонента\n"
          f"3. Удалить абонента\n"
          f"4. Найти абонента\n")
    
    choice = int(input("Выберите действие (1-4): "))

    if choice == 1:
        phone_book.display_subs()

    elif choice == 2:
        full_name = input("Введите имя: ")
        home_phone = input("Домашний номер: ")
        work_phone = input("Рабочий номер: ")
        mobile_phone = input("Мобильный номер: ")
        additional_info = input("Доп. информация: ")

        sub = Subscriber(full_name, home_phone, work_phone, mobile_phone, additional_info)
        phone_book.add_sub(sub)

    elif choice == 3:
        name = input("Укажите имя для удаления: ")
        phone_book.delete_sub(name)

    elif choice == 4:
        name = input("Укажите имя для поиска: ")
        phone_book.find_sub(name)