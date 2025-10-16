class Basechai:
    def __init__(self, type_):
        self.type = type_

    def prepare(self):
        print(f"Preparing a cup of {self.type} chai.")

class MasalaChai(Basechai):
    def add_spices(self):
        print("Adding masala spices to the chai.")

class ChaiShop:
      chai_cls = Basechai

      def __init__(self):
          self.chai = self.chai_cls("Regular")

      def serve_chai(self):
          self.chai.prepare()
          if isinstance(self.chai, MasalaChai):
              self.chai.add_spices()
          print("Serving the chai.")

