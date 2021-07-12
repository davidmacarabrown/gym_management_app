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


# def generate_booking_details(bookings):

#     if bookings is not None:

#         for booking in bookings:
#             print(member_repository.select_member(booking.member_id).first_name)
#             booking_detail = []
#             booking_detail.append(booking.booking_id)

            