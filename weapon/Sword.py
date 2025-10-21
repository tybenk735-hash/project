from Weapon import Weapon

class Sword(Weapon):
    def __init__(self, 
                name: str, 
                durability: int,
                cooldown: int,
                ph_dmg: int,
                m_dmg: int,
):
        super().__init__(name, durability, cooldown, ph_dmg, m_dmg)

    def calculate_dmg():
        Weapon.use_melle_attack

    def get_info(self):
        msg = (f"""
{"Урон:": >10}{self.ph_dmg: <}
""")
        print(msg)

