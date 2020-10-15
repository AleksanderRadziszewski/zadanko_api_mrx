"""Blog_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
import Articles
import Comments
import Products
import Blog
from Articles import views
from Comments import views
from Products import views
from Blog import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('Articles.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
    path('articles_list/', Articles.views.ArticlesListView.as_view(),
         name="articles list"),
    path('entry/', Blog.views.EntryView.as_view(), name="entry"),
    path('entry_list/', Blog.views.EntryListView.as_view(), name="entry list"),
    path('comments_list/', Comments.views.CommentsListView.as_view(),
         name="comments list"),
    path('add_comment/<int:article_id>/',
         Comments.views.CommentsAddView.as_view(), name="comment add"),
    path('article_add/', Articles.views.ArticlesAddView.as_view(), name="article add"),
    path('articles/<int:article_id>/comments/',
         Articles.views.ArticleDetailView.as_view(), name="article detail"),
    path('articles/_search', Articles.views.SearchView.as_view(),
         name="search_article"),
    path('add_product_to_cart/',
         Products.views.AddProductToCartView.as_view(), name="add product"),
    path('create_profile/', Blog.views.CreateProfileView.as_view(),
         name="create profile"),
    path('products_list/', Products.views.ProductListView.as_view(),
         name="products list"),
    # path('logout/', Blog.views.LogOutView.as_view(), name='logout'),
    path('cart_display/<int:pk>',
         Products.views.CartDisplayView.as_view(), name="cart display"),
    path('change_quantity/<int:product_id>',
         Products.views.ChangeQuantity.as_view(), name="change quantity"),
    path('confirm_order/', Products.views.ConfirmOrderView.as_view(),
         name="confirm order"),

]
