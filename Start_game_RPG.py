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

#Ввод информации о персонаже
def input_data():
    global person
    try:
        person["type"] = input("Введите расу(Человек, Эльф или Дракон): ").lower()
        if not(person["type"].lower() == "человек" or person["type"].lower() == "эльф" or person["type"].lower() == "дракон"):
            print("Несуществующая раса, введите расу ещё раз")
            input_data()
    except:
        input_data()

#Определение характеристик персонажа
def finding_stats():
    global person
    rat = 100
    if (person['type'] == 'эльф' and int(person['age']) <= 79):
        person["health"] = rat*0.8
        person["m_dmg"] = rat*0.35
        person['intellect'] = 3
    elif (person['type'] == 'эльф' and int(person['age']) >= 80):
        person["health"] = rat*0.7
        person["m_dmg"] = rat*0.5
        person['intellect'] = 15
    elif   (person['type'] == 'человек' and int(person['age']) <= 79):
        person["health"] = rat
        person["f_dmg"] = rat*0.25
        person['intellect'] = 5
    elif   (person['type'] == 'человек' and int(person['age']) >= 80):
        person["health"] = rat*0.8
        person["f_dmg"] = rat*0.25
        person['intellect'] = 5
    elif   (person['type'] == 'дракон' and int(person['age']) <= 124):
        person["health"] = rat
        person["f_dmg"] = rat*0.6
        person['intellect'] = 1
    elif   (person['type'] == 'дракон' and int(person['age']) >= 125):
        person["health"] = rat*10
        person["f_dmg"] = rat*1.5
        person['intellect'] = 1
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
