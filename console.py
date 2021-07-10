from models.member import Member
# from models.gym_class import Gym_Class
# from models.booking import Booking

import repositories.member_repository as member_repository
# import repositories.gym_class_repository as gym_class_repository
# import repositories.booking_repository as booking_repository

member_1 = Member("David", "Brown")

print(member_repository.save_member(member_1))