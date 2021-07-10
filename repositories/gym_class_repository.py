from pdb import run
from db.run_sql import run_sql

from models.gym_class import GymClass

def create_class(gym_class):
    sql = "INSERT INTO classes (class_name, class_description) VALUES (%s, %s) RETURNING *"
    values = [gym_class.name, gym_class.description]
    results = run_sql(sql, values)
    name = results[0]["class_name"]
    description = results[0]["class_description"]
    id = results[0]["id"]
    returned_class = GymClass(name, description, id)
    return returned_class