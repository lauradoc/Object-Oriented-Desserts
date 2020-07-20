"""Dessert classes."""


class Cupcake:
    """A cupcake."""
    cache = {}

    def __init__(self, name, flavor, price):

      self.name = name
      self.flavor = flavor
      self.price = price
      self.qty = 0
      self.cache[self.name] = self

    def add_stock(self, amount):

      self.qty += amount

    def sell(self, amount):

      if self.qty == 0:
        print('Sorry, these cupcakes are sold out')

      if amount > self.qty:
        self.qty = 0

      else:
        self.qty = self.qty - amount

    def __repr__(self):
        """Human-readable printout for debugging."""

        return f'<Cupcake name="{self.name}" qty={self.qty}>'

    @staticmethod
    def scale_recipe(ingredients, amount):

      ingredients_scaled = []

      for ingredient in ingredients:
        ingredient_tuple = (ingredient[0], (ingredient[1] * amount))
        ingredients_scaled.append(ingredient_tuple)

      return ingredients_scaled

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
