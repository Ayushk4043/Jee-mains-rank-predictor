from flask import Flask, send_from_directory
from flask import request
from pymessenger.bot import Bot
import time
from predict import Mains
bot = Bot("EAAFjyAjyRHkBAK5IukOMkbInMWRm3pWjwZC040O4xDcc60xoylKIAxDcd9YZAquGXBLJGA8wZBPWb2wuAvbZBtPvnsp1dYRXFJPqPgQKTkvxjpmO3gJDiuKtZBZAFGxhfWEowhnZCpjb8cSWioznrRWTuFwwayXT7BvUCahtVoJWXyjqKvoQ7SI")
server_loc = "https://9f9c30d2.ngrok.io/"
app = Flask(__name__)


@app.route("/temp/<path>", methods=["GET"])
def images(path):
    return send_from_directory("temp", path)


@app.route("/", methods=["GET"])
def verify():
    if request.args.get("hub.challenge"):
        return request.args.get("hub.challenge")
    else:
        return "Please run it on facebook dev"


@app.route("/", methods=["POST"])
def message():
    data = request.get_json()

    print(data)

    if data.get("entry"):
        for entry in data["entry"]:
            if entry.get("messaging"):
                for message in entry["messaging"]:
                    if message.get('message'):
                        # Facebook Messenger ID for user so we know where to send response back to
                        user = message['sender']['id']
                        if message['message'].get('text')=="Jee Mains":

                            bot.send_text_message(user, "Please give me you jee mains marks:")
                            time.sleep(5)
                            t=message['message'].get('text')
                            print(t)

                        elif message['message'].get('text')!="Jee Mains":
                            text=message['message'].get('text')

                            t=int(text)
                            Mains(t)
                            print(text)
                            bot.send_text_message(user, text+" means bot ")






                        if message['message'].get('attachments'):  # json beautifier query
                            for attachment in message['message']['attachments']:
                                link = attachment['payload']['url']



                                bot.send_image_url(user, link)
    return "Message recieved"

app.run()