from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from urlparse import urlparse, parse_qs
import cgi
import sys
from connect import Base, Restaurant, MenuItem, session_creator

form = '''
<form method='POST' enctype='multipart/form-data' action='/hello'><h2>What would you like me to say?</h2><input name="message" type="text" ><input type="submit" value="Submit"> </form>
'''

class WebServerHandler(BaseHTTPRequestHandler):

   def do_GET(self):

      s = None

      try:

         s = session_creator()

         print 'Path: ' + self.path

         parsed = urlparse(self.path);

         if parsed.path.startswith("/hello"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            message = ""
            message += "<html><body>Hello!"
            message += form
            message += "</body></html>"

            self.wfile.write(message)
            print message
            return

         elif parsed.path.startswith("/restaurant/id/"):
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            id, ix = '', parsed.path.rfind('/')

            if ix > 0:
               id = parsed.path[ix+1:]
               if id == '':
                  raise Exception("No such id parameter")
            else:
               raise Exception("No such id parameter")
               
            # params = parse_qs(parsed.query)

            restaurant = s.query(Restaurant).filter(Restaurant.id == int(id)).first()

            if restaurant == None:
               raise Exception("No such restaurant for id " + id)

            message = ""
            message += "<html><body>Restaurant:"
            message += restaurant.name
            message += "</body></html>"

            self.wfile.write(message)
            print message
            return

         elif parsed.path == "" or self.path == "/":
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            message = ""
            message += "<html><body><h1>Index page</h1>"
            message += form
            message += "</body></html>"

            self.wfile.write(message)
            print message
            return

      except Exception as e:
         self.send_error(404, 'File Not Found: %s; %s' % (self.path, str(e)))
      finally:
         if s != None: s.close()

   def do_POST(self):
      try:

         self.send_response(301)
         self.send_header('Content-type', 'text/html')
         self.end_headers()

         ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

         if ctype == 'multipart/form-data':
            fields = cgi.parse_multipart(self.rfile, pdict)
            messagecontent = fields.get('message')
            print 'fields: %s ' % type(fields)
            print fields

         output = ""
         output += "<html><body>"
         output += " <h2> Okay, how about this: </h2>"
         output += "<h1> %s </h1>" % messagecontent[0]
         output += form
         output += "</body></html>"

         self.wfile.write(output)

         print output

      except:
          pass

def main():
    try:

        port = 8081
        server = HTTPServer(('', port), WebServerHandler)
        
        print "Web Server running on port %s" % port

        server.serve_forever()

    except KeyboardInterrupt:
        print " ^C entered, stopping web server...."
        server.socket.close()

if __name__ == '__main__':
    main()

