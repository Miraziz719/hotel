import colors

welcome = (f"""
{colors.CYAN}Добро пожаловать в отель "Python Killer!"{colors.RESET}
- Нажмите [1], чтобы выбрать язык  
- Нажмите [2], чтобы узнать о тарифах  
- Нажмите [3], чтобы забронировать номер  
- Нажмите [4], чтобы отменить или изменить бронирование  
- Нажмите [0], чтобы выйти  
{colors.RED}• Выход {colors.RESET}
""")

tariflar = (f"""
{colors.CYAN}Ознакомьтесь с описаниями отеля Python Killer! {colors.RESET}

• Стандартные номера  
   Кондиционер, холодильник, телевизор, кровать  

• VIP номера  
   Кондиционер, холодильник, телевизор, кровать  

• Люксовые номера  
   Кондиционер, холодильник, телевизор, кровать  

{colors.RED}• Нажмите [0], чтобы вернуться назад   {colors.RESET}
""")

tillar = (f"""
{colors.CYAN}Tilni tanlang  • Выбрать язык  • Select language {colors.RESET}
• O'zbek tilini tanlash uchun [1] ni bosing
• Для выбора русского языка нажмите цыфру [2]
• Press [3] to choose language as English

{colors.RED}• ORQAGA • ВЫХОД • EXIT [0] {colors.RESET}
""")