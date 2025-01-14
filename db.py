import pyodbc

class Database:
    def __init__(self,db):  
        self.con = pyodbc.connect("Driver={SQL Server};"
                                  "Server=DESKTOP-S53UJGM;"
                                  "Database=project;"
                                  "Trusted_Connection=yes;")
        self.cur = self.con.cursor()
        sql = """
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='students' AND xtype='U')
        CREATE TABLE students (
            id INT IDENTITY(1,1) PRIMARY KEY,
            name VARCHAR(255),
            age VARCHAR(255),
            dob VARCHAR(255),
            email VARCHAR(255),
            gender VARCHAR(50),
            contact VARCHAR(50),
            address VARCHAR(255)
        )
        """
        self.cur.execute(sql)
        self.con.commit()

    # Insert Function
    def insert(self, name, age, dob, email, gender, contact, address):
         self.cur.execute("insert into students values (?,?,?,?,?,?,?)",
                         (name, age, dob, email, gender, contact, address))
         self.con.commit()


    # Fetch All Data from DB
    def fetch(self):
      self.cur.execute("SELECT * FROM students")
      rows = self.cur.fetchall()
      return rows

    
    # Delete a Record in DB
    def remove(self, id):
        self.cur.execute("delete from students where id=?", (id,))
        self.con.commit()

    # Update a Record in DB
    def update(self, id, name, age, dob, email, gender, contact, address):
        self.cur.execute(
            "update students set name=?, age=?, dob=?, email=?, gender=?, contact=?, address=? where id=?",
            (name, age, dob, email, gender, contact, address, id))
        self.con.commit()




