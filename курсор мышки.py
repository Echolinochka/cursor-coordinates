import tkinter as tk
import pyautogui

def update_coordinates():
    x, y = pyautogui.position()  # Получаем текущие координаты курсора
    label.config(text=f"Координаты курсора: X={x}, Y={y}")
    root.after(100, update_coordinates)  # Обновляем каждые 100 мс

root = tk.Tk()
root.title("Координаты курсора")

label = tk.Label(root, font=("Arial", 16))
label.pack(pady=20)

update_coordinates()  # Запускаем обновление координат

root.mainloop()