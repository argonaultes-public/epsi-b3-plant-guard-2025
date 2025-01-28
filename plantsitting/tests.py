from django.test import TestCase
from plantsitting.models import Plant, Owner

# Create your tests here.

class PlantTestCase(TestCase):
    def setUp(self):
        Owner.objects.create(email='test@email.com')

    def test_plant_has_owner(self):
        owner = Owner.objects.get(email='test@email.com')
        Plant.objects.create(name='plant1', owner=owner)
        plant_result = Plant.objects.get(name='plant1')
        self.assertEqual(plant_result.name, 'plant1')
        self.assertEqual(plant_result.owner.email, 'test@email.com')

    def test_plant_2(self):
        pass