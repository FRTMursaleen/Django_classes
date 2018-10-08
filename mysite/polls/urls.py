from . import views
from .views import SignUp,SignIn,HomeViewList

from django.conf.urls import url, include

app_name = 'polls'
urlpatterns = [
    url('about_us/', views.AboutUsView.as_view(), name='About_us'),
    url('accounts_data/(?P<pk>[0-9]+)/',views.AccountsData.as_view(), name='AccountsData'),
    url('postdata/', views.PostData.as_view(), name='postdata'),
    url('post_ser/', views.post_ser, name='post_ser'),
    url('se_post/(?P<pk>[0-9]+)/', views.post_data, name='se_post'),
    url('ser_post/(?P<pk>[0-9]+)/', views.PostdataSerializer.as_view(), name='ser_post'),
    url('show_post/', views.ShowPosts.as_view(),name='show_post'),
    url('edit_post/(?P<pk>[0-9]+)/', views.EditPostView.as_view(), name='edit_post'),
    url(r'^new_post/$', views.NewPostView.as_view(), name='new_post'),
    url('songs_enter/(?P<pk_id>[0-9]+)/',views.songs, name='songs_list'),
    url('songs/',views.Songs_data, name='songs_list'),
    url('edit/(?P<pk_id>[0-9]+)/',views.Edit_Data, name='edit'),
    url('Dr/',views.check,name='Dr'),
    url('sys/',views.CheckSerializer, name='sys'),
    url('serializer/',views.PostSerialize.as_view(), name='check'),
    url('show/', views.ArticleViews.as_view(), name='show'),
    url('delete_data/(?P<pk_id>[0-9]+)/',views.delete_data, name='delete'),
    url('books_list/', views.DataShow.as_view(),name='list'),
    url('delete_view/(?P<pk_id>[0-9]+)/',views.profiledelete, name='delete_profile'),
    url('list/', views.ProfileList.as_view(template_name='crud.html'), name='profile_list'),
    url('view/<int:pk>/',views.ProfileView.as_view(), name='profile_view'),
    url('create/',views.ProfileCreate.as_view(),name='profile_create'),
    url('delete/<int:pk>/',views.ProfileDelete.as_view(), name='profile_delate'),
    url('update/<int:pk>/',views.ProfileUpdate.as_view(),name='profile_update'),
    url('detail/',HomeViewList.as_view(template_name='home.html'),name='HomeDetail'),
    url('signin/', SignIn.as_view(template_name='signin.html'), name='signin'),
    url('bookschecker/', views.GetData.as_view(template_name='books.html'), name='books_list'),
    url('', SignUp.as_view(template_name='signup.html'), name='signup'),
]