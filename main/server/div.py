from datetime import datetime
# from main_DB_modul import *
from . add_new_div import add_new_div
class New_div:
	def __init__(self, name, year):
		self.name = name
		self.year = year


def add_div(info):
	current_date = datetime.today()
	div = New_div(info, current_date)
	add_new_div.add_new_div(div)

def remove_div(info):
# 	divs = get_all_divs()
	id_dalete = None
# 	for [name, _id] in divs:
# 		if name == info:
# 			id_dalete = _id
	if id_dalete == None:
		return
# 	delete_div(id_dalete)
#
def change_people_div(info):
# 	divs = get_all_divs()
# 	dive_id = None
# 	for [name, _id] in divs:
# 		if name == info['div']:
# 			dive_id = _id
#
# 	people_id = None
# 	pupils = get_all_pupils()
# 	for [surname, name, patronymic, cf, div_name, pupil_id, div_id] in pupils:
# 		print(surname, name, patronymic, cf, div_name, pupil_id, div_id)
# 		if info['name'] == name && info['surname'] == surname && info['patronymic'] == patronymic :
# 			people_id = pupil_id
#
# 	ch = pupil_div(people_id, dive_id)
# 	change_pupil_div(ch)
	return
#
def write_div():
# 	divs = get_all_divs()
	write_div = {}
	div_name =  ["A", "B", "C", "не выбрано"]
# 	for [name, _id] in divs:
# 		div_name.append(name)
# 	div_name.append("не выбрано")
	write_div["divisions"] = div_name
	return write_div
