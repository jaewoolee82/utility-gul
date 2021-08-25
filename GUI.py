from tkinter import *
import tkinter.messagebox as msgbox
import webbrowser
from datetime import datetime
import psutil
import platform
import requests
import os


root = Tk()
root.title("유틸")
root.iconbitmap("app.ico")
root.geometry("420x170")
root['background']='#856ff8'
bot_id = "869029507019968512" # 디스코드 봇 아이디 (Koreanbots에 등록돼있는 경우만)

class Menus(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Github", command=Github)
        menu.add_cascade(label="Information", menu=fileMenu)


def get_size(byte, suf="B"):
    GB = 1024
    for names in ["", "K", "M", "G", "T", "P"]:
        if byte < GB:
            return f"{byte:.2f}{names}{suf}"
        byte /= GB

def check_status(status):
    if status == "offline":
        return "오프라인"
    elif status == "online":
        return "온라인"
    elif status == "dnd":
        return "다른 용무중"
    elif status == "idle":
        return "자리 비움"
    elif status == "streaming":
        return "방송중"
    else:
        return status


def error():
    confirm = msgbox.askokcancel("경고", "계속하시겠습니까?")

    if confirm:
        for i in range(1000):
            msgbox.showerror("도배", f"오류 도배 ({i}/1000)")

def computer():
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    uname = platform.uname()
    svmem = psutil.virtual_memory()
    msgbox.showinfo(
        "컴퓨터 정보", 
        f"시스템: {platform.platform()}\nCPU: {uname.processor}\n전체 코어: {psutil.cpu_count(logical=True)}\nCPU 이용률: {psutil.cpu_percent()}%\n전체 메모리: {get_size(svmem.total)}\n메모리 이용률: {psutil.virtual_memory().percent}%")
        
def restart():
    confirm = msgbox.askokcancel("PC 재시작", "PC를 재시작하겠습니까?")
    if confirm: 
        os.system('shutdown -t 0 -r -f')

def check_server():
    try:
        result = requests.get(f'https://koreanbots.dev/api/v2/bots/{bot_id}')
        data = result.json()
        servers = data['data']['servers']
        votes = data['data']['votes']
        id = data['data']['id']
        status = data['data']['status']
        name = data['data']['name']
        status = check_status(status)
        msgbox.showinfo(
            "디스코드 봇 정보",
            f"봇 이름: {name}\n봇 아이디: {id}\n서버 수: {servers}\n하트 수: {votes}\n상태 (Status): {status}")
    except:
        msgbox.showerror("실패", "정보 확인 실패.")
    
def Github():
    webbrowser.open('https://discord.gg/sSH5KnT9zv')


button1 = Button(root, command=error,text="오류 도배", bg="#54FA9B")
button1.place(x=0, y=0)

button2 = Button(root, command=computer,text="컴퓨터 정보", bg="#54FA9B")
button2.place(x=62, y=0)

button2 = Button(root, command=restart,text="PC 재시작", bg="#54FA9B")
button2.place(x=136, y=0)

button3 = Button(root, command=check_server,text="디스코드 봇 정보", bg="#00FFFF")
button3.place(x=0, y=26)


app = Menus(root)
root.mainloop()