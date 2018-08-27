# -*- coding: utf-8 -*-
from persiantools import utils

EN_FA_MAP = {
    '0': '۰',
    '1': '۱',
    '2': '۲',
    '3': '۳',
    '4': '۴',
    '5': '۵',
    '6': '۶',
    '7': '۷',
    '8': '۸',
    '9': '۹'
}

AR_FA_MAP = {
    '٠': '۰',
    '١': '۱',
    '٢': '۲',
    '٣': '۳',
    '٤': '۴',
    '٥': '۵',
    '٦': '۶',
    '٧': '۷',
    '٨': '۸',
    '٩': '۹'
}

AR_EN_MAP = {
    '٠': '0',
    '١': '1',
    '٢': '2',
    '٣': '3',
    '٤': '4',
    '٥': '5',
    '٦': '6',
    '٧': '7',
    '٨': '8',
    '٩': '9'
}


def en_to_fa(string):
    """Convert EN digits to Persian

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.en_to_fa("0123456789")

        :param string:  A string, will be converted
        :rtype: str
    """

    return utils.replace(string, EN_FA_MAP)


def fa_to_en(string):
    """Convert Persian digits to EN

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.fa_to_en("۰۱۲۳۴۵۶۷۸۹")

        :param string: A string, will be converted
        :rtype: str
        """
    fa_to_en_map = dict((x, y) for (y, x) in EN_FA_MAP.items())

    return utils.replace(string, fa_to_en_map)


def ar_to_fa(string):
    """Convert Arabic digits to Persian

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.ar_to_fa("٠١٢٣٤٥٦٧٨٩")

        :param string: A string, will be converted
        :rtype: str
        """

    return utils.replace(string, AR_FA_MAP)


def fa_to_ar(string):
    """Convert Persian digits to Arabic

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.fa_to_ar("۰۱۲۳۴۵۶۷۸۹")

        :param string: A string, will be converted
        :rtype: str
        """
    fa_to_ar_map = dict((x, y) for (y, x) in AR_FA_MAP.items())

    return utils.replace(string, fa_to_ar_map)


def ar_to_en(string):
    """Convert Arabic digits to EN

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.ar_to_en("٠١٢٣٤٥٦٧٨٩")

        :param string: A string, will be converted
        :rtype: str
        """

    return utils.replace(string, AR_EN_MAP)


def en_to_ar(string):
    """Convert EN digits to Arabic

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.en_to_ar("0123456789")

        :param string: A string, will be converted
        :rtype: str
        """
    en_to_ar_map = dict((x, y) for (y, x) in AR_EN_MAP.items())

    return utils.replace(string, en_to_ar_map)


def to_fa(string):
    """Convert digits to Persian

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.to_fa("0123456789٠١٢٣٤٥٦٧٨٩")

        :param string: A string, will be converted
        :rtype: str
        """
    return en_to_fa(ar_to_en(string))


def to_en(string):
    """Convert digits to EN

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.to_en("۰۱۲۳۴۵۶۷۸۹٠١٢٣٤٥٦٧٨٩")

        :param string: A string, will be converted
        :rtype: str
        """
    return fa_to_en(ar_to_fa(string))


def to_ar(string):
    """Convert digits to Arabic

        Usage::
        >>> from persiantools import digits
        >>> converted = digits.to_en("۰۱۲۳۴۵۶۷۸۹0123456789")

        :param string: A string, will be converted
        :rtype: str
        """
    return fa_to_ar(en_to_fa(string))
