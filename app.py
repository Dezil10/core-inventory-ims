from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# connect to MySQL
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="inventory_db"
)

cursor = db.cursor()

# dashboard
@app.route("/")
def dashboard():

    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()

    return render_template("dashboard.html", products=products)


# add product
@app.route("/add_product", methods=["POST"])
def add_product():

    name = request.form["name"]
    sku = request.form["sku"]
    category = request.form["category"]
    quantity = request.form["quantity"]

    sql = "INSERT INTO products (name,sku,category,quantity) VALUES (%s,%s,%s,%s)"
    val = (name,sku,category,quantity)

    cursor.execute(sql,val)
    db.commit()

    return redirect("/")


## receive stock
@app.route("/receive/<int:id>", methods=["POST"])
def receive(id):

    qty = request.form["qty"]

    # update product quantity
    sql = "UPDATE products SET quantity = quantity + %s WHERE id=%s"
    val = (qty, id)

    cursor.execute(sql, val)
    db.commit()

    # save movement history
    cursor.execute(
        "INSERT INTO movements (product_id,type,quantity) VALUES (%s,%s,%s)",
        (id,"receive",qty)
    )

    db.commit()

    return redirect("/")


# deliver stock
@app.route("/deliver/<int:id>", methods=["POST"])
def deliver(id):

    qty = request.form["qty"]

    sql = "UPDATE products SET quantity = quantity - %s WHERE id=%s"
    val = (qty, id)

    cursor.execute(sql, val)
    db.commit()

    # save movement history
    cursor.execute(
        "INSERT INTO movements (product_id,type,quantity) VALUES (%s,%s,%s)",
        (id,"deliver",qty)
    )

    db.commit()

    return redirect("/")

#delete product
@app.route("/delete/<int:id>")
def delete(id):

    sql = "DELETE FROM products WHERE id=%s"
    val = (id,)

    cursor.execute(sql,val)
    db.commit()

    return redirect("/")


@app.route("/history")
def history():

    cursor.execute("""
    SELECT movements.id, products.name, movements.type, movements.quantity, movements.date
    FROM movements
    JOIN products ON movements.product_id = products.id
    ORDER BY movements.date DESC
    """)

    movements = cursor.fetchall()

    return render_template("history.html", movements=movements)
app.run(debug=True)

