class Audi:
    def __init__(self):
        self.models = ['q7','a6','a8','a3']

    def outModels(self):
        print("Models available in Audi : ")
        for i in self.models:
            print("\t%s"%i)