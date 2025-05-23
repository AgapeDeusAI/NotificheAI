from datetime import datetime
import json
import os

class NotificheAI:
    """
    Gestisce notifiche, promemoria e messaggi programmati.
    """

    def __init__(self):
        self.file_notifiche = "notifiche.json"
        self.notifiche = self._carica()

    def _carica(self):
        if os.path.exists(self.file_notifiche):
            with open(self.file_notifiche, "r") as f:
                return json.load(f)
        return []

    def aggiungi_notifica(self, messaggio: str, tipo: str = "info", urgente: bool = False):
        notifica = {
            "data": datetime.now().isoformat(),
            "messaggio": messaggio,
            "tipo": tipo,
            "urgente": urgente
        }
        self.notifiche.append(notifica)
        self._salva()
        return notifica

    def _salva(self):
        with open(self.file_notifiche, "w") as f:
            json.dump(self.notifiche, f, indent=2)

    def tutte(self):
        return self.notifiche[-20:]  # ultime 20

    def filtra_per_tipo(self, tipo: str):
        return [n for n in self.notifiche if n["tipo"] == tipo]