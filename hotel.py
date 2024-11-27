from datetime import datetime
sana_string = "24-11-27"
sana1 = datetime.strptime("24.11.2024", "%d.%m.%Y")
sana2 = datetime.strptime("28.11.2024", "%d.%m.%Y")
kun_farqi = (sana2 - sana1).days

print(f"Ikkita sana orasidagi kun farqi: {kun_farqi} kun")

import lang.uz
import lang.ru
import lang.en

text = lang.uz

rooms = [
  {'id': 101, 'type': 'Lux', 'price': 200, 'book': [
    {'name': 'Ali', 'age': 18, 'start': '20.11.2024', 'finish': '20.11.2024'}
  ]},
  {'id': 102, 'type': 'Vip', 'price': 100, 'book': []},
  {'id': 103, 'type': 'Vip', 'price': 100, 'book': []},
  {'id': 104, 'type': 'Standard', 'price': 50, 'book': []},
  {'id': 105, 'type': 'Standart', 'price': 50, 'book': []},
]

def bosh(room):
    if len(room['book']) == 0:
        return True
    else:
        return False

def band(room):
    if len(room['book']) != 0:
        return True
    else:
        return False
    

def honalarniKorish(status):
    row = 'Bush xonalar \n'
    fun = bosh if status == 'bosh' else band
    filtered = filter(fun, rooms)
    for room in filtered:
        row += (f"{room['id']}-xona {room['type']} Xona Narxi {room['price']} dollar  \n")

    print(row)


def tariflarniKorish():
	command = int(input(text.tariflar))
	if command == 0:
		welcome()
	else: 
		print("Noto'g'ri qiymat")
		tariflarniKorish()


def tilTanlash():
	global text
	command = int(input(text.tillar))
	if command == 1:
		text = lang.uz
	elif command == 2:
		text = lang.ru
	elif command == 3:
		text = lang.en
	elif command == 0:
		pass
	else: 
		print("Noto'g'ri qiymat")
		tilTanlash()
	welcome()

rooms = [
    {'id': 101, 'type': 'Lux', 'price': 200, 'book': [
        {'name': 'Ali', 'age': 18, 'start': '20.11.2024', 'finish': '20.11.2024'}
    ]},
    {'id': 102, 'type': 'Vip', 'price': 100, 'book': []},
    {'id': 103, 'type': 'Vip', 'price': 100, 'book': []},
    {'id': 104, 'type': 'Standard', 'price': 50, 'book': []},
    {'id': 105, 'type': 'Standart', 'price': 50, 'book': []},
]

def bronQilish():
    name = input('Ваше имя: ')
    age = int(input('Введите ваш возраст: '))
    
    if age < 18:
        print("Ваш возраст еще мал!")
        return
		
    xona_raqam = int(input('Введите номер комнаты: '))

		# Boshlanish vaqtini kiritish
    startT = input('Время начала (дд.мм.гггг): ')
    start = datetime.strptime(startT, "%d.%m.%Y")

		# Tugash vaqtini kiritish
    finishT = input('Время окончания (дд.мм.гггг): ')
    finish = datetime.strptime(finishT, "%d.%m.%Y")


    xona_topildi = False
    
    for room in rooms:
        if xona_raqam == room['id']:
            xona_topildi = True
            if len(room['book']) != 0:
                print("Комната занята!")
                return
            room['book'].append({'name': name, 'age': age, 'start': start, 'finish': finish})  # Xonani bron qilish
            print("Комната забронирована!")
    
    if not xona_topildi:
      print("Комната не найдена")




def report():
	xonalarSoni = len(rooms)

	for xona in rooms:
		soni = len(xona['book'])


	print(f"""
Umumiy xonalr soni {xonalarSoni}
Mijozlar soni
Umumiy bron qilingan kunlar
Daromat	
	""") 


report()

def welcome():
	command = int(input(text.welcome))
	if command == 1: 
		tilTanlash()
	elif command == 2: 
		tariflarniKorish()
	elif command == 3: 
		honalarniKorish('bosh')
	elif command == 4: 
		honalarniKorish('band')
	elif command == 5: 
		bronQilish()
	elif command == 6: 
		tilTanlash()
	elif command == 7: 
		tilTanlash()
	elif command == 8: 
		tilTanlash()
	elif command == 0: 
		print("E'tiboringiz uchun rahmat")
	else: 
		print("Noto'g'ri qiymat")


while True:
	welcome()


