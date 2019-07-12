import pytest

from LeapYear import getLeapYear

def test_getLeapYear_1():
	year = getLeapYear(1991)
	assert year==1992("Hello My Name is ")