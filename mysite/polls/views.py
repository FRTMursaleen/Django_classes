from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from .serializer import PostSerilizer, SongsSerializer,PostSerializerData,TodoSerializer
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView, View, ListView, DetailView
from rest_framework.decorators import api_view, schema
# Create your views here.


class SignUp(FormView):
    template_name = 'signup.html'
    form_class = SignUpForm
    success_url = '/signup/signin/'
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = True
        print('Authentication of user', user.is_authenticated)
        user.save()
        return redirect('/signup/signin/')


class SignIn(FormView):
    template_name = 'signin.html'
    form_class = SignInForm
    success_url = '/signup/home/'
    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(self.request, user)
            return redirect('/signup/detail/')
        return render(self.request,self.template_name , {'form':self.form_class})


class HomeViewList(View):
    template_name = 'home.html'
    form_class = Profile
    success_url = '/signup/list/'

    def get(self,request, *args, **kwargs):
        return render(request, self.template_name, {'form':self.form_class,})

    def post(self, request, *args, **kwargs):
        form = self.form_class
        if form.is_valid:
            user_name = ''
            id = None
            data = Accounts.objects.filter()
            age = request.POST['age']
            age_ = int(age)
            name = request.POST['name']
            name_ = str(name)
            gender = request.POST['gender']
            gender_ = str(gender)
            print(form)
            print(name , age  , gender)
            if request.user.is_authenticated:
                user_name = request.user.username
                id = request.user.id
                print(user_name , id)
            data_save = Accounts(user_id = id, age = age_, name = name_, gender = gender_)
            data_save.save()
            return redirect('/signup/bookschecker/')
        return render(request, self.template_name, {'form':self.form_class})


class ProfileList(ListView):
    model = Accounts


class ProfileView(DetailView):
    model = Accounts
    success_url = '/signup/detail/'


class ProfileCreate(CreateView):
    model = Accounts
    fields = ['age', 'name', 'gender']
    success_url = '/signup/detail/'


class ProfileDelete(DeleteView):
    model = Accounts
    success_url = '/signup/detail/'


class ProfileUpdate(UpdateView):
    model = Accounts
    fields = ['age','name', 'gender']
    success_url = '/signup/detail'


def profiledelete(request, pk_id=None):
    id = int(pk_id)
    print(id)
    object = get_object_or_404(Accounts, id=id)
    form = Profile(request.POST or None, instance = object)
    print(object)
    if request.method == 'POST':
        if form.is_valid:
            instance = form.save(commit=False)
            instance.save()
            return redirect('/signup/list/')
        else:
            form = Profile(instance = object)
    return render(request,'home.html', {'form':form})


class GetData(FormView):
    template_name = 'books.html'
    form_class = BooksProfile

    def form_valid(self, form):
        print('okkkk')
        bookname = form.cleaned_data.get('bookname')
        print(bookname)
        form = self.form_class
        form.save()
        return super(GetData, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        id = None
        if self.form_class.is_valid:
            if request.GET.get('issuedate') is not None:
                issuedate = request.GET['issuedate']
                print(issuedate)
                bookname_ = request.GET['bookname']
                issue = datetime.strptime("{}".format(issuedate), '%m/%d/%Y %I:%M %p')
                bookname_ = str(bookname_)
                print(type(issuedate),  type(bookname_))
                print(issue, bookname_)
                if request.user.is_authenticated:
                    user_name = request.user.username
                    id = request.user.id
                    print(user_name, id)
                data_save = Books(user_id=id, book_name = bookname_, issue_date=issue)
                data_save.save()
                return redirect('/signup/books_list/')
        return render(request,'books.html', {'form':self.form_class})


class DataShow(ListView):
    template_name = 'bookslist.html'
    queryset = Books.objects.all()
    context_object_name = 'books'


def delete_data(request, pk_id=None):
    id = int(pk_id)
    instance = get_object_or_404(Books, id=id)
    print(instance)
    instance.delete()
    return redirect('/signup/books_list/')

def show(request):
    return render(request,'prac.html')


class ArticleViews(ListView):
    queryset = Accounts.objects.filter(name='Mursaleen')
    template_name = 'prac.html'
    paginate_by = 15
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

@api_view(['GET','POST'])
def CheckSerializer(request):
    if request.method == 'GET':
        queryset = Accounts.objects.all()
        serializer = PostSerilizer(queryset, many=True)
    return Response(serializer.data)

class PostSerialize(ListView):
    queryset = Accounts.objects.all()
    serializer_type = PostSerilizer


def check(request):
    return render(request,'Dr.html')


def Edit_Data(request,pk_id=None):
    pk = int(pk_id)
    instance = get_object_or_404(Accounts , pk=pk)
    print(instance)
    form = Profile(request.GET or None, instance=instance)
    if request.method == 'GET':
        if form.is_valid():
            instance = form.save()
            instance.save()
            return redirect('/signup/show/')
        else:
            form = Profile(request.POST or None, instance=instance)
    return render(request,'Dr.html', {'form':form})



class SongsList(CreateView):
    model = Songs
    serializer_type = SongsSerializer
    fields = ['title', 'artist']


@api_view(['GET'])
def Songs_data(request):
    if request.method == 'GET':
        queryset = Songs.objects.all()
        serializer = SongsSerializer(queryset, many=True)
        return Response({"message": "Got some data!", "data": serializer.data})


# def songs(request):
#     form = Songs_data_enter(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             instance = form.save()
#             instance.save()
#         return redirect('/signup/songs/')
#     return render(request, 'serialize.html',{'form':form})


@api_view(['POST'])
def songs(request,pk_id):
    id = int(pk_id)
    songs_data = Songs.objects.filter(id=pk_id)
    print(songs_data)
    title = request.Post.get('title')
    name = request.Post.name('artist')
    try:
        Songs.objects.create(title= title, artist = name)
        return Response("Data Saved!", status=status.HTTP_201_CREATED)
    except BaseException as ex:
        return Response(ex, status=status.HTTP_400_BAD_REQUEST)


class NewPostView(CreateView):
    model = Post
    form_class = PostForm
    success_url = "/signup/show_post/"
    template_name = "Post.html"


@method_decorator(login_required, name='dispatch')
class EditPostView(UpdateView):
    model = Post
    fields = ('message',)
    success_url = "/signup/show_post/"
    pk_url_kwarg = "pk"
    context_object_name = "Post"
    template_name = "edit.html"

    def form_valid(self, form):
        post = form.save()
        post.updated_by = self.request.user
        post.created_by = self.request.user
        post.save()
        return redirect('/signup/show_post/')


class ShowPosts(ListView):
    model = Post
    template_name = "show_Post.html"
    context_object_name = "Post"
    paginate_by = 2
    queryset = Post.objects.all().order_by('id')


class PostdataSerializer(APIView):
    serializer_class = PostSerializerData
    template_name = 'fine.html'
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        id = int(pk)
        queryset = Post.objects.filter(id = id)
        serializer = PostSerializerData(queryset, many=True)
        return Response(serializer.data)


    def post(self,request, pk):
        serializer = PostSerializerData(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def post_data(request, pk):
    id = pk
    serializer = PostSerializerData(request.data)
    queryset = Post.objects.filter(id=id)
    serializer = PostSerializerData(queryset, many=True)
    return Response(serializer.data)


@api_view(['POST','GET'])
def post_ser(request):
    serializer = PostSerializerData(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return render(request,'post_ser.html', {'serializer':serializer})


class PostData(APIView):
    serializer_class = PostSerializerData
    permission_classes = [IsAuthenticated, ]
    template_name = 'accounts_data.html'

    def get(self, request):
        queryset = Post.objects.all()[1:2]
        serilizer = PostSerializerData(queryset , many=True)
        return Response(serilizer.data)

    def post(self,request):
        serializer = PostSerializerData(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AccountsData(APIView):
    #use to show form on UI
    serializer_class = PostSerilizer
    template_name = 'accounts_data.html'
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        id = int(pk)
        queryset = Accounts.objects.filter(id = id)
        serializer = PostSerilizer(queryset, many=True)
        return Response(serializer.data)

    def post(self,request, pk):
        serializer = PostSerilizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class AboutUsView(TemplateView):
    template_name = 'about_us.html'

    def get_context_data(self, **kwargs):
        context = super(AboutUsView,self).get_context_data(**kwargs)
        context['open'] =Post.objects.all()[1:2]
        return context