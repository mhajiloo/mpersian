# -*- coding: utf-8 -*-
from unittest import TestCase

from persiantools import utils


class TestUtils(TestCase):
    def test_replace(self):
        self.assertEqual(utils.replace("Persian Tools", {"Persian": "Parsi", " ": "_"}), "Parsi_Tools")
        self.assertEqual(utils.replace("آب بی فلسفه می‌خوردم", {"آب": "آآآب", " ": "_"}), "آآآب_بی_فلسفه_می‌خوردم")

    def test_int_valid_data(self):
        self.assertEqual(utils.check_int_field(100010001), 100010001)

    def test_int_invalid_data_float(self):
        with self.assertRaises(TypeError):
            utils.check_int_field(1111.9999)

    def test_int_invalid_data_string(self):
        with self.assertRaises(TypeError):
            utils.check_int_field("1000")

    def test_is_valid_national_valid_data(self):
        self.assertTrue(utils.is_valid_national_id('3934540414'))

    def test_is_valid_national_id_invalid_data(self):
        self.assertFalse(utils.is_valid_national_id('3934540413'))

    def test_generate_random_national_id(self):
        self.assertTrue(utils.is_valid_national_id(utils.generate_random_national_id()))

    def test_clean_mobile_number(self):
        self.assertEqual(utils.clean_mobile_number('9366926847'), '09366926847')
        self.assertEqual(utils.clean_mobile_number('09366926847'), '09366926847')
        self.assertEqual(utils.clean_mobile_number('+989366926847'), '09366926847')
        self.assertEqual(utils.clean_mobile_number('989366926847'), '09366926847')

    def test_clean_mobile_number_with_prefix(self):
        self.assertEqual(utils.clean_mobile_number('9366926847', add_98=True), '989366926847')
        self.assertEqual(utils.clean_mobile_number('09366926847', add_98=True), '989366926847')
        self.assertEqual(utils.clean_mobile_number('+989366926847', add_98=True), '989366926847')
        self.assertEqual(utils.clean_mobile_number('989366926847', add_98=True), '989366926847')

    def test_clean_mobile_number_with_plus(self):
        self.assertEqual(utils.clean_mobile_number('9366926847', add_98=True, add_plus=True), '+989366926847')
        self.assertEqual(utils.clean_mobile_number('09366926847', add_98=True, add_plus=True), '+989366926847')
        self.assertEqual(utils.clean_mobile_number('+989366926847', add_98=True, add_plus=True), '+989366926847')
        self.assertEqual(utils.clean_mobile_number('989366926847', add_98=True, add_plus=True), '+989366926847')

    def test_is_valid_mobile_number_valid_data(self):
        self.assertTrue(utils.is_valid_mobile_number('09366926847'))
        self.assertTrue(utils.is_valid_mobile_number('9366926847'))
        self.assertTrue(utils.is_valid_mobile_number('989366926847'))
        self.assertTrue(utils.is_valid_mobile_number('+989366926847'))

    def test_is_valid_mobile_number_invalid_data(self):
        self.assertFalse(utils.is_valid_mobile_number(''))
        self.assertFalse(utils.is_valid_mobile_number('093669268777'))
        self.assertFalse(utils.is_valid_mobile_number('invalid'))
        self.assertFalse(utils.is_valid_mobile_number('+981212121212121212'))
        self.assertFalse(utils.is_valid_mobile_number('0812713232323'))
