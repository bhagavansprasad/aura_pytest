import pytest
from amath import is_even

data = [
        {"data" : 10, "exp_result" : True},
        {"data" : 15, "exp_result" : False},
        {"data" : 0, "exp_result" : False},
        {"data" : -0, "exp_result" : True},
] 

@pytest.mark.parametrize("ipd", data)
def test_phone_number(ipd):
    print (ipd)
    rvalue = is_even(ipd["data"])
    assert rvalue == ipd["exp_result"], f"For {ipd['data']} is_even retval :{rvalue} expected :{ipd['exp_result']}"
