from flask import Flask, render_template, session, request, redirect, url_for
import pymysql
from flask import jsonify
from flask import flash

app = Flask(__name__)

#kunci rahasia agar session berjalan, isinya ngasal juga gapapa
app.secret_key = "12345"

#untuk mengconnect python dengan database menggunakan library pymysql
connection = pymysql.connect(
    host = "127.0.0.1", #### local host udah dari sananya
    user = "root",      #### root udah dari sananya
    password = "",
    db = "db_project"  ####  nama database aku
)

cursor = connection.cursor()

############################################ fungsi login
@app.route('/', methods=["GET", "POST"])

def login():
    if request.method == "POST" and "inpEmail" in request.form and "inpPass" in request.form:
        email = request.form["inpEmail"]
        passwd = request.form["inpPass"]

        cur = connection.cursor()

        cur.execute("SELECT * FROM tb_login where email = %s and password = %s", (email, passwd))

        result = cur.fetchone()

        if result:
            session['is_logged_in'] = True
            session["username"] = result[1]

            return redirect(url_for("home"))
        else:
            return render_template("login.html")
    else:
            return render_template("login.html")


####################################### fungsi home
@app.route("/home")

def home ():
    if "is_logged_in" in session:
        cur = connection.cursor() 

        cur.execute("SELECT * FROM tb_login")

        data = cur.fetchall()
        cur.close()
    else:
         return redirect(url_for("login"))

    return render_template('home.html', users=data)

@app.route("/keranjang")

def keranjang ():
    if "is_logged_in" in session:
        cur = connection.cursor() 

        cur.execute("SELECT * FROM tb_keranjang")

        data = cur.fetchall()
        cur.close()
    else:
         return redirect(url_for("login"))

    return render_template('keranjang.html', users=data)


# Fungsi registrasi
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST" and "inpEmail" in request.form and "inpPass" and "inpUsername" in request.form:
        username = request.form["inpUsername"]
        email = request.form["inpEmail"]
        passwd = request.form["inpPass"]

        cur = connection.cursor()

        # Cek apakah email sudah terdaftar
        cur.execute("SELECT * FROM tb_login  where email = %s", (email,))
        result = cur.fetchone()

        if result:
            return "Email sudah terdaftar, silakan gunakan email lain."
        else:
            # Jika email belum terdaftar, tambahkan pengguna baru
            cur.execute("INSERT INTO tb_login (username, email, password) VALUES (%s, %s, %s)", (username, email, passwd))
            connection.commit()

            # Set sesi agar pengguna terdaftar dan bisa login
            session['is_logged_in'] = True
            session["username"] = email

            return redirect(url_for("home"))
    else:
        return render_template("register.html")



###################################### fungsi untuk logout
@app.route("/logout")
def logout():
     
     session.pop("is_logged_in", None)
     session.pop("username", None)

     return redirect(url_for("login"))


####################################### Fungsi tambah keranjang
@app.route("/add_default_to_cart")
def add_default_to_cart():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 1")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart2")
def add_default_to_cart2():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 2")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart3")
def add_default_to_cart3():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 3")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart4")
def add_default_to_cart4():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 4")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart5")
def add_default_to_cart5():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 5")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart6")
def add_default_to_cart6():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 6")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart7")
def add_default_to_cart7():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 7")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

@app.route("/add_default_to_cart8")
def add_default_to_cart8():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Fetch the product with id=1 from tb_product
        cur.execute("SELECT * FROM tb_product WHERE id = 8")
        product_data = cur.fetchone()

        if product_data:
            # Insert the fetched product into the tb_keranjang table
            cur.execute("INSERT INTO tb_keranjang (nama, kategori, size, harga) VALUES (%s, %s, %s, %s)",
                        (product_data[1], product_data[2], product_data[3], product_data[4]))
            connection.commit()

            flash("Product added to cart successfully", "success")
        else:
            flash("Product not found", "error")

        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))


@app.route("/total_harga")
def total_harga():
    if "is_logged_in" in session:
        cur = connection.cursor()

        # Mengambil data harga dari tb_keranjang
        cur.execute("SELECT harga FROM tb_keranjang")
        data = cur.fetchall()

        # Menghitung total harga
        total_harga = sum(row[0] for row in data)

        # Clear the contents of the tb_keranjang table
        cur.execute("DELETE FROM tb_keranjang")
        connection.commit()

        flash("Total harga retrieved and cart cleared successfully", "success")

        return render_template('total_harga.html', total_harga=total_harga)
    else:
        return redirect(url_for("login"))

@app.route("/selesai", methods=["POST"])
def selesai():
    if "is_logged_in" in session:
        # Redirect to home or any other appropriate page after completing the payment
        flash("Payment completed successfully", "success")
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))
    
@app.route('/struk', methods=['GET', 'POST'])

def struk():
    # Menghitung total harga
    cur = connection.cursor()
    cur.execute("SELECT harga FROM tb_keranjang")
    data = cur.fetchall()
    total_harga = sum(row[0] for row in data)

    if request.method == 'POST':
        # Handle form submission logic here
        print(f"Total Harga: {total_harga}")  # Cek nilai total harga di konsol Flask
        return render_template('struk.html', total_harga=total_harga)
    else:
        # Handle GET request logic here
        # This could be rendering the initial form or redirecting to another page
        return render_template('struk.html', total_harga=total_harga)
    
#fungsi untuk about.html
@app.route("/about")
def about():
    return render_template("about.html")

from flask import request

@app.route("/remove_from_cart", methods=["POST"])
def remove_from_cart():
    if "is_logged_in" in session:
        cur = connection.cursor()

        product_id = request.form.get("product_id")

        # Delete the product with the given ID from tb_keranjang
        cur.execute("DELETE FROM tb_keranjang WHERE id = %s", (product_id,))
        connection.commit()

        flash("Product removed from cart successfully", "success")
        return redirect(url_for("keranjang"))
    else:
        return redirect(url_for("login"))

# database ke komen
@app.route('/komen', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        email = request.form['email']
        pesan = request.form['pesan']

        # Simpan data ke database
        cursor.execute("INSERT INTO tb_komen (nama, email, pesan) VALUES (%s, %s, %s)", (nama, email, pesan))
        connection.commit()

    return render_template('about.html')  # Ganti dengan nama template HTML Anda


### Menjalankan aplikasi
if __name__ == "__main__":
     app.run(debug=True)


