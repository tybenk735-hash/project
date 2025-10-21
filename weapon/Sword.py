from weapon import Weapon

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
        pass

    def use_melle_attack(self):
        

        return self.ph_dmg

    def get_info(self):
        msg = (f"""
{"МЕЧ:": <16}{self.name: >16}
{"Урон:": <16}{self.ph_dmg: >16}
{"Магический урон:": <16}{self.m_dmg: >16}
{"Скорость атаки:": <16}{self.cooldown: >16}
""")
        return msg

sw = Sword("Эскалибур", 100, 1, 1000, 200)
print(sw.get_info())
print(sw.use_melle_attack())
