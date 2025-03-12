# -*- coding: utf-8 -*-

# Sample Python code for youtube.videos.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

import tkinter
import tkinter.messagebox

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

# Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret_90275261165-3inmam072fe93om13fp41t9g5v1pa56h.apps.googleusercontent.com.json"

    # Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_local_server(port=10000)
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def showLikedVideos():

    request = youtube.videos().list(
        part="snippet",
        myRating="like"
    )
    response = request.execute() #request pretstavuva query vo json format na YouTube videa kade specifirame da bidat nasi lajknati videa

    newList = []

    i = 0

    for i in range(len(response['items'])):
        responseNew = response['items'][i]['snippet']['title'] #for loop za izminuvanje na site videa, pritoa responseNew pravi filtriranje da se izlistaat samo naslovite na videata
        newList.append(responseNew) #rezultatot se smestuva vo lista
    
    tkinter.messagebox.showinfo("Result", newList) #listata se prikazuva na nov prozorec

def showDislikedVideos():

    request = youtube.videos().list(
        part="snippet",
        myRating="dislike"
    )
    response = request.execute()

    newList = []

    i = 0

    for i in range(len(response['items'])):
        responseNew = response['items'][i]['snippet']['title']
        newList.append(responseNew)
    
    tkinter.messagebox.showinfo("Result", newList)

def subscriptions():
    request = youtube.subscriptions().list(
        part="snippet",
        mine=True
    )
    response = request.execute()

    newList = []

    #for item in response['items']:
        #newList.append([item['snippet']['title']])   #moze i vaka da raboti, no podolniot kod pravi izlezot da e podobar
    
    i = 0

    for i in range(len(response['items'])):
        responseNew = response['items'][i]['snippet']['title']
        newList.append(responseNew)

    tkinter.messagebox.showinfo("Result", newList)

def usHits():
    request = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode="US"
    )
    response = request.execute()

    newList = []

    i = 0

    for i in range(len(response['items'])):
        responseNew = response['items'][i]['snippet']['title']
        newList.append(responseNew)
    
    tkinter.messagebox.showinfo("Result", newList)

def mkHits():
    request = youtube.videos().list(
        part="snippet",
        chart="mostPopular",
        regionCode="MK"
    )
    response = request.execute()

    newList = []

    i = 0

    for i in range(len(response['items'])):
        responseNew = response['items'][i]['snippet']['title']
        newList.append(responseNew)
    
    tkinter.messagebox.showinfo("Result", newList)

def myChannelDetails():
    request = youtube.channelSections().list(
        part="snippet,contentDetails",
        mine=True
    )
    response = request.execute()

    newList = []

    i = 0

    for i in range(len(response['items'])):
        responseNew = response['items'][i]['snippet']
        newList.append(responseNew)
    
    tkinter.messagebox.showinfo("Result", response)
    

#if __name__ == "__main__":  #trebase da se komentira ovoj del za da raboti mainloop
m = tkinter.Tk()
w = tkinter.Canvas(m, width=700, height=700)
#w.pack()
w.configure(background="white")
m.geometry("720x540")
m.title("My YouTube Data") #naslov na prozorecot
btn = tkinter.Button(m, text='My Liked Videos', width=25, command=showLikedVideos) #ja povikuva funkcijata sto e vo command delot
btn.pack(side="top")
btn.configure(background="red") #boja na kopce
btn3 = tkinter.Button(m, text='My Disliked Videos', width=25, command=showDislikedVideos)
btn3.pack(side="top")
btn3.configure(background="red")
btn4 = tkinter.Button(m, text="My Subscriptions", width=25, command=subscriptions)
btn4.pack(side="top")
btn4.configure(background="red")
btn6 = tkinter.Button(m, text="Most Popular Videos In US", width=25, command=usHits)
btn6.pack(side="top")
btn6.configure(background="red")
btn7 = tkinter.Button(m, text="Most Popular Videos In MK", width=25, command=mkHits)
btn7.pack(side="top")
btn7.configure(background="red")
btn9 = tkinter.Button(m, text="My Channel Details", width=25, command=myChannelDetails)
btn9.pack(side="top")
btn9.configure(background="red")
#main()
m.mainloop() #pravi da ne se gasi programata posle stiskanje na kopce
