"""blog_api URL Configuration

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
from django.views.generic import TemplateView
import articles
import comments
import products
import blog
from articles import views
from comments import views
from products import views
from blog import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('social-auth/', include('social_django.urls', namespace='social-media')),
    path('articles_list/', articles.views.ArticlesListView.as_view(),
         name="articles list"),
    path('entry/', blog.views.EntryView.as_view(), name="entry"),
    path('entry_list/', blog.views.EntryListView.as_view(), name="entry list"),
    path('comments_list/', comments.views.CommentsListView.as_view(),
         name="comments list"),
    path('add_comment/<int:article_id>/',
         comments.views.CommentsAddView.as_view(), name="comment add"),
    path('article_add/', articles.views.ArticleAddView.as_view(), name="article add"),
    path('article_detail/<int:article_id>/comments/',
         articles.views.ArticleDetailView.as_view(), name="article detail"),
    path('articles_search/', articles.views.ArticleSearchView.as_view(),
         name="search_article"),
    path('add_product_to_cart/',
         products.views.AddProductToCartView.as_view(), name="add product"),
    path('create_profile/', blog.views.CreateProfileView.as_view(),
         name="create profile"),
    path('products_list/', products.views.ProductListView.as_view(),
         name="products list"),
    path('cart_display/<int:pk>',
         products.views.CartDisplayView.as_view(), name="cart display"),
    path('change_quantity/<int:product_id>',
         products.views.ChangeQuantity.as_view(), name="change quantity"),
    path('confirm_order/', products.views.ConfirmOrderView.as_view(),
         name="confirm order"),

]
