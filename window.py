import tkinter as tk
from tkinter import *
import random as r
def rgbtohex(r,g,b):
    return f'#{r:02x}{g:02x}{b:02x}'
"""출처:https://web.archive.org/web/20170430000206/http://www.psychocodes.in/rgb-to-hex-conversion-and-hex-to-rgb-conversion-in-python.html"""
def randomcolor():
    return rgbtohex(r.randint(1,255),r.randint(1,255),r.randint(1,255))


win = tk.Tk() #윈도우
win.geometry("1920x1080")
win.title("Game of Life")
win.option_add("*Font","Arial 25")
win.configure(bg="white")

W_SIZE=127
H_SIZE=58

class Pixel():
    def __init__(self, canvas, line: int, column: int, width_line: int, width_column: int, colour: str = "black",
                 outline: str = "black"):
        self.canvas = canvas
        self.line = line
        self.column = column
        self.width_line = width_line
        self.width_column = width_column
        self.colour = colour
        self.outline = outline
        self.create() #픽셀 클래스: 자동으로 찍힘
    def create(self): #점 찍기
        x1 = self.column * self.width_column
        y1 = self.line * self.width_line
        x2 = self.column * self.width_column + self.width_column
        y2 = self.line * self.width_line + self.width_line
        self.pixel = self.canvas.create_rectangle(x1, y1, x2, y2, fill=self.colour, outline=self.outline)
    def delete(self): #지우기
        self.canvas.delete(self.pixel)

class Grid():
    """Grid(window, lines:int, columns:int, width:int, height:int, colour:str="white")
Creates a grid."""
    def __init__(self, window, lines: int, columns: int, width: int, height: int, colour: str = "white"):
        self.lines = lines
        self.columns = columns
        self.width = width
        self.width_line = width // columns
        self.height = height
        self.width_column = height // lines
        self.colour = colour
        self.canvas = tk.Canvas(window, height=self.height, width=self.width, bg=self.colour)
        self.canvas.grid(row=2,column=0,columnspan=4)
        self.pixels = []
    def pixel(self, line: int, column: int, colour: str = "black", outline: str = ""):
        """Grid.pixel(line:int, column:int, colour:str="black", outline:str="")
Changes a specific pixel's colour."""
        if outline == "":
            outline = colour #외곽선 default
        if self.pixels != []:
            for i, px in enumerate(self.pixels): #픽셀 리스트에서 꺼내서
                if px.line == line and px.column == column:
                    px.delete() #겹치면 지우고
                    self.pixels.pop(i)
                    break
            if colour != self.colour: # 색 다름
                self.pixels.append(
                    Pixel(self.canvas, line, column, self.width_line, self.width_column, colour, outline))
        else: #픽셀 리스트에 픽셀 존재하면
            if colour != self.colour:
                self.pixels.append(
                    Pixel(self.canvas, line, column, self.width_line, self.width_column, colour, outline))
    def clear(self): #픽셀들 지우기
        """Clears the entire grid."""
        if self.pixels != []:
            for px in self.pixels:
                px.delete()
            self.pixels = []
"""Pixel() Grid() 출처:https://github.com/Max-py54/Tkinter-grid  (수정해서 사용함) """
class Points:
    def __init__(self):
        self.pointList= [[False for _ in range(W_SIZE)]for _ in range(H_SIZE)]
        self.dr,self.dc=[0,1,1,1,0,-1,-1,-1],[1,1,0,-1,-1,-1,0,1]
    def add_list(self, string):
        try:
            ls = list(map(int,string.split()))
            if len(ls) %2 !=0:
                messagebox.showerror("Error","짝수 개 숫자를 입력하세요.")
            while ls:
                c = ls.pop() + 53
                r = ls.pop() + 26
                if 0<=r<H_SIZE and 0<=c<W_SIZE:
                    self.pointList[r][c]=True
        except ValueError:
                messagebox.showerror("Error","숫자만 입력하세요.")
    def del_list(self, string):
        try:
            ls = list(map(int, string.split()))
            if len(ls) %2 !=0:
                messagebox.showerror("Error","짝수 개 숫자를 입력하세요.")
            while ls:
                c = ls.pop() + 53
                r = ls.pop() + 26
                self.pointList[r][c]=False
        except ValueError:
                messagebox.showerror("Error","숫자만 입력하세요.")
    def life(self,m,n): #규칙 적용
        count,mylife=0,self.pointList[m][n]
        for i in range(8):
            nm,nn=m+self.dr[i],n+self.dc[i]
            if 0 <= nm < H_SIZE and 0 <= nn < W_SIZE:
                if self.pointList[nm][nn]:
                    count+=1
        if mylife:
            if 2<=count<=3: return True
            return False
        else:
            if count ==3: return True
            return False

    def compute(self): #덮어씌우기
        self.pointList = [[self.life(m, n) for n in range(W_SIZE)] for m in range(H_SIZE)]

running = False #옵션
delay = tk.IntVar()
delay.set(200)
grid_visible=True

griid = Grid(win, H_SIZE,W_SIZE, 1910, 800, "black")
points=Points()

def draw_points():
    griid.clear()
    for r in range(H_SIZE):
        for c in range(W_SIZE):
            if points.pointList[r][c]:
                griid.pixel(r,c,colour=randomcolor(),outline=randomcolor()) #점 찍기

def add_points():
    points.add_list(entry_var.get())
    draw_points()

def step():
    points.compute()
    draw_points() #

def run():
    global running
    if running:
        step()
        win.after(delay.get(), run)

speed_scale = tk.Scale(win, from_=50, to=1000,orient=HORIZONTAL,variable=delay,label="간격(ms)", length=400)
speed_scale.grid(row=1,column=2)

runBtn=tk.Button(win, text="Run")
runBtn.grid(row=1,column=2)
def toggle_run():
    global running
    running = not running
    runBtn.config(text="Pause" if running else "Run")
    if running:run()
runBtn.config(command=toggle_run)

entry_var=tk.StringVar()
entry=tk.Entry(win,textvariable=entry_var,font=("Arial",14),width=50).grid(row=0,column=2,columnspan=2)

tk.Button(win, text="Add", command=add_points).grid(row=1, column=0)

win.mainloop()
