from ..lib import testing

def format_record(rec: tuple[str, str, float]):

    if type(rec)!=tuple: raise TypeError("Введен не кортеж")
    if len(rec)!=3: raise ValueError("Неверно введен кортеж с элементами")

    fio = rec[0].split()
    group = rec[1]
    gpa = rec[2]

  
    if len(fio)<=1: raise ValueError("Неверно введено имя")
    if len(group)==0: raise ValueError("Неверно введена группа")
    if type(gpa)!=float and type(gpa)!=int: raise TypeError("Неверно введена gpa")

    fio1 = ""
    if len(fio)==3:
        fio1 = fio[0]+" "+fio[1][0]+". "+fio[2][0]+"." 
    else: 
        fio1 = fio[0]+" "+fio[1][0]+"."

    return f"{fio1.title()}, гр. {group}, GPA {gpa:.2f}"

test_format_record = [
    ("Иванов Иван Иванович", "BIVT-25", 4.6),
    ("Петров Пётр", "IKBO-12", 5.0),
    ("Петров Пётр Петрович", "IKBO-12", 5.0),
    ("  сидорова  анна   сергеевна ", "ABB-01", 3.999),
    (1,),
    "123"
]
print()
print("FORMAT_RECORD")
print()
testing(format_record,test_format_record)
print()