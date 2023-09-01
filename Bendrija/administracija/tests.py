from datetime import date

from mock import patch
from Bendrija.ataskaita import siusti_menesine_ataskaita
from django.test import TestCase

from administracija.models import Kaupiamasis_Inasas
from gyventojas.models import Flat


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


class KaupiamasisInasasTestCase(TestCase):

    def setUp(self):
        # Sukuriame bandomąjį butą ir Kaupiamasis_Inasas objektą
        self.flat = Flat.objects.create(size_kv=100)
        self.inasas = Kaupiamasis_Inasas.objects.create(flat_owner=self.flat, payment_rate=2.0)

    def test_calculate_size(self):
        # Patikriname, ar calculate_size metodas teisingai skaičiuoja dydį
        self.assertEqual(self.inasas.calculate_size(), 200.0)

    def test_calculate_monthly_inasas(self):
        # Patikriname, ar calculate_monthly_inasas metodas grąžina teisingą mėnesinį inasą
        self.assertEqual(self.inasas.calculate_monthly_inasas(), 200.0)

    def test_calculate_total_inasas(self):
        # Sukuriame keletą Kaupiamasis_Inasas objektų
        flat1 = Flat.objects.create(size_kv=100)
        flat2 = Flat.objects.create(size_kv=150)

        inasas1 = Kaupiamasis_Inasas.objects.create(flat_owner=flat1, payment_rate=2.0)
        inasas2 = Kaupiamasis_Inasas.objects.create(flat_owner=flat2, payment_rate=1.5)

        # Skaičiuojame viso inaso dydį
        total_inasas = inasas1.calculate_size() + inasas2.calculate_size()

        self.assertEqual(total_inasas, 425.0)




