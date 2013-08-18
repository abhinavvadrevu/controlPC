import tornado.ioloop
from tornado.web import *
import win32api
import ImageGrab

#########################
# Configuration options #
#########################

tornado_options = {
  "port": 8888
}

#########################
# Handlers go here      #
#########################

class MainHandler(RequestHandler):
  def get(self):
    self.render("index.html")

class DoublerHandler(RequestHandler):
  def get(self):
    x = self.get_argument("x")
    y = self.get_argument("y")
    c = self.get_argument("c")
    print(x + ", " + y + ", " + c)
    tempx = open("tempx", "w")
    tempy = open("tempy", "w")
    if (c=='true'):
        print("inside")
        click = open("click", "w")
        click.write(c)
        click.close()
    tempx.write(x)
    tempy.write(y)
    tempx.close()
    tempy.close()

class ImageHandler(RequestHandler):
	def get(self):
		#first, update the screenshot
		img = ImageGrab.grab()
		img.save('test.jpg','JPEG')
		#now, encode it and send it over
		k = None
		with open("test.jpg", "rb") as f:
			data = f.read()
			k=data.encode("base64")
		self.write(k)

  ###### get ends here ######

############################
# Routes go here           #
############################
application = tornado.web.Application([

  (r"/",       MainHandler),
  (r"/doubler",  DoublerHandler),
  (r"/getimage",  ImageHandler)

  ###### routes end here ######

#########################
# Don't change this     #
#########################
], debug=True,
   template_path=os.path.join(os.path.dirname(__file__), ""),
   static_path=os.path.join(os.path.dirname(__file__), ""),
)

if __name__ == "__main__":
  application.listen(tornado_options["port"])
  tornado.ioloop.IOLoop.instance().start()
