from models.gym_class import GymClass
from db.run_sql import run_sql

from models.member import Member

import repositories.gym_class_repository as gym_class_repository

import pdb

def save_member(member):
    
    sql = "INSERT INTO members (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]
    return member
    
def update_member(member):
    sql = "UPDATE members SET first_name = %s, last_name = %s WHERE id = %s"
    values = [member.first_name, member.last_name, member.id]
    results = run_sql(sql, values)
    print(results)

def select_member(id):
    
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results is not None:
        member = Member(results[0]['first_name'], results[0]['last_name'] , results[0]['id'])
    
    return member

def select_all():
    
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    return results

def show_booked_classes(id):

    booked_classes = []
    
    sql = "SELECT bookings.class_id FROM bookings INNER JOIN members ON members.id = bookings.member_id WHERE member_id = %s"

    values = [id]
    result = run_sql(sql, values)

    for row in result:
        booked_class = gym_class_repository.select_class(row[0])
        booked_classes.append(booked_class)
    
    print(booked_classes)
    return booked_classes

def delete_member(id):

    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():

    sql = "DELETE FROM members"
    run_sql(sql)