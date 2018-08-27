# -*- coding: utf-8 -*-
import random
import re
import string


def replace(string, dictionary):
    if not isinstance(string, str):
        raise ValueError("accept string type")

    pattern = re.compile('|'.join(dictionary.keys()))
    return pattern.sub(lambda x: dictionary[x.group()], string)


def check_int_field(value):
    if isinstance(value, int):
        return value

    if not isinstance(value, float):
        try:
            value = value.__int__()
        except AttributeError:
            pass
        else:
            if isinstance(value, int):
                return value

            raise TypeError(
                '__int__ returned non-int (type %s)' % type(value).__name__)

        raise TypeError(
            'an integer is required (got type %s)' % type(value).__name__)

    raise TypeError('integer argument expected, got float')


def is_valid_national_id(number):
    """Check whether number is a valid national id or not

        Usage::
        >>> from persiantools import utils
        >>> is_valid = utils.is_valid_national_id("3934540414")

        :param number:  A number, will be checked for validation
        :rtype: str
    """

    if number is None or number == '':
        return False

    pattern = re.compile('^\d{10}$')

    if not pattern.match(number):
        return False

    n = 0
    for i in range(9):
        n += (10 - i) * int(number[i])

    r = n % 11

    if r > 1:
        r = 11 - r

    no = number[0:9] + str(r)

    return no == number


def generate_random_national_id():
    """Generate random Iranian national ID

        Usage::
        >>> from persiantools import utils
        >>> national_id = utils.generate_random_national_id()

    """

    national_id = ''.join(random.choice(string.digits) for _ in range(9))
    n = 0
    for i in range(9):
        n += (10 - i) * int(national_id[i])

    r = n % 11
    if r > 1:
        r = 11 - r

    national_id += str(r)

    return national_id


def clean_mobile_number(number, add_98=False, add_plus=False):
    """Clean mobile number

        Usage::
        >>> from persiantools import utils
        >>> cleaned_number = utils.clean_mobile_number('+989366926847')

    :param number: A string, will be cleaned
    :param add_98: Add country code prefix to the final number
    :param add_plus: Add + prefix to the final number
    :return: str
    """
    number = re.sub('^\+?98', '0', number)
    number = re.sub('^9', '09', number)

    if add_98:
        number = re.sub('^0', '98', number)
        if add_plus:
            number = re.sub('^9', '+9', number)

    return number


def is_valid_mobile_number(number):
    """Check whether the number is valid mobile number or not

        Usage::
        >>> from persiantools import utils
        >>> is_valid = utils.is_valid_mobile_number('093432212121212')

    :param number: A mobile number, will be checked for validation
    :return: boolean
    """
    if not number:
        return False

    pattern = re.compile('^(\+?98|0?)9[0-3|9]\d{8}$')
    if not pattern.match(number):
        return False

    return True
