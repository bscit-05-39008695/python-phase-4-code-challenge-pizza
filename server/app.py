from flask import Flask, make_response, jsonify, request
from flask_migrate import Migrate
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)
db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = db.session.get(Restaurant, id)  # Replaced .get() with session.get()
    if not restaurant:
        return make_response(
            jsonify({"error": "Restaurant not found"}),
            404
        )
    return jsonify(restaurant.to_dict(include_restaurant_pizzas=True))

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = db.session.get(Restaurant, id)  # Replaced .get() with session.get()
    if not restaurant:
        return make_response(
            jsonify({"error": "Restaurant not found"}),
            404
        )
    
    db.session.delete(restaurant)
    db.session.commit()
    
    return make_response('', 204)

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    return jsonify([pizza.to_dict() for pizza in pizzas])

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    try:
        data = request.get_json()

        restaurant = Restaurant.query.get(data.get('restaurant_id'))
        pizza = Pizza.query.get(data.get('pizza_id'))

        if not restaurant or not pizza:
            return make_response(
                jsonify({"errors": ["Restaurant or Pizza not found"]}),
                404
            )

        # Check if the price is valid before creating RestaurantPizza
        price = data.get('price')
        if not 1 <= price <= 30:
            return make_response(
                jsonify({"errors": ["validation errors"]}),
                400
            )

        restaurant_pizza = RestaurantPizza(
            price=price,
            restaurant_id=data.get('restaurant_id'),
            pizza_id=data.get('pizza_id')
        )

        db.session.add(restaurant_pizza)
        db.session.commit()

        response_data = {
            "id": restaurant_pizza.id,
            "price": restaurant_pizza.price,
            "pizza_id": restaurant_pizza.pizza_id,
            "restaurant_id": restaurant_pizza.restaurant_id,
            "pizza": restaurant_pizza.pizza.to_dict(),
            "restaurant": restaurant_pizza.restaurant.to_dict()
        }

        return jsonify(response_data), 201

    except ValueError as e:
        return make_response(
            jsonify({"errors": ["validation errors"]}),
            400
        )

if __name__ == '__main__':
    app.run(port=5555, debug=True)

