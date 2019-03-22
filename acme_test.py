import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_stealability(self):
        """Test stealability() method."""
        prod = Product('Test Product')
        self.assertEqual(prod.stealability(), 'Kinda stealable.')
            

    def test_explode(self):
        """Test explode() method."""
        prod = Product('Test Product')
        self.assertEqual(prod.explode(), '...boom!')

class AcmeReportTests(unittest.TestCase):
    """ Test that generate_products returns 30 results by default """
    def test_default_num_products(self):
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        """ Tests if the names are in the appropriate format """
        # valid lists of adjectives and nouns
        adjectives = set(['Awesome', 'Shiny', 'Impressive', 'Portable',
                         'Improved'])
        nouns = set(['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???'])
        # generate product names from report
        products = generate_products()
        # split into adjectives and nouns
        bad_adjectives = [prod.name.split()[0] for prod in products
            if prod.name.split()[0] not in adjectives]
        bad_nouns = [prod.name.split()[1] for prod in products
            if prod.name.split()[1] not in nouns]
        self.assertEqual(len(bad_adjectives), 0)
        self.assertEqual(len(bad_nouns), 0)



if __name__ == '__main__':
    unittest.main()