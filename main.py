import pymysql as pms
from tabulate import tabulate
from datetime import datetime

host= 'localhost'
port=3306
user='kjs'
psw='rlawnstn11'
charset='utf8'
db='musicapp'

connection=pms.connect(host=host,user=user,password=psw,database=db,port=port,charset=charset)

cursor=connection.cursor()

# try:
#     with connection.cursor() as cursor:
#         sql = "INSERT INTO administrator VALUES(1,'kjs','M')"
#         cursor.execute(sql)
#         result=cursor.fetchall()
#         print(result)
#         connection.commit()
# finally:
#     connection.close()

def EnrollMusic(id):
    #처음 음악 등록할 때는 들은 횟수와 들은 날짜는 없으므로 default값과 null 값으로 설정해준다. 
    sql='INSERT INTO music(adminID, MID, Mname, singer, AlbumID) VALUES (%s, %s, %s, %s, %s)'
    a=input('ID: ')
    b=input('title: ')
    c=input('singer: ')
    d=input('albumID: ')
    cursor.execute(sql,(id,a,b,c,d))
    connection.commit()
    sql='SELECT Mname FROM music WHERE MID= %s'
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "enrolled!")
    print()


def DeleteMusic():
    sql='SELECT Mname FROM music WHERE MID=%s'
    a=input("music ID to delete: ")
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "deleted!")
    connection.commit()

    sql='DELETE FROM music WHERE MID=%s'
    cursor.execute(sql,a)
    connection.commit()


def Managemusic(id):
    print()
    while True:
        print('0. Return to previous menu')
        print('1. Enroll music')
        print('2. Delete music')
        print('3. Show music list')
        x=int(input("Select option: "))
        if x==0:
            break
        elif x==1:
            EnrollMusic(id)
        elif x==2:
            DeleteMusic()
        elif x==3:
            sql="Select * from music"     #music table 출력
            cursor.execute(sql)
            result=cursor.fetchall()
            headers=['admin ID', 'Music ID', 'Music name', 'Singer', 'Album ID']
            print(tabulate(result,headers,tablefmt='grid'))
            connection.commit()
            

def RegisterUser(id):
    #adminID는 관리자 한 명이므로 그 ID를 받아와서 넣어줌, 유저 처음 등록할때는 구독 안된 상태이므로 sudStatus는 default값 'N'로 설정해주고, subName도 Null로 설정해줌
    sql="INSERT INTO user(adminID, UID,password,name,sex) VALUES(%s, %s, %s, %s, %s)"   
    a=input('ID: ')
    b=input('password: ')
    c=input('Name: ')
    d=input('Sex: ')
    # d=input('subStatus: ')
    # e=input('subName: ')

    cursor.execute(sql,(id,a,b,c,d))
    connection.commit()
    sql="SELECT name FROM user WHERE UID=%s"
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "register done")
    
    connection.commit()

def DeleteUser(id):
    
    sql='SELECT name FROM user WHERE UID=%s'
    a=input("user ID to delete: ")
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "deleted!")
    connection.commit()

    sql='DELETE FROM user WHERE UID=%s'
    cursor.execute(sql,a)
    connection.commit()


def ManageUser(id):
    print()
    while True:
        print()
        print('0. Return to previous menu')
        print('1. Register User')
        print('2. Delete User')
        print('3. Show user list')
        x=int(input("Select option: "))
        if x==0:
            break
        elif x==1:
            RegisterUser(id)
        elif x==2:
            DeleteUser(id)
        elif x==3:
            sql="Select * from user"
            cursor.execute(sql)
            result=cursor.fetchall()
            headers=['admin ID', 'User ID', 'User password','User name', 'Sex', 'subStatus', 'subName']
                
            print(tabulate(result,headers,tablefmt='grid'))
            print()
            connection.commit()
        else:
            print("Error: input correct number.")

def adminmenu():
    sql="SELECT ID FROM administrator"
    cursor.execute(sql)
    ID=cursor.fetchall()
    connection.commit()
    while True:
        print()
        print("Administrator mode!!")
        print('0. Return to previous menu')
        print('1. Manage music')
        print('2. Manage user')
        x=int(input("Select option: "))
        if x==0:
            break
        elif x==1:
            Managemusic(ID)
        elif x==2:
            ManageUser(ID)
        else:
            print("Error: input correct menu")

def Signup():
    sql="SELECT ID FROM administrator"
    cursor.execute(sql)
    ID=cursor.fetchall()
    connection.commit()
    sql="INSERT INTO user(adminID, UID,name,sex) VALUES(%s, %s, %s, %s)"
    a=input('ID: ')
    b=input('Name: ')
    c=input('Sex: ')
    # d=input('subStatus: ')
    # e=input('subName: ')

    cursor.execute(sql,(ID,a,b,c))
    connection.commit()
    sql="SELECT name FROM user WHERE UID=%s"
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "sign up completed!")
    
    connection.commit()
    print()

def ManagePlaylist():
    print("s")

def PlayMusic(id):
    global count
 
    while True:
        print("count: ",count)
        sql='SELECT MID,Mname from music WHERE MID=%s'
        a=input('Input music ID: ')
        cursor.execute(sql,a)
        connection.commit()
        rows=cursor.fetchall()

        if rows:
            
            #primary key가 중복일때(이미 들은 음악일 때), 들은 횟수와 들은 날짜 update해줌
            sql='INSERT INTO heard VALUES (%s,%s,%s,%s) ON DUPLICATE KEY UPDATE heardNum=heardNum+1, heardDate=%s'
            
            cursor.execute(sql,(id,a,count,datetime.now(),datetime.now()))
            MID = cursor.fetchall()
            for MID in rows:
                print("Playing ",MID[1])
            connection.commit()
            return
        else:
            print("There is no music!")

def Login():
    print("Login")

    sql='SELECT name,UID FROM user WHERE UID=%s and password=%s'
    a=input("ID: ")
    b=input("password: ")

    cursor.execute(sql,(a,b))
    rows = cursor.fetchall()
    
    for row in rows:
        name=row[0]
        id=row[1]
        print("log in completed!")
    if rows:
        while True:
            print()
            print(rows[0][0],"nice to meet you!")
            print('0. log out')
            print('1. Manage playlist')
            print('2. Show music list')
            print('3. Play Music ')
            print('4. Subscribe')

            x=int(input('select option: '))
            if x==0:
                break
            elif x==1:
                ManagePlaylist()
            elif x==2:
                sql="Select * from music"     #music table 출력
                cursor.execute(sql)
                result=cursor.fetchall()
                
                headers=['admin ID', 'Music ID', 'Music name', 'Singer', 'Album ID']
                print(tabulate(result,headers,tablefmt='grid'))
                connection.commit()
            elif x==3:
                PlayMusic(id)
    else:
        print("Error! Check your ID or password")

    connection.commit()

    
def usermenu():
    while True:
        print()
        print("User mode!!")
        print('0. Return to previous menu')
        print('1. Sign up')
        print('2. Log in')
        x=int(input("Select option: "))
        if x==0:
            break
        elif x==1:
            Signup()
        elif x==2:
            Login()
     

def main():
      
    while True:
        
        print()
        print('0. Exit')
        print('1. Administrator Menu')
        print('2. User Menu')
        x=int(input("Select menu:"))
        if x==0:
            exit(0)
        elif x==1:
            adminmenu()
        elif x==2:
            usermenu()
        else:
            print("Error: input correct menu")

count=1    #음악 들은 횟수
main()