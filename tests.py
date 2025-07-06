import unittest
from credit_card_validator import credit_card_validator

class TestCreditCardValidator(unittest.TestCase):

    """ VALID PREFIXES AT BOUNDARY """
    """ testing valid card combinations using boundary value testing for the prefixes """
    
    """ valid visa w prefix 4, length 16, and correct luhn """
    def test_visa_prefix_4(self):
        self.assertTrue(credit_card_validator("4111111111111111")) 

    """ valid mastercards with prefixes 51 & 55, len 16, correct luhn """
    def test_mastercard_prefix_51_55(self):
        self.assertTrue(credit_card_validator("5100000000000004")) """ BUG FOUND """
        self.assertTrue(credit_card_validator("5500000000000008")) """ BUG FOUND """

    """ valid mastercards with prefixes 2221 & 2720, length 16, correct luhn """
    def test_mastercard_prefix_2221_2720(self):
        self.assertTrue(credit_card_validator("2221000000000009")) """ BUG FOUND """
        self.assertTrue(credit_card_validator("2720990000000003")) """ BUG FOUND """

    """ valid american express with prefixes 34 & 37, length 15, correct luhn """
    def test_amex_prefix_34_37(self):
        self.assertTrue(credit_card_validator("340000000000009")) 
        self.assertTrue(credit_card_validator("370000000000002")) 
        

    """ INVALID PREFIXES NEAR BOUNDARY """
    """ boundary value testing using edge cases / error guessing for invalid prefixes """
    def test_invalid_prefixes(self):
        """ visa edge case/error guess for prefix 4 """
        self.assertFalse(credit_card_validator("3000000000000004")) 
        """ visa & mastercard edge case/error guess for prefix 4 & 51 """
        self.assertFalse(credit_card_validator("5000000000000009")) 
        """ mastercard edge case for prefix 55"""
        self.assertFalse(credit_card_validator("5600000000000003")) 
        """ mastercard edge case for prefix 2221 """
        self.assertFalse(credit_card_validator("2220000000000000")) 
        """ mastercard edge case for prefix 2720 """
        self.assertFalse(credit_card_validator("2721000000000004")) 
        """ amex edge cases for prefix 34 """
        self.assertFalse(credit_card_validator("330000000000001"))
        self.assertFalse(credit_card_validator("350000000000006"))
        """ amex edge cases for prefix 37 """
        self.assertFalse(credit_card_validator("360000000000004"))
        self.assertFalse(credit_card_validator("380000000000000"))
        
    """ INVALID LENGTH - BOUNDARY VALUE TESTING  """
    """ edge case testing/boundary value testing for invalid lengths w/ valid prefixes"""
    def test_invalid_length(self):
        """ visa edge case length 15 (bad checksum) """
        self.assertFalse(credit_card_validator("411111111111111")) """ BUG FOUND """
        """ visa edge case length 15 (valid checksum) """
        self.assertFalse(credit_card_validator("411111111111116"))
        """ visa edge case length 17 (bad checksum)"""
        self.assertFalse(credit_card_validator("41111111111111111"))
        """ visa edge case length 17 (valid checksum)"""
        self.assertFalse(credit_card_validator("41111111111111113"))
        """ mastercard edge case length 15 (bad checksum) """
        self.assertFalse(credit_card_validator("550000000000000"))   
        """ mastercard edge case length 15 (valid checksum) """
        self.assertFalse(credit_card_validator("550000000000004"))  
        """ mastercard edge case length 17 (bad checksum)"""
        self.assertFalse(credit_card_validator("55000000000000044"))
        """ mastercard edge case length 17 (valid checksum)"""
        self.assertFalse(credit_card_validator("55000000000000046"))
        """ amex edge case length 14 (bad checksum)"""
        self.assertFalse(credit_card_validator("34000000000003"))
        """ amex edge case length 14 (valid checksum)"""
        self.assertFalse(credit_card_validator("34000000000000"))
        """ amex edge case length 16 (bad checksum) """
        self.assertFalse(credit_card_validator("3400000000000009")) """ BUG FOUND """
        """ amex edge case length 16 (valid checksum) """
        self.assertFalse(credit_card_validator("3400000000000000"))
        
        
    """ BAD LUHN DIGIT """
    def test_invalid_luhn(self):
        self.assertFalse(credit_card_validator("4111111111111112"))  """ Visa """
        self.assertFalse(credit_card_validator("5500000000000005"))  """ MasterCard BUG FOUND """
        self.assertFalse(credit_card_validator("2221000000000008"))  """ MasterCard """
        self.assertFalse(credit_card_validator("340000000000001"))   """ AmEx """
        self.assertFalse(credit_card_validator("370000000000003"))   """ AmEx """

if __name__ == '__main__':
    unittest.main()
