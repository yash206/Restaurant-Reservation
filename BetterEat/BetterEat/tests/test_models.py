from django.test import TestCase
from reservation.models import Menu

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(Title="IceCream", Price=80.00, Inventory=100)
        self.assertEquals(item, "IceCream : 80.00")