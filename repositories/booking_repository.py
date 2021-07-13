import pdb

from db.run_sql import run_sql
import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
from models.booking import Booking


def save_booking(member, gym_class):

    sql = "INSERT INTO bookings (member_id, class_id) VALUES (%s, %s) RETURNING *"
    values = [member.id, gym_class.id]
    result = run_sql(sql, values)
    booking = Booking(member.id, gym_class.id, result[0]["id"])
    return booking


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


def delete_booking(id):

    sql ="DELETE FROM bookings WHERE id = %s"
    values = [id]
    run_sql(sql, values)