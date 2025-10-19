class Chai:

    def __init__(self, type_, strength):
        self.type = type_
        self.strength = strength


# class GingerChai(Chai):

#     def __init__(self, type_, strength, ginger_level):
#         self.type = type_
#         self.strength = strength
#         self.ginger_level = ginger_level

# class GingerChai(Chai):

#     def __init__(self, type_, strength, ginger_level):
#         Chai.__init__(type_, strength)
#         self.ginger_level = ginger_level

class GingerChai(Chai):

    def __init__(self, type_, strength, ginger_level):
        super().__init__(type_, strength)
        self.ginger_level = ginger_level
