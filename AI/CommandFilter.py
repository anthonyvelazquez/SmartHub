from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.urls import reverse
from django.http import HttpResponse
from django.views.generic import TemplateView, View
# *******************************************
# AI Setup Commands
# *******************************************
def AISetupCommandRouter(active, section, profile, command):
    # AI Setup is active
    if active:
        # AI Name Setup
        if section == 1:
            name = command
            response = {'status': 200, 'message': "Your error", 'url':reverse('AI_Setup_Name')}
            return response, name
        # AI Gender Setup
        elif section == 2:
            gender = command
            response = {'status': 200, 'message': "Your error", 'url':reverse('AI_Setup_Gender')}
            return response, gender
    else:
        found = False
        if any(command in command_list for command_list in AI_Name_Setup_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('AI_Setup_Name_Request')}
        elif any(command in command_list for command_list in AI_Gender_Setup_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('AI_Setup_Gender_Request')}
        else:
            response = {'status': 0, 'message': "Your error", 'url':reverse('Profile')}
        return found, response
# *******************************************
# Alarm Commands
# *******************************************
from AI.CommandPhrases import *
import AI.CommandPhrases
def AlarmCommandRouter(active, profile, command):
    # Alarm is currently on
    if active:
        if any(command in command_list for command_list in Alarm_Disable_Commands_List):
            print("Alarm Turned Off")
            response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Disable')}
        else:
            print("Alarm Active - Cant Run: " + command)
            response = {'status': 0, 'message': "Your error", 'url':reverse('Profile')} 
        return response
    # Alarm is off
    else:
        found = False
        # Setting Alarm Name
        if profile.alarm_creating_name:
            found = True
            print("Setting Alarm Name: " + command)
            response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Request_Set_Name', kwargs={'pk':AI.CommandPhrases.Alarm_PK, 'name':command})}
            return found, response
        # Setting Alarm Time
        elif profile.alarm_creating_time:
            found = True
            print("Setting Alarm Time: " + command)
            response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Request_Set_Time', kwargs={'pk':AI.CommandPhrases.Alarm_PK, 'time':command})}
            return found, response
        elif profile.alarm_creating_mode:
            found = True
            print("Setting Alarm Mode: " + command)
            response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Request_Set_Mode', kwargs={'pk':AI.CommandPhrases.Alarm_PK, 'mode':command})}
            return found, response
        # Deleting Specific Alarm
        elif profile.alarm_deleting_specific:
            found = True
            print("Deleting Specific Alarm Named:" + command)
            response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Delete_Specific', kwargs={'name':command})}
            return found, response
        else:
            # Asking to delete specific alarm
            if any(command in command_list for command_list in Specific_Alarm_Delete_Commands_List):
                found = True
                print("Requested Specific Alarm Deletion")
                response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Delete_Request_Name')}
            # Asking to delete all alarms
            elif any(command in command_list for command_list in Generic_Alarm_Delete_Commands_List):
                found = True
                print("Deleting All Alarms")
                response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Delete_All')}
            elif any(command in command_list for command_list in Generic_Alarm_Request_Commands_List):
                found = True
                print("Creating Alarm")
                profile.alarm_creating_name = True
                profile.save()
                response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Request')}
            else:
                response = ""
            for commands in Set_Alarm_Request_Commands_List:
                if commands in command:
                    found = True
                    response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Create_Specific', kwargs={'alarm':command})}
            for commands in Quick_Alarm_Request_Commands_List:
                if commands in command:
                    found = True
                    response = {'status': 200, 'message': "Your error", 'url':reverse('Alarm_Create_Quick', kwargs={'alarm':command})}
            return found, response
# *******************************************
# Sleep Commands
# *******************************************
def SleepCommandRouter(active, profile, command):
    # AI is in sleep mode
    if active:
        if any(command in command_list for command_list in Generic_Sleep_Disable_Commands_List):
            speech_response = "Hello. How can I help you?"
            profile.sleep_active = False
            profile.save()
            response = {'status': 200, 'message': "Your error", 'url':reverse('Dashboard')}
        else:
            print("Sleep Mode Active - Cant Run: " + command)
            speech_response = ""
            response = {'status': 0, 'message': "Your error", 'url':reverse('Profile')}
        return response, speech_response
    else:
        found = False
        if any(command in command_list for command_list in Generic_Sleep_Enable_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Sleep')}
        else:
            response = ""
        return found, response
# *******************************************
# Search Commands
# *******************************************
def SearchCommandRouter(active, profile, command):
    if active:
        speech_response = "This is what I found for. " + command
        profile.search_active = False
        profile.save()
        response = {'status': 200, 'message': "Your error", 'url':reverse('Search_Result')}
        return response, speech_response, command
    else:
        found = False
        if "can you look something up for me" in command or "search something for me" in command:
            found = True
            speech_response = "What do you want me to look up?"
            response = {'status': 200, 'message': "Your error", 'url':reverse('Search_Request')}
        else:
            speech_response = ""
            response = ""
        return found, response, speech_response
# *******************************************
# Reminder Commands
# *******************************************
def ReminderCommandRouter(creating, time, profile, command):
    if creating:
        if not time:
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Request_Time', kwargs={'name':command})}
            return response
        elif time:
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder', kwargs={'time':command})}
            return response
    else:
        found = False
        if any(command in command_list for command_list in Generic_Reminder_Request_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Request')}
        elif any(command in command_list for command_list in Generic_Reminder_Delete_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Delete_All')}
        elif any(command in command_list for command_list in Reminder_Me_Request_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Create_Specific', kwargs={'reminder':command})}
        elif "delete my first reminder" in command or "delete the first reminder" in command:
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Delete_First')}
        elif "delete my last reminder" in command or "delete the last reminder" in command:
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Delete_Last')}
        else:
            response = ""
        for commands in Quick_Reminder_Request_Commands_List:
                if commands in command:
                    found = True
                    response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Create_Quick', kwargs={'reminder':command})}
        for commands in Reminder_Me_Request_Commands_List:
                if commands in command:
                    found = True
                    response = {'status': 200, 'message': "Your error", 'url':reverse('Reminder_Create_Specific', kwargs={'reminder':command})}
        return found, response
# *******************************************
# Email Commands
# *******************************************
def EmailCommandRouter(active, unread, profile, command):
    if active and unread:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Email_Unread_Specific', kwargs={'number':command})}
        return response
    elif active and not unread:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Email_All_Specific', kwargs={'number':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in Generic_Email_Unread_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Email_Unread_List')}
        elif any(command in command_list for command_list in Generic_Email_All_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Email_All_List')}
        else:
            response = ""
        return found, response
# *******************************************
# Apple Commands
# *******************************************
def AppleCommandRouter(active, profile, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Apple_Find_iPhone_Ping_Request', kwargs={'response':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in Generic_Apple_Find_iPhone_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Apple_Find_iPhone')}
        else:
            response = ""
        return found, response
# *******************************************
# Equation Commands
# *******************************************
def EquationCommandRouter(asking, profile, command):
    if asking:
        equation = command
        profile.math_request_active = False
        profile.save()
        response = {'status': 200, 'message': "Your error", 'url':reverse('Math')}
        return response, equation
    else:
        found = False
        if "what is" in command or "what's" in command and "-" in command or "minus" in command or "+" in command or "plus" in command or "times" in command or "*" in command or "divided by" in command or "/" in command:
            found = True
            print("Found: " + command)
            equation = command
            speech_response = ""
            response = {'status': 200, 'message': "Your error", 'url':reverse('Math')}
        elif "solve this for me" in command or "help me solve this" in command:
            found = True
            profile.math_request_active = True
            profile.save()
            speech_response = "What is the problem?"
            equation = ""
            response = {'status': 200, 'message': "Your error", 'url':reverse('Math_Request')}
        else:
            response = ""
            speech_response = ""
            equation = ""
        return found, response, speech_response, equation
# *******************************************
# Navigation Commands
# *******************************************
def NavigationCommandRouter(command):
    found = False
    if "dashboard" in command:
        found = True
        speech_response = ""
        response = {'status': 200, 'message': "Your error", 'url':reverse('Dashboard')}
    elif "mirror mode" in command:
        found = True
        speech_response = "Mirror Mode"
        response = {'status': 200, 'message': "Your error", 'url':reverse('Mirror')}
    else:
        response = ""
        speech_response = ""
    return found, response, speech_response
# *******************************************
# Weather Commands
# *******************************************
def WeatherCommandRouter(active, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Current_Weather_Search', kwargs={'location':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in Current_Weather_Location_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Current_Weather_Request')}
        else:
            response = ""
    return found, response
# *******************************************
# Crypto Commands
# *******************************************
def CryptoCommandRouter(active, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Crypto_Display', kwargs={'coin':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in Crypto_List_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Crypto_List')}
        elif any(command in command_list for command_list in Crypto_Search_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Crypto_Request')}
        elif any(command in command_list for command_list in Popular_Coin_Commands_List):
            found = True
            if "BTC" in command:
                response = {'status': 200, 'message': "Your error", 'url':reverse('Crypto_Display', kwargs={'coin':"BTC"})}
            elif "eth" in command:
                response = {'status': 200, 'message': "Your error", 'url':reverse('Crypto_Display', kwargs={'coin':"ETH"})}
            elif "LTC" in command:
                response = {'status': 200, 'message': "Your error", 'url':reverse('Crypto_Display', kwargs={'coin':"LTC"})}
            else:
                response = ""
        else:
            response = ""
    return found, response
# *******************************************
# Reddit Commands
# *******************************************
def RedditCommandRouter(active, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Current_Weather_Search', kwargs={'location':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in Reddit_Dashboard_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Reddit_Dashboard')}
        else:
            response = ""
    return found, response
# *******************************************
# Twitter Commands
# *******************************************
def TwitterCommandRouter(active, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Current_Weather_Search', kwargs={'location':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in Twitter_Timeline_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Twitter_Timeline')}
        else:
            response = ""
    return found, response
# *******************************************
# Uber Commands
# *******************************************
def UberCommandRouter(active, phase, command):
    if active:
        if phase == 0:
            # Remove space for words like uber XL or uber black or uber SUV
            command = command.replace(" ", "")
            response = {'status': 200, 'message': "Your error", 'url':reverse('Uber_Request_Seat', kwargs={'car':command})}
            return response
        elif phase == 1:
            response = {'status': 200, 'message': "Your error", 'url':reverse('Uber_Request_Address', kwargs={'seat':command})}
            return response
        elif phase == 2:
            response = {'status': 200, 'message': "Your error", 'url':reverse('Uber_Estimate', kwargs={'address':command})}
            return response
    else:
        found = False
        if any(command in command_list for command_list in Uber_Estimate_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Uber_Request_Car')}
        else:
            response = ""
    return found, response
# *******************************************
# System Commands
# *******************************************
def SystemCommandRouter(active, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Current_Weather_Search', kwargs={'location':command})}
        return response
    else:
        found = False
        if any(command in command_list for command_list in System_Volume_Up_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('System_Volume_Up')}
        elif any(command in command_list for command_list in System_Volume_Down_Commands_List):
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('System_Volume_Down')}
        else:
            response = ""
    return found, response
# *******************************************
# Dictionary Commands
# *******************************************
def DictionaryCommandRouter(active, command):
    if active:
        response = {'status': 200, 'message': "Your error", 'url':reverse('Current_Weather_Search', kwargs={'location':command})}
        return response
    else:
        found = False
        for commands in Dictionary_Definition_Commands_List:
            if commands in command:
                found = True
                response = {'status': 200, 'message': "Your error", 'url':reverse('Dictionary_Definition', kwargs={'word':command})}
                return found, response
        for commands in Dictionary_SynAnt_Commands_List:
            if commands in command:
                found = True
                response = {'status': 200, 'message': "Your error", 'url':reverse('Dictionary_SynAnt', kwargs={'word':command})}
                return found, response
        for commands in Dictionary_Translate_Word_Commands_List:
            if commands in command:
                found = True
                response = {'status': 200, 'message': "Your error", 'url':reverse('Dictionary_Translate_Word', kwargs={'word':command})}
                return found, response
        for commands in Dictionary_Translate_Sentence_Commands_List:
            if commands in command:
                found = True
                response = {'status': 200, 'message': "Your error", 'url':reverse('Dictionary_Translate_Sentence', kwargs={'sentence':command})}
                return found, response
        response = ""
        return found, response
# *******************************************
# Timer Commands
# *******************************************
def TimerCommandRouter(command):
    found = False
    for commands in Timer_Set_Commands_List:
        if commands in command:
            found = True
            response = {'status': 200, 'message': "Your error", 'url':reverse('Timer_Set', kwargs={'timer':command})}
            return found, response
    response = ""
    return found, response