import unittest
from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    """VALID PREFIXES AT BOUNDARY"""
    # Testing valid card combinations using boundary value testing for the prefixes

    def test_visa_prefix_4(self):
        """Valid Visa with prefix 4, length 16, and correct checksum"""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test_mastercard_prefix_51_55(self):
        """Valid MasterCards with prefixes 51 & 55, len 16, correct checksum"""
        self.assertTrue(credit_card_validator("5100000000000004"))  
        self.assertTrue(credit_card_validator("5500000000000008"))  

    def test_mastercard_prefix_2221_2720(self):
        """Valid MasterCards with prefixes 2221 & 2720, length 16, correct checksum"""
        self.assertTrue(credit_card_validator("2221000000000009"))  
        self.assertTrue(credit_card_validator("2720990000000007"))  

    def test_amex_prefix_34_37(self):
        """Valid American Express with prefixes 34 & 37, length 15, correct checksum"""
        self.assertTrue(credit_card_validator("340000000000009"))
        self.assertTrue(credit_card_validator("370000000000002"))

    """INVALID PREFIXES NEAR BOUNDARY"""
    # Boundary value testing using edge cases for invalid prefixes w/ valid checksum

    def test_invalid_prefixes(self):
        """Visa edge case for prefix 4"""
        self.assertFalse(credit_card_validator("3000000000000004"))
        """Visa & MasterCard edge case/error guess for prefix 4 & 51"""
        self.assertFalse(credit_card_validator("5000000000000009"))
        """MasterCard edge case for prefix 55"""
        self.assertFalse(credit_card_validator("5600000000000003"))
        """MasterCard edge case for prefix 2221"""
        self.assertFalse(credit_card_validator("2220000000000000"))
        """MasterCard edge case for prefix 2720"""
        self.assertFalse(credit_card_validator("2721000000000004"))
        """AmEx edge cases for prefix 34"""
        self.assertFalse(credit_card_validator("330000000000001"))
        self.assertFalse(credit_card_validator("350000000000006"))
        """AmEx edge cases for prefix 37"""
        self.assertFalse(credit_card_validator("360000000000004"))
        self.assertFalse(credit_card_validator("380000000000000"))

    """INVALID LENGTH - BOUNDARY VALUE TESTING"""
    # Edge case testing/boundary value testing for invalid lengths w/ valid prefixes

    def test_invalid_length(self):
        """Visa edge case length 15 (bad checksum)"""
        self.assertFalse(credit_card_validator("411111111111111"))  
        """Visa edge case length 17 (bad checksum)"""
        self.assertFalse(credit_card_validator("41111111111111111"))
        """MasterCard edge case length 15 (bad checksum)"""
        self.assertFalse(credit_card_validator("550000000000000"))
        """MasterCard edge case length 17 (bad checksum)"""
        self.assertFalse(credit_card_validator("55000000000000044"))
        """AmEx edge case length 14 (bad checksum)"""
        self.assertFalse(credit_card_validator("34000000000003"))
        """AmEx edge case length 16 (bad checksum)"""
        self.assertFalse(credit_card_validator("3400000000000009"))  

    
    def test_invalid_length_Luhn(self):
        """Visa edge case length 15 (valid checksum)"""
        self.assertFalse(credit_card_validator("411111111111116"))
        """Visa edge case length 17 (valid checksum)"""
        self.assertFalse(credit_card_validator("41111111111111113"))
        """MasterCard edge case length 15 (valid checksum)"""
        self.assertFalse(credit_card_validator("550000000000004"))
        """MasterCard edge case length 17 (valid checksum)"""
        self.assertFalse(credit_card_validator("55000000000000046"))
        """AmEx edge case length 14 (valid checksum)"""
        self.assertFalse(credit_card_validator("34000000000000"))
        """AmEx edge case length 16 (valid checksum)"""
        self.assertFalse(credit_card_validator("3400000000000000"))

    """BAD LUHN DIGIT"""
    # Edge case testing/boundary value testing for invalid checksum w/ valid prefixes & length

    def test_invalid_checksum(self):
        """Edge cases for Visa checksum digit"""
        # Visa (checksum = 2)
        self.assertFalse(credit_card_validator("4000000000000001"))  
        self.assertFalse(credit_card_validator("4000000000000003"))
        # MasterCard 
        self.assertFalse(credit_card_validator("5500000000000003"))  
        self.assertFalse(credit_card_validator("5500000000000005"))
        self.assertFalse(credit_card_validator("5100000000000007"))  
        self.assertFalse(credit_card_validator("5100000000000009"))  
        self.assertFalse(credit_card_validator("2221000000000008")) 
        self.assertFalse(credit_card_validator("2221000000000000"))
        self.assertFalse(credit_card_validator("2720000000000004"))
        self.assertFalse(credit_card_validator("2720000000000006"))
        # AmEx
        self.assertFalse(credit_card_validator("340000000000001"))  
        self.assertFalse(credit_card_validator("370000000000003"))   


if __name__ == '__main__':
    unittest.main()
