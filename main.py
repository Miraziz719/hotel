import json
from datetime import datetime

# Fayl nomi
DATA_FILE = "hotel_data.json"

# Xonalar va mijozlar ma'lumotlari
rooms = {}
customers = []


def save_data():
    """Ma'lumotlarni faylga yozish"""
    data = {"rooms": rooms, "customers": customers}
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4, default=str)
    print("Ma'lumotlar saqlandi.")


def load_data():
    """Fayldan ma'lumotlarni yuklash"""
    global rooms, customers
    try:
        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            rooms = data["rooms"]
            customers = data["customers"]

            # Stringni datetime ga aylantirish
            for room_data in rooms.values():
                for booking in room_data["bookings"]:
                    booking["start_date"] = datetime.fromisoformat(booking["start_date"])
                    booking["end_date"] = datetime.fromisoformat(booking["end_date"])
            print("Ma'lumotlar yuklandi.")
    except FileNotFoundError:
        print("Ma'lumotlar fayli topilmadi, yangi boshlanmoqda.")
        initialize_rooms()  # Xonalar lug'atini dastlabki qiymat bilan to'ldirish


def initialize_rooms():
    """Dastlabki xonalar ro'yxatini yaratish"""
    global rooms
    rooms = {
        101: {"type": "Oddiy xona", "price": 50, "bookings": []},
        102: {"type": "Yuqori darajadagi xona", "price": 100, "bookings": []},
        103: {"type": "Oilaviy xona", "price": 150, "bookings": []},
        201: {"type": "Luks xona", "price": 200, "bookings": []},
    }
    print("Dastlabki xonalar ro'yxati yaratildi.")


def check_rooms_exist():
    """Xonalar mavjudligini tekshirish"""
    if not rooms:
        print("Hozirda mehmonxonada xonalar mavjud emas.")
        return False
    return True


def show_rooms(filter_by=None):
    """Xonalar ro'yxatini filtrlash"""
    if not check_rooms_exist():
        return

    print("\nMehmonxona xonalari:")
    for room_number, details in rooms.items():
        if filter_by == "bo'sh" and details["bookings"]:
            continue
        if filter_by == "band" and not details["bookings"]:
            continue

        print(f"Xona {room_number}: {details['type']} | Narxi: ${details['price']}")
        if details["bookings"]:
            print("  Bandlik:")
            for booking in details["bookings"]:
                print(f"    {booking['guest']} ({booking['start_date']} - {booking['end_date']})")
    print()


def check_availability(room_number, start_date, end_date):
    """Ko'rsatilgan sanalarda xona bandligini tekshirish"""
    for booking in rooms[room_number]["bookings"]:
        if (start_date <= booking["end_date"] and end_date >= booking["start_date"]):
            return False
    return True


def book_room():
    """Xona bron qilish"""
    if not check_rooms_exist():
        return

    try:
        room_number = int(input("Bron qilishni istagan xonaning raqamini kiriting: "))
        if room_number not in rooms:
            print("Bunday xona mavjud emas. Iltimos, to'g'ri xona raqamini kiriting.")
            return

        guest_name = input("Mijozning ismini kiriting: ")
        start_date = datetime.strptime(input("Boshlanish sanasini kiriting (yyyy-mm-dd): "), "%Y-%m-%d")
        end_date = datetime.strptime(input("Tugash sanasini kiriting (yyyy-mm-dd): "), "%Y-%m-%d")

        if end_date <= start_date:
            print("Tugash sanasi boshlanish sanasidan keyin bo'lishi kerak.")
            return

        if check_availability(room_number, start_date, end_date):
            rooms[room_number]["bookings"].append({
                "guest": guest_name,
                "start_date": start_date,
                "end_date": end_date,
            })
            print(f"Xona {room_number} {start_date.date()} - {end_date.date()} sanalarida muvaffaqiyatli bron qilindi!")
        else:
            print("Uzr, bu xona ko'rsatilgan sanalarda band.")
    except ValueError:
        print("Ma'lumotlarni to'g'ri kiriting.")


def main_menu():
    """Asosiy menyu"""
    load_data()
    while True:
        print("\n--- Mehmonxona boshqaruv dasturi ---")
        print("1. Xonalarni ko'rish")
        print("2. Xona bron qilish")
        print("3. Ma'lumotlarni saqlash")
        print("4. Dasturdan chiqish")

        choice = input("Tanlovingizni kiriting: ")
        if choice == "1":
            show_rooms()
        elif choice == "2":
            book_room()
        elif choice == "3":
            save_data()
        elif choice == "4":
            save_data()
            print("Dasturdan chiqildi. E'tiboringiz uchun rahmat!")
            break
        else:
            print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")


# Dastur ishga tushiriladi
main_menu()
