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
    sql='INSERT INTO music(adminID, MID, Mname, singer) VALUES (%s, %s, %s, %s)'
    a=input('ID: ')
    b=input('title: ')
    c=input('singer: ')
    cursor.execute(sql,(id,a,b,c))
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
    
    #heard table에서 삭제
    sql = 'DELETE FROM heard WHERE MID=%s'
    cursor.execute(sql, a)

    #including 테이블에서 삭제
    sql = 'DELETE FROM including WHERE MID=%s'
    cursor.execute(sql, a)

    #music 테이블에서 삭제
    sql = 'DELETE FROM music WHERE MID=%s'
    cursor.execute(sql, a)

    #favorite 테이블에서 삭제
    sql = 'DELETE FROM favorite WHERE MID=%s'
    cursor.execute(sql, a)

    #search table에서 삭제
    sql='DELETE FROM search WHERE MID=%s'
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
            headers=['admin ID', 'Music ID', 'Music name', 'Singer']
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
     
    #user table에서 삭제
    sql='DELETE FROM user WHERE UID=%s'
    cursor.execute(sql,a)

    #heard table에서 삭제
    sql='DELETE FROM heard WHERE UID=%s'
    cursor.execute(sql,a)

    #including table에서 삭제
    sql='DELETE FROM including WHERE UID=%s'
    cursor.execute(sql,a)
    
    # favorite table에서 삭제
    sql='DELETE FROM favorite WHERE UID=%s'
    cursor.execute(sql,a)

    #playlist table에서 삭제

    sql='DELETE FROM playlist WHERE MgrID=%s'
    cursor.execute(sql,a)

    #search table에서 삭제
    sql='DELETE FROM search WHERE UID=%s'
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

def CreatePlaylist(id):

    sql='INSERT INTO playlist (Pname, MgrID, PID) VALUES (%s, %s, %s)'
    a=input("Input playlist name: ")
    b=input('Input playlist ID: ')
    cursor.execute(sql,(a,id,b))
    connection.commit()
    sql='SELECT Pname FROM playlist WHERE PID= %s'
    cursor.execute(sql,b)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "created!")
    print()

def DeletePlaylist(id):

    sql='SELECT Pname FROM playlist WHERE PID=%s'
    a=input("Playlist ID to delete: ")
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "deleted!")
    connection.commit()

    sql='DELETE FROM playlist WHERE PID=%s'
    cursor.execute(sql,a)
    connection.commit()

    sql='DELETE FROM including WHERE PID=%s'
    cursor.execute(sql,a)
    connection.commit()
    

def ShowMyPlayslist(id):

    sql="Select Pname from playlist WHERE MgrID=%s"     #music table 출력
    cursor.execute(sql,id)
    result=cursor.fetchall()
    headers=['Playlistname']
    print(tabulate(result,headers,tablefmt='grid'))
    connection.commit()

#플레이리스트 공유
def ShowAllPlaylist(id):
    sql="Select playlist.Pname, user.name,playlist.PID from user,playlist WHERE user.UID=playlist.MgrID"
         #music table 출력
    cursor.execute(sql)
    result=cursor.fetchall()
    headers=['Playlistname','Owner name','Playlist ID']
    print(tabulate(result,headers,tablefmt='grid'))
    connection.commit()

def AddMusicToPlaylist(id):
    sql='INSERT INTO including VALUES (%s, %s, %s)'
    a=input('Music ID to add to playlist: ')
    b=input('Playlist Id: ')
    cursor.execute(sql,(id,a,b))
    connection.commit()
    sql='SELECT Mname FROM music WHERE MID= %s'
    cursor.execute(sql,a)
    rows = cursor.fetchall()
    for row in rows:
        print(row[0], "inserted!")
    print()

def DeleteMusicToPlaylist(id):
    sql='SELECT Mname FROM music WHERE MID=%s'
    a=input("Music ID to delete: ")
    b=input('Playlist ID to delete: ')
    cursor.execute(sql,a)
    rows = cursor.fetchall()

    for row in rows:
        print(row[0], "deleted!")
    connection.commit()

    #현재 로그인 한 user가 만든 플레이리스트에 한해서만 음악 삭제
    sql='DELETE FROM including WHERE UID=%s and MID=%s and PID=%s'
    cursor.execute(sql,(id,a,b))
    connection.commit()

def ShowMusicInPlaylist(id):
    sql='''SELECT music.Mname from music,including 
    WHERE including.UID=%s and including.PID=%s and music.MID=including.MID'''
    a=input('Input Playlist ID to show music: ')
    cursor.execute(sql,(id,a))
    result=cursor.fetchall()
    headers=['Music name']
    print(tabulate(result,headers,tablefmt='grid'))
    connection.commit()

def ManagePlaylist(id):
    while True:

        print()
        print('0. Return to previous menu')
        print('1. Create playlist')
        print('2. Delete playlist')
        print('3. Show my playlists')
        print('4. Show all playlists')
        print('5. Add music to playlist')
        print('6. Delete music from playlist')
        print('7. Show Music in Playlist')
        a=int(input('select option: '))
        if a==0:
            return
        elif a==1:
            CreatePlaylist(id)
        elif a==2:
            DeletePlaylist(id)
        elif a==3:
            ShowMyPlayslist(id)
        elif a==4:
            ShowAllPlaylist(id)
        elif a==5:
            AddMusicToPlaylist(id)
        elif a==6:
            DeleteMusicToPlaylist(id)
        elif a==7:
            ShowMusicInPlaylist(id)
        else:
            print("Error: input correct option")

def PlayMusic(id):
    global count
 
    while True:
        sql='SELECT MID,Mname from music WHERE MID=%s'
        a=input('Input music ID: ')
        cursor.execute(sql,a)
        connection.commit()
        rows=cursor.fetchall()

        if rows:
            #primary key가 중복일때(이미 들은 음악일 때), 들은 횟수와 들은 날짜 update해줌
            sql='''INSERT INTO heard VALUES (%s,%s,%s,%s) 
            ON DUPLICATE KEY UPDATE heardNum=heardNum+1, heardDate=%s'''
            
            cursor.execute(sql,(id,a,count,datetime.now(),datetime.now()))
            MID = cursor.fetchall()
            for MID in rows:
                print("Playing ",MID[1])
            connection.commit()
            return
        else:
            print("There is no music!")

def ShowRecentlyListenMusic(id):
    sql='''SELECT music.Mname,music.singer,heard.heardDate from heard,music
     WHERE UID=%s and music.MID=heard.MID ORDER BY heardDate DESC LIMIT 3'''
    cursor.execute(sql,id)
    result=cursor.fetchall()
    headers=['Music name', 'Singer','Heard Date']
    print(tabulate(result,headers,tablefmt='grid'))

    connection.commit()

def ShowMostHeardMusic(id):
    sql='SELECT music.MID,music.Mname,music.singer,heard.heardNum FROM heard,music WHERE heardNum=(SELECT MAX(heardNum) FROM heard WHERE UID=%s) and music.MID=heard.MID and UID=%s'
    cursor.execute(sql,(id,id))
    result=cursor.fetchall()
    headers=['Music ID','Music name', 'Singer','Heard number']
    print(tabulate(result,headers,tablefmt='grid'))

    connection.commit()
    
def SearchMusic(id):
    sql='SELECT MID,Mname,singer FROM music WHERE Mname=%s'
    print('Search music by name')
    name=input('Input Music name: ')
    cursor.execute(sql,name)
    result=cursor.fetchall()
    tmp=result[0][0]
    headers=['Music ID', 'Music name', 'Singer']
    print(tabulate(result,headers,tablefmt='grid'))
    sql='INSERT INTO search VALUES (%s, %s)'
    cursor.execute(sql,(id,tmp))
    connection.commit()

#좋아요 표시를 한 음악 모아두는 table
def LikeMusic(id):
    sql_check_music='SELECT Mname FROM music WHERE MID=%s'
    a=input('Input Music ID to like: ')
    cursor.execute(sql_check_music,a)
    
    music=cursor.fetchone()
    if not music:
        print("Invalid music ID. Enter a valid ID")
        return

    sql_check_like = 'SELECT * FROM favorite WHERE UID = %s AND MID = %s'
    cursor.execute(sql_check_like, (id, a))
    already_liked = cursor.fetchone()

    if already_liked:
        print("You already liked the music:",music[0])
        return

    sql='INSERT INTO favorite (UID,MID) VALUES (%s, %s)'
    cursor.execute(sql,(id,a))
    connection.commit()
    print("Successfully liked the music:",music[0])
    
    connection.commit()

def ShowLikedMusic(id):
    sql='''SELECT music.Mname,music.singer from favorite,music
     WHERE UID=%s and music.MID=favorite.MID'''
    cursor.execute(sql,id)
    result=cursor.fetchall()
    headers=['Music name', 'Singer']
    print(tabulate(result,headers,tablefmt='grid'))

    connection.commit()

#구독을 시작하면 user table의 구독상태와 구독권의 이름이 update 됨
def Subscription(id):
    sql='SELECT * from membership'
    cursor.execute(sql)
    result=cursor.fetchall()
    sname=result[0][0]
    connection.commit()
    sql='UPDATE user SET subStatus=%s, subName=%s WHERE UID=%s'
    cursor.execute(sql,('Y',sname,id))
    print("Subcription complete of",sname,"memebership")
    connection.commit()


def Signup():
    sql="SELECT ID FROM administrator"
    cursor.execute(sql)
    ID=cursor.fetchall()
    connection.commit()
    sql="INSERT INTO user(adminID, UID,password, name,sex) VALUES(%s, %s, %s, %s, %s)"
    a=input('ID: ')
    b=input('Password: ')
    c=input('Name: ')
    d=input('Sex: ')
    # d=input('subStatus: ')
    # e=input('subName: ')

    cursor.execute(sql,(ID,a,b,c,d))
    connection.commit()
    sql="SELECT name FROM user WHERE UID=%s"
    cursor.execute(sql,a)
    rows = cursor.fetchall()

    for row in rows:
        print(row[0], "sign up completed!")
    
    connection.commit()
    print()


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
            print('5. Show recently listen music list')
            print('6. Show mostly heard music')
            print('7. Search Music')
            print('8. Like music')
            print('9. Show Liked music list')
            
            x=int(input('select option: '))
            if x==0:
                break
            elif x==1:
                ManagePlaylist(id)
            elif x==2:
                sql="Select * from music"     #music table 출력
                cursor.execute(sql)
                result=cursor.fetchall()
                
                headers=['admin ID', 'Music ID', 'Music name', 'Singer']
                print(tabulate(result,headers,tablefmt='grid'))
                connection.commit()
            elif x==3:
                PlayMusic(id)
            elif x==4:
                Subscription(id)
            elif x==5:
                ShowRecentlyListenMusic(id)
            elif x==6:
                ShowMostHeardMusic(id)
            elif x==7:
                SearchMusic(id)
            elif x==8:
                LikeMusic(id)
            elif x==9:
                ShowLikedMusic(id)
            else:
                print("Error: Input correct option.")
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
        else:
            print("Error: Input correct option.")
     

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