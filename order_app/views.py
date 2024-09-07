from rest_framework import generics
from .models import Discount, Order, OrderItem
from .serializers import DiscountSerializer, OrderSerializer, OrderItemSerializer
from rest_framework.permissions import IsAdminUser,IsAuthenticated

class DiscountListCreateView(generics.ListCreateAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]

class DiscountDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Discount.objects.all()
    serializer_class = DiscountSerializer
    permission_classes = [IsAuthenticated,IsAdminUser]


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Order.objects.filter(buyer = self.request.user.username)


class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderItemListCreateView(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        orders = Order.objects.filter(buyer = self.request.user.username)
        return OrderItem.objects.filter(order = orders)


class OrderItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]







# def order_list_func(request):
#     orders = Order.objects.all()
#     orders_list = []
#     for order in orders:
#         order : Order
#         order_dict = {
#             'buyer' : order.buyer.name,
#             'date' : order.date,
#             'code' : order.code,
#             'cart_code' : order.cart.code,
#             'bill' : order.bill
#         }
#         orders_list.append(order_dict)
#     return JsonResponse(orders_list,safe=False)
#
# def order_item_func(request):
#     order_items = Order_item.objects.all()
#     order_items_list = []
#     for order_item in order_items:
#         order_item : Order_item
#         order_item_dict = {
#             'order_code' : order_item.order.code,
#             'buyer' : order_item.order.buyer.name,
#             'seller' : order_item.seller.name,
#             'product' : order_item.product.name,
#             'bill' : order_item.price
#         }
#         order_items_list.append(order_item_dict)
#     return JsonResponse(order_items_list, safe=False)
#
# def order_by_buyer(request, buyer_name):
#     try:
#         orders = Order.objects.filter(buyer__name = buyer_name)
#         orders_list = []
#         for order in orders:
#             order : Order
#             order_dict = {
#                 'buyer' : order.buyer.name,
#                 'date' : order.date,
#                 'code' : order.code,
#                 'cart_code' : order.cart.code,
#                 'bill' : order.bill
#             }
#             orders_list.append(order_dict)
#         return JsonResponse(orders_list,safe=False)
#     except Order.DoesNotExist:
#         return JsonResponse({'error' : 'order not found'})
#
# def order_item_by_seller(request, seller_name):
#     try:
#         orders = Order_item.objects.filter(seller__name = seller_name)
#         orders_list = []
#         for order_item in orders:
#             order_item : Order_item
#             order_dict = {
#                 'order_code' : order_item.order.code,
#                 'buyer' : order_item.order.buyer.name,
#                 'seller' : order_item.seller.name,
#                 'product' : order_item.product.name,
#                 'bill' : order_item.price
#             }
#             orders_list.append(order_dict)
#         return JsonResponse(orders_list,safe=False)
#     except Order.DoesNotExist:
#         return JsonResponse({'error' : 'order not found'})
#
# def order_item_by_product(request, product_name):
#     order_items = Order_item.objects.filter(product__name = product_name)
#     order_items_list = []
#     for order_item in order_items:
#         order_item : Order_item
#         order_item_dict = {
#             'order_code' : order_item.order.code,
#             'buyer' : order_item.order.buyer.name,
#             'product' : order_item.product.name,
#             'bill' : order_item.price
#         }
#         order_items_list.append(order_item_dict)
#     return JsonResponse(order_items_list, safe=False)
#
# def order_by_code(request, code_input):
#     try:
#         order = Order.objects.get(code = code_input)
#         order_dict = {
#                 'buyer' : order.buyer.name,
#                 'date' : order.date,
#                 'code' : order.code,
#                 'cart_code' : order.cart.code,
#                 'bill' : order.bill
#             }
#         return JsonResponse(order_dict, safe=False)
#     except Order.DoesNotExist:
#         return JsonResponse({'error' : 'that order code does not exist'})
#
#
#
#
# def create_order_view(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#
#         buyer = Costumer.objects.get(name=data['buyer_name'])
#
#         cart = Cart.objects.get(code=data['cart_code'])
#
#         discount_code = Discount.objects.get(code=data['discount_code']) if 'discount_code' in data else None
#
#         order = Order.objects.create(
#             buyer=buyer,
#             cart=cart,
#             discount_code=discount_code,
#             bill=data.get('bill', 0.0),
#             code=data.get('code', None)
#         )
#
#         return JsonResponse({'message': 'Order created successfully', 'order_code': order.code})
#
#     return JsonResponse({'error': 'Invalid request method'})
#
#
# def delete_order_view(request, order_code):
#     if request.method == 'DELETE':
#         try:
#             order = Order.objects.get(code=order_code)
#             order.delete()
#             return JsonResponse({'message': 'Order deleted successfully'})
#         except Order.DoesNotExist:
#             return JsonResponse({'error': 'Order not found'})
#     return JsonResponse({'error': 'Invalid request method'})
#
#
#
