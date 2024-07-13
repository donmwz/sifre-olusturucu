import tkinter as tk
import random

class PasswordGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Yüksek Güvenlikli Şifre Oluşturucu")
        self.root.geometry("350x150+570+320")
        self.root.resizable(False, False)

        self.entry = tk.Entry(self.root, width=50)
        self.entry.pack(pady=30)

        self.btn = tk.Button(self.root, text="Şifre Oluştur", command=self.sifre, width=50, height=2)
        self.btn.pack(pady=10)

    def sifre(self):
        sayi = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        harf = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        harf_upper = [letter.upper() for letter in harf]
        sembol = [".", ",", "!", "*", "?", "/", "-"]

        char_list = [sayi, harf, harf_upper, sembol]
        password = ""
        for _ in range(5):
            for char_set in char_list:
                password += str(random.choice(char_set))

        self.entry.delete(0, tk.END)
        self.entry.insert(0, password)

    def run(self):
        self.root.mainloop()

        self.window.mainloop()
