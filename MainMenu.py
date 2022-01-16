import time
import sys
import mysql.connector as sql
print("\t\t\t", time.ctime())
conn = sql.connect(host='localhost', user='root', password='root', database='VikasLimitedCompany')
mycursor = conn.cursor()


def menu():
    c='yes'
    print("Do you want to continue?(yes/no")
    while (c == 'yes'):
        print("1.employee registration")
        print("2.employee details")
        print("3.update salary")
        print("4.employees list")
        print("5.know the number of employees")
        print("6.know your salary")
        print("7.exiting")
        choice = int(input("      enter the choice:          "))
        if choice == 1:
            register()
        elif choice == 2:
            details()
        elif choice == 3:
            em_salary()
        elif choice == 4:
            em_list()
        elif choice == 5:
            em_count()
        elif choice == 6:
            salary()
        elif choice==7:
            print("Thanku!! you have successfully exited")
            sys.exit()
        else:
            print("Sorry!! Not a valid choice")



def register():
    mycursor.execute("create table vikaslimited(empid int primary key,empname varchar(20),\
                    empage int,empdept varchar(20),\
                    empsalary int)")
    empid = int(input("enter your employee ID"))
    empname = input("enter your name:")
    empage = int(input("enter your age:"))
    empdept = input("enter department you want to join : ")
    empsalary =int(input("enter your salary:"))
    insertemp = "insert into VikasLimited values({},'{}','{}','{}',{})".format(empid,empname,empage,empdept,empsalary)
    mycursor.execute(insertemp)
    conn.commit()
    print("congrats!!! you have joined successfully")


def details():
    mycursor.execute("select * from VikasLimited")
    results = mycursor.fetchall()
    conn.commit()
    for x in results:
        print(x)


def em_salary():
    nam = input("enter your name")
    mycursor.execute("update VikasLimited set empsalary=empsalary+empsalary*10/100 where empname='{}'".format(nam))
    print(f"{nam} your salary updated successfully")
    details()
    conn.commit()


def em_list():
        mycursor.execute("select empname from VikasLimited order by empname asc")
        list_ = mycursor.fetchall()
        try:
                for x in list_:
                    print(x)
                a = mycursor.rowcount()
                print("total employees are", a)
        except:
            print("unable to show the list")


def em_count():
    mycursor.execute("select count(distinct empname) from VikasLimited")
    count = mycursor.fetchall()
    for x in count:
        print("    number of employees : ", x)
    conn.commit()


def salary():
    nam = input("enter your name :")
    a = mycursor.execute("select empsalary from VikasLimited where empname='{}'".format(nam))
    mycursor.execute(a)
    salary = mycursor.fetchall()
    for x in salary:
        print(x, "is your current salary", nam)
    conn.commit()


user_id = input("enter USER ID :")
pwd = int(input("enter the password :"))
if user_id == 'vikas' and pwd == 1234:
        print("welcome to EMPLOYEE MANAGEMENT SYSTEM ")
        menu()
else:
        print("invalid user id and password")
        sys.exit()


