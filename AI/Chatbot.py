from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, View
# *******************************************
# Chatbot Commands
# *******************************************

def ChatbotCommandRouter(command):
    response = {'status': 200, 'message': "Your error", 'url':reverse('Chatbot', kwargs={'speech':command})}
    return response