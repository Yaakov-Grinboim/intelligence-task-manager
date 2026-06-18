from db_connection import DBConnection
from logger_config import logger


class AgentDB:
    def __init__(self, conn: DBConnection):
        self.conn = conn

    def create_agent(self, data):
        connect = self.conn.get_connection()
        if not connect:
            return False
        cursor = connect.cursor(dictionary=True)
        agent = """
            INSERT INTO agent(
                       id, name, speciality, is_active, completed_missions, failed_missions, agent_rank
                       ) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        try:
            cursor.execute(
                agent,
                (
                    data["id"],
                    data["name"],
                    data["speciality"],
                    data["is_active"],
                    data["completed_missions"],
                    data["failed_missions"],
                    data["agent_rank"],
                ),
            )
            connect.commit()
            return True
        except Exception as e:
            logger.error(f"Error creating agent: {e}")
            return False
        finally:
            cursor.close()
            connect.close()

    def get_all_agents(self):
        connect = self.conn.get_connection()
        if not connect:
            return []
        cursor = connect.cursor(dictionary=True)
        try:
            cursor.execute("SELECT * FROM agents")
            return cursor.fetchall()
        except Exception as e:
            logger.error(f"Error fatching agent: {e}")
            return []
        finally:
            cursor.close()
            connect.close()

    def get_agent_by_id(self, id):
        connect = self.conn.get_connection()
        if not connect:
            return None
        cursor = connect.cursor(dictionary=True)
        try:
            cursor.execute("SELECTED * FROM agents WHERE id = %s", id)
            return cursor.fetchall()
        except Exception as e:
            logger.error(f"Error fatching agent: {e}")
            return None
        finally:
            cursor.close()
            connect.close()

    def update_agent(self, id, data):
        connect = self.conn.get_connection()
        if not connect:
            return False
        cursor = connect.cursor(dictionary=True)
        agent = """UPDATA agents SET  
                    name = %s, 
                    speciality = %s, 
                    is_active = %s, 
                    completed_missions = %s, 
                    failed_missions = %s, 
                    agent_rank = %s
                    WHERE id = %s
                    """
        try:
            cursor.execute(
                agent,
                (
                    data["id"],
                    data["name"],
                    data["speciality"],
                    data["is_active"],
                    data["completed_missions"],
                    data["failed_missions"],
                    data["agent_rank"],
                    id
                ),
            )
            connect.commit()
            return
        except Exception as e:
            logger.error(f"Error updating agent: {e}")
            return False
        finally:
            cursor.close()
            connect.close()

    def deactivate_agent(self, id):
        connect = self.conn.get_connection()
        if not connect:
            return False
        cursor = connect.cursor(dictionary=True)
        cursor.execute()
        cursor.close()
        connect.close()

    def increment_completed(self, id):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute()
        cursor.close()
        connect.close()

    def increment_failed(self, id):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute()
        cursor.close()
        connect.close()

    def get_agent_performance(self, id):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute()
        cursor.close()
        connect.close()

    def count_active_agents(self):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute()
        cursor.close()
        connect.close()
