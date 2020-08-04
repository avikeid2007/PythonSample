import mysql.connector
class MySqlDataService:
    
    def __init__(self,userName,password):
        self.userName=userName
        self.password=password
        self.databaseName=""
   
    def createConnection(self):
        if not self.databaseName or self.databaseName.isspace():
            return mysql.connector.connect(host="localhost",user=self.userName,password=self.password)
        else:
            return mysql.connector.connect(host="localhost",user=self.userName,password=self.password,database=self.databaseName)
    
    #def getCursor(self):
    #    myDb = self.createConnection()
    #    cursor= myDb.cursor()
    #    return cursor

    def createDatabase(self):
        myDb = self.createConnection()
        myCursor = myDb.cursor()
        myCursor.execute("CREATE DATABASE IF NOT EXISTS pythonSample;")
        print("Database created.")
        self.databaseName="pythonsample"
        self.createTable()
       
    
    def createTable(self):
        myDb = self.createConnection()
        myCursor = myDb.cursor()
        myCursor.execute("CREATE TABLE IF NOT EXISTS Post(Id int AUTO_INCREMENT PRIMARY KEY,Title  VARCHAR(255) NOT NULL,Discription VARCHAR(15000),Author  VARCHAR(255),PublishDate  VARCHAR(50),Picture  VARCHAR(255))")
        print("tables created.")
     
    def savePost(self,title,discription,author,publishDate,picture):
        sql = "INSERT INTO Post (Title, Discription,Author,PublishDate,Picture) VALUES (%s, %s, %s, %s, %s)"
        val = (title, discription,author,publishDate,picture)
        myDb = self.createConnection()
        myCursor = myDb.cursor()
        myCursor.execute(sql,val);
        myDb.commit()
        print("post saved.")

    def getAllPost(self):
        sql = "select * from post"
        myDb = self.createConnection()
        myCursor = myDb.cursor()
        myCursor.execute(sql);
        return myCursor.fetchall()

    def getPost(self,id):
        sql = "select * from post where id="+id
        myDb = self.createConnection()
        myCursor = myDb.cursor()
        myCursor.execute(sql);
        return myCursor.fetchall()

    def deletePost(self,id):
        sql = "delete from post where id="+id
        myDb = self.createConnection()
        myCursor = myDb.cursor()
        myCursor.execute(sql);
        mydb.commit()
        print("post deleted.")
