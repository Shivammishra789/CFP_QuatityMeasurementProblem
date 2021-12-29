'''
@author: Shivam Mishra
@date: 29-12-21 12:09 PM

'''
import pytest as pytest

from quatity_custom_execption import QuatityCustomException
from quatity_mesurement import Measurement


class TestMeasurement:

    @pytest.mark.parametrize('len1,unit1,len2,unit2',[(0.0,"feet",0.0, "feet")])
    def test_zero_feet_and_zero_feet_return_equal(self,len1, unit1, len2, unit2):
        obj1 = Measurement(len1, unit1)
        obj2 = Measurement(len2, unit2)
        assert obj1 == obj2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(0.0,"feet",None,"feet")])
    def test_if_none_return_exception(self, len1, unit1, len2, unit2):
        obj1 = Measurement(len1, unit1)
        obj2 = Measurement(len2, unit2)
        with pytest.raises(QuatityCustomException) as exeception:
            obj1 == obj2
        assert exeception.value.message == "Value can't be none"

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(1.0, "feet", 2.0, "feet")])
    def test_whether_reference_are_equal(self, len1, unit1, len2, unit2):
        obj1 = Measurement(len1, unit1)
        obj2 = Measurement(len2, unit2)
        with pytest.raises(QuatityCustomException) as exeception:
            obj1 == obj2
        assert exeception.value.message == "Reference are different"

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(2.0, "feet", 2.0, "feet")])
    def test_whether_type_is_equal(self, len1, unit1, len2, unit2):
        obj1 = Measurement(len1, unit1)
        obj2 = Measurement(len2, unit2)
        assert obj1 == obj2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(2.0, "feet", 2.0, "feet")])
    def test_whether_value_is_equal(self, len1, unit1, len2, unit2):
        obj1 = Measurement(len1, unit1)
        obj2 = Measurement(len2, unit2)
        assert obj1 == obj2







