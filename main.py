import tkinter as tk


# def createWindow():
#     window = tk.Tk()
#     window.title("視窗抬頭")
#     btn = tk.Button(window,text="請按我",padx=20,pady=20,font=('arial',16))
#     btn.pack(padx=50,pady=50)
#     window.mainloop()


class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('這是我的視窗')
        
#        btn = tk.Button(self,text="請按我",padx=20,pady=20,font=('arial',16),command=self.userClick)
#        btn.pack(padx=50,pady=50)
        
        tk.Button(self,text="請按我",padx=20,pady=20,font=('arial',16),command=self.userClick).pack(padx=50,pady=50)

    def userClick(self):
        print('User按下按鈕')

def main():
    # createWindow()
    window1 = Window()
    window1.mainloop()

if __name__ == "__main__":
    main()
