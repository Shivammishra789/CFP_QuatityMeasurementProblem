'''
@author: Shivam Mishra
@date: 29-12-21 12:09 PM
@desc: test cases for comparing length
'''
import pytest as pytest

from quantity_custom_execption import QuantityCustomException
from quantity_mesurement import Measurement


class TestMeasurement:

    @pytest.fixture
    def measure(self, len1, unit1, len2, unit2):
        self.obj1 = Measurement(len1, unit1)
        self.obj2 = Measurement(len2, unit2)

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(0.0, "feet", 0.0, "feet"),(0.0, "feet", 0.0, "inch")])
    def test_zero_feet_and_zero_feet_return_equal(self,measure):
        assert self.obj1 == self.obj2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(0.0, "feet", None, "feet"), (0.0, "inch", None, "inch")])
    def test_if_none_return_exception(self, measure):
        with pytest.raises(QuantityCustomException) as exeception:
            self.obj1 == self.obj2
        assert exeception.value.message == "Value can't be none"

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(1.0, "feet", 2.0, "feet"), (1.0, "inch", 2.0, "inch")])
    def test_whether_reference_are_equal(self, measure):
        with pytest.raises(QuantityCustomException) as exeception:
            self.obj1 == self.obj2
        assert exeception.value.message == "Reference are different"

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(2.0, "feet", 2.0, "feet"), (2.0, "inch", 2.0, "inch")])
    def test_whether_type_is_equal(self, measure):
        assert self.obj1 == self.obj2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(2.0, "feet", 2.0, "feet"), (2.0, "inch", 2.0, "inch"),
                                                       (1.0, "feet", 12.0, "inch"),(12.0, "inch", 1.0, "feet"),
                                                       (3.0, "feet", 1.0, "yard"),(1.0, "yard", 3.0, "feet"),
                                                       (1.0, "yard", 36.0, "inch"), (36.0, "inch", 1.0, "yard" )])
    def test_whether_value_is_equal(self, measure):
        assert self.obj1 == self.obj2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(1.0, "feet", 1.0, "inch"), (1.0, "inch", 1.0, "feet"),
                                                       (1.0, "feet", 1.0, "yard"), (1.0, "inch", 1.0, "yard")])
    def test_whether_values_are_not_equal(self, measure):
        assert self.obj1 != self.obj2
