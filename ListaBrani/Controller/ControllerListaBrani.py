import json

class ControllerListaBrani():
    def __init__(self, listabrani):
        super(ControllerListaBrani, self).__init__()
        self.model = listabrani()


    def Carica_listabrani(self):
        if os.path.isfile('ListaBrani/data/listabrani.json'):
            with open("data_file.json", "w") as write_file:
                json.dump(self.model, write_file)

        else:
            jsonList = json.dumps(self.model)
            jsonFile = open("listabrani.json", "w")
            jsonFile.write(jsonList)
            jsonFile.close()
            print("fatto")

