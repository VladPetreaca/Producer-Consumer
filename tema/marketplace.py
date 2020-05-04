"""
This module represents the Marketplace.

Computer Systems Architecture Course
Assignment 1
March 2020
"""


class Marketplace:
    """
    Class that represents the Marketplace. It's the central part of the implementation.
    The producers and consumers use its methods concurrently.
    """
    def __init__(self, queue_size_per_producer):
        """
        Constructor

        :type queue_size_per_producer: Int
        :param queue_size_per_producer: the maximum size of a queue associated with each producer
        """

        self.queue_size = queue_size_per_producer
        self.list_of_carts = []
        self.list_of_producers = []
        # pass

    def register_producer(self):
        """
        Returns an id for the producer that calls this.
        """
        # create an id by given the length of the specified list
        id_prod = self.list_of_producers.__len__()

        # put a list with the id in the list_of_producers
        self.list_of_producers.append([id_prod])
        return id_prod

    def publish(self, producer_id, product):
        """
        Adds the product provided by the producer to the marketplace

        :type producer_id: String
        :param producer_id: producer id

        :type product: Product
        :param product: the Product that will be published in the Marketplace

        :returns True or False. If the caller receives False, it should wait and then try again.
        """
        # check if a specified producer can produce a product
        # if he can, add the product in her list
        for i in self.list_of_producers:
            if producer_id == i[0]:
                if len(self.list_of_producers[producer_id]) <= self.queue_size + 1:
                    self.list_of_producers[producer_id].append(product)
                    return True

        return False

    def new_cart(self):
        """
        Creates a new cart for the consumer

        :returns an int representing the cart_id
        """
        # create an id by given the length of the specified list
        id_cart = self.list_of_carts.__len__()

        # put a list with the id in the list_of_carts
        self.list_of_carts.append([id_cart])
        return id_cart

    def add_to_cart(self, cart_id, product):
        """
        Adds a product to the given cart. The method returns

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to add to cart

        :returns True or False. If the caller receives False, it should wait and then try again
        """

        # check if a "shelf" of a producer contain the specified product
        # if it has, i will remove the product from producer's list
        # and add a tuple as (id_producer, product) in a specified cart
        for prod in self.list_of_producers:
            for j in prod[1:]:
                if j == product:
                    prod.remove(j)
                    for k in self.list_of_carts:
                        if cart_id == k[0]:
                            aux_list = [prod[0], product]
                            self.list_of_carts[k[0]].append(tuple(aux_list))
                            return True
        return False

    def remove_from_cart(self, cart_id, product):
        """
        Removes a product from cart.

        :type cart_id: Int
        :param cart_id: id cart

        :type product: Product
        :param product: the product to remove from cart
        """
        # search the specified product in the specified cart and remove him
        # search the producer to put the product on her "shelf"
        # return True in both case or pylint :)
        for cart in self.list_of_carts:
            if cart[0] == cart_id:
                for prod in cart[1:]:
                    if product == prod[1]:
                        cart.remove(prod)
                        for k in self.list_of_producers:
                            if k[0] == prod[0]:
                                self.list_of_producers[k[0]].append(prod[1])
                                return True
        return True

    def place_order(self, cart_id):
        """
        Return a list with all the products in the cart.

        :type cart_id: Int
        :param cart_id: id cart
        """
        # return a list with products from a specified cart

        result = []

        for i in self.list_of_carts[cart_id][1:]:
            result.append(i[1])

        return result
