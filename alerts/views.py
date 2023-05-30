from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from alerts.models import Alert
from alerts.serializers import AlertSerializer, AlertListSerializer
from alerts.models import AlertStatus
from alerts.mypagination import MyLimitOffsetPagination
from brine.constants import ID, PRICE, USERNAME
from brine.constants import ERROR

from brine.constants import MESSAGE
from users.models import User
import redis
import json
            

class Redis:
    redisClient = redis.StrictRedis(host='localhost', port=6379, db=0)

    @classmethod
    def get_data(cls, key): 
        alerts_data = json.loads(Redis.redisClient.get(key))
        return alerts_data    
   
class AlertList(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            payload = request.data
            
            limit = payload.get("limit", 10)
            offset = payload.get("offset", 0)
            if offset<0:
                return Response({ MESSAGE: "Offset should be a positive number" }, status=status.HTTP_400_BAD_REQUEST)    
            elif limit<0: 
                return Response({ MESSAGE: "Limit should be a positive number" }, status=status.HTTP_400_BAD_REQUEST)    
            
            if payload.get("status", False):
                filter_status = payload.get("status", False)
                alerts = Alert.objects.select_related("status").filter(status__status = filter_status)[offset:offset+limit]
            else:
                alerts = Alert.objects.all()[offset:offset+limit]
            serializer = AlertListSerializer(alerts, many = True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({ MESSAGE: ERROR }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AlertView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            alert = Alert.objects.get(id=id)
            serializer = AlertSerializer(alert, many = False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({ MESSAGE: ERROR }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request):
        try:
            alert = Alert.objects.get(id = request.data.get(ID))
            serializer = AlertSerializer(instance=alert, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                data = { MESSAGE: "Alert updated successfully" }
                return Response(data, status=status.HTTP_200_OK)
            else:
                return Response({ MESSAGE: ERROR }, status=status.HTTP_400_BAD_REQUEST)
            
        except Exception as e:
            return Response({ MESSAGE: ERROR }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            payload = request.data
            price = payload.get(PRICE)
            username = request.user.username
            email = request.user.email
            user = User.objects.get(username = username)
            alert_status = AlertStatus.objects.get(status = "Created")
            Alert.objects.create(created_by = user, price=price, status=alert_status)
            
            # payload.update({"user":user,"status":aler_status })
            # AlertSerializer.create(data=payload)
            if not request.session.get('alerts', False):
                request.session['alerts'] = []
            else:
                request.session['alerts'].append(price)
            
            # price = str(price)
            user_key = username +"~"+ email
            if Redis.redisClient.exists("alerts"):
                alerts_data = Redis.get_data("alerts")
                print(alerts_data)
                if price in alerts_data.keys():
                    users_list = alerts_data.get(price)
                    if username not in users_list:
                        users_list.append( user_key )
                        alerts_data.update({ price : users_list })
                        Redis.redisClient.set("alerts", json.dumps(alerts_data))
                    else:
                        data = { MESSAGE: "Alert already exists for the price {}".format(price) }
                        return Response(data, status=status.HTTP_201_CREATED)
                else:
                    alerts_data.update({ price : [ user_key ] })
                    Redis.redisClient.set("alerts", json.dumps(alerts_data))
                    
            else:
                alerts_data = { price : [ user_key  ] }
                Redis.redisClient.set("alerts", json.dumps(alerts_data))
           
            data = { MESSAGE: "Alert Created Successfully" }
            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as e:
            print(e)
            return Response({ MESSAGE: e }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



    def delete(self, request, id):
        try:
            task = Alert.objects.get(id = id)
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
            
        except Exception as e:
            return Response({ MESSAGE: ERROR }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
