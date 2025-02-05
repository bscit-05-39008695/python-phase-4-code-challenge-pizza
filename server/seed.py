from app import app, db
from models import Restaurant, Pizza, RestaurantPizza

def seed_database():
    # Clear existing data
    RestaurantPizza.query.delete()
    Restaurant.query.delete()
    Pizza.query.delete()

    # Create Restaurants
    restaurants = [
        Restaurant(name="Karen's Pizza Shack", address="address1"),
        Restaurant(name="Sanjay's Pizza", address="address2"),
        Restaurant(name="Kiki's Pizza", address="address3")
    ]
    db.session.add_all(restaurants)
    db.session.commit()

    # Create Pizzas
    pizzas = [
        Pizza(name="Emma", ingredients="Dough, Tomato Sauce, Cheese"),
        Pizza(name="Geri", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni"),
        Pizza(name="Melanie", ingredients="Dough, Sauce, Ricotta, Red peppers, Mustard")
    ]
    db.session.add_all(pizzas)
    db.session.commit()

    # Create RestaurantPizzas
    restaurant_pizzas = [
        RestaurantPizza(restaurant=restaurants[0], pizza=pizzas[0], price=15),
        RestaurantPizza(restaurant=restaurants[1], pizza=pizzas[1], price=20),
        RestaurantPizza(restaurant=restaurants[2], pizza=pizzas[2], price=10)
    ]
    db.session.add_all(restaurant_pizzas)
    db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        seed_database()
        print("Database seeded successfully!")