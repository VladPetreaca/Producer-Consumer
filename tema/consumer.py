"""
This module represents the Consumer.

Computer Systems Architecture Course
Assignment 1
March 2020
"""

from threading import Thread
import time


class Consumer(Thread):
    """
    Class that represents a consumer.
    """

    def __init__(self, carts, marketplace, retry_wait_time, **kwargs):
        """
        Constructor.

        :type carts: List
        :param carts: a list of add and remove operations

        :type marketplace: Marketplace
        :param marketplace: a reference to the marketplace

        :type retry_wait_time: Time
        :param retry_wait_time: the number of seconds that a producer must wait
        until the Marketplace becomes available

        :type kwargs:
        :param kwargs: other arguments that are passed to the Thread's __init__()
        """
        self.carts = carts
        self.market = marketplace
        self.re_wait_time = retry_wait_time
        self.cons_id = -1
        self.kwargs = kwargs
        Thread.__init__(self, **kwargs)
        # pass

    def run(self):

        # shopping list for all carts:)
        result = []

        # for a specified action, add/remove a product in/from the cart
        for one_cart in self.carts:
            self.cons_id = self.market.new_cart()

            for operation in one_cart:

                if operation["type"] == "add":
                    for _ in range(0, operation["quantity"]):
                        while not self.market.add_to_cart(self.cons_id, operation["product"]):
                            time.sleep(self.re_wait_time)
                elif operation["type"] == "remove":
                    for _ in range(0, operation["quantity"]):
                        self.market.remove_from_cart(self.cons_id, operation["product"])

            # shopping list from a cart
            products_bought = self.market.place_order(self.cons_id)

            result.append(products_bought)

        # print the purchases
        for i in result:
            for j in i:
                print(self.kwargs["name"] + " bought " + str(j))
