from django.db import models
from django.db import models



# class Reader(models.Model): 
#     comment_count = models.IntegerField(default=0)
#     comments = models.TextField(null=True,blank=True)

#     def __str__(self):
#             return self.post

# class Author(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     full_name=models.CharField(max_length=200)
#     about_author=models.TextField()
# #     profile_picture = models.ImageField()

# #     def __str__(self):
# #         return self.user.username

# class Blogpost(models.Model):
#     # # author = models.ForeignKey(Author,on_delete=models.CASCADE)
#     # title = models.CharField(max_length=200)
#     # post = models.TextField()
#     # timestamp = models.DateTimeField(auto_now_add=True)
#     # image = models.ImageField(upload_to='blog_image')

#     # def __str__(self):
#     #     return self.title

class Advertising(models.Model):
    title = models.CharField(max_length=200)
    detail =models.TextField(blank = True)
    website= models.URLField(max_length=200 , blank=True , null=True) 
    image = models.ImageField(upload_to='blog_image')

    def __str__(self):
        return self.title


