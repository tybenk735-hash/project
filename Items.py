item_shablon = []
    {"type_class": "sword",
    "damage": [
        {
            "dmg_type": "m_dmg",
            "value":0
        }
    {
        "dmg_type": "ph_dmg",
        "value": 0
    }
    ]
    }
]

class Item:
    def __init__(self, name, durability: int, properties: dict):
        self.name = name
        self.durability = durability
        self.properties = properties

    def use(self):
