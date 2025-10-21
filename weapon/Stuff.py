from weapon import Weapon

class Stuff(Weapon):
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

    def use_range_attack():
        pass

    def get_info():
        msg = f"""
{"Меч:": <16}
"""