from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import DetailView, ListView
from Blog_api.tasks import email_task

from Products.models import Cart, Product, CartProducts


class AddProductToCartView(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "Products/add_product.html", {"products": products})

    def post(self, request):
        cart, created = Cart.objects.get_or_create(client=request.user)
        product = Product.objects.get(id=request.POST.get("id_product"))
        cart.products.add(product)
        cart_products = Cart.objects.filter(client=request.user)
        return HttpResponse("")

class CartDisplayView(DetailView):
    model = Cart
    fields = "__all__"
    template_name = "Products/cart_display.html"

    def get_context_data(self, **kwargs):
        total_products = CartProducts.objects.filter(cart=self.object.client.cart.id)
        total_price = sum([product_cart.product.price * product_cart.quantity for product_cart in total_products])
        context=super().get_context_data(**kwargs)
        context["total_price"]=total_price
        return context

    def get_object(self, queryset=None):
        self.object, created = self.model.objects.get_or_create(client=self.request.user)
        return self.object

class ChangeQuantity(View):
    def post(self, request, product_id):
        cart,created = Cart.objects.get_or_create(client=request.user)
        product = Product.objects.get(pk=product_id)
        kp = CartProducts.objects.get(cart=cart, product=product)
        if request.POST.get('type') == '+':
            kp.quantity += 1
        elif request.POST.get("type") == "-":
            kp.quantity -= 1
        else:
            kp.quantity = 0
        kp.save()


        return redirect(f"/cart_display/{cart.pk}")

# Create your views here.
class ProductListView(ListView):
    model=Product
    paginate_by = 2
    template_name = "Products/products_list.html"

class ConfirmOrderView(View):
    def get(self,request):
        cart=Cart.objects.get(client=request.user.id)
        products_cart=CartProducts.objects.filter(cart=cart)
        total_price = sum([product_cart.product.price * product_cart.quantity for product_cart in products_cart])
        return render(request, "Products/order.html",{"products_cart":products_cart,
                                                            "total_price":total_price})
    def post(self,request):
        email=request.user.email
        total_price = request.POST.get("totalprice")
        email_task.delay(total_price,email)
        return HttpResponse(status=202)



