import tkinter as tk
window = tk.Tk()
window.geometry("500x500")
label = tk.Label(window,text="wdym.ajii",
                 font=("italic",100, "bold"),
                 fg = "purple", borderwidth=45)
label.pack(fill="both", expand=True)
def btnfun():
    #window.destroy()
    print("Am gud")
btn = tk.Button(window, text= "Change",
                font=("Arial", 50, "italic"),
                fg="yellow", borderwidth=45,
                command= btnfun)
btn.pack()
window.mainloop()
