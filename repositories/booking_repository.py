import pdb

from db.run_sql import run_sql
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
from models.booking import Booking


def save_booking(member, gym_class):

    values = [member.id, gym_class.id]
    sql = "SELECT id FROM bookings WHERE member_id = %s AND class_id = %s"

    booking_check = run_sql(sql, values)
    
    if len(booking_check) == 0:

        sql_2 = "INSERT INTO bookings (member_id, class_id) VALUES (%s, %s) RETURNING *"
        result = run_sql(sql_2, values)
        booking = Booking(member.id, gym_class.id, result[0]["id"])
        return True
    
    else:
        return False
    
    


def select_all():

    all_bookings = []
    sql = "SELECT * FROM bookings"
    result = run_sql(sql)

    if result is not None:
        for row in result:
            member_id = row["member_id"]
            class_id = row["class_id"]
            booking_id = row["id"]
            booking = Booking(member_id, class_id, booking_id)
            all_bookings.append(booking)

    return all_bookings

def select_booking_by_class_and_member_id(member_id, class_id):

    
    sql = "SELECT bookings.id FROM bookings INNER JOIN classes ON classes.id = bookings.class_id INNER JOIN members ON members.id = bookings.member_id "
    values =[member_id, class_id]
    result = run_sql(sql, values)[0]["id"]
    return result


def delete_bookings_by_member(member_id):
    
    sql = "DELETE FROM bookings WHERE member_id = %s"
    values = [member_id]
    run_sql(sql, values)
    

def delete_booking(id):

    sql ="DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)