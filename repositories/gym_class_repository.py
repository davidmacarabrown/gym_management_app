import pdb

from db.run_sql import run_sql

from models.gym_class import GymClass
import repositories.member_repository as member_repository

def create_class(gym_class):

    sql = "INSERT INTO classes (class_name, class_description) VALUES (%s, %s) RETURNING *"
    values = [gym_class.name, gym_class.description]
    result = run_sql(sql, values)
    name = result[0]["class_name"]
    description = result[0]["class_description"]
    id = result[0]["id"]
    returned_class = GymClass(name, description, id)
    return returned_class

def show_booked_members(gym_class):
    booked_members = []
    sql = "SELECT bookings.member_id FROM bookings INNER JOIN classes ON classes.id = bookings.class_id WHERE class_id = %s"
    values = [gym_class.id]
    result = run_sql(sql, values)
    if result is not None:
        for row in result:
            member = member_repository.select_member(row[0])
            booked_members.append(member)
            
    return booked_members
        

def select_class(id):

    sql = "SELECT * FROM classes WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    returned_class = GymClass(result[0]["class_name"], result[0]["class_description"], result[0]["id"])
    return returned_class

def select_all():

    all_classes= []
    sql = "SELECT * FROM classes ORDER BY id ASC"
    result = run_sql(sql)
    for row in result:
        selected_class = GymClass(row[0], row[1], row[2])
        all_classes.append(selected_class)
    
    return all_classes


def update_class(class_input):

    sql = "UPDATE classes SET class_name = %s, class_description = %s WHERE id = %s RETURNING *"
    values = [class_input.name, class_input.description, class_input.id]
    result = run_sql(sql, values)
    updated_class = GymClass(result[0]["class_name"], result[0]["class_description"], class_input.id)
    return updated_class

def delete_class(id):

    sql = "DELETE FROM classes WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all_classes():
    
    sql = "DELETE FROM classes"
    run_sql(sql)