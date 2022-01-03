from rest_framework import serializers
from rest_framework.decorators import api_view
from .models import DeviceApi
from .serializers import DeviceApiSerializer
from rest_framework.response import Response
@api_view(['GET','POST'])
def DeviceApiView(request):
  if request.method == 'GET':
      deviceapidata= DeviceApi.objects.all()
      serializedata=DeviceApiSerializer(deviceapidata,many=True)
      return Response(serializedata.data)
  elif request.method == 'POST':
      deviceapipostdata=request.data
      serializeddata=DeviceApiSerializer(data=deviceapipostdata)
      if serializeddata.is_valid():
          serializeddata.save()
          return Response('Saved Successfully')
@api_view(['GET','PUT','DELETE'])
def ManipulateDeviceData(request,pk):
    if request.method == 'GET':
        try:
         deviceapidata= DeviceApi.objects.get(pk=pk)
         serializedata=DeviceApiSerializer(deviceapidata,many=False)
         return Response(serializedata.data)
        except:
            return Response('Data Does not exist',)
        
    elif request.method =='PUT':
        deviceapidata = DeviceApi.objects.get(pk=pk)
        serializedforupdate= DeviceApiSerializer(instance=deviceapidata,data=request.data)
        if serializedforupdate.is_valid():
            serializedforupdate.save()
            return Response('Record Updated Successfully..')
    elif request.method == 'DELETE':
        datatodelete=DeviceApi.objects.get(pk=pk)
        datatodelete.delete()
        return Response('Record Deleted Successfully')



