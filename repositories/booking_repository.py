import pdb

from db.run_sql import run_sql

from models.booking import Booking

def save_booking(member, gym_class):
    # pdb.set_trace()
    sql = "INSERT INTO bookings (member_id, class_id) VALUES (%s, %s) RETURNING *"
    values = [member.id, gym_class.id]
    result = run_sql(sql, values)
    booking = Booking(member.id, gym_class.id, result[0]["id"])
    return booking

