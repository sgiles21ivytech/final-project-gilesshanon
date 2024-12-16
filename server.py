from flask import Flask, render_template, request, session, redirect
from menu import menu

app = Flask(__name__)
app.secret_key = '0@7!gV185dl06Sm30A'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def display_menu():
    return render_template("menu.html", menu=menu)

@app.route("/cart", methods=["POST"])
def add_to_cart():
    cart_items = request.form
    if 'cart' not in session:
        session['cart'] = {}

    # Add items to cart
    for item in cart_items:
        if cart_items[item] == "1":  # Only add items with checkbox checked
            session['cart'][item] = session['cart'].get(item, 0) + 1

    session.modified = True  # Mark session as modified
    return redirect('/cart')





@app.route("/cart")
def view_cart():
    print("Cart session:", session.get('cart'))  # Debug print
    if 'cart' not in session:
        session['cart'] = {}
    cart_items = session['cart']
    total_cost = 0  # Initialize total cost to 0
    cart_display = []  # For displaying items in the cart

    # Loop through the cart and calculate total cost
    for item, quantity in cart_items.items():
        for category in menu.values():
            if item in category:
                price = category[item]
                if isinstance(price, str):  # Handle price ranges
                    price = float(price.split(" - ")[0])  # Take the first price in the range
                total_cost += price * quantity
                cart_display.append({
                    "item": item,
                    "price": price,
                    "quantity": quantity,
                    "total": price * quantity
                })

    return render_template("cart.html", cart_items=cart_display, total_cost=total_cost)





@app.route("/order", methods=["POST"])
def place_order():
    cart_items = session.get('cart', {})
    total_cost = 0  # Initialize total cost

    for item, quantity in cart_items.items():
        for category in menu.values():
            if item in category:
                price = category[item]
                if isinstance(price, str):  # Handle price ranges
                    price = float(price.split(" - ")[0])  # Take the first price in the range
                total_cost += price * quantity

    session.pop('cart', None)  # Clear the cart after order is placed

    # Pass menu to the template
    return render_template(
        "order_confirmation.html",
        cart_items=cart_items,
        total_cost=total_cost,
        menu=menu  # Include the menu dictionary
    )


if __name__ == '__main__':
    app.run(debug=True)



