from unittest.mock import patch
from service import Service
import unittest

'''class test_function(unittest.TestCase):
	
	def setUp(self):
		self.service = Service()
		self.num1 = 10
		self.num2 = 5
		'''


@patch('service.Service.bad_random')
def test_bad_random(bad_random):
	bad_random.return_value = 10


@patch('service.Service.bad_random')
def test_divide(bad_random):
	bad_random.return_value = 10
	service = Service()
	x = service.divide(2)
	assert(x == 5)

def test_abs_plus():
	service = Service()
	returnAbs = service.abs_plus(-5)
	assert (returnAbs == 6)

@patch('service.Service.bad_random')
def test_complicated_function(bad_randomStub):
	bad_randomStub.return_value = 10
	serviceTest = Service()
	returnDiv, returnAbs = serviceTest.complicated_function(5)
	assert (returnDiv == 2)
	assert (returnAbs == 0)

