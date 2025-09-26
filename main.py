person = {
    "name": "",
    "age": 0,
    "health": 0,
    "f_dmg": 0,
    "m_dmg": 0,
    "intellect": 0,
    "type": "",
    "rat": 100
}

person["name"] = input("Введите имя: ")
person["age"] = input("Введите возраст: ")

def input_data():
    global person
    try:
        person["type"] = input("Введите расу(Человек, Эльф или Дракон): ").lower()
        if not(person["type"].lower() == "человек" or person["type"].lower() == "эльф" or person["type"].lower() == "дракон"):
            print("Несуществующая раса, введите расу ещё раз")
            input_data()
    except:
        input_data()

def finding_stats():
    global person
    rat = 100
    if (person['type'] == 'эльф' and int(person['age']) <= 79):
        person["health"] = rat*0.8
        person["m_dmg"] = rat*0.35
        person['intellect'] = 3
    return person['health'], person['m_dmg'], person['intellect']


def u_info_out():
    msg = f"""
    {"Физический урон:":-<20}{person['f_dmg']:->20}
    {"Магический урон:":-<20}{person['m_dmg']:->20}
    {"Имя:":-<20}{person['name']:->20}
    {"Возраст:":-<20}{person['age']:->20}
    {"Здоровье:":-<20}{person['health']:->20}
    {"Интеллект:":-<20}{person['intellect']:->20}
    {"Раса:":-<20}{person['type']:->20}
    """
    return msg




input_data()
finding_stats()

print(u_info_out())
