import psycopg2
# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        conn = psycopg2.connect(
            host="postgres",
            port="5432",
            database="property",
            user="postgres",
            password="test")

        cursor = conn.cursor()
        cursor.execute('SET client_encoding TO "UTF8"')

        postgreSQL_select_Query = "select * from properties"

        cursor.execute(postgreSQL_select_Query)
        mobile_records = cursor.fetchall()

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Available flats</title>"
                               "<meta charset='UTF-8' ></head>", "utf-8"))

        self.wfile.write(bytes("<body>", "utf-8"))

        self.wfile.write(bytes("<div style='width: 500px;'>", "utf-8"))
        for row in mobile_records :
            self.wfile.write(bytes("<div style='margin:5px; border: 1px solid black; padding: 5px;'>", "utf-8"))
            self.wfile.write(bytes(f"<h3>{row[0]}</h3>", "utf-8"))
            self.wfile.write(bytes(f'<img src="{row[1]}">', "utf-8"))
            self.wfile.write(bytes("</div>", "utf-8"))

        self.wfile.write(bytes("</div>", "utf-8"))

        self.wfile.write(bytes("</body></html>", "utf-8"))

        cursor.close()
        conn.close()

if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


