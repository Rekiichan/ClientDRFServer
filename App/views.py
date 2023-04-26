import shutil
import os 
from os.path import exists

from rest_framework import status
from rest_framework.parsers import MultiPartParser
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


from django.core.files.storage import FileSystemStorage
from django.http import FileResponse

# from .serializers import ItemSerializer
from .serializers import FileUploadSerializer

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class FileUploadView(APIView):
    parser_classes = (MultiPartParser ,)
    def post(self, request):
        serializer = FileUploadSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data['file']
            # Handle the file upload here

            # get file param .h5 with key = 'file' sent from center 
            file_param = request.FILES['file']
            print("==============================")
            # use this for save that file param .h5
            fs = FileSystemStorage()

            # path of file param .h5 in module AI
            file_param_path = BASE_DIR.joinpath('module_ai/wpod-net.h5')

            # path of file that will saved in
            src_file_path = BASE_DIR.joinpath('wpod-net.h5')

            # path of file that will be moved in to module AI
            module_path = BASE_DIR.joinpath('module_ai')

            # check that file param h5 has already been in module ai, delete that if exist
            if exists(file_param_path):
                os.remove(file_param_path)

            # save file .h5 in src_path
            fs.save(file_param.name, file_param)
            
            # move that file to file_param_path
            shutil.move(src_file_path, module_path)

            # TODO apply file .h5 and train that then response file param .h5 back to center
            # TODO train process()

            file_response = FileResponse(open(file_param_path), 'rb')

            response = FileResponse(file_response)
            try :
                return response
            except ValueError:
                print(ValueError)
                return Response(response)

            # return Response({'status': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# ======================= AUTHEN REGION ======================= # 

def login_view(request):
    context = {
        "login_view": "active"
    }
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return HttpResponse("invalid credentials")
    return render(request, "authen/login.html", context)

def logout_view(request):
  logout(request)
  return redirect("/")

# ======================= HOME ======================= # 
def home(request):
    return render(request, 'base.html')

