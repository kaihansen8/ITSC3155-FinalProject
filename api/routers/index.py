from . import orders, order_details, payment_information, promo_codes, resources, customers, recipes, reviews, sandwiches


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(payment_information.router)
    app.include_router(promo_codes.router)
    app.include_router(resources.router)
    app.include_router(customers.router)
    app.include_router(recipes.router)
    app.include_router(sandwiches.router)
    app.include_router(reviews.router)