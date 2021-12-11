import datetime as dt
import tkinter as tk
from tkinter import ttk, messagebox


def get_text():
    w1 = entry_1.get()  # 名称
    w2 = entry_2.get()  # 日付
    if w1 and w2.isdecimal():  # w1が空じゃない　w2が数字
        word_list = []

        today = dt.date.today()
        future = today + dt.timedelta(days=int(w2))
        word = f"{w1}({today:%Y/%m/%d}散布)"
        word_list.append(word)
        entry_1.delete(0, tk.END)

        word_2 = f"{future:%Y/%m/%d}迄"
        word_2.rjust(len(word))
        word_list.append(word_2)
        entry_2.delete(0, tk.END)

        print_word = "\n".join(word_list)
        label_sub = tk.Label(frame_3, text=print_word)
        label_sub.pack()

    elif not w1:
        messagebox.showerror("エラー", "名前を入力してください")
    elif w2.isnumeric():
        messagebox.showerror("エラー", "算用数字で入力してください")
    else:
        messagebox.showerror("エラー", "数字を入力してください")


root = tk.Tk()
root.title("目安日")
root.geometry("400x300")

label_top = tk.Label(text=f"今日は:{dt.date.today()}", width=200, font=("MSゴシック", 12, "bold"))
label_top.pack()

# 入力欄1段目
frame_1 = tk.Frame(root)
frame_1.pack()
label_1 = tk.Label(frame_1, text="名称：")
label_1.pack(side=tk.LEFT)
entry_1 = ttk.Entry(frame_1, width=35)
entry_1.pack()

# 入力欄2段目
frame_2 = tk.Frame(root)
frame_2.pack()
label_2 = tk.Label(frame_2, text="日数：")
label_2.pack(side=tk.LEFT)
entry_2 = ttk.Entry(frame_2)
entry_2.pack(side=tk.LEFT)
button_entry = ttk.Button(frame_2, text="保存")
button_entry["command"] = get_text
button_entry.pack()

# 表示欄
frame_3 = tk.Frame(root)
frame_3.pack()

# 閉じるボタン
exit_button = tk.Button()
exit_button["text"] = "閉じる"
exit_button["command"] = root.destroy
exit_button.pack(side="bottom")

root.mainloop()
