class Backpack:
    def __init__(self, durability, value):
        self.durability = durability
        self.value = value
        self.items = []
    
    def create_backpack(self):
        msg = f"""
Сумка создана
Прочность: {self.durability}
Вместимость: {self.value}
"""

    def item_in_backpack(self,item):
        self.items.append(item)
        print(f"Предмет {self.items} добавлен в сумку")

    def open_backpack(self):
        for i, item in enumerate(self.items):
            print(f"№{i}) {item}")

    def use_item(self):
        self.open_backpack()
        id_item = int(input("Введите номер предмета, который хотите испольковать: "))
        return self.items[id_item]
    
    
    