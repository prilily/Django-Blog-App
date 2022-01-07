from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
from django.views.generic import ListView,DetailView,CreateView,UpdateView, DeleteView

# Create your views here.

'''
to be used as http response
def home(request):
    return HttpResponse('<h1> Blog Home </h1>')

def about(request):
    return HttpResponse('<h1> About page </h1>')'''

# as render
# so the dict we are passing from our render will be accesible to the page that can be accessed
# via the key (i.e here context)
def home(request):
    context={
        'posts':Post.objects.all()
    }
    return render(request, 'blog/home.html',context)

class PostListView(ListView):
    model=Post
    template_name= 'blog/home.html'
    context_object_name= 'posts' # why?  in home template context is post i.e why
    # <app>/<model>_<view_type>.html  template naming convention for class view 
    ordering=['-date_posted']
    paginate_by=2
    
class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    model=Post
    fields=['title','content']

    def test_func(self):
        post=self.get_object()
        if(self.request.user == post.author):
            return True
        return False

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'blog/about.html')

class PostDeleteView(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    #user login + author
    model=Post
    success_url='/blog'
    def test_func(self):
        post=self.get_object()
        if(self.request.user == post.author):
            return True
        return False



'''blog/
diff in class vs function

in class we are setting variables, less code
in func render a function and expilicitly pass the information


to create new post,
same as detail but add fields too

then url also, 
spli
    path('post/new' ,PostCreateView.as_view(),name='post-create'),

then a new template
as post_form.html

now, when we submit it, we get integrity error as no author,
so author be cuurent lgged on user, 
so,
in views ovverride, form valid method
now, to secure it andallow only logged in user to make a new post

then redirect to home page
using getabsoluteurl method in models.py Post class itself
redirect to a paticular route
reverse will return the fullurl to that route as a string

so we will reverse and views will handle redirect
'''