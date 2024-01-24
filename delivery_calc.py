# this is for calculating how much money are you actually making
#*********************************************************************
# Author: Giancarlo Rhodes
# Description: Getting to accurate taxable amount
#*********************************************************************


import delivery_calc_lib

print("Welcome my delivery friend\n")
_name = input("Please enter your name: ")
print("Hello ", _name, ", delivery is hard work. Are you working in vain?")
print("This calculator should help in that question.")

_money = input("Enter how much you made over a period of hours. \n"
"Round to the nearest dollar: ")
print("Enter the flat number of hours including travel time between deliveries.\n"
"  Don't include large breaks like if you stop to eat or pick up groceries \n"
" for yourself. Work only related hours please.\n")
_hours = input("Enter the number of hours you delivered. Round to 15 minute "
"increments ##.##, 4.15, 1.45: ")

print("\n")
print("The mileage ratio input in very important. Example: You typically travel\n"
" 10 miles for $20. That's $2 for 1 mile ratio entered as  2/1 (best scenerio). \n"
" You travel 5 miles for 5 dollars. Thats a $1 for 1 mile ratio. 1/1 (worst scenerio). \n"
" This number should reflect your acceptance criteria pattern\n"
" when your accepting or declining jobs.\n")

_mileage_ratio = input("Enter the dollars/mile ratio in the format ##/##: ")
_mrConvert: float = delivery_calc_lib._mileage_ratio_str_to_float(_mileage_ratio)

print("67 cents per mile driven for business use is that standard reimbursement rate")
print("standard reimbursement includes costs for: gas, oil, tires, "
"maintenance and repairs, as well as the fixed costs of operating the "
"vehicle, such as insurance, registration and depreciation or lease payments.")

_reimbursement_cents_per_mile = int(input("Enter cents per mile reimbursement rate ##: "))
_debit = delivery_calc_lib._debit_calc_func(_money, _mrConvert,
                                            _reimbursement_cents_per_mile)
print("Credit: $", _money, ", Debit: $", _debit)
_diff: float = round(float(_money) - _debit,2)
print("You made $",_diff,"in ", _hours, " hours.")
_dollar_per_hour = _diff / float(_hours)
print("You'll be taxed on the $",_diff,". You made $",_dollar_per_hour, "per hour.")