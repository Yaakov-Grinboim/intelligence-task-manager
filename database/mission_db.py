from db_connection import DBConnection
from logger_config import logger


class MissionDB:
    def __init__(self, db: DBConnection):
        self.db = db 

    def create_mission(self):
        connect = self.db.get_connection()
        if not connect:
            return False
        cursor = connect.cursor()
        mission = "INSERT INTO mission (id, title, description, location, difficulty, importance, status, )"
    