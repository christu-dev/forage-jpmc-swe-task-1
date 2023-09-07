import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        # getDataPoint returns stock, bid price, ask price, and price (calculated as the avg between bid and ask price)
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        # dummy data in quotes always has ask price greater than bid price, but assertion check is the same
        for quote in quotes:
            self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                                   (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

    """ ------------ Add more unit tests ------------ """

    # write 3 getRatio tests (import at top) one fake one and 2 edge ones
    def test_getRatio_PriceAIsZero(self):
        # expected ratio is 0
        self.assertEqual(0, getRatio(0, 120.84))

    def test_getRatio_PriceBIsZero(self):
        self.assertEqual(None, getRatio(120.84, 0))

    def test_getRatio_calculateRatio_1_to_1(self):
        self.assertEqual(1, getRatio(120.84, 120.84))

    def test_getRatio_calculateRatio_ATwiceOfB(self):
        self.assertEqual(2, getRatio(200, 100))

    def test_getRatio_calculateRatio_BTwiceOfA(self):
        self.assertEqual(0.5, getRatio(100,200))

    def test_getRatio_calculateRatio_AGreaterThanB(self):
        self.assertEqual(1.25, getRatio(125, 100))

    def test_getRatio_calculateRatio_BGreaterThanA(self):
        self.assertEqual(0.75, getRatio(75, 100))


if __name__ == '__main__':
    unittest.main()
