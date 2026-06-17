import mysql.connector

class DBConnection:
    def __init__(self):
        self.config={
            "host": "127.0.0.1",
            "port": 3306,
            "user": "root",
            "password": "1234",
            "database": "Intelligence_db"
        }
        self._connection = None

    def get_connection(self):
        if self._connection:
            return self._connection
        
        try:
            self._connection = mysql.connector.connect(
                **self.config
            )
            return self._connection
        except mysql.connector.Error as arr:
            return arr
        
    def create_database(self):
        connect = self.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute("CREATE DATABASE IF NOT EXISTS Intelligence_db")
        cursor.close()


    def create_tables(self):
        connect = self.get_connection()
        cursor = connect.cursor(dictionary=True)
        create_agent_tabke =  """
        CREATE TABLE IF NOT EXISTS agent(
                id INT PRIMARY KEY AUTO_INCREMENT,
                name VARCHAR(50),
                speciality VARCHAR(50),
                is_active BOOLEAN DEFAULT TRUE,
                completed_missions INT DEFAULT 0,
                failed_missions INT DEFAULT TRUE,
                agent_rank ENUM ("junior", "senior", "commander")
            );
        """
        create_mission_tabke =  """
        CREATE TABLE IF NOT EXISTS mission(
                id INT PRIMARY KEY AUTO_INCREMENT,
                title VARCHAR(50),
                description TEXT,
                location VARCHAR(50),
                difficuly INT,
                importance INT,
                status VARCHAR(50) DEFAULT "NEW",
                risk_level VARCHAR(50),
                assigned_agent_id INT NULL
                 
            );
        """
        cursor.execute(create_agent_tabke)
        cursor.execute(create_mission_tabke)
        connect.commit()
        cursor.close()


t = DBConnection()
t.create_database()
t.create_tables()