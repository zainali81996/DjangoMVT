import re
from django.shortcuts import render, redirect,HttpResponse
from feedback.models import feedbackModel
from .forms import feedbackForm

def feedbackView(request):
    queryset=[]    
    pageForm=feedbackForm()
    if (request.method=="POST"):
        f = feedbackForm(request.POST)
        if f.is_valid():
            f.save()
        

    queryset =feedbackModel.objects.all()
    
    return render(request,'feedback.html',{"feedbacks":queryset,"feedbackForm":feedbackForm})
