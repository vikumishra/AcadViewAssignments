#Question-1
#An access token is a secret key which helps in authentication and keeps track that only logged in user can acces the Api
#Steps to generate access token.. 1)make account on developer tools
#2)sign in and enter all the required credentials to generate new app
#3)click on keys and token to get token button..click on that button to get the access tokens

#Question-2
#google ip address-216.58.217.110
#facebook ip address-31.13.69.228

#Question-3
'''
from keys import consumer_key,consumer_secret,access_token,access_secret
import tweepy
oauth=tweepy.OAuthHandler(consumer_key,consumer_secret)
oauth.set_access_token(access_token,access_secret)
api=tweepy.API(oauth)
print(api.search("#race3"))


user=api.get_user("viku_mishra")
print(user.screen_name)
print(user.followers_count)

'''

#Question-4
#Library-It is a collection of classes that have some functions..All the code of all classes present in it can be seen, modified by user
#API-It is an interface that allows to use functionality of few websites.. it only offers functions but not the code and also not allows the modificatio

#Question-5
import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something")
    audio=r.listen(source)
try:
    print("Google thinks you said:\n"+r.recognize_google(audio))
except:
    pass


