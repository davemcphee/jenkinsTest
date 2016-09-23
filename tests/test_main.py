import os
import sys
import pytest
import runner
from datetime import datetime
from unittest import TestCase


class TestMain(TestCase):

	def test_get_webpage_return_integer(self):
		result = runner.get_webpage('http://www.google.com')
		assert isinstance(result, int)

	def test_get_webpage_return_200_on_good_webpage(self):
		result = runner.get_webpage('http://www.google.com')
		assert result == 200

	def test_get_webpage_get_lots_of_pages_quickly(self):
		times_to_run = 40
		result = [runner.get_webpage('http://www.google.com') for x in range(times_to_run)]
		assert len(result) == times_to_run
		for x in result:
			assert x == 200

	def test_get_webpage_return_404_on_non_existent_webpage(self):
		result = runner.get_webpage('http://www.google.com/asdasdasd/asdasda/asdasdaddasd/html')
		assert result == 404

	def test_get_webpage_return_minus_1_on_missing_schema(self):
		result = runner.get_webpage('sdnasdcnadsjkncadkscjna')
		assert result == -1

	def test_get_webpage_return_minus_1_on_bad_schema(self):
		result = runner.get_webpage('hrrp://www.hello.com')
		assert result == -1

	def test_get_webpage_return_minus_1_on_integer_url(self):
		result = runner.get_webpage(1)
		assert result == -1

	def test_get_webpage_return_minus_1_on_null_url(self):
		with pytest.raises(Exception) as exc:
			runner.get_webpage()
		assert exc.typename == "TypeError"

	def test_get_time_return_string(self):
		result = runner.get_time()
		assert isinstance(result, str)

	def test_get_time_return_valid_time(self):
		result = runner.get_time()
		try:
			my_time = datetime.strptime(result[:10], "%Y-%m-%d")
		except ValueError:
			assert False
		assert isinstance(my_time, datetime)

	def test_main_return_1_or_0(self):
		result = runner.main()
		assert result == 1 or result == 0

	def test_main_exits_with_status_code_0(self):
		result = runner.main()
		assert result == 0
