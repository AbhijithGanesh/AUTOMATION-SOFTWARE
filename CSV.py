import csv

def present_students(file_param):
    f = open(file_param)
    csv_reader = csv.reader(f)
    a = []
    b = []
    name_list = []
    attendance_list = []
    name_final = []
    attendance_final = []
    list_1 = []
    final_list = []
    dict_list =[]   
    for row in csv_reader:
        a.append(row[1:])
    for i in a:
        b.append(i[0:3])
    for i in b:
        name_list.append(i[1])
        if i[2] == "Attendance":
            attendance_list.append("Attendance")
        elif i[2] == "Present":
            attendance_list.append(1)
        elif i[2] == "Absent":
            attendance_list.append(0)

    for i in range(1,len(attendance_list)):
        corresponding_list = [name_list[i],attendance_list[i]]
        final_list.append(corresponding_list)
        final_list.sort()


    for i in final_list:
        name_final.append(i[0])
        attendance_final.append(i[1])

    for i in range(len(name_final)):
        if name_final.count(name_final[i]) >=2:
            count = 0
            corresponding_dict={}
            for j in range(name_final.count(name_final[i])):
                count += attendance_final[j]
            corresponding_dict[name_final[i]] = count
        else:
            corresponding_dict[name_final[i]]=attendance_final[i]
    return corresponding_dict
def absentee(file_param):
    f = open(file_param)
    csv_reader = csv.reader(f)
    a = []
    b = []
    name_list = []
    attendance_list = []
    name_final = []
    attendance_final = []
    list_1 = []
    final_list = []
    dict_list =[]   

    for row in csv_reader:
        a.append(row[1:])
    for i in a:
        b.append(i[0:3])
    for i in b:
        name_list.append(i[1])
        if i[2] == "Attendance":
            attendance_list.append("Attendance")
        elif i[2] == "Present":
            attendance_list.append(0)
        elif i[2] == "Absent":
            attendance_list.append(1)

    for i in range(1,len(attendance_list)):
        corresponding_list = [name_list[i],attendance_list[i]]
        final_list.append(corresponding_list)
        final_list.sort()


    for i in final_list:
        name_final.append(i[0])
        attendance_final.append(i[1])

    for i in range(len(name_final)):
        if name_final.count(name_final[i]) >=2:
            count = 0
            corresponding_dict={}
            for j in range(name_final.count(name_final[i])):
                count += attendance_final[j]
            corresponding_dict[name_final[i]] = count
        else:
            corresponding_dict[name_final[i]]=attendance_final[i]
    return corresponding_dict

def Value_changer(x):
    if type(x) != dict:
        raise TypeError
    a = list(x.keys())
    b = list(x.values())
    c = []
    for i in range(len(a)):
        c.append([a[i],b[i]])
    return c
def key_return_fun(x):
    if type(x) != dict:
        raise TypeError
    b = list(x.values())
    return b
def writing_convertor():
    a = input(r"Enter File Directory/Location")
    b = Value_changer(present_students(a))
    c = key_return_fun(absentee(a)) 
    for i in range(len(b)):
        b[i].append(c[i])
    for i in range(len(b)):
        a=b[i][1]/(b[i][1]+b[i][2])*100
        b[i].append(a)
    return b


def writer(y):
    a = writing_convertor()
    with open(y,'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Name","Days Present","Days Absent","Percentage"])
        for i in a:
            csv_writer.writerow(i)
writer("Output.csv")