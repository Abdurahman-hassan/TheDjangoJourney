from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from django.views.generic import ListView
from coreblog.models import Post
from .forms import CommentForm
dict_months = {"Jeruary": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7,
               "August": 8, "September": 9, "October": 10,
               "November": 11, "December": 12}


# def home(request):
#     return HttpResponse("Hello World!")
#
#
# def months_by_number(request, month):
#     months = list(dict_months.keys())
#     if month > len(months):
#         return HttpResponseNotFound("Invalid Month")
#     redirect_month = months[month - 1]
#     redirect_month_path = reverse("month_str", args=[redirect_month])
#     return HttpResponseRedirect(redirect_month_path)
#
#
# def months(request, month):
#     try:
#         month_number = dict_months[month]
#         return HttpResponse(f"<h1>{month_number}</h1>")
#     except:
#         return HttpResponseNotFound("Invalid Month")


# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountin.jpeg",
#         "author": "Abdelrahman",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared "
#                    "for what happened whilst I was enjoying the view!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "programming.jpg",
#         "author": "Abdelrahman",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me "
#                    "yesterday...",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpeg",
#         "author": "Abdelrahman",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#
#           Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#           aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#           velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]


# def get_date(post):
#     # return post.get('date')
#     # or
#     return post['date']

# normal view
# def starting_page(request):
#     # sorted_post = all_posts.sort(key=get_date)
#     # or using the built-in fun to return a new list instead of sorted the same list
#
#     latest_post = Post.objects.all().order_by('-date')[:3]
#     # auther_firstName = Author.objects.get(post_auther__slug=slug)
#
#     # sorted_post = sorted(all_posts, key=get_date)
#     # latest_post = sorted_post[-3:]
#
#     return render(request, 'blog/index.html', {
#         "posts": latest_post,
#     })

# class base view (List view)

class StartingPageView(ListView):
    # sorted_post = all_posts.sort(key=get_date)
    # or using the built-in fun to return a new list instead of sorted the same list
    model = Post
    template_name = 'blog/index.html'
    ordering = ['-date', ]
    context_object_name = "posts"

    def get_queryset(self):
        query = super().get_queryset()
        data = query[:3]
        return data


# normal view
# def posts(request):
#     all_posts = Post.objects.all().order_by('-date')
#
#     return render(request, 'blog/all-posts.html', {
#         "all_posts": all_posts
#     })

# class base view (ListView)
class PostsView(ListView):
    model = Post
    template_name = "blog/all-posts.html"
    ordering = ['-date']
    context_object_name = 'all_posts'


# normal view
# def post_details(request, slug):
#     # slug_post = Post.objects.get(slug=slug)
#     # identified_post = next(po for po in all_posts if po['slug'] == slug)
#     identified_post = Post.objects.get(slug=slug)
#
#     return render(request, 'blog/post-detail.html', {
#         "post": identified_post,
#         "tags": identified_post.tag.all()
#
#     })


# class base view (Detail view)
class PostDetailsView(View):
    # model = Post
    # template_name = 'blog/post-detail.html'
    def is_stored_post(self, request, post_id):
        stored_posts = request.session.get('stored_posts')
        if stored_posts is not None:
            is_saved_for_later = post_id in stored_posts
        else:
            is_saved_for_later = False
        return is_saved_for_later

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)

        context = {
            "post": post,
            "tags": post.tag.all(),
            "comment_form": CommentForm(),
            "comments": post.comments.all().order_by("-id"),
            "saved_for_later": self.is_stored_post(request, post.id)
        }

        return render(request, 'blog/post-detail.html', context=context)

    def post(self, request, slug):
        comment_form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            # after making a post request and send the data
            # I redirect to the post details page and make a get request again in order to load the comments
            return HttpResponseRedirect(reverse('post-details-page', args=[slug]))
        context = {
            "post": post,
            "tags": post.tag.all(),
            "comment_form": comment_form,
            "comments": post.comments.all().order_by("-id")
        }
        return render(request, 'blog/post-detail.html', context=context)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['tags'] = self.object.tag.all()
    #     context['comment_form'] = CommentForm()
    #     return context


class ReadLaterView(View):

    def get(self, request):
        stored_posts = request.session.get("stored_posts")
        context = {}
        if stored_posts is None or len(stored_posts) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context['posts'] = posts
            context['has_posts'] = True
        return render(request, "blog/stored-posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST['post_id'])

        if post_id not in stored_posts:
            stored_posts.append(post_id)

        else:
            stored_posts.remove(post_id)

        request.session['stored_posts'] = stored_posts

        return HttpResponseRedirect("/")
