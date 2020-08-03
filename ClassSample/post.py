import datetime
class post:
    Id = 0
    Title = ""
    Discription = ""
    Author = ""
    PublishDate = datetime.datetime.now
    Picture = ""
    def __init__(self,Title,Discription,Author,PublishDate,Picture):
        self.Title = Title
        self.Author = Author
        self.Discription = Discription
        self.Picture = Picture
        self.PublishDate = PublishDate

    

    


    


