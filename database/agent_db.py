from db_connection import DBConnection


class AgentDB:
    def __init__(self, conn: DBConnection):
        self.conn = conn

    def create_agent(self, data):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        agent = """
            INSERT INTO agent(
                       id, name, speciality, is_active, completed_missions, failed_missions, agent_rank
                       ) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
        cursor.execute(cursor.execute(agent, """(
                                      data['id'], 
                                      data['name'], 
                                      data['speciality'], 
                                      data['is_active'], 
                                      data['completed_missions'], 
                                      data['failed_missions'], 
                                      data['agent_rank'], 
                                      """))
        cursor.close()
        connect.close()

    def get_all_agents(self):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute("SELECT * FROM agents")
        cursor.close()
        connect.close()

    def get_agent_by_id(self, id):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute("SELECTED * FROM agents WHERE id = %s", id)
        cursor.close()
        connect.close()

    def update_agent(self, id, data):
        connect = self.conn.get_connection()
        cursor = connect.cursor(dictionary=True)
        cursor.execute("""UPDATA agents SET  
                       name = %, 
                       speciality = %, 
                       is_active = %, 
                       completed_missions = %, 
                       failed_missions = %, 
                       agent_rank = %
                       WHERE id = %,
                       """)

        connect.commit()
        cursor.close()
        connect.close()

    def deactivate_agent(self, id):
        connect = self.conn.get_connection()
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
