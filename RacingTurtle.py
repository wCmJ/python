from turtle import *
from random import randint
speed(30)
penup()
goto(-140,140)
for step in range(15):
	write(step,align='center')
	right(90)	
	forward(10)
	pendown()
	for n in range(9):
		forward(10)
		penup()
		forward(10)
		pendown()
	penup()
	backward(190)
	left(90)
	forward(20)
ada = Turtle()
ada.color('red')
ada.shape('turtle')
ada.penup()
ada.goto(-160,120)
ada.pendown()

for turn in range(10):
	ada.right(36)

bob = Turtle()
bob.color('blue')
bob.shape('turtle')
bob.penup()
bob.goto(-160,90)
bob.pendown()

for turn in range(10):
	bob.right(36)
ctc = Turtle()
ctc.color('purple')
ctc.shape('turtle')
ctc.penup()
ctc.goto(-160,60)
ctc.pendown()

for turn in range(10):
	ctc.right(36)
dld = Turtle()
dld.color('magenta')
dld.shape('turtle')
dld.penup()
dld.goto(-160,30)
dld.pendown()

for turn in range(10):
	dld.right(36)



suma,sumb,sumc,sumd=0,0,0,0
for turn in range(100):
	ta = randint(1,5)
	ada.forward(ta)
	suma = suma + ta
	if suma >=300:
		break
		
	tb=randint(1,5)
	bob.forward(tb)
	sumb = sumb + tb
	if sumb >=300:
		break
		
	tc=randint(1,5)
	ctc.forward(tc)
	sumc = sumc + tc
	if sumc >=300:
		break
		
	td=randint(1,5)
	dld.forward(td)
	sumd = sumd + td
	if sumd >=300:
		break
