from django.test import TestCase
from reservation.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Noodles", Price=50.00, Inventory=20)
        Menu.objects.create(Title="Cold Drink", Price=20.00, Inventory=200)
        
    def test_getall(self):
        item1 = Menu.objects.get(Title="Noodles")
        item2 = Menu.objects.get(Title="Cold Drink")
        self.assertEquals(item1.Price, 50.00)
        self.assertEquals(item2.Price, 20.00)
        