from django.tests import TestCase
from reservation.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Noodles", price=50, inventory=20)
        Menu.objects.create(title="Cold Drink", price=20, inventory=200)
    def test_getall(self):
        item1 = Menu.objects.get(title="Noodles")
        item2 = Menu.objects.get(title="Cold Drink")
        self.assertEquals(item1, "Noodles : 50")
        self.assertEquals(item2, "Cold Drink : 20")
        self.assertEquals(1,2)
        