from db.run_sql import run_sql

from models.member import Member

import pdb

def save_member(member):
    
    sql = "INSERT INTO members (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]
    return member
    

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

def delete_all():
    
    sql = "DELETE FROM members"
    run_sql(sql)