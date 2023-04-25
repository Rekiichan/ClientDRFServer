import shutil
import os
from pathlib import Path
from os.path import exists
from django.core.files.storage import FileSystemStorage
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework import status
from django.http import FileResponse

from .models import Item
from .serializers import ItemSerializer

BASE_DIR = Path(__file__).resolve().parent.parent



@api_view(["POST"])
def getParamsFile(request):
    # get file param .h5 with key = 'file' sent from center 
    file_param = request.FILES['file']

    # use this for save that file param .h5
    fs = FileSystemStorage()

    # path of file param .h5 in module AI
    file_param_path = BASE_DIR.joinpath('module_ai/wpod-net.h5')

    # path of file that will saved in
    src_path = BASE_DIR.joinpath('wpod-net.h5')

    # path of file that will be moved in to module AI
    module_path = BASE_DIR.joinpath('module_ai')

    # check that file param h5 has already been in module ai, delete that if exist
    if exists(file_param_path):
        os.remove(file_param_path)

    # save file .h5 in src_path
    fs.save(file_param.name, file_param)
    
    # move that file to file_param_path
    shutil.move(src_path, module_path)

    # TODO apply file .h5 and train that then response file param .h5 back to center
    # TODO train process()
    file_response = FileResponse(open(file_param_path), 'rb')

    response = FileResponse(file_response)

    return response
    


