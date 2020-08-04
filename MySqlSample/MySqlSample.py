#from post import post
from MySqlDataService import MySqlDataService
dataService=MySqlDataService("root","xavi@1234")
dataService.createDatabase()

print("Press 1 for show All posts \nPress 2 for show post \nPress 3 for add a new post \nPress 4 for delete a post \n Press 0 for Exit \n")
while True:
    choise = int(input("enter choise "))
    if choise == 0:
       exit()
    if choise == 1:
       result = dataService.getAllPost()
       for x in result:
           print(x)
    if choise == 2:
       result = dataService.getPost(int(input("Enter post id ")))
       for x in result:
          print(x)
    if choise == 3:
       dataService.savePost(input("Enter post title "),input("Enter post discription "),input("Enter post author name "),"22/02/2020",input("Enter post picture Url "))
    if choise == 4:
       dataService.deletePost(int(input("Enter post id ")))

