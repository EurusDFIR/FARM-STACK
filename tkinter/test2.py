import tkinter as tk
from tkinter import messagebox


class App(tk.Tk):
    def __init__(self, screenName = None, baseName = None, className = "Tk", useTk = True, sync = False, use = None):
        super().__init__(screenName, baseName, className, useTk, sync, use)

        self.title("Mahiru")
        self.geometry("400x200")

        #1.
        self.label = tk.Label(self,text="Vui long nhap ten cua ban:", font=("Arial",12))
        self.label.pack(pady = 10)

        #2. Tao o entry de nhap
        self.name_entry = tk.Entry(self,width=30, font=("Arial",12))
        self.name_entry.pack(pady=5)


        #3 Tao nut de xac nhan 
        self.submit_button = tk.Button(self, text="Chao",command=self.greet)
        self.submit_button.pack(pady=5)

    def greet(self):
        user_name = self.name_entry.get()

        if user_name:
            messagebox.showinfo("loi chao", f"xin chao {user_name}")
        else:
            messagebox.showwarning("Thieu thong tin", "ban chua nhap ten!")





if __name__ == "__main__":
    app = App()
    app.mainloop()