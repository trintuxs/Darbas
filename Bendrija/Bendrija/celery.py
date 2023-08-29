'''
Sis failas atsako uz automatini email siuntima.
'''
from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

# Nustatyti Django projekto settings modulį
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Bendrija.settings')

app = Celery('Bendrija')

# Įtraukti visus Django Celery konfigūracijos nustatymus
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatiškai raskite ir užregistruokite visas Django užduotis
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# Pridedame periodinę užduotį siųsti mėnesinę ataskaitą
app.conf.beat_schedule = {
    'siusti-menesine-ataskaita': {
        'task': 'Bendrija.siusti_menesine_ataskaita',  # Keiskite 'jusu_projekto' į savo projekto pavadinimą.
        'schedule': crontab(day_of_month='26', hour='0', minute='0'),  # Vykdymas kiekvieno mėnesio 8 dieną 00:00 val.
    },
}

