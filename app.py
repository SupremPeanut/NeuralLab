from flask import Flask, render_template, request, jsonify
import requests
import os
from dotenv import load_dotenv

# Charger les variables d'environnement
load_dotenv()

app = Flask(__name__)

# Récupère la clé API depuis le fichier .env
API_KEY = os.getenv("API_KEY")

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def info():
    # Exemple de requête pour récupérer des informations via l'API CedMod
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get("https://api.cedmod.com/example_endpoint", headers=headers)
    if response.status_code == 200:
        data = response.json()
    else:
        data = {"error": "Impossible de récupérer les informations"}
    return render_template('info.html', data=data)

@app.route('/espace-personnel/<player_id>')
def espace_personnel(player_id):
    # Récupère les informations du joueur depuis l'API
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(f"https://api.cedmod.com/player/{player_id}", headers=headers)
    if response.status_code == 200:
        player_data = response.json()
    else:
        player_data = {"error": "Impossible de récupérer les informations du joueur"}
    return render_template('espace_personnel.html', player=player_data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=25546)