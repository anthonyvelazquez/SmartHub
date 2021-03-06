from django.conf.urls import url
from Dashboard import views
from Dashboard.Module_Views.Alarm import *
from Dashboard.Module_Views.Sleep import *
from Dashboard.Module_Views.Reminder import *
from Dashboard.Module_Views.Setup import *
from Dashboard.Module_Views.Email import *
from Dashboard.Module_Views.Apple import *
from Dashboard.Module_Views.LoL import *
from Dashboard.Module_Views.Weather import *
from Dashboard.Module_Views.Chatbot import *
from Dashboard.Module_Views.Uber import *
from Dashboard.Module_Views.Crypto import *
from Dashboard.Module_Views.Reddit import *
from Dashboard.Module_Views.Twitter import *
from Dashboard.Module_Views.System import *
from Dashboard.Module_Views.Dictionary import *
from Dashboard.Module_Views.Timer import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    url(r'^$', views.DashboardView.as_view(), name='Dashboard'),
    # *******************************************
    # Setup
    # *******************************************
    url(r'^Setup/AI/Name/Request$', AISetupNameRequestView.as_view(), name='AI_Setup_Name_Request'),
    url(r'^Setup/AI/Name$', AISetupNameView.as_view(), name='AI_Setup_Name'),
    url(r'^Setup/AI/Gender/Request$', AISetupGenderRequestView.as_view(), name='AI_Setup_Gender_Request'),
    url(r'^Setup/AI/Gender$', AISetupGenderView.as_view(), name='AI_Setup_Gender'),
    url(r'^Setup/Profile$', views.ProfileView.as_view(), name='Profile'),
    url(r'^Setup/Profile/Create$', views.CreateProfileView.as_view(), name='Profile_Create'),
    # *******************************************
    # Alarm
    # *******************************************
    url(r'^Alarm/Request$', AlarmRequestView.as_view(), name='Alarm_Request'),
    url(r'^Alarm/Request/Name/(?P<pk>[^/]+)/(?P<name>[^/]+)$', AlarmRequestNameView.as_view(), name='Alarm_Request_Set_Name'),
    url(r'^Alarm/Request/Time/(?P<pk>[^/]+)/(?P<time>[^/]+)$', AlarmRequestTimeView.as_view(), name='Alarm_Request_Set_Time'),
    url(r'^Alarm/Request/Mode/(?P<pk>[^/]+)/(?P<mode>[^/]+)$', AlarmRequestModeView.as_view(), name='Alarm_Request_Set_Mode'),
    url(r'^Alarm/Request/Quick/(?P<alarm>[^/]+)$', CreateQuickAlarmView.as_view(), name='Alarm_Create_Quick'),
    url(r'^Alarm/Request/Specific/(?P<alarm>[^/]+)$', CreateSpecificAlarmView.as_view(), name='Alarm_Create_Specific'),
    url(r'^Alarm/Disable$', DisableAlarmView.as_view(), name='Alarm_Disable'),
    url(r'^Alarm/Delete/All$', DeleteAllAlarmView.as_view(), name='Alarm_Delete_All'),
    url(r'^Alarm/Delete/Request$', DeleteAlarmRequestView.as_view(), name='Alarm_Delete_Request_Name'),
    url(r'^Alarm/Delete/Request/(?P<name>[^/]+)$', DeleteSpecificAlarmView.as_view(), name='Alarm_Delete_Specific'),
    url(r'^Alarm/Display/(?P<pk>[^/]+)$', DisplayAlarmView.as_view(), name='Alarm_Display'),
    # *******************************************
    # Reminder
    # *******************************************
    url(r'^Reminder/Request$', ReminderRequestNameView.as_view(), name='Reminder_Request'),
    url(r'^Reminder/Request/(?P<name>[^/]+)$', ReminderRequestTimeView.as_view(), name='Reminder_Request_Time'),
    url(r'^Reminder/Create/(?P<time>[^/]+)$', ReminderView.as_view(), name='Reminder'),
    url(r'^Reminder/Request/Quick/(?P<reminder>[^/]+)$', CreateQuickReminderView.as_view(), name='Reminder_Create_Quick'),
    url(r'^Reminder/Delete/All$', DeleteAllReminderView.as_view(), name='Reminder_Delete_All'),
    url(r'^Reminder/Delete/First$', DeleteFirstReminderView.as_view(), name='Reminder_Delete_First'),
    url(r'^Reminder/Delete/Last$', DeleteLastReminderView.as_view(), name='Reminder_Delete_Last'),
    url(r'^Reminder/Request/Specific/(?P<reminder>[^/]+)$', CreateSpecificReminderView.as_view(), name='Reminder_Create_Specific'),
    url(r'^Reminder/Display/(?P<pk>[^/]+)$', DisplayReminderView.as_view(), name='Reminder_Display'),
    # *******************************************
    # Email
    # *******************************************
    url(r'^Email/List/Unread$', EmailUnreadListView.as_view(), name='Email_Unread_List'),
    url(r'^Email/Display/Unread/(?P<number>[^/]+)$', SpecificEmailUnreadView.as_view(), name='Email_Unread_Specific'),
    url(r'^Email/List/All$', EmailAllListView.as_view(), name='Email_All_List'),
    url(r'^Email/Display/All/(?P<number>[^/]+)$', SpecificEmailAllView.as_view(), name='Email_All_Specific'),
    # *******************************************
    # League of Legends
    # *******************************************
    url(r'^LoL/Me$', SelfLoLProfileView.as_view(), name='LoL_Me'),
    # *******************************************
    # Apple
    # *******************************************
    url(r'^Apple/iPhone/Find$', AppleFindiPhoneView.as_view(), name='Apple_Find_iPhone'),
    url(r'^Apple/iPhone/Find/Ping/(?P<response>[^/]+)$', AppleFindiPhonePingRequestView.as_view(), name='Apple_Find_iPhone_Ping_Request'),
    # *******************************************
    # Weather
    # *******************************************
    url(r'^Weather/Current/Request$', CurrentWeatherRequestView.as_view(), name='Current_Weather_Request'),
    url(r'^Weather/Current/Here$', CurrentWeatherHereView.as_view(), name='Current_Weather_Here'),
    url(r'^Weather/Current/Search/(?P<location>[^/]+)$', CurrentWeatherSearchView.as_view(), name='Current_Weather_Search'),
    # *******************************************
    # Alarm
    # *******************************************
    url(r'^Setup/(?P<profile_id>[^/]+)$', views.SetupView.as_view(), name='Setup'),
    url(r'^Command$', csrf_exempt(views.VoiceCommandView.as_view()), name='Voice_Command'),
    url(r'^Math/Request$', views.MathRequestView.as_view(), name='Math_Request'),
    url(r'^Math/Solve$', views.MathView.as_view(), name='Math'),
    # *******************************************
    # Alarm
    # *******************************************
    url(r'^Mirror$', views.MirrorView.as_view(), name='Mirror'),
    # *******************************************
    # Sleep
    # *******************************************
    url(r'^Sleep$', SleepView.as_view(), name='Sleep'),
    # *******************************************
    # System
    # *******************************************
    url(r'^System/Volume/Up$', SystemVolumeUpView.as_view(), name='System_Volume_Up'),
    url(r'^System/Volume/Down$', SystemVolumeDownView.as_view(), name='System_Volume_Down'),
    # *******************************************
    # Uber
    # *******************************************
    url(r'^Uber/Request$', UberCarTypeRequestView.as_view(), name='Uber_Request_Car'),
    url(r'^Uber/Request/Car/(?P<car>[^/]+)$', UberSeatRequestView.as_view(), name='Uber_Request_Seat'),
    url(r'^Uber/Request/Seat/(?P<seat>[^/]+)$', UberAddressRequestView.as_view(), name='Uber_Request_Address'),
    url(r'^Uber/Request/Estimate/(?P<address>[^/]+)$', UberEstimateView.as_view(), name='Uber_Estimate'),
    # *******************************************
    # Twitter
    # *******************************************
    url(r'^Twitter/Timeline$', TwitterTimelineView.as_view(), name='Twitter_Timeline'),
    url(r'^Twitter/Request$', TwitterRequestView.as_view(), name='Twitter_Request'),
    url(r'^Twitter/Tweet$', TwitterTweetView.as_view(), name='Twitter_Tweet'),
    # *******************************************
    # Reddit
    # *******************************************
    url(r'^Reddit/Dashboard$', RedditDashboardView.as_view(), name='Reddit_Dashboard'),
    # *******************************************
    # Crypto Currency
    # *******************************************
    url(r'^Crypto/List$', CryptoListView.as_view(), name='Crypto_List'),
    url(r'^Crypto/Request$', CryptoRequestView.as_view(), name='Crypto_Request'),
    url(r'^Crypto/Display/(?P<coin>[^/]+)$', CryptoDisplayView.as_view(), name='Crypto_Display'),
    # *******************************************
    # Alarm
    # *******************************************
    url(r'^Search/Request$', views.SearchRequestView.as_view(), name='Search_Request'),
    url(r'^Search/Result$', views.SearchResultView.as_view(), name='Search_Result'),
    url(r'^Chatbot/(?P<speech>[^/]+)$', ChatbotView.as_view(), name='Chatbot'),
    # *******************************************
    # Dictionary
    # *******************************************
    url(r'^Dictionary/Definition/(?P<word>[^/]+)$', DefinitionView.as_view(), name='Dictionary_Definition'),
    url(r'^Dictionary/SynAnt/(?P<word>[^/]+)$', SynAntView.as_view(), name='Dictionary_SynAnt'),
    url(r'^Dictionary/Translate/Word/(?P<word>[^/]+)$', TranslateWordView.as_view(), name='Dictionary_Translate_Word'),
    url(r'^Dictionary/Translate/Sentence/(?P<sentence>[^/]+)$', TranslateSentenceView.as_view(), name='Dictionary_Translate_Sentence'),
    # *******************************************
    # Timer
    # *******************************************
    url(r'^Timer/Set/(?P<timer>[^/]+)$', TimerSetView.as_view(), name='Timer_Set'),
    url(r'^Timer/Display$', TimerDisplayView.as_view(), name='Timer_Display'),
    url(r'^Timer/Done$', TimerDoneView.as_view(), name='Timer_Done'),
]

# https://docs.smart-mirror.io/docs/configure_the_mirror.html#giphy
