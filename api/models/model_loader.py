from . import orders, order_details, recipes, sandwiches, resources, payment_information, promo_codes, customers, reviews

from ..dependencies.database import engine


def index():
    customers.Base.metadata.create_all(engine)
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)
    sandwiches.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    payment_information.Base.metadata.create_all(engine)
    promo_codes.Base.metadata.create_all(engine)
    reviews.Base.metadata.create_all(engine)