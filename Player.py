import Backpack

class Player:
    def __init__(self, name):
        self.name = name
        self.age = 0
        self.health = 0
        self.m_dmg = 0
        self.ph_dmg = 0
        self.speed = 0
        self.backpack = Backpack.Backpack(100, 50)
        self.backpack.item_in_backpack(Меч)
        self.backpack.item_in_backpack(Еда)
        self.backpack.item_in_backpack(Лук)
        self.backpack.item_in_backpack(Руда)
        self.type = self.change_type()
        
        
    def change_type(self):
        try:
            type = input("Выбери класс(Воин, Маг, Лучник) ").lower()
            if type == "воин" or type == "в":
                self.health = 1000
                self.ph_dmg = 275
                self.speed = 10
                return "воин"
        except:
            print("Неверные данные, попробуйте снова")
            return self.change_type()