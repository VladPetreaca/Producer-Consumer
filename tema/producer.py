"""
This module represents the Producer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time


class Producer(Thread):
    """
    Class that represents a producer.
    """

    def __init__(self, products, marketplace, republish_wait_time, **kwargs):
        """
        Constructor.

        @type products: List()
        @param products: a list of products that the producer will produce

        @type marketplace: Marketplace
        @param marketplace: a reference to the marketplace

        @type republish_wait_time: Time
        @param republish_wait_time: the number of seconds that a producer must
        wait until the marketplace becomes available

        @type kwargs:
        @param kwargs: other arguments that are passed to the Thread's __init__()
        """
        self.products = products
        self.market = marketplace
        self.re_wait_time = republish_wait_time
        self.id_prod = -1
        Thread.__init__(self, **kwargs)

    def run(self):

        # get a id for the producer
        self.id_prod = self.market.register_producer()

        # while the shelf for every producer is accessible, put the products on it
        # wait a specified time for every product
        while True:
            for products in self.products:
                for _ in range(0, products[1]):
                    while not self.market.publish(self.id_prod, products[0]):
                        time.sleep(self.re_wait_time)
                    time.sleep(products[2])
