class Weapon:
    def __init__(self, name: str, durability, cooldown, ph_dmg, m_dmg: int):
        self.name = name
        self.durability = durability
        self.cooldown = cooldown
        self.ph_dmg = ph_dmg
        self.m_dmg = m_dmg
    def use_range_attack(self):
        pass

    def use_melle_attack(self):
        pass

    def get_info():
        pass