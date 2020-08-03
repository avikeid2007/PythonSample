from post import post
import datetime
postObject=post(input("Enter post title"),input("Enter post dicription"),input("Enter post author name"),datetime.datetime.now,input("Enter post picture Url"))
print(postObject.Title)
print(postObject.Author)
print(postObject.PublishDate.strftime("%A"))
print(postObject.Discription)

