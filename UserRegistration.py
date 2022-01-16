import  mysql.connector as sql
import datetime as dt
conn=sql.connect(host='localhost',user='root',passwd='root',database='VikasLimitedCompany')
cur = conn.cursor()
cur.execute('create table user_registration_table(username varchar(25) primary key,password int not null )')
print('=========================WELCOME TO EMPLOYEE MANAGEMENT SYSTEM============================================================')
print(dt.datetime.now())
print('1.REGISTER')
print()
print('2.LOGIN')
print()

if __name__ == '__main__':
     n=int(input('enter your choice='))
     print()

     if n== 1:
          name=input('Enter a Username=')
          print()
          passwd=int(input('Enter a 4 DIGIT Password='))
          print()

          query="INSERT  INTO user_registration_table(username,password) values ('{}',{})".format(name,passwd);
          cur.execute(query)
          conn.commit()
          print()
          print(f"Congrats {name}!!!, you have successfully registered. Now you can login your account.")
          import MainMenu

     if  n==2 :
          name=input('Enter your Username=')
          print()
          passwd=int(input('Enter your 4 DIGIT Password='))
          query='select * from user_registration_table where password=passwd and username=name '
          cur.execute(query)
          if cur.fetchall() is  None:
               print()
               print('Invalid username or password')
          else:
               print()
               import MainMenu