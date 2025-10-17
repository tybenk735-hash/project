from Backpack import Backpack

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
        
    #Функция выбора класса    
    def change_type(self):
        try:
            type = input("Выбери класс(Воин, Маг, Лучник) ").lower()
            if type == "воин" or type == "в":
                self.health = 1000
                self.ph_dmg = 175
                self.speed = 8
                return "воин"
            elif type == "маг" or type == "м":
                self.health = 600
                self.m_dmg = 550
                self.speed = 6
                return "маг"
            elif type == "лучник" or type == "л":
                self.health = 500
                self.ph_dmg = 305
                self.speed = 10
                return "лучник"
            raise
        except:
            print("Неверные данные, попробуйте снова")
            return self.change_type()
    
    def get_info(self):
        msg = f"""
{"Имя":-<20}{self.name:->20}
{"Возраст":-<20}{self.age:->20}
{"Класс":-<20}{self.type:->20}
{"Здоровье:":-<20}{self.health:->20}
{"Физический урон:":-<20}{self.ph_dmg:->20}
{"Магичемккий урон:":-<20}{self.m_dmg:->20}
{"Скорость":-<20}{self.speed:->20}
"""
        print(msg)
        