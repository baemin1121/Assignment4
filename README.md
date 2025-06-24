# Assignment4
오픈소스 SW와 파이썬 프로그래밍 4차 과제입니다.

---
## Conway's Game of Life
1. 설명
   > 라이프 게임(Game of Life) 또는 생명 게임은 영국의 수학자 존 호턴 콘웨이가 고안해낸 세포 자동자의 일종으로, 가장 널리 알려진 세포 자동자 가운데 하나이다. (위키백과)
   
2. 규칙
     2차원 배열에서 진행된다.
   |칸 구분|다음 세대에 살아 남기 위한 주위 살아 있는 세포의 개수 |
   |-------|:-------------:|
   |산 세포  | 2~3|
   |죽은 세포|3|


## 사용 방법
  window.py를 실행합니다.
  우상단 빈칸에 시작할 칸의 정보를 입력합니다. 입력 양식은 *"행 열 행 열 행 열 ..."*과 같습니다.
  
  적당한 크기의 정수를 짝수 개 입력해야 하며, 음수도 입력 가능합니다.
  
  입력 후에 Add를 눌러 세포를 생성하고 Run을 눌러 게임을 시작합니다. 버튼을 다시 눌러 게임을 일시정지한 채로 세포를 추가할 수도 있습니다.
  
  Scale바로 시간 간격(단위:ms)을 조절할 수 있습니다.
  
  예를 들어 
5 1 5 2 6 1 6 2 5 11 6 11 7 11 4 12 8 12 3 13 9 13 3 14 9 14 6 15 4 16 8 16 5 17 6 17 7 17
을 입력하고 Run을 누르면 재미있는 패턴을 볼 수 있습니다.

## 코드 설명
`class Pixel():`, `class Grid():` 출처:<https://github.com/Max-py54/Tkinter-grid>
`def rgbtohex(r,g,b):` 출처:<https://web.archive.org/web/20170430000206/http://www.psychocodes.in/rgb-to-hex-conversion-and-hex-to-rgb-conversion-in-python.html>
`class Points():`는 bool 배열 pointList로 세포들의 좌표를 가지고 있는 클래스입니다. `compute(self)`,`life(self,m,n)`를 통해 위에서 설명한 생명 게임의 규칙을 적용하기 위한 연산을 수행합니다. 어떤 좌표를 life에 넣으면 주변 8칸을 둘러보고 조건에 따라 True나 False를 반환합니다. compute는 모든 칸에 대해 life를 실행하고 그 결과를 종합하여 pointList에 덮어씁니다.
`griid`는 `Grid`객체, `points`는 `Points`객체 입니다.

```
def draw_points():
    griid.clear()
    for r in range(H_SIZE):
        for c in range(W_SIZE):
            if points.pointList[r][c]:
                griid.pixel(r,c,colour=randomcolor(),outline=randomcolor())

def add_points():
    points.add_list(entry_var.get())
    draw_points()

def step():
    points.compute()
    draw_points()

def run():
    global running
    if running:
        step()
        win.after(delay.get(), run)
```
`draw_points()`는 griid를 초기화하고 다시 griid에 세포를 표시합니다.
`add_points()`는 빈칸에 입력된 `entry_var`값을 가져와 `add_list` 메소드를 통해 적절한 좌표 쌍 형태로 바꾸어 `points.pointList`에 추가합니다.
`step()`과 `run()`은 단계적인 동작을 구현하는 코드입니다.
그 외의 코드는 tkinter를 이용한 GUI와 옵션에 관한 코드입니다.

## 개선할 점
클릭을 통해 세포를 생성하거나 제거하는 기능을 구현하면 좋을 것 같습니다. 확대/축소, 테마 변경 등의 기능을 넣으면 재미있을 것 같습니다.

