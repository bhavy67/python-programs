class Chaiorder:
    def __init__(self, tea_type, sugar_level, size):
        self.tea_type = tea_type
        self.sugar_level = sugar_level
        self.size = size

    @classmethod
    def from_string(cls, order_string):
        tea_type, sugar_level, size = order_string.split('-')
        return cls(tea_type, sugar_level, size)
    
    @classmethod
    def from_dict(cls, order_dict):
        return cls(
            order_dict['tea_type'],
            order_dict['sugar_level'],
            order_dict['size']
        )