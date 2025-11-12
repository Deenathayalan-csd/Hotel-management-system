import sqlite3

# ---------- DATABASE SETUP ----------
def create_table():
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS rooms (
                    room_no INTEGER PRIMARY KEY,
                    room_type TEXT,
                    price REAL,
                    is_booked INTEGER DEFAULT 0
                )''')
    c.execute('''CREATE TABLE IF NOT EXISTS guests (
                    guest_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone TEXT,
                    room_no INTEGER,
                    FOREIGN KEY(room_no) REFERENCES rooms(room_no)
                )''')
    conn.commit()
    conn.close()

# ---------- BASIC OPERATIONS ----------
def add_room(room_no, room_type, price):
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("INSERT INTO rooms VALUES (?, ?, ?, 0)", (room_no, room_type, price))
    conn.commit()
    conn.close()
    print("✅ Room added successfully!")

def view_rooms():
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT * FROM rooms")
    rows = c.fetchall()
    print("\n--- All Rooms ---")
    for row in rows:
        status = "Booked" if row[3] else "Available"
        print(f"Room No: {row[0]}, Type: {row[1]}, Price: ₹{row[2]}, Status: {status}")
    conn.close()

def book_room(name, phone, room_no):
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("SELECT is_booked FROM rooms WHERE room_no=?", (room_no,))
    result = c.fetchone()

    if result and result[0] == 0:
        c.execute("INSERT INTO guests (name, phone, room_no) VALUES (?, ?, ?)", (name, phone, room_no))
        c.execute("UPDATE rooms SET is_booked=1 WHERE room_no=?", (room_no,))
        conn.commit()
        print(f"✅ Room {room_no} booked successfully for {name}!")
    else:
        print("❌ Room not available or does not exist.")
    conn.close()

def checkout(room_no):
    conn = sqlite3.connect("hotel.db")
    c = conn.cursor()
    c.execute("DELETE FROM guests WHERE room_no=?", (room_no,))
    c.execute("UPDATE rooms SET is_booked=0 WHERE room_no=?", (room_no,))
    conn.commit()
    conn.close()
    print(f"✅ Room {room_no} checked out successfully!")

# ---------- MAIN MENU ----------
def menu():
    create_table()
    while True:
        print("\n🏨 HOTEL MANAGEMENT SYSTEM")
        print("1. Add Room")
        print("2. View Rooms")
        print("3. Book Room")
        print("4. Checkout")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            room_no = int(input("Room Number: "))
            room_type = input("Room Type: ")
            price = float(input("Room Price: "))
            add_room(room_no, room_type, price)
        elif choice == '2':
            view_rooms()
        elif choice == '3':
            name = input("Guest Name: ")
            phone = input("Phone Number: ")
            room_no = int(input("Room Number: "))
            book_room(name, phone, room_no)
        elif choice == '4':
            room_no = int(input("Room Number: "))
            checkout(room_no)
        elif choice == '5':
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice!")

# ---------- RUN ----------
if __name__ == "__main__":
    menu()
