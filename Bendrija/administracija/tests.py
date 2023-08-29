from datetime import date

from mock import patch
from Bendrija.ataskaita import siusti_menesine_ataskaita
from django.test import TestCase



class SiustiAtaskaitaTest(TestCase):

    @patch('Bendrija.ataskaita.send_mail')
    def test_siusti_menesine_ataskaita_men26(self, mock_send_mail):
        today = date.today()
        day_8 = date(today.year, today.month, 8)

        # Paleidžiame funkciją
        with patch('Bendrija.ataskaita.date', return_value=day_8):
            siusti_menesine_ataskaita()

        # Tikriname, ar send_mail nebuvo iškvietas
        mock_send_mail.assert_not_called()

#(python manage.py test )






