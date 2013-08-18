import win32api
import win32gui
import win32con

def start():
	while True:
		(cy, cx) = win32gui.GetCursorPos()
		tempx = open("tempx", "r")
		tempy = open("tempy", "r")
		click = open("click", "r")
		x = tempx.read()
		y = tempy.read()
		c = click.read()
		if True: #not (cx==tempx and cy==tempy):
			print((x + ", " + y + ", " + c))
			try:
				a=3
				win32api.SetCursorPos((int(x),int(y)))
                #          win32api.SetCursorPos((x,y))
				if (c == 'true'):
					win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,int(x),int(y),0,0)
					win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,int(x),int(y),0,0)
					click.close()
					print("click!")
					click = open("click", "w")
					click.write("false")
					click.close()
			except ValueError:
				print("oops")
		tempx.close()
		tempy.close()
		click.close()


start()
