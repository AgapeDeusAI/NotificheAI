from flask import Flask, request, jsonify
from flask_cors import CORS
from NotificheAI import NotificheAI

app = Flask(__name__)
CORS(app)

notifiche = NotificheAI()

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "✅ Notifiche AI attiva"})

@app.route("/notifica", methods=["POST"])
def aggiungi():
    data = request.get_json()
    messaggio = data.get("messaggio")
    tipo = data.get("tipo", "info")
    urgente = data.get("urgente", False)

    if not messaggio:
        return jsonify({"success": False, "errore": "Messaggio mancante."})

    risultato = notifiche.aggiungi_notifica(messaggio, tipo, urgente)
    return jsonify({"success": True, "notifica": risultato})

@app.route("/lista", methods=["GET"])
def lista():
    return jsonify({"success": True, "notifiche": notifiche.tutte()})

if __name__ == "__main__":
    app.run(port=3013)