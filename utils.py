import json


FILE="data/stud.json"

def json_read():
    with open (FILE) as f:
        data=json.load(f)
    return data
        
        
def json_write(data):
    with open (FILE,"w") as f:
        json.dump(data,f,indent=3)        
    