from Weapon import Weapon

class Sword(Weapon):
    def __init__(self, 
                 name: str, 
                 durability: int,
                 cooldown: int,
                 ph_dmg: int,
                 m_dmg: int):
        super().__init__(name, durability, cooldown)
        self.ph_dmg = ph_dmg
        self.m_dmg = m_dmg

    def calculate_dmg():
        pass

    def get_info():
        pass