from db.run_sql import run_sql

from models.member import Member

import pdb

def save_member(member):
    # pdb.set_trace()
    sql = "INSERT INTO members (first_name, last_name) VALUES (%s, %s) RETURNING id"
    values = [member.first_name, member.last_name]
    results = run_sql(sql, values)
    member.id = results[0]
    return member
    

def delete_all():
    sql = "DELETE FROM members"
    run_sql(sql)

def select_all():
    sql = "SELECT * FROM members"
    results = run_sql(sql)
    return results