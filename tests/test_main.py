import main
from datetime import datetime
from unittest import TestCase


class TestMain(TestCase):

	def test_get_webpage_return_integer(self):
		result = main.get_webpage('http://www.google.com')
		assert isinstance(result, int)

	def test_get_webpage_return_200_on_good_webpage(self):
		result = main.get_webpage('http://www.google.com')
		assert result == 200

	def test_get_webpage_return_404_on_non_existent_webpage(self):
		result = main.get_webpage('http://www.google.com/asdasdasd/asdasda/asdasdaddasd/html')
		assert result == 404

	def test_get_webpage_return_minus_1_on_missing_schema(self):
		result = main.get_webpage('sdnasdcnadsjkncadkscjna')
		assert result == -1

	def test_get_webpage_return_minus_1_on_bad_schema(self):
		result = main.get_webpage('hrrp://www.hello.com')
		assert result == -1

	def test_get_webpage_return_minus_1_on_integer_url(self):
		result = main.get_webpage(1)
		assert result == -1

	def test_get_time_return_string(self):
		result = main.get_time()
		assert isinstance(result, str)

	def test_get_time_return_valid_time(self):
		result = main.get_time()
		try:
			my_time = datetime.strptime(result[:10], "%Y-%m-%d")
		except ValueError:
			assert False
		assert isinstance(my_time, datetime)

	def test_main_return_1_or_0(self):
		result = main.main()
		assert result == 1 or result == 0
