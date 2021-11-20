import datetime as dt
import tkinter as tk


def future_day(y, m, d, a):  # a日後の日付
    return dt.date(y, m, d) + dt.timedelta(days=a)  # 出力:year-month-day


class Application(tk.Frame):
    def __init__(self, root):
        super().__init__(root, width=380, height=280, borderwidth=1, relief="groove")
        self.pack()
        self.pack_propagate(0)
        self.root = root
        self.create_widgets()

    def create_widgets(self):
        message = tk.Message(self, text=f"今日は　{dt.date.today()}", width=200, font=("MSゴシック", 15, "bold"))
        message.pack()

        exit_button = tk.Button(self)
        exit_button["text"] = "閉じる"
        exit_button["command"] = self.root.destroy
        exit_button.pack(side="bottom")


root = tk.Tk()
root.title("田んぼの目安日")
root.geometry("400x300")
app = Application(root=root)
app.mainloop()
