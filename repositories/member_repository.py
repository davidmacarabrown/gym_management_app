from models.gym_class import GymClass
from db.run_sql import run_sql

from models.member import Member

import repositories.gym_class_repository as gym_class_repository

import pdb

def save_member(member):
    
    sql = "INSERT INTO members (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member
    

def update_member(member):
    sql = "UPDATE members SET first_name = %s, last_name = %s WHERE id = %s"
    values = [member.first_name, member.last_name, member.id]
    results = run_sql(sql, values)


def select_member(id):
    
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result is not None:
        member = Member(result[0]['first_name'], result[0]['last_name'] , result[0]['id'])
    
    return member


def select_all():
    
    all_members = []
    sql = "SELECT * FROM members ORDER BY id ASC"
    result = run_sql(sql)
    for row in result:
        selected_member = Member(row[0], row[1], row[2])
        all_members.append(selected_member)
        
    return all_members


def show_booked_classes(id):

    booked_classes = []
    
    sql = "SELECT bookings.class_id FROM bookings INNER JOIN members ON members.id = bookings.member_id WHERE member_id = %s"

    values = [id]
    result = run_sql(sql, values)

    print(result)


def delete_member(id):

    sql = "DELETE FROM members WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():

    sql = "DELETE FROM members"
    run_sql(sql)