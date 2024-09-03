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
    json_read()
    for stud in data["student"]:
        if {{stud.sno}}==id:
            data["student"].removel(stud)
            break

    i=1
    for stud in data["studend"]:
        stud["sno"]=i
        i+=1    