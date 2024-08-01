class BMW:
    def __init__(self):
            self.models = ['i8','x1','x5','x6']

    def outModels(self):
        print("Models available in BMW : ")
        for i in self.models:
            print("\t%s"%i)