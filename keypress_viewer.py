import tkinter as tk

window_main = tk.Tk()
window_main.title("Keypress Viewer")
window_main.iconbitmap("favicon.ico")
window_main.geometry("500x500")

text_to_display = tk.StringVar(window_main)
display_label = tk.Label(window_main, textvariable=text_to_display, font="none 60 bold")
display_label.config(anchor="center")
display_label.pack(expand="yes")

def key(event):
    text_to_display.set(event.keysym)
    window_main.after(200, lambda : text_to_display.set(""))

window_main.bind("<Key>", key)
window_main.mainloop()