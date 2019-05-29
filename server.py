#the client in this case is a web browser
from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8081

class myHandler(BaseHTTPRequestHandler):
	
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		
		self.wfile.write("Natnael Berhane | Atr/9305/09 | sec-3 !")
		return

try:
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print ('Server running on port: ' , PORT_NUMBER)
	
	server.serve_forever()

except KeyboardInterrupt:
	print ('^C received, shutting down the web server')
	server.socket.close()
