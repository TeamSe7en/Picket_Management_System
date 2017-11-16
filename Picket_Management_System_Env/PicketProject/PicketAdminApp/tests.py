from django.test import TestCase
from .models import Metrostation
# Create your tests here.

m = Metrostation.objects.all()
print(m)