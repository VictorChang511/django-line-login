from django.shortcuts import render, redirect
from dotenv import load_dotenv
import os
import random, string
import requests

load_dotenv()

def index(request):
  if "user_info" in request.session:
    return redirect("/user")
  return render(request, "index.html")

def login(request):
  permission_url = "https://access.line.me/oauth2/v2.1//authorize?response_type={response_type}&client_id={client_id}&redirect_uri={redirect_uri}&state={state}&scope={scope}&bot_prompt={bot_prompt}".format(
    response_type = "code",
    client_id = os.getenv("CLIENT_ID"),
    redirect_uri = "{app_url}/auth/line/callback".format(app_url=os.getenv("APP_URL")),
    state = "".join(random.choice(string.ascii_letters) for x in range(10)),
    scope = "profile%20openid%20email",
    bot_prompt = "aggressive"
  )
  return redirect(permission_url)

def callback(request):
  code = request.GET.get("code")
  data = {"id_token": get_id_token(code), "client_id": os.getenv("CLIENT_ID")}
  r = requests.post("https://api.line.me/oauth2/v2.1/verify", headers={"Content-Type": "application/x-www-form-urlencoded"}, data=data)
  user_info = r.json()
  request.session["user_info"] = user_info
  return redirect("/user")

def get_id_token(code):
  data = {
    "grant_type": "authorization_code",
    "code": code,
    "redirect_uri": "{app_url}/auth/line/callback".format(app_url=os.getenv("APP_URL")),
    "client_id": os.getenv("CLIENT_ID"),
    "client_secret": os.getenv("CLIENT_SECRET")
  }
  r = requests.post("https://api.line.me/oauth2/v2.1/token", headers={"Content-Type": "application/x-www-form-urlencoded"}, data=data)
  return r.json()["id_token"]

def get_user(request):
  if "user_info" in request.session:
    user_info = request.session["user_info"]
    return render(request, 'user.html', user_info)
  return redirect("/login")

def logout(request):
  del request.session["user_info"]
  return redirect("/")