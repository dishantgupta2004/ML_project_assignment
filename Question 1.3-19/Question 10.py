import pandas as pd
import mysql.connector as sql


class Airline:
    
    conn = sql.connect(host= "localhost", user= "dishantguptaa", password= "@Dishant_2015133", database= "airline")

    def menu(self):
        print("*"*50)
        print("FLIGHT MANAGEMENT SYSTEM")
        print("1. Create table passenger")
        print("2. Add new passenger detail")
        print("3. Create table classtype")
        print("4. Add new class type detail")
        print("5. Create table food")
        print("6. Add food item detail")
        print("7. Show food menu")
        print("8. Search by food item Name")
        print("9. Delete food item detail if no more available")
        print("10. Revise rates of food items")
        print("11. create table luggage")
        print("12. Add new charges for more weights")
        print("13. Show all types of seats and their ticket price")
        print("14. Show type of seats passenger has chosen and its ticket price")
        print("15. if extra luggage then its bill")
        print("16. if food item ordered then its bill")
        print("*"*100)
        
    def create_passenger(self):
        c1 = Airline.conn.cursor()
        c1.execute("create table if not exists passenger(name varchar(25), address varchar(25), mobile integer(10), rdate date, source varchar(20), destination varchar(20))")
        
    def add_passenger(self):
        c1 = Airline.conn.cursor()
        L = []
        name = input("Enter your name: ")
        L.append(name)
        address = input("Enter your address: ")
        L.append(address)
        mobile = input("Enter your mobile number: ")
        L.append(mobile)
        rdate = input("Enter the reservation date: (YY-MM-DD): ")
        L.append(rdate)
        source = input("Enter the source locaton: ")
        L.append(source)
        destination = input("Enter the destination of flight: ")
        L.append(destination)
        pas= (L)
        sql = "insert into passenger(name, address, mobile, rdate, source, destination)values(%s, %s, %s, %s, %s)"
        c1.execute(sql, pas)
        Airline.conn.commit()
        print("Records of passenger inserted")
        
        
    def create_classtype(self):
        c1 = Airline.conn.cursor()
        c1.execute("create table if not exists classtype(sno int(5), classtype varchar(20), rate varchar(10));")
        print("table classtype created")
        
    def add_classtype(self):
        c1 = Airline.conn.cursor()
        df = pd.read_sql("select * from classtype", Airline.conn)
        print(df)
        L =[]
        sno = input("Enter the serial number: ")
        L.append(sno)
        itemname = input("Enter name of classtype: ")
        L.append(itemname)
        rate = input("Enter the rate per ticket: ")
        L.append(rate)
        ct = (L)
        sql = "insert into classtype(sno, classtype, rate) values(%s, %s, %s)"
        c1.execute(sql, ct)
        Airline.conn.commit()
        print("Record inserted in classtype")
        
    def create_food(self):
        c1 = Airline.conn.cursor()
        c1.execute("create table if not exists food(sno integer(5), itemname varchar(25), rate integer(5))")
        print("table food created")
        
    def add_food(self):
        c1 = Airline.conn.cursor()
        df = pd.read_sql("select * from food", Airline.conn)
        print(df)
        L = []
        sno = input("Enter the serial no: ")
        L.append(sno)
        itemname = input("Enter the name of food item: ")
        L.append(itemname)
        rate = input("Enter the rate of food items per price: ")
        L.append(rate)
        f = (L)
        sql = "insert into food(sno, itemname, rate)values(%s.%s.%s)"
        c1.execute(sql, f)
        Airline.conn.commit()
        print("Record inserted in food")
        
    def showfoodmenu(self):
        print("All food items available")
        df = pd.read_sql("select * from food", Airline.conn)
        print(df)
        
    def search_by_fooditem(self):
        print("All food items available")
        df = pd.read_sql("select * from food", Airline.conn)
        print(df)
        print("Search rate of fooditem by entering food item")
        a = float(input("Enter the food item no: "))
        qry = "select * from food where sno= %s;"%(a, )
        df1 = pd.read_sql(qry, Airline.conn)
        print(df1)
        
    def delete_food(self):
        print("Before any changes in food menu")
        df = pd.read_sql("select * from food", Airline.conn)
        print(df)
        mc = Airline.conn.cursor()
        mc.execute("delete from food where itemname= 'SAMOSA'")
        print("Record deleted")
        df = pd.read_sql("select * from food", Airline.conn)
        print(df)
        Airline.conn.commit()
        

        
        
        
        
        
        