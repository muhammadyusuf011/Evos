from tkinter import Tk, Label, Frame, LabelFrame, Button, Spinbox
from PIL import ImageTk

window = Tk()
window.geometry("1000x1000")
window.configure(bg="#279240")

frame = Frame(window)
frame.grid(padx=80, pady=80)

label_frame = LabelFrame(frame, bg="#279240")
label_frame.grid()

# YOZUV ================================================
e_label = Label(window, text="Evos Fast Food",
                fg="white", bg="#279240",
                font=("Verdana", 40))
e_label.place(x=280, y=10)

# BURGER =================================================
burger_photo = ImageTk.PhotoImage(file="burger.png")
burger_label = Label(label_frame, image=burger_photo)
burger_label.grid(row=1, column=0)

burger_label = Label(label_frame, text="Burger",
                     font=("Verdana", 20),
                     fg="white", bg="#279240")
burger_label.grid(row=2, column=0)

burger_label2 = Label(label_frame, text="25,000 so'm",
                      font=("Verdana", 20),
                      fg="white", bg="#279240")
burger_label2.grid(row=3, column=0)

burger_spinbox = Spinbox(label_frame, from_=1, to=100)
burger_spinbox.grid(row=4, column=0)
# LAVASH ==================================================
lavash_photo = ImageTk.PhotoImage(file="lavash.png")
lavsh_label = Label(label_frame, image=lavash_photo)
lavsh_label.grid(row=1, column=1)

lavsh_label = Label(label_frame, text="Lavash",
                    font=("Verdana", 20),
                    fg="white", bg="#279240")
lavsh_label.grid(row=2, column=1)

lavsh_label2 = Label(label_frame, text="28,000 so'm",
                     font=("Verdana", 20),
                     fg="white", bg="#279240")
lavsh_label2.grid(row=3, column=1)

lavash_spinbox = Spinbox(label_frame, from_=1, to=100)
lavash_spinbox.grid(row=4, column=1)
# Shaurma ===================================================

shaurma_photo = ImageTk.PhotoImage(file="shaurma.png")
shaurma_label = Label(label_frame, image=shaurma_photo)
shaurma_label.grid(row=1, column=2)

shaurma_label = Label(label_frame, text="Shaurma",
                      font=("Verdana", 20),
                      fg="white", bg="#279240")
shaurma_label.grid(row=2, column=2)

shaurma_label2 = Label(label_frame, text="25,000 so'm",
                       font=("Verdana", 20),
                       fg="white", bg="#279240")
shaurma_label2.grid(row=3, column=2)

shaurma_spinbox = Spinbox(label_frame, from_=1, to=100)
shaurma_spinbox.grid(row=4, column=2)
# HOT DOG ===============================================
Hot_dog_photo = ImageTk.PhotoImage(file="hot dog.png")
Hot_dog_label = Label(label_frame, image=Hot_dog_photo)
Hot_dog_label.grid(row=1, column=3)

Hot_dog_label = Label(label_frame, text="Hot dog",
                      font=("Verdana", 20),
                      fg="white", bg="#279240")
Hot_dog_label.grid(row=2, column=3)

Hot_dog_label2 = Label(label_frame, text="15,000 so'm",
                       font=("Verdana", 20),
                       fg="white", bg="#279240")
Hot_dog_label2.grid(row=3, column=3)

hotdog_spinbox = Spinbox(label_frame, from_=1, to=100)
hotdog_spinbox.grid(row=4, column=3)
# FRIES====================================================
fries_photo = ImageTk.PhotoImage(file="fries.png")
fries_label = Label(label_frame, image=fries_photo)
fries_label.grid(row=5, column=0)

fries_label = Label(label_frame, text="Fries",
                    font=("Verdana", 20),
                    fg="white", bg="#279240")
fries_label.grid(row=6, column=0)

fries_label2 = Label(label_frame, text="14,000 so'm",
                     font=("Verdana", 20),
                     fg="white", bg="#279240")
fries_label2.grid(row=7, column=0)

fries_spinbox = Spinbox(label_frame, from_=1, to=100)
fries_spinbox.grid(row=8, column=0)
# SNACKS ================================================
snacks_photo = ImageTk.PhotoImage(file="snacks.png")
snacks_label = Label(label_frame, image=snacks_photo)
snacks_label.grid(row=5, column=1)

snacks_label = Label(label_frame, text="Snacks",
                     font=("Verdana", 20),
                     fg="white", bg="#279240")
snacks_label.grid(row=6, column=1)

snacks_label2 = Label(label_frame, text="9,000 so'm",
                      font=("Verdana", 20),
                      fg="white", bg="#279240")
snacks_label2.grid(row=7, column=1)

snack_spinbox = Spinbox(label_frame, from_=1, to=100)
snack_spinbox.grid(row=8, column=1)
# HOT DOG ===============================================
combo_photo = ImageTk.PhotoImage(file="combo.png")
combo_label = Label(label_frame, image=combo_photo)
combo_label.grid(row=5, column=2)

combo_label = Label(label_frame, text="Combo",
                    font=("Verdana", 20),
                    fg="white", bg="#279240")
combo_label.grid(row=6, column=2)

combo_label2 = Label(label_frame, text="30,000 so'm",
                     font=("Verdana", 20),
                     fg="white", bg="#279240")
combo_label2.grid(row=7, column=2)

combo_spinbox = Spinbox(label_frame, from_=1, to=100)
combo_spinbox.grid(row=8, column=2)
# COFFEE ===========================================
coffee_photo = ImageTk.PhotoImage(file="coffee.png")
coffee_label = Label(label_frame, image=coffee_photo)
coffee_label.grid(row=5, column=3)

coffee_label = Label(label_frame, text="Coffee",
                     font=("Verdana", 20),
                     fg="white", bg="#279240")
coffee_label.grid(row=6, column=3)

coffee_label2 = Label(label_frame, text="12,000 so'm",
                      font=("Verdana", 20),
                      fg="white", bg="#279240")
coffee_label2.grid(row=7, column=3)

coffee_spinbox = Spinbox(label_frame, from_=1, to=100)
coffee_spinbox.grid(row=8, column=3)


# KNOPKA=================================================
def button_count():
    burger_total = int(burger_spinbox.get()) * 25_000
    lavash_total = int(lavash_spinbox.get()) * 28_000
    shaurma_total = int(shaurma_spinbox.get()) * 25_000
    hot_dog_total = int(hotdog_spinbox.get()) * 15_000
    fries_total = int(fries_spinbox.get()) * 14_000
    snack_total = int(snack_spinbox.get()) * 9_000
    combo_total = int(combo_spinbox.get()) * 30_000
    coffee_total = int(coffee_spinbox.get()) * 12_000
    total_bills = sum([burger_total, lavash_total, shaurma_total, hot_dog_total,
                       fries_total, snack_total, combo_total, coffee_total])
    bills = Label(text=f"Sizning hisobingiz {total_bills} so'm bop'ldi",
                  bg="#279340", fg="white", font=("Arial", 20, "bold"))
    bills.place(x=140, y=685)


buyur_button = Button(window, text="Buyurtma berish",
                      font=("Verdana", 25),
                      fg="#279240", bg="white", command=button_count)
buyur_button.place(x=310, y=680)

# =====================================================

for widget in label_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

window.mainloop()
