import requests
import json
import time
import mysql.connector

viber_token = "56dbdfa04fb0cc6e-2002af90949dd65c-ba202f172ac1a131"
user_id = "q1vcW2wB7x8JO4BQs1DZYA=="
viber_url = "https://chatapi.viber.com/pa/post"

Pl_url = "https://sdp-prem-prod.premier-league-prod.pulselive.com/api/v1/competitions/8/seasons/11/players?competition=8&season=11&_limit=20"


def send_message_viber(message):
    payload = {
        "auth_token": viber_token,
        "from": user_id,
        "type": "text",
        "text": message,
    }
    r = requests.post(url=viber_url, data=json.dumps(payload))


db = mysql.connector.connect(
    host="localhost", user="root", port=3306, database="football"
)

terminal = db.cursor()

query = """
CREATE TABLE IF NOT EXISTS Champion (
    player_id INT,
    player_name varchar (60),
    club varchar(100),
    country VARCHAR(100)
);
"""

terminal.execute(query)
db.commit()

next_token = None

try:

    while True:

        if next_token:
            url = Pl_url + "&_next=" + next_token
        else:
            url = Pl_url
        r = requests.get(url=url)
        if r.status_code == 200:
            team = r.json()
            result = team["data"]
            for i in result:
                upload = [
                    i["id"]["playerId"],
                    i["name"]["firstName"] + " " + i["name"]["lastName"],
                    i["currentTeam"]["name"],
                    i["country"]["country"],
                ]
                query = f"Insert into champion (player_id,player_name,club,country) values(%s,%s,%s,%s)"

                terminal.execute(query, upload)

            db.commit()

            next_token = team["pagination"]["_next"]
            if next_token is None:
                break

        else:
            print("API Error")
            break

except Exception as e:
    print("Error:", e)

user_choice = input("Enter the club_name:").lower()

query = "select * from champion where club =%s"
terminal.execute(
    query,
    (user_choice,),
)
result = terminal.fetchall()
if result:
    for i in result:
        message = f"""{i[1]}with id{i[0]} playing in the club {i[2]} is from {i[3]}."""
        send_message_viber(message)
        time.sleep(5)
else:
    print("Invalid club Name")