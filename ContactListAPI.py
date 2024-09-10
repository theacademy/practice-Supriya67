import http.server
import json
import mysql.connector
from urllib.parse import urlparse

# Database connection
db_config = {
    'user': 'root',
    'password': '981167@Sup',
    'host': 'localhost',
    'port': 3306,
    'database': 'contactlist2'
}

class ContactList:
    def __init__(self):
        self.conn=mysql.connector.connect(**db_config)
        self.cursor = self.conn.cursor(dictionary=True)
        self.contacts = []


    def create_contact(self, fullName, phone, email):
        sql="insert into contacts(fullname,phone,email) values(%s , %s, %s)"
        self.cursor.execute(sql,(fullName, phone, email,))
        self.conn.commit()
        new_contact=Contact(self.cursor.lastrowid, fullName, phone,email)
        self.contacts.append(new_contact)

    def read_contacts(self):
        sql="select * from contacts"
        self.cursor.execute(sql)
        contacts = self.cursor.fetchall()
        if not contacts:
            print("No contact found")
        else:
            for i in contacts:
                print(i)

    def get_contact_by_id(self,contact_id):
        sql="select * from contacts where id = %s"
        self.cursor.execute(sql,(contact_id,))
        contacts = self.cursor.fetchone()
        if contacts:
            print(contacts)
        else:
            print("No contact found")

    def update_contact(self, contact_id, new_fullName=None, new_phone=None, new_email=None):

        sql="update contacts set "
        params=[]
        update_fields=[]
        if new_fullName:
            update_fields.append("fullname = %s")
            params.append(new_fullName)
        if new_phone:
            update_fields.append("phone = %s")
            params.append(new_phone)
        if new_email:
            update_fields.append("email = %s")
            params.append(new_email)
        if update_fields:
            sql = sql + ", ".join(update_fields) + " where id  = %s"
            params.append(contact_id)
        self.cursor.execute(sql,params,)
        self.conn.commit()

    def delete_contact(self,contact_id):
        sql="delete from contacts where id = %s"
        self.cursor.execute(sql,(contact_id,))
        self.conn.commit()

contact_list = ContactList()

class RequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.split('/')
        if len(path_parts) == 2 and path_parts[1] == "contacts":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(contact_list.read_contacts()).encode())
        elif len(path_parts) == 3 and path_parts[1] == "contacts":
            contact_id = path_parts[2]
            contact = contact_list.get_contact_by_id(contact_id)
            if contact:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(contact).encode())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path == "/contacts":
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data)
            new_contact = contact_list.create_contact(data['fullName'], data['phone'], data['email'])
            self.send_response(201)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(new_contact).encode())
        else:
            self.send_response(404)
            self.end_headers()

    def do_PUT(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.split('/')
        if len(path_parts) == 3 and path_parts[1] == "contacts":
            contact_id = path_parts[2]
            content_length = int(self.headers['Content-Length'])
            put_data = self.rfile.read(content_length)
            data = json.loads(put_data)
            updated = contact_list.update_contact(contact_id, data.get('phone'), data.get('email'))
            if updated:
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"message": "Contact updated successfully"}).encode())
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

    def do_DELETE(self):
        parsed_path = urlparse(self.path)
        path_parts = parsed_path.path.split('/')
        if len(path_parts) == 3 and path_parts[1] == "contacts":
            contact_id = path_parts[2]
            if contact_list.delete_contact(contact_id):
                self.send_response(200)
                self.end_headers()
            else:
                self.send_response(404)
                self.end_headers()
        else:
            self.send_response(404)
            self.end_headers()

def run(server_class=http.server.HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()