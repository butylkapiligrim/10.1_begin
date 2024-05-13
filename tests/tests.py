from src.masks import tests_mask, card_mask
from src.widget import convert_date, number_or_account

#
#
# nums_card_input = str(input("Введите номер карты: "))
# card_mask(nums_card_input)
#
# nums_check_input = str(input("Введите номер счета: "))
# tests_mask(nums_check_input)

print(convert_date("2018-07-11T02:26:18.671407"))

inputs = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305"
]

for input_str in inputs:
    print(number_or_account(input_str))
