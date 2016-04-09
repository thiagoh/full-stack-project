import sys
import json

from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect
from connect import Base, Restaurant, MenuItem, session_creator

app = Flask(__name__)

@app.route('/')
def index():
    return "index"

@app.route('/hello')
def hello():
    return "Hello World"

@app.route('/nha')
def nha():
    return "hu"

@app.route('/restaurant/<int:id>')
def get_restaurant(id):

    s = None
    try:

        s = session_creator()

        restaurant = s.query(Restaurant).filter(Restaurant.id == id).first()
        items = []

        if restaurant != None:
            items = s.query(MenuItem).filter(MenuItem.restaurant == restaurant)

        # if restaurant == None:
        #     raise Exception("No such restaurant for id " + id)

        return render_template('restaurant.html', restaurant=restaurant, items=items)

    except Exception as e:
        if s != None: s.close()
        raise e


#Task 1: Create route for newMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/new', methods=['GET', 'POST'])
def newMenuItem(restaurant_id):

    restaurant = None
    s = None

    try:

        s = session_creator()
        restaurant = s.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

        if request.method == 'POST':
            new_item = MenuItem(name=request.form['name'], restaurant_id = restaurant_id)
            s.add(new_item)
            s.commit()
            return redirect(url_for('get_restaurant', id=restaurant_id))

        return render_template('new_menu_item.html', restaurant=restaurant)

    except Exception, e:
        if s != None: s.close()
        raise e


#Task 2: Create route for editMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit/')
def editMenuItem(restaurant_id, menu_id):
    return "page to edit a new menu item. Task 2 complete!"

#Task 3: Create a route for deleteMenuItem function here
@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete/')
def deleteMenuItem(restaurant_id, menu_id):

    restaurant = None
    s = None

    try:

        s = session_creator()
        restaurant = s.query(Restaurant).filter(Restaurant.id == restaurant_id).first()

        if restaurant == None:
            return redirect(url_for('index'))

        menu_item = s.query(MenuItem).filter(MenuItem.restaurant_id == restaurant_id, MenuItem.id == menu_id).first()

        if menu_item == None:
            return redirect(url_for('get_restaurant', id=restaurant_id))

        s.delete(menu_item)
        s.commit()

        return redirect(url_for('get_restaurant', id=restaurant_id))

    except Exception, e:
        if s != None: s.close()
        raise e



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

