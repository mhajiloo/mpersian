# -*- coding: utf-8 -*-
from unittest import TestCase
import pytest

from persiantools import characters
from persiantools import digits


class TestDigits(TestCase):
    def test_ar_to_fa(self):
        self.assertEqual(characters.ar_to_fa("السلام عليكم"), "السلام علیکم")
        self.assertEqual(characters.ar_to_fa("HI ي"), "HI ی")
        self.assertEqual(
            characters.ar_to_fa("دِ بِ زِ ذِ شِ سِ ى ي ك"), "د ب ز ذ ش س ی ی ک"
        )
        self.assertEqual(
            characters.ar_to_fa(u"دِ بِ زِ ذِ شِ سِ ى ي ك"), u"د ب ز ذ ش س ی ی ک"
        )
        self.assertEqual(
            characters.ar_to_fa(
                "ظ ط ذ د ز ر و ، . ش س ي ب ل ا ت ن م ك ض ص ث ق ف غ ع ه خ ح ؟"
            ),
            "ظ ط ذ د ز ر و ، . ش س ی ب ل ا ت ن م ک ض ص ث ق ف غ ع ه خ ح ؟",
        )

        with pytest.raises(TypeError):
            characters.ar_to_fa(12345)

        orig = "السلام عليكم ٠١٢٣٤٥٦٧٨٩"
        converted = characters.ar_to_fa(orig)
        converted = digits.ar_to_fa(converted)
        self.assertEqual(converted, "السلام علیکم ۰۱۲۳۴۵۶۷۸۹")

    def test_fa_to_fa(self):
        self.assertEqual(characters.ar_to_fa("السلام علیکم"), "السلام علیکم")
        self.assertEqual(characters.ar_to_fa(u"السلام علیکم"), u"السلام علیکم")

    def test_fa_to_ar(self):
        self.assertEqual(characters.fa_to_ar("کیک"), "كيك")

        with pytest.raises(TypeError):
            characters.ar_to_fa(12345)
