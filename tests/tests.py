import main


class TestClass:

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
