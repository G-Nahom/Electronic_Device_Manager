from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def devicePage(requst):
    return HttpResponse("""<body style='background-color:lightblue'>
     <h1 style='text-align:center;color:green'>Home Page</h1>
    </body>""")