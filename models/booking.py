class Booking:
    def __init__(self, member_id, gym_class_id, id = None):
        self.id = id
        self.member_id = member_id
        self.gym_class_id = gym_class_id