from django.shortcuts import render
from distutils.sysconfig import get_python_lib
import os


# Create your views here.
def index(request):
    path = get_python_lib() + "/iconatron" + "/templatetags" + "/icons"
    svg_list = os.listdir(path)
    svg_new = []
    for file_name in svg_list:
        svg_new.append(file_name[0:-4])

    return render(request, 'index.html', {'svgs': svg_new})


