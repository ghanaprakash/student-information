from utils import *

def registration(name,age, address,course,duration):
    data=json_read()
    temp_stud={
        "sno":len(data["student"])+1,
        "name":name,
        "age":age,
        "address":address,
        "course":course,
        "duration":duration
    }
    data["student"].append(temp_stud)
    json_write(data)


def update():
    pass

def delete():
    pass