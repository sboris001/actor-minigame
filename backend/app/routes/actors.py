from fastapi import APIRouter
import json
import random
from ..config import DATA_PATH

router = APIRouter(
)

@router.get("/actors")
def get_actors():
    with open(f"{DATA_PATH}/actors.json", "r") as file:
        data = json.load(file)
    actors = data["actors"]
    length = len(actors)
    pos1 = random.randint(0, length-1)
    pos2 = random.randint(0, length-1)
    while pos2 == pos1:
        pos2 = random.randint(0, length-1)
    actor1 = actors[pos1]
    actor2 = actors[pos2]
    return [actor1, actor2]