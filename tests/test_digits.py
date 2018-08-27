# -*- coding: utf-8 -*-

from unittest import TestCase

from persiantools import digits


class TestDigits(TestCase):
    def test_en_to_fa(self):
        self.assertEqual(digits.en_to_fa("0987654321"), "۰۹۸۷۶۵۴۳۲۱")

    def test_fa_to_en(self):
        self.assertEqual(digits.fa_to_en("۰۹۸۷۶۵۴۳۲۱"), "0987654321")

    def test_ar_to_fa(self):
        self.assertEqual(digits.ar_to_fa("٠٩٨٧٦٥٤٣٢١"), "۰۹۸۷۶۵۴۳۲۱")

    def test_fa_to_ar(self):
        self.assertEqual(digits.fa_to_ar("۰۹۸۷۶۵۴۳۲۱"), "٠٩٨٧٦٥٤٣٢١")

    def test_en_to_ar(self):
        self.assertEqual(digits.en_to_ar("0987654321"), "٠٩٨٧٦٥٤٣٢١")

    def test_ar_to_en(self):
        self.assertEqual(digits.ar_to_en("٠٩٨٧٦٥٤٣٢١"), "0987654321")

    def test_to_fa(self):
        self.assertEqual(digits.to_fa("0987٦٥٤۳۲۱"), "۰۹۸۷۶۵۴۳۲۱")

    def test_to_en(self):
        self.assertEqual(digits.to_en("0987٦٥٤۳۲۱"), "0987654321")

    def test_to_ar(self):
        self.assertEqual(digits.to_ar("0987٦٥٤۳۲۱"), "٠٩٨٧٦٥٤٣٢١")

    def test_fa_to_fa(self):
        self.assertEqual(digits.en_to_fa("۰۹۸۷۶۵۴۳۲۱"), "۰۹۸۷۶۵۴۳۲۱")

    def test_to_en_with_non_digits(self):
        self.assertEqual(digits.to_en("aذ0987٦٥٤۳۲۱"), "aذ0987654321")

    def test_int_arg(self):
        with self.assertRaises(ValueError):
            digits.en_to_fa(12345)
