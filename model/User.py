import json

class User:
    def __init__(
            self, 
            ID, 
            telegram_id, 
            username,
            condition,
            preferred_district,
            createdDate,
            isActive,
            question_count,
            question_history    
                ):  
        self.ID = ID
        self.telegram_id = telegram_id
        self.username = username
        self.condition = json.loads(condition)
        self.preferred_district = json.loads(preferred_district)
        self.createdDate = createdDate
        self.isActive = isActive
        self.question_count = question_count
        self.question_history = question_history

    def to_dict(self):
        return {
            'ID': self.ID,
            'telegram_id': self.telegram_id,
            'username': self.username,
            'condition': self.condition,
            'preferred_district': self.preferred_district,
            'createdDate': self.createdDate,
            'isActive': self.isActive,
            'question_count': self.question_count,
            'question_history': self.question_history
        }