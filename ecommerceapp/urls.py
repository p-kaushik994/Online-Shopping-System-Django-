from django.urls import path
from .views import home,signup,loginuser,headphones,profile,logout_view, add_to_cart, cart, speakers, earbuds, update_quantity,remove_from_cart,get_cart_count,printers,monitors,smartwatches,appliances,topdeals,decorationitems,fashiondeals,emptycart,order_summary,payment_page

app_name = 'cart'

urlpatterns = [
    path('', home, name='home'),
    path('signup', signup, name='signup'),
    path('login', loginuser, name='loginuser'),
    path('headphones', headphones, name='headphones'),
    path('profile', profile, name='profile'),
    path('logout', logout_view, name='logout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name="add_to_cart"),
    path('cart', cart, name='cart'),
    path('speakers',speakers, name='speakers'),
    path('earbuds',earbuds,name='earbuds'),
    path('update-quantity/<int:item_id>/', update_quantity, name='update_quantity'),
    path('remove-from-cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('cart/count/',get_cart_count, name='cart_count'),
    path('printers', printers, name='printers'),
    path('smartwatches', smartwatches, name='smartwatches'),
    path('monitors', monitors, name='monitors'),
    path('appliances', appliances, name='appliances'),
    path('topdeals', topdeals, name='topdeals'),
    path('decorationitems', decorationitems, name='decorationitems'),
    path('fashiondeals', fashiondeals, name='fashiondeals'),
    path('emptycart',emptycart,name='emptycart'),
    path('order_summary', order_summary, name="order_summary"),
    path('payment', payment_page, name="payment"),
]