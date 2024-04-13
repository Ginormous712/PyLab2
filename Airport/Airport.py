import MySQLdb


class Airport():
    def __init__(self, url, user, password):
        self.__db = MySQLdb.connect(url, user, password, "airport")
        self.__cursor = self.__db.cursor()

    @property
    def db(self):
        return self.__db

    @db.setter
    def db(self, db):
        self.__db = db

    @property
    def cursor(self):
        return self.__cursor

    @cursor.setter
    def cursor(self, cursor):
        self.__cursor = cursor

    @staticmethod
    def print_airlines(results):
        for row in results:
            id = row[0]
            name = row[1]
            print(f"ID: {id}\tName: {name}")

    @staticmethod
    def print_flights(results):
        for row in results:
            id = row[0]
            airline_id = row[1]
            destination = row[2]
            departure = row[3]
            arrival = row[4]
            print(f"ID: {id}\tAirline: {airline_id}\tDestination: {destination}\t"
                  f"Departure {departure}\tArrival: {arrival}")

    def show_airlines(self):
        sql = "SELECT * FROM airline"
        print(" === Table: Airline === ")
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            for row in results:
                id = row[0]
                name = row[1]
                print(f"ID: {id}\tName: {name}")
        except:
            print("Error")

    def show_flights(self):
        sql = "SELECT * FROM flight"
        print(" === Table: Flight === ")
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            Airport.print_flights(results)
        except:
            print("Error")

    def show_flights_for_airline(self, airline_id):
        sql = f"SELECT * FROM flight WHERE id_airline = {airline_id}"
        print(f" === All flights referenced to Airline with ID: {airline_id} === ")
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            Airport.print_flights(results)
        except:
            print("Error")

    def add_airline(self, id, name):
        sql = "INSERT INTO airline VALUES (%d, '%s')" % (id, name)
        try:
            self.cursor.execute(sql)
            self.__db.commit()
            print(f"Airline with ID: {id} added")
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Airline with ID: {id} is not added")
            self.__db.rollback()

    def add_flight(self, id, airline_id, destination, departure, arrival):

        sql = "INSERT INTO flight VALUES (%d, %d, '%s', '%s', '%s')" % (id, airline_id, destination, departure, arrival)
        try:
            self.cursor.execute(sql)
            self.__db.commit()
            print(f"Flight with ID: {id} added")
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Flight with ID: {id} is not added")
            self.__db.rollback()

    def delete_airline(self, id):
        sql = f"DELETE FROM airline WHERE id_airline = {id}"
        try:
            self.cursor.execute(sql)
            self.__db.commit()
            print(f"Airline with ID: {id} deleted")
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Airline with ID: {id} is not deleted")
            self.__db.rollback()

    def delete_flight(self, id):
        sql = f"DELETE FROM flight WHERE id_flight = {id}"
        try:
            self.cursor.execute(sql)
            self.__db.commit()
            print(f"Flight with ID: {id} deleted")
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Flight with ID: {id} is not deleted")
            self.__db.rollback()

    def change_airline(self, id, name):
        sql = f"UPDATE airline SET name = '{name}' WHERE id_airline = {id}"
        try:
            self.cursor.execute(sql)
            self.__db.commit()
            print(f"Airline with ID: {id} changed")
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Airline with ID: {id} is not changed")
            self.__db.rollback()

    def change_flight(self, id, airline_id, destination, departure, arrival):
        sql = ("UPDATE flight SET id_airline = %d, destination = '%s', departure_time = '%s', arrival_time = '%s' WHERE id_flight = %d"
               % (airline_id, destination, departure, arrival, id))
        try:
            self.cursor.execute(sql)
            self.__db.commit()
            print(f"Flight with ID: {id} changed")
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Flight with ID: {id} is not changed")
            self.__db.rollback()

    def search_airline(self, id):
        sql = f"SELECT * FROM airline WHERE id_airline = {id}"
        print(f" === Airline with ID: {id} === ")
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            Airport.print_airlines(results)
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Airline with ID: {id} is not found")

    def search_flight(self, id):
        sql = f"SELECT * FROM flight WHERE id_flight = {id}"
        print(f" === Flight with ID: {id} === ")
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            Airport.print_flights(results)
        except MySQLdb.Error as e:
            print(f"Error: {e}")
            print(f"Flight with ID: {id} is not found")
