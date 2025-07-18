import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    # REJECT EMPTY STRING - ERROR GUESSING

    def test_reject_empty_string(self):
        """Empty Input"""
        self.assertFalse(credit_card_validator(""))

    # VALID PREFIXES AT BOUNDARY/EDGE

    def test_valid_visa_prefix_4(self):
        """Valid Visa with prefix 4, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test_valid_mastercard_prefix_51(self):
        """Valid MasterCard with prefix 51, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("5100000000000008"))

    def test_valid_mastercard_prefix_55(self):
        """Valid MasterCard with prefix 55, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test_valid_mastercard_prefix_53(self):
        """Valid MasterCard with prefix 53 (in between), length 16, correct checksum"""
        self.assertTrue(credit_card_validator("5300000000000006"))

    def test_valid_mastercard_prefix_2221(self):
        """Valid MasterCard with prefix 2221, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_valid_mastercard_prefix_2720(self):
        """Valid MasterCard with prefix 2720, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2720990000000007"))

    def test_valid_mastercard_prefix_2222(self):
        """Valid MasterCard with prefix 2222, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2222000000000008"))

    def test_valid_mastercard_prefix_2719(self):
        """Valid MasterCard with prefix 2719, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2719000000000008"))

    def test_valid_amex_prefix_34(self):
        """Valid American Express with prefix 34, length 15, correct checksum"""
        self.assertTrue(credit_card_validator("340000000000009"))

    def test_valid_amex_prefix_37(self):
        """Valid American Express with prefix 37, length 15, correct checksum"""
        self.assertTrue(credit_card_validator("370000000000002"))

    # INVALID PREFIXES NEAR BOUNDARY WITH VALID LENGTH & CHECKSUM

    def test_invalid_prefix_3(self):
        """Error guess/Edge case for Visa"""
        self.assertFalse(credit_card_validator("3000000000000004"))

    def test_invalid_prefix_50(self):
        """Error guess/Edge case for Mastercard"""
        self.assertFalse(credit_card_validator("5000000000000009"))

    def test_invalid_prefix_56(self):
        """Error guess/Edge case for Mastercard"""
        self.assertFalse(credit_card_validator("5600000000000003"))

    def test_invalid_prefix_2220(self):
        """Error guess/Edge case for Mastercard"""
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test_invalid_prefix_2721(self):
        """Error guess/Edge case for Mastercard"""
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test_invalid_prefix_33(self):
        """Error guess/Edge case for Amex"""
        self.assertFalse(credit_card_validator("330000000000001"))

    def test_invalid_prefix_35(self):
        """Error guess/Edge case for Amex"""
        self.assertFalse(credit_card_validator("350000000000006"))

    def test_invalid_prefix_36(self):
        """Error guess/Edge case for Amex"""
        self.assertFalse(credit_card_validator("360000000000004"))

    def test_invalid_prefix_38(self):
        """Error guess/Edge case for Amex"""
        self.assertFalse(credit_card_validator("380000000000000"))

    # INVALID LENGTH WITH VALID PREFIX & CHECKSUM

    def test_invalid_visa_length_15(self):
        """Error guessing for visa length -1"""
        self.assertFalse(credit_card_validator("411111111111116"))

    def test_invalid_visa_length_17(self):
        """Error guessing for visa length +1"""
        self.assertFalse(credit_card_validator("41111111111111113"))

    def test_invalid_mastercard_length_15(self):
        """Error guessing for mastercard length -1"""
        self.assertFalse(credit_card_validator("550000000000004"))

    def test_invalid_mastercard_length_17(self):
        """Error guessing for mastercard length +1"""
        self.assertFalse(credit_card_validator("55000000000000046"))

    def test_invalid_mastercard_length_15_other_prefix(self):
        """Error guessing for mastercard length -1 other prefixes"""
        self.assertFalse(credit_card_validator("510000000000003"))

    def test_invalid_amex_length_14(self):
        """Error guessing for amex length -1"""
        self.assertFalse(credit_card_validator("370000000000002"))

    def test_invalid_amex_length_16(self):
        """Error guessing for amex length +1"""
        self.assertFalse(credit_card_validator("3400000000000000"))

    # INVALID CHECKSUM WITH VALID LENGTH & PREFIX

    def test_invalid_visa_checksum_1(self):
        """actual checksum is 2 (-1 for boundary testing?)"""
        self.assertFalse(credit_card_validator("4000000000000001"))

    def test_invalid_mastercard_checksum_3(self):
        """actual checksum is 4 (-1 for boundary testing?)"""
        self.assertFalse(credit_card_validator("5500000000000003"))

    def test_invalid_mastercard_checksum_7(self):
        """actual checksum is 8 (-1 for boundary testing?)"""
        self.assertFalse(credit_card_validator("5100000000000007"))


if __name__ == "__main__":
    unittest.main()
