import sys
import json
import threading

from flask import Flask
from flask import jsonify
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

thread_local = threading.local()

def open_session():

    if hasattr(thread_local, 'session') is not True or thread_local.session is None:
        # print "open new session"
        thread_local.session = session_creator()

    return thread_local.session

def close_session(s):

    if s is None:
        return

    if hasattr(thread_local, 'session') and thread_local.session is not None and thread_local.session == s:
        thread_local.session = None

    s.close()
    # print "closed session"

def transactional(original_func):

    def inner_decorator(*args, **kwargs):

        s = None

        try:

            s = open_session()

            return original_func(*args, **kwargs)

        except Exception, e:
            raise e
        finally:
            close_session(s)

    return inner_decorator

@app.route('/restaurant/<int:restaurant_id>/menu/json')
@transactional
def restaurantMenuJSON(restaurant_id):

    s = open_session()

    restaurant = s.query(Restaurant).filter_by(id=restaurant_id).one()

    items = s.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()

    return jsonify(items=[i.serialize for i in items])

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)

