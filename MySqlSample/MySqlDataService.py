import mysql.connector
class MySqlDataService:
    
   
    def createConnection(self,userName,password):
        return mysql.connector.connect(host="localhost",user=userName,password=password)
    
    def createDatabase(self,userName,password):
        myDb=self.createConnection(userName,password)
        myCursor=myDb.cursor()
        myCursor.execute("CREATE DATABASE IF NOT EXISTS pythonSample;")
