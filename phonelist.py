#import sqlite3
#conn = sqlite3.connect("phone.db")

import psycopg2

# Global connection
conn = psycopg2.connect(
        host = "localhost",
        database = "phone",
        user = "phone",
        password = "abc123"
    )


def read_phonelist(C):
    cur = C.cursor()
    cur.execute("SELECT * FROM phonelist;")
    rows = cur.fetchall()
    cur.close()
    return rows

def add_phone(C, name, phone, address):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist (name, phone, address) VALUES ('{name}', '{phone}', '{address}');")
    cur.close()
    
def delete_phone(C, id):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE id = '{id}';")
    cur.close()
    
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
        print("Committed!")
    except:
        print("No changes!")
    cur.close()

def display_help():
    print("Hello and welcome to the phone list, available commands:")
    print("  help - display this list of commands")
    print("  add - add a phone number")
    print("  delete - delete a contact")
    print("  list - list all phone numbers")
    print("  save - commit all the changes to the database")
    print("  quit - quit the program")


display_help()

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().upper()
    if cmd == "LIST":
        phones = read_phonelist(conn)
        for name, phone, address, id in phones:
            print(f"{id}. {name}, phone: {phone}, address: {address}")
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        address = input("  Address: ")
        add_phone(conn, name, phone, address)
    elif cmd == "DELETE":
        id = input("  Id: ")
        delete_phone(conn, id)
    elif cmd == "HELP":
        display_help()
    elif cmd == "SAVE":
        print("Saving the changes...")
        save_phonelist(conn)
    elif cmd == "QUIT":
        print("Saving the changes...")
        save_phonelist(conn)
        #exit()
        print("Quitting...")
        break
    else:
        print(f"  Unknown command: {cmd}")

print("-----Goodbye!------")

