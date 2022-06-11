#import sqlite3
#conn = sqlite3.connect("phone.db")

import psycopg2
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
def add_phone(C, name, phone):
    cur = C.cursor()
    cur.execute(f"INSERT INTO phonelist VALUES ('{name}', '{phone}');")
    cur.close()
def delete_phone(C, name):
    cur = C.cursor()
    cur.execute(f"DELETE FROM phonelist WHERE name = '{name}';")
    cur.close()
def save_phonelist(C):
    cur = C.cursor()
    try:
        cur.execute("COMMIT;")
        print("Committed!")
    except:
        print("No changes!")
    cur.close()


print("Hello and welcome to the phone list, available commands:")
print("  add - add a phone number")
print("  delete - delete a contact")
print("  list - list all phone numbers")
print("  save - commit all the changes to the database")
print("  quit - quit the program")

while True: ## REPL - Read Execute Program Loop
    cmd = input("Command: ").strip().upper()
    if cmd == "LIST":
        print(read_phonelist(conn))
    elif cmd == "ADD":
        name = input("  Name: ")
        phone = input("  Phone: ")
        add_phone(conn, name, phone)
    elif cmd == "DELETE":
        name = input("  Name: ")
        delete_phone(conn, name)
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

