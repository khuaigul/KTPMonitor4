from . import main_DB_modul
def people_add(info):
# 	pupil = New_pupil(info["name"], info["surname"], info["patronymic"], info["school"], "10", info["cf"], info["date"])
# 	add_new_pupil(pupil)
    return
#
def people_write_one(info):
    #pupils = get_all_pupils()
    write_people = {}
    # write_people["nickname"] = info
    write_people = {"nickname": "abcd", "surname": "Иванов", "name": "Иван", "secondname": "Иванович",
                    "div": "A",
           "datebirth": "12.05.2005", "school": "Школа № 99", "form": 10}
    # for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
    #     if info == cf:
    # 		write_people["surname"] = surname
    # 		write_people["name" ] = name
    # 		write_people["secondname" ] = patronymic
    # 		write_people["div" ] = div_name
    return write_people

def people_write_div():
# 	pupils = get_all_pupils()
    write_people = {}
    write_people = {"students": [
    {"nickname": "abcd", "surname": "Иванов", "name": "Иван", "secondname": "Иванович", "div": "не выбрано"},
    {"nickname": "qwer", "surname": "Петров", "name": "Пётр", "secondname": "Петрович", "div": "C"},
    {"nickname": "wertyui", "surname": "Смирнов", "name": "Валерий", "secondname": "Михайлович", "div": "B"},
    {"nickname": "aaaanbvc", "surname": "Иванова", "name": "Мария", "secondname": "Ивановна", "div": "A"},
    {"nickname": "elele", "surname": "Крылова", "name": "Анна", "secondname": "Александровна", "div": "не выбрано"}]}

# 	name_people = []
# 	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
# 		info_people = {}
# 	    info_people["nickname" ] = cf
# 		info_people["surname"] = surname
# 		info_people["name" ] = name
# 		info_people["secondname" ] = patronymic
# 		info_people["div" ] = div_name
# 		name_people.append(info_people)
# 	write_people["students"] = name_people
    return write_people

def people_write_div_onle(info):
# 	pupils = get_all_pupils()
    write_people = {}
    write_people = {"students": [
    {"nickname": "abcd", "surname": "Иванов", "name": "Иван", "secondname": "Иванович"},
    {"nickname": "qwer", "surname": "Петров", "name": "Пётр", "secondname": "Петрович"},
    {"nickname": "wertyui", "surname": "Смирнов", "name": "Валерий", "secondname": "Михайлович"},
    {"nickname": "aaaanbvc", "surname": "Иванова", "name": "Мария", "secondname": "Ивановна"},
    {"nickname": "elele", "surname": "Крылова", "name": "Анна", "secondname": "Александровна"}]}

# 	name_people = []
# 	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
# 		if div_name==info:
    # 		info_people = {}
    # 	    info_people["nickname" ] = cf
    # 		info_people["surname"] = surname
    # 		info_people["name" ] = name
    # 		info_people["secondname" ] = patronymic
    # 		info_people["div" ] = div_name
    # 		name_people.append(info_people)
# 	write_people["students"] = name_people
    return write_people
