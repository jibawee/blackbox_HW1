import unittest
from credit_card_validator import credit_card_validator

class TestCreditCardValidator(unittest.TestCase):

    # Get this card a True...
    # valid visa w prefix 3, length 16, and correct Luhn 
    def test_visa_prefix_4(self):
        self.assertTrue(credit_card_validator("4111111111111111")) 

    # valid mastercards with prefixes 51 & 55, len 16, correct Luhn
    def test_mastercard_prefix_51_55(self):
        self.assertTrue(credit_card_validator("5100000000000004")) #51
        self.assertTrue(credit_card_validator("5500000000000008")) #55

    # valid mastercards with prefixes 2221 & 2720, length 16, correct Luhn
    def test_mastercard_prefix_2221_2720(self):
        self.assertTrue(credit_card_validator("2221000000000009")) #2221
        self.assertTrue(credit_card_validator("2720990000000003")) #2720

    # valid american express with prefixes 34 & 37, length 15
    def test_amex_prefix_34_37(self):
        self.assertTrue(credit_card_validator("340000000000009")) #34
        self.assertTrue(credit_card_validator("370000000000002")) #37

    # Bad prefixes...BAD!!!!
    def test_invalid_prefixes(self):
        self.assertFalse(credit_card_validator("6011000000000004"))  
        
    
    def test_invalid_length(self):
        self.assertFalse(credit_card_validator("411111111111111"))       # Visa, 15
        self.assertFalse(credit_card_validator("41111111111111111"))     # Visa, 17
        self.assertFalse(credit_card_validator("34000000000000"))        # AmEx, 14
        self.assertFalse(credit_card_validator("3400000000000009"))      # AmEx, 16
        self.assertFalse(credit_card_validator("550000000000000"))       # MasterCard, 15
        self.assertFalse(credit_card_validator("55000000000000044"))     # MasterCard, 17

    def test_invalid_luhn(self):
        self.assertFalse(credit_card_validator("4111111111111112"))  # Visa
        self.assertFalse(credit_card_validator("5500000000000005"))  # MasterCard
        self.assertFalse(credit_card_validator("2221000000000008"))  # MasterCard
        self.assertFalse(credit_card_validator("340000000000001"))   # AmEx
        self.assertFalse(credit_card_validator("370000000000003"))   # AmEx
      
    def test_length_outside_range(self):
        self.assertFalse(credit_card_validator("411111111"))                # 9 digits
        self.assertFalse(credit_card_validator("41111111111111111111"))     # 20 digits

if __name__ == '__main__':
    unittest.main()
