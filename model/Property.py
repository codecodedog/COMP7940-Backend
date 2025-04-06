import json

class Property:
    def __init__(
            self, 
            ID, 
            user_id, 
            district,
            address,
            condition,
            isRent,
            price_min,
            price_max,
            paid_duration    
        ):  
        self.ID = ID
        self.user_id = user_id
        self.district = district
        self.address = address
        self.condition = json.loads(condition)
        self.isRent = isRent
        self.price_min = price_min
        self.price_max = price_max
        self.paid_duration = paid_duration

    def to_dict(self):
        return {
            'ID': self.ID,
            'user_id': self.user_id,
            'district': self.district,
            'address': self.address,
            'condition': self.condition,
            'preferred_district': self.preferred_district,
            'isRent': self.isRent,
            'price_min': self.price_min,
            'price_max': self.price_max,
            'paid_duration': self.paid_duration
        }