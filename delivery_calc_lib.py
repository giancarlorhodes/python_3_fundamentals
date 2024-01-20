
def _mileage_ratio_str_to_float(inMileageRatio: str):
    _numbers = inMileageRatio.rsplit('/')
    _numerator = int(_numbers[0])
    _denominator = int(_numbers[1])
    _rounded: float = round(_numerator/_denominator, 2)
    return _rounded

def _debit_calc_func(inDollarsEarned: int, inMileageRatio: float, 
                     inReimbursementCentsPerMile: int):
    #_value: float = round(float(inDollarsEarned),2)
    #print("Dollars: ", _value)
    _miles_estimate: float = int(inDollarsEarned) / inMileageRatio
    #print("Miles: ", _miles_estimate)
    _miles_cost: float = round(inReimbursementCentsPerMile/100 * _miles_estimate, 2) # in cents
    #print("Cost of Miles: ", _miles_cost)
    return _miles_cost

