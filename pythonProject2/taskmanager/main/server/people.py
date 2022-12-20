from datetime import datetime
# from main_DB_modul import *
from . add_contest import add_contest
from . add_new_div import add_new_div
from . add_new_pupil import add_new_pupil
from . change_pupil_div import change_pupil_div
from . delete_div import delete_div
from . get_all_contests import get_all_contests
from . get_all_divs import get_all_divs
from . get_all_pupils import get_all_pupils

class New_div:
	def __init__(self, name, year):
		self.name = name
		self.year = year

class New_pupil:
	def __init__(self, surname, name, patronymic, school, grade, nick_CF, birthday):
		self.surname = surname
		self.name = name
		self.patronymic = patronymic

		self.school = school
		self.grade = grade
		self.nick_CF = nick_CF
		self.birthday = birthday

class pupil_div:
	def __init__(self, pupil_id, div_id):
		self.pupil_id = pupil_id
		self.div_id = div_id

class contest:
	def __init__(self, name, link, div_id, tasks, pupils_tasks):
		self.name = name
		self.link = link
		self.div_id = div_id
		self.tasks = tasks
		self.pupils_tasks = pupils_tasks

class task:
	def __init__(self, letter, name):
		self.letter = letter
		self.name = name

class pupil_task:
	def __init__(self, pupil_CF, task_letter, cnt_try, result):
		self.pupil_CF = pupil_CF
		self.task_letter = task_letter
		self.cnt_try = cnt_try
		self.result = result


def people_add(info):
	print(info.POST["name"])
	pupil = New_pupil(info.POST["name"], info.POST["surname"], info.POST["secondname"], info.POST["school"], "10", info.POST["nickname"], info.POST["datebirth"])
	add_new_pupil.add_new_pupil(pupil)
    # return;

def people_write_one(info):
    pupils = get_all_pupils()
    write_people = {}
    write_people["nickname"] = info
    write_people = {"nickname": "abcd", "surname": "Иванов", "name": "Иван", "secondname": "Иванович",
                    "div": "A",
           "datebirth": "12.05.2005", "school": "Школа № 99", "form": 10}
    for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
        if info == cf:
            write_people["surname"] = surname
            write_people["name" ] = name
            write_people["secondname" ] = patronymic
            write_people["div" ] = div_name
    return write_people

def people_write_div():
	pupils = get_all_pupils.get_all_pupils()
	write_people = {}
	write_people = {"students": [
    {"nickname": "abcd", "surname": "Иванов", "name": "Иван", "secondname": "Иванович", "div": "не выбрано"},
    {"nickname": "qwer", "surname": "Петров", "name": "Пётр", "secondname": "Петрович", "div": "C"},
    {"nickname": "wertyui", "surname": "Смирнов", "name": "Валерий", "secondname": "Михайлович", "div": "B"},
    {"nickname": "aaaanbvc", "surname": "Иванова", "name": "Мария", "secondname": "Ивановна", "div": "A"},
    {"nickname": "elele", "surname": "Крылова", "name": "Анна", "secondname": "Александровна", "div": "не выбрано"}]}

	# name_people = []
	# for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
	# 	info_people = {}
	# 	info_people["nickname" ] = cf
	# 	info_people["surname"] = surname
	# 	info_people["name" ] = name
	# 	info_people["secondname" ] = patronymic
	# 	info_people["div" ] = div_name
	# 	name_people.append(info_people)
	# write_people["students"] = name_people
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
