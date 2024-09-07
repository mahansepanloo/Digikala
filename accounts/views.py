from django.http.response import JsonResponse
from accounts.models import Costumer, Seller
import json
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CostumerSerializer, SellerSerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



class Login(TokenObtainPairView):
    pass

class Refresh(TokenRefreshView):
    pass





class CostumerListView(APIView):
    def get(self, request):
        costumers = Costumer.objects.all()
        serializer = CostumerSerializer(costumers, many=True)
        return Response(serializer.data)

class SellerListView(APIView):
    def get(self, request):
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

class FindCostumerByNameView(APIView):
    def get(self, request, input_name):
        costumers = Costumer.objects.filter(name=input_name)
        serializer = CostumerSerializer(costumers, many=True)
        return Response(serializer.data)

class FindSellerByNameView(APIView):
    def get(self, request, input_name):
        sellers = Seller.objects.filter(name=input_name)
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

class FindCostumerByUsernameView(APIView):
    def get(self, request, input_username):
        try:
            costumer = Costumer.objects.get(username=input_username)
            serializer = CostumerSerializer(costumer)
            return Response(serializer.data)
        except Costumer.DoesNotExist:
            return Response({'error': 'Costumer not found'}, status=status.HTTP_404_NOT_FOUND)

class FindSellerByUsernameView(APIView):
    def get(self, request, input_username):
        try:
            seller = Seller.objects.get(username=input_username)
            serializer = SellerSerializer(seller)
            return Response(serializer.data)
        except Seller.DoesNotExist:
            return Response({'error': 'Seller not found'}, status=status.HTTP_404_NOT_FOUND)

class AddSellerView(APIView):
    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            if Seller.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            elif Seller.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "Seller added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddCostumerView(APIView):
    def post(self, request):
        serializer = CostumerSerializer(data=request.data)
        if serializer.is_valid():
            if Costumer.objects.filter(email=serializer.validated_data['email']).exists():
                return Response({"message": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
            elif Costumer.objects.filter(username=serializer.validated_data['username']).exists():
                return Response({"message": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({"message": "Costumer added successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



























# def costumers_list_func(request):
#     costumers = Costumer.objects.all()
#     costumers_list = []
#     for costumer in costumers:
#         costumer_dict = {
#             'name' : costumer.name,
#             'city' : costumer.city,
#             'username' : costumer.username
#         }
#         costumers_list.append(costumer_dict)
#
#     return JsonResponse(costumers_list, safe=False)
#
# def sellers_list_func(request):
#     sellers = Seller.objects.all()
#     sellers_list = []
#     for seller in sellers:
#         seller_dict = {
#             'name' : seller.name,
#             'city' : seller.city,
#             'username' : seller.username
#         }
#         sellers_list.append(seller_dict)
#
#     return JsonResponse(sellers_list, safe=False)
#
# def find_costumers_by_name(request, input_name):
#     costumers = Costumer.objects.filter(name = input_name)
#     costumers_list = []
#     for costumer in costumers:
#         costumer_dict = {
#             'name' : costumer.name,
#             'city' : costumer.city,
#             'username' : costumer.username
#         }
#         costumers_list.append(costumer_dict)
#
#     return JsonResponse(costumers_list, safe=False)
#
# def find_sellers_by_name(request, input_name):
#     sellers = Seller.objects.filter(name = input_name)
#     sellers_list = []
#     for seller in sellers:
#         seller_dict = {
#             'name' : seller.name,
#             'city' : seller.city,
#             'username' : seller.username
#         }
#         sellers_list.append(seller_dict)
#
#     return JsonResponse(sellers_list, safe=False)
#
# def find_costumers_by_username(request, input_username):
#     try:
#         costumer = Costumer.objects.get(username=input_username)
#         costumer_dict = {
#             'name': costumer.name,
#             'city': costumer.city,
#             'username': costumer.username
#         }
#         return JsonResponse(costumer_dict, safe=False)
#     except Costumer.DoesNotExist:
#         return JsonResponse({'error': 'Costumer not found'}, status=404)
#
# def find_sellers_by_username(request, input_username):
#     try:
#         seller = Seller.objects.get(username=input_username)
#         seller_dict = {
#             'name' : seller.name,
#             'city' : seller.city,
#             'username' : seller.username
#         }
#         return JsonResponse(seller_dict, safe=False)
#     except Seller.DoesNotExist:
#         return JsonResponse({'error' : 'seller not found'}, status=404)
#
# @csrf_exempt
# def add_seller(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         try:
#             name = data['name']
#             email = data['email']
#             city = data['city']
#             address = data['address']
#             password = data['password']
#             username = data['username']
#
#             if Seller.objects.filter(email = email).exists():
#                 return JsonResponse({"message": "Email already exists"})
#             elif Seller.objects.filter(username = username).exists():
#                 return JsonResponse({"message": "Username already exists"})
#             else:
#                 new_seller = Seller.objects.create(name= name ,
#                                       username=username,
#                                       password=password,
#                                       city=city,
#                                       address=address,
#                                       email=email)
#                 new_seller.save()
#                 return JsonResponse({"message": "Seller added successfully"})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
#
# @csrf_exempt
# def add_costumer(request):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         try:
#             name = data['name']
#             email = data['email']
#             city = data['city']
#             address = data['address']
#             password = data['password']
#             username = data['username']
#
#             if Costumer.objects.filter(email = email).exists():
#                 return JsonResponse({"message": "Email already exists"})
#             elif Costumer.objects.filter(username = username).exists():
#                 return JsonResponse({"message": "Username already exists"})
#             else:
#                 new_costumer = Costumer.objects.create(name= name ,
#                                       username=username,
#                                       password=password,
#                                       city=city,
#                                       address=address,
#                                       email=email)
#                 new_costumer.save()
#                 return JsonResponse({"message": "Costumer added successfully"})
#         except Exception as e:
#             return JsonResponse({'error': str(e)})
#     else:
#         return JsonResponse({'error': 'Invalid request method'})
#
#
#
