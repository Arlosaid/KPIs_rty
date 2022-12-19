import json

class Log:
    def __init__(self, id_log, fecha):
        self.id_log = id_log
        self.fecha = fecha
    
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)