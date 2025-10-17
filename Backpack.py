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

    def item_in_backpack(self,items):
        self.items.append(items)
        print(f"Предмет {self.items} добавлен в сумку")