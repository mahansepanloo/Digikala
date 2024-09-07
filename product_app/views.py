from rest_framework import generics
from .models import Product, Category, Comment, Rate
from .serializers import ProductSerializer, CategorySerializer, CommentSerializer, RateSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class RateListCreateView(generics.ListCreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]


class RateDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer
    permission_classes = [IsAuthenticated]








# def list_product(request):
#     products = Product.objects.all()
#     my_product_list = []
#     for item in products:
#             ticket_dictionary = {
#                 "name": item.name,
#                 "price": item.price,
#                 "category": item.category.name,
#                 "seller": item.seller.username,
#                 "stock": item.stock,
#             }
#             my_product_list.append(ticket_dictionary)
#     return JsonResponse(my_product_list, safe=False)
#
# def category(request,category):
#     products = Product.objects.filter(category__name=category)
#     my_product_list = []
#     if products.exists():
#         for item in products:
#             ticket_dictionary = {
#                 "name": item.name,
#                 "price": item.price,
#                 "category": item.category.name,
#                 "seller": item.seller.username,
#                 "stock": item.stock,
#                 }
#             my_product_list.append(ticket_dictionary)
#     return JsonResponse(my_product_list, safe=False)
#
#
#
#
# def buy(request, name):
#     try:
#         products = Product.objects.get( name=name)
#         comments = Comment.objects.filter(product=products)
#         rate = Rate.objects.filter(product=products).count()
#
#
#         if rate > 0:
#             total_rating = round(products.total_rate() / rate, 2)
#         else:
#             total_rating = "-"
#
#
#         ticket_dictionary = {
#             "name": products.name,
#             "price": products.price,
#             "category": products.category.name,
#             "seller": products.seller.username,
#             "stock": products.stock,
#             "description": products.description,
#             'total_rating': total_rating,
#             'comments': [comment.comment_text for comment in comments],
#         }
#
#         return JsonResponse(ticket_dictionary, safe=False)
#     except Product.DoesNotExist:
#         return JsonResponse({})
#
#
#
# def seller(request,name):
#     products = Product.objects.filter(seller__username=name)
#     my_product_list = []
#     if products.exists():
#         for item in products:
#             ticket_dictionary = {
#                 "title": item.name,
#                 "source": item.price,
#                 "destination": item.description
#             }
#             my_product_list.append(ticket_dictionary)
#     return JsonResponse(my_product_list, safe=False)
#
# @csrf_exempt
# def add_product(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             name = data['name']
#             description = data['description']
#             seller_id = data['seller_id']
#             code = data['code']
#             price = data['price']
#             stock = data['stock']
#             category_id = data['category_id']
#
#             if Product.objects.filter(code=code).exists():
#                 return JsonResponse({"message": "Product code already exists"}, status=400)
#
#             seller = Seller.objects.get(id=seller_id)
#             category = Category.objects.get(id=category_id)
#
#             new_product = Product.objects.create(
#                 name=name,
#                 description=description,
#                 seller=seller,
#                 code=code,
#                 price=price,
#                 stock=stock,
#                 category=category
#             )
#             new_product.save()
#             return JsonResponse({"message": "Product added successfully"})
#         except Seller.DoesNotExist:
#             return JsonResponse({'error': 'Seller not found'})
#         except Category.DoesNotExist:
#             return JsonResponse({'error': 'Category not found'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
#
# @csrf_exempt
# def add_comment(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             comment_text = data['comment_text']
#             buyer_id = data['buyer_id']
#             product_id = data['product_id']
#             buyer = Costumer.objects.get(id = buyer_id)
#             product = Product.objects.get(id = product_id)
#             new_comment = Comment.objects.create(
#                 comment_text= comment_text,
#                 buyer= buyer,
#                 product = product)
#             new_comment.save()
#             return JsonResponse({"message": "Comment added successfully"})
#         except Costumer.DoesNotExist:
#             return JsonResponse({'error': 'Buyer not found'})
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
#
# @csrf_exempt
# def add_rate(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             rating = data['rating']
#             rater_id = data['rater_id']
#             product_id = data['product_id']
#
#             if rating is None or not (1 <= rating <= 5):
#                 return JsonResponse({'error': 'Rating must be between 1 and 5'})
#             rater = Costumer.objects.get(id=rater_id)
#             product = Product.objects.get(id=product_id)
#             new_rate = Rate.objects.create(
#                 rating=rating,
#                 rater=rater,
#                 product=product
#             )
#             new_rate.save()
#             return JsonResponse({"message": "Rating added successfully"})
#         except Costumer.DoesNotExist:
#             return JsonResponse({'error': 'Rater not found'})
#         except Product.DoesNotExist:
#             return JsonResponse({'error': 'Product not found'})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request meth
