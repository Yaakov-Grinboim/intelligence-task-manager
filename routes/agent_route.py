from fastapi import APIRouter
from pydantic import BaseModel
from database.agent_db import AgentDB

# from database.mission_db import
from logger_config import logger

router = APIRouter(prefix="/agents", tags="Agents")
agent_db = AgentDB()


class AgentCreate(BaseModel):
    id: int
    name: str
    specialy: str
    is_active: bool
    completed_: int


@router.post("")
def add_agents(agent: AgentCreate):
    logger.info("POST /agents called")
    # add = agent_db.create_agent(agent)
    return agent


@router.get("")
def get_agent():
    return agent_db.get_all_agents()


@router.get("/{id}")
def agent_by_id(id: int):
    agent = agent_db.get_agent_by_id(id)
    return agent


@router.put("/{id}")
def update_agent(id: int, agent: AgentCreate):
    return