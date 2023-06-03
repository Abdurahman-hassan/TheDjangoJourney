from django.core.validators import MinLengthValidator
from django.db import models


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"

    class Meta:
        verbose_name_plural = "tags"


class Author(models.Model):
    # parent one -> many with Post
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField(max_length=80)

    class Meta:
        verbose_name_plural = "Author's"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    # child one -> many with author
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    # image_name = models.CharField(max_length=250)
    image = models.ImageField(upload_to="posts", null=True)
    date = models.DateField(max_length=250, auto_now=True)
    # db_index always true with SlugField
    slug = models.SlugField(unique=True, db_index=True, max_length=200)
    content = models.TextField(max_length=7000, validators=[MinLengthValidator(10)])
    #     models.SET_NULL -> if I deleted the auther -> keep the posts of this auther
    #     and don't delete it, I should set null = True
    author = models.ForeignKey(Author, models.CASCADE, related_name='post_auther')
    tag = models.ManyToManyField(Tag, related_name='post_tag')

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    email_field = models.EmailField()
    text_comment = models.TextField(max_length=4000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return f"{self.user_name}"
