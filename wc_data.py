import requests
import mysql.connector

url = "https://worldcup26.ir/get/games"

r = requests.get(url)
if r.status_code == 200:
    data = r.json()
    data1 = data['games']

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    port = 3306,
    database = "wc_26"
)

terminal = db.cursor()

query = """
    INSERT INTO `scores_and_scorers`
    (`Home team`, `Home team score`, `Scored by home`,
    `Away team`, `Away team score`, `Scored by away`)
    VALUES (%s, %s, %s, %s, %s, %s)
  """

for i in data1:
    VALUES = (
               i.get("home_team_name_en","null"),
               int(i['home_score']), 
               i['home_scorers'], 
               i.get('away_team_name_en','null'), 
               int(i['away_score']),
               i['away_scorers'],
               )
    terminal.execute(query,VALUES)
db.commit()
