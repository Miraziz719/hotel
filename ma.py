from tkinter import *
from tkinter import messagebox
# from PIL import Image, ImageTk  
# Rasmni yuklash uchun

# Funksiyalar
def hisobla():
    try:
        kun = int(entry_kun.get())
        narx = int(entry_narx.get())
        jami = kun * narx
        label_jami.config(text=f"Jami to'lov: {jami} so'm")
    except ValueError:
        messagebox.showerror("Xato", "Iltimos, kiritilgan ma'lumotlar to'g'ri ekanligini tekshiring!")

def rezervatsiya():
    ism = entry_ism.get()
    xona = entry_xona.get()
    kun = entry_kun.get()
    if ism and xona and kun:
        messagebox.showinfo("Rezervatsiya", f"{ism} uchun xona {xona} ga {kun} kun davomida rezervatsiya qilindi!")
        # Muvaffaqiyatli xabar chiqsa, rezervatsiya qilinganligini ko'rsatuvchi rasmni almashtirish
        label_result_img.config(image=rez_img)
    else:
        messagebox.showerror("Xato", "Iltimos, barcha maydonlarni to'ldiring!")

# Oynani yaratish
window = Tk()
window.title("Mehmonxona Xizmati")
window.geometry("600x600")
window.configure(bg="#f0f8ff")  # Orqa fon rangini o'zgartirish (AliceBlue)

# # Rasmlar
# default_img = ImageTk.PhotoImage(Image.open("default.png").resize((200, 200)))  # Odatiy rasm
# rez_img = ImageTk.PhotoImage(Image.open("reserved.png").resize((200, 200)))  # Rezervatsiya qilingan rasm

# Mavzular
label_title = Label(window, text="Mehmonxona Xizmati", font=("Arial", 20, "bold"), bg="#4682b4", fg="white")
label_title.pack(pady=10, fill=X)

# Bo'lim foni
frame = Frame(window, bg="#e6f2ff", padx=10, pady=10)
frame.pack(pady=20, fill=BOTH, expand=True)

# Ism
label_ism = Label(frame, text="Mijoz ismi:", font=("Arial", 12), bg="#e6f2ff")
label_ism.grid(row=0, column=0, sticky=W, pady=5)
entry_ism = Entry(frame, font=("Arial", 12), width=30)
entry_ism.grid(row=0, column=1, pady=5)

# Xona raqami
label_xona = Label(frame, text="Xona raqami:", font=("Arial", 12), bg="#e6f2ff")
label_xona.grid(row=1, column=0, sticky=W, pady=5)
entry_xona = Entry(frame, font=("Arial", 12), width=30)
entry_xona.grid(row=1, column=1, pady=5)

# Kunlar soni
label_kun = Label(frame, text="Kunlar soni:", font=("Arial", 12), bg="#e6f2ff")
label_kun.grid(row=2, column=0, sticky=W, pady=5)
entry_kun = Entry(frame, font=("Arial", 12), width=30)
entry_kun.grid(row=2, column=1, pady=5)

# Kunlik narx
label_narx = Label(frame, text="Kunlik narx (so'm):", font=("Arial", 12), bg="#e6f2ff")
label_narx.grid(row=3, column=0, sticky=W, pady=5)
entry_narx = Entry(frame, font=("Arial", 12), width=30)
entry_narx.grid(row=3, column=1, pady=5)

# Tugmalar
btn_hisobla = Button(frame, text="To'lovni hisobla", command=hisobla, bg="#4682b4", fg="white", font=("Arial", 12), padx=10)
btn_hisobla.grid(row=4, column=0, pady=10, sticky=E)

btn_rezerv = Button(frame, text="Rezervatsiya qilish", command=rezervatsiya, bg="#4682b4", fg="white", font=("Arial", 12), padx=10)
btn_rezerv.grid(row=4, column=1, pady=10, sticky=W)

# Jami to'lovni ko'rsatish
label_jami = Label(window, text="Jami to'lov: 0 so'm", font=("Arial", 14, "bold"), bg="#f0f8ff", fg="#4682b4")
label_jami.pack(pady=10)

# Rasm bo'limi
# label_result_img = Label(window, image=default_img, bg="#f0f8ff")
# label_result_img.pack(pady=20)

# Oynani ishga tushirish
window.mainloop()