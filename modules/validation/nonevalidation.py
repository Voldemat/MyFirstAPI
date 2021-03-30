from typing import List


def strictvalidation(value_list:list):
    for value in value_list:
        if value == None:
            raise ValueError('None value!')


def comparisonvalidation(valuelists:List[list]):
    for pair_list in value_list:
        if len(pair_list) > 2:
            raise ValueError('Comparison values lists have more than 2 elements')
        if pair_list[0] == None and pair_list[1] == None:
            raise ValueError('Both of elements are equill to None')

def validateNone(strict_list:list, comparison_list:List[list]):
    if strict_list == None and comparison_list == None: 
        raise ValueError('strict_list and comparison_list wasn`t passed in validateNone function!')

    strictvalidation(strict_list)

    comparisonvalidation(comparison_list)


