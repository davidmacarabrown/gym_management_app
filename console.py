from models.member import Member
from models.gym_class import GymClass
# from models.booking import Booking

import repositories.member_repository as member_repository
import repositories.gym_class_repository as gym_class_repository
# import repositories.booking_repository as booking_repository

# member_repository.delete_all()
# member_1 = Member("David", "Brown")
# member_repository.save_member(member_1)

# member_1 = member_repository.select_member(1)
# member_1.first_name = "John"
# member_1.last_name = "117"
# member_repository.update_member(member_1)

# print(member_repository.select_all())
# member_1.last_name = "Awesome"
# member_repository.update_member(member_1)
# print(member_repository.select_all())

class_1 = GymClass("Personal Training", "One to one personal training session focusing on helping the client achieve their specific fitness goals, and providing structured training for clients of all levels of ability. This includes workout planning and training the client in the safe use of machines and gym equipment.")

print(gym_class_repository.create_class(class_1).description)