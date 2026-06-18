from fastapi import FastAPI, HTTPException
# from routes.agent_route import router as agent_router
# from routes.mission_route import router as mission_router
# from routes.report_route import router as report_router
# from database.db_connection import DBConnection
# from logger_config import logger

app = FastAPI()
# app.include_router(agent_router)
# app.include_router(mission_router)

# db = DBConnection()

@app.get("/")
def add_agents(agent):
    # logger.info("POST /agents called")
    # add = agent_db.create_agent(agent)
    return agent