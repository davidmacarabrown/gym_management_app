import pdb
from models.member import Member
from models.gym_class import GymClass
from models.booking import Booking


import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
import repositories.booking_repository as booking_repository



member_1 = Member("David", "Brown")
member_2 = Member("John", "117")
member_3 = Member("Saruman", "The White")
member_4 = Member("Gandalf", "The Grey")


class_1 = GymClass("Personal Training", "One to one personal training session focusing on helping the client achieve their specific fitness goals, and providing structured training for clients of all levels of ability. This includes workout planning and training the client in the safe use of machines and gym equipment.")

class_2 = GymClass("Badminton Singles", "Solo badminton coaching with one instructor, highly focused training suitable for individuals of any skill level.")

class_3 = GymClass("Introduction To Martial Arts", "Group sessions teaching the fundamentals of Martial Arts. A beginner level class for students with little to no experience.")

member_repository.save_member(member_1)
member_repository.save_member(member_2)
member_repository.save_member(member_3)
member_repository.save_member(member_4)

gym_class_repository.create_class(class_1)
gym_class_repository.create_class(class_2)
gym_class_repository.create_class(class_3)

booking_repository.save_booking(member_1, class_1)
booking = booking_repository.select_booking_by_class_and_member_id(1, 1)

print(booking)
# pdb.set_trace()