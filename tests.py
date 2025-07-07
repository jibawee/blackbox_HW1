import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    # REJECT EMPTY STRING - ERROR GUESSING

    def test_reject_empty_string(self):
        self.assertFalse(credit_card_validator(""))  # BUG 1

    def test_valid_prefix_too_short(self):
        self.assertFalse(credit_card_validator("4"))
        self.assertFalse(credit_card_validator("51"))
        self.assertFalse(credit_card_validator("34"))

    # VALID PREFIXES AT BOUNDARY

    def test_valid_visa_prefix_4(self):
        """Valid Visa with prefix 4, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("4111111111111111"))  # BUG 2

    def test_valid_mastercard_prefix_51(self):
        """Valid MasterCard with prefix 51, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("5100000000000004"))

    def test_valid_mastercard_prefix_55(self):
        """Valid MasterCard with prefix 55, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("5500000000000008"))

    def test_valid_mastercard_prefix_53(self):
        """Valid MasterCard with prefix 53 (in between), length 16, correct checksum"""
        self.assertTrue(credit_card_validator("5300000000000006"))  # BUG 4

    def test_valid_mastercard_prefix_2221(self):
        """Valid MasterCard with prefix 2221, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2221000000000009"))  # BUG 4

    def test_valid_mastercard_prefix_2720(self):
        """Valid MasterCard with prefix 2720, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2720990000000007"))

    def test_valid_mastercard_prefix_2500(self):
        self.assertTrue(credit_card_validator("2500000000000006"))  # Luhn-valid

    def test_valid_mastercard_prefix_2222(self):
        """Valid MasterCard with prefix 2222, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2222000000000008"))  # BUG 4

    def test_valid_mastercard_prefix_2719(self):
        """Valid MasterCard with prefix 2719, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2719000000000008"))  # BUG 4

    def test_valid_amex_prefix_34(self):
        """Valid American Express with prefix 34, length 15, correct checksum"""
        self.assertTrue(credit_card_validator("340000000000009"))  # BUG 10

    def test_valid_amex_prefix_37(self):
        """Valid American Express with prefix 37, length 15, correct checksum"""
        self.assertTrue(credit_card_validator("370000000000002"))  # BUG 10

    # INVALID PREFIXES NEAR BOUNDARY

    def test_invalid_prefix_300(self):
        self.assertFalse(credit_card_validator("3000000000000004"))

    def test_invalid_prefix_500(self):
        self.assertFalse(credit_card_validator("5000000000000009"))

    def test_invalid_prefix_560(self):
        self.assertFalse(credit_card_validator("5600000000000003"))

    def test_invalid_prefix_2220(self):
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test_invalid_prefix_2721(self):
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test_invalid_prefix_330(self):
        self.assertFalse(credit_card_validator("330000000000001"))  # BUG 5

    def test_invalid_prefix_350(self):
        self.assertFalse(credit_card_validator("350000000000006"))  # BUG 5

    def test_invalid_prefix_360(self):
        self.assertFalse(credit_card_validator("360000000000004"))  # BUG 5

    def test_invalid_prefix_380(self):
        self.assertFalse(credit_card_validator("380000000000000"))  # BUG 5

    # INVALID LENGTH AND INVALID CHECKSUM

    def test_invalid_visa_length_15(self):
        self.assertFalse(credit_card_validator("411111111111111"))

    def test_invalid_visa_length_17(self):
        self.assertFalse(credit_card_validator("41111111111111111"))

    def test_invalid_mastercard_length_15(self):
        self.assertFalse(credit_card_validator("550000000000000"))

    def test_invalid_mastercard_length_17(self):
        self.assertFalse(credit_card_validator("55000000000000044"))

    def test_invalid_amex_length_14(self):
        self.assertFalse(credit_card_validator("34000000000003"))

    def test_invalid_amex_length_16(self):
        self.assertFalse(credit_card_validator("3400000000000009"))

    # INVALID LENGTH WITH VALID CHECKSUM

    def test_invalid_visa_length_15_valid_checksum(self):
        self.assertFalse(credit_card_validator("411111111111116"))  # BUG 6

    def test_invalid_visa_length_17_valid_checksum(self):
        self.assertFalse(credit_card_validator("41111111111111113"))  # BUG 6

    def test_invalid_mastercard_length_15_valid_checksum(self):
        self.assertFalse(credit_card_validator("550000000000004"))  # BUG 8

    def test_invalid_mastercard_length_17_valid_checksum(self):
        self.assertFalse(credit_card_validator("55000000000000046"))  # BUG 4

    def test_invalid_amex_length_14_valid_checksum(self):
        self.assertFalse(credit_card_validator("34000000000000"))

    def test_invalid_amex_length_16_valid_checksum(self):
        self.assertFalse(credit_card_validator("3400000000000000"))  # BUG 7

    # INVALID CHECKSUM WITH VALID LENGTH & PREFIX

    def test_invalid_visa_checksum_1(self):
        self.assertFalse(credit_card_validator("4000000000000001"))

    def test_invalid_visa_checksum_3(self):
        self.assertFalse(credit_card_validator("4000000000000003"))

    def test_invalid_mastercard_checksum_3(self):
        self.assertFalse(credit_card_validator("5500000000000003"))  # BUG 3

    def test_invalid_mastercard_checksum_5(self):
        self.assertFalse(credit_card_validator("5500000000000005"))  # BUG 3

    def test_invalid_mastercard_checksum_7(self):
        self.assertFalse(credit_card_validator("5100000000000007"))  # BUG 3

    def test_invalid_mastercard_checksum_9(self):
        self.assertFalse(credit_card_validator("5100000000000009"))

    def test_invalid_mastercard_checksum_8(self):
        self.assertFalse(credit_card_validator("2221000000000008"))  # BUG 3

    def test_invalid_mastercard_checksum_0(self):
        self.assertFalse(credit_card_validator("2221000000000000"))  # BUG 3

    def test_invalid_mastercard_checksum_4(self):
        self.assertFalse(credit_card_validator("2720000000000004"))

    def test_invalid_mastercard_checksum_6(self):
        self.assertFalse(credit_card_validator("2720000000000006"))

    def test_invalid_amex_checksum_1(self):
        self.assertFalse(credit_card_validator("340000000000001"))

    def test_invalid_amex_checksum_3(self):
        self.assertFalse(credit_card_validator("370000000000003"))


if __name__ == "__main__":
    unittest.main()
