from tkinter import *
from tkinter import ttk
from tkinter import messagebox

win = Tk()
win.geometry("1920x1080")
win.title("Game of Life")
win.option_add("*Font","Arial 25")
win.configure(bg="white")

canvas = Canvas(win,width=1910, height=1200,bg ="black")
canvas.grid(row=2,column=0,columnspan=3)
W_SIZE=127
H_SIZE=58
CELL_SIZE=15

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
    def life(self,m,n):
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

    def compute(self):
        newlist=[[False for _ in range(W_SIZE)] for _ in range(H_SIZE)]
        for m in range(H_SIZE):
            for n in range(W_SIZE):
                newlist[m][n]=self.life(m,n)
        self.pointList = newlist

def draw_grid():
    for i in range(H_SIZE+1):#수평선
        canvas.create_line(0,i*CELL_SIZE,W_SIZE*CELL_SIZE,i*CELL_SIZE,fill="lightgray",tags="grid")
    for i in range(W_SIZE+1):#수직선
        canvas.create_line(i*CELL_SIZE,0,i*CELL_SIZE,H_SIZE*CELL_SIZE,fill="lightgray",tags="grid")
def draw_points():
    canvas.delete("dot")
    for r in range(H_SIZE):
        for c in range(W_SIZE):
            if points.pointList[r][c]:
                x0=c*CELL_SIZE+2
                y0=r*CELL_SIZE+2
                x1 = (c + 1) * CELL_SIZE - 2
                y1 = (r + 1) * CELL_SIZE - 2
                canvas.create_rectangle(x0, y0, x1, y1, fill="red", tags="dot")
running = False
delay = IntVar()
delay.set(200)
grid_visible=True
def toggle_grid():
    global grid_visible
    grid_visible = not grid_visible
    canvas.itemconfigure("grid",state="normal"if grid_visible else "hidden")
    gridBtn.config(text="Grid:ON"if grid_visible else "Grid:OFF")
gridBtn = Button(win, text="Grid:ON",command=toggle_grid)
gridBtn.grid(row=0,column=1)
def run():
    global running
    if running:
        points.compute()
        draw_points()
        win.after(delay.get(), run)

speed_scale = Scale(win, from_=50, to=1000,
                    orient=HORIZONTAL,
                    variable=delay,
                    label="간격(ms)",
                    length=400)
speed_scale.grid(row=1, column=2)

def toggle_run():
    global running
    running = not running
    runBtn.config(text="Pause" if running else "Run")
    if running:run()
runBtn=Button(win,text="Run")
runBtn.grid(row=0,column=2)
runBtn.config(command=lambda: toggle_run())

points= Points()
pointStr = StringVar()
textbox = ttk.Entry(win, width = 20,textvariable=pointStr)
textbox.configure()
textbox.grid(column=0,row=0)

addBtn=Button(win, text="Add")
addBtn.grid(row=1,column=0)
addBtn.config(command=lambda: points.add_list(string=pointStr.get()))
delBtn=Button(win,text="Del")
delBtn.grid(column=1,row=1)
delBtn.config(command=lambda: points.del_list(string=pointStr.get()))

draw_grid()
win.mainloop()