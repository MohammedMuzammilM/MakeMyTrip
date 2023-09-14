from flask import Flask,render_template,request
import mysql.connector

app = Flask(__name__)


def registration_data(mobilenoOremail,password):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MMMuzzu*888', 
        database='travel'
    )
    cursor = connection.cursor()
    """sql1 = 'INSERT INTO registration (mobilenoOremail,password) VALUES (%s,%s)'"""
    sql2 = 'SELECT * FROM registration WHERE mobilenoOremail = %s AND password = %s'
    data = (mobilenoOremail,password)
    cursor.execute(sql2, data)
    user = cursor.fetchone()
    connection.commit()
    connection.close()
    return user

def account_details_data(name, gender, martialStatus, mobileno, address, city, pincode):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MMMuzzu*888',
        database='travel'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO accountdetails (name, gender, martialStatus, mobileno, address, city, pincode) VALUES (%s,%s,%s,%s,%s,%s,%s)'
    data = (name, gender, martialStatus, mobileno, address, city, pincode)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()

def booking_details_data(place_from, place_to, travel_date, NoOfSeats):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='MMMuzzu*888',
        database='travel'
    )
    cursor = connection.cursor()
    sql = 'INSERT INTO busbooking (place_from, place_to, travel_date, NoOfSeats) VALUES (%s,%s,%s,%s)'
    data = (place_from, place_to, travel_date, NoOfSeats)
    cursor.execute(sql, data)
    connection.commit()
    connection.close()



@app.route('/', methods=['GET', 'POST'])
def registration():
    if request.method == 'POST':
        mobilenoOremail = request.form['mobilenoOremail']
        password = request.form['password']
        
        """registration_data(mobilenoOremail,password)"""
        user = registration_data(mobilenoOremail,password)

        if user:
            return render_template('menu.html')
        else:
            return 'Invalid Paassword'
        
    return render_template('registration.html')

@app.route('/accdetail', methods=['GET', 'POST'])
def acc_details():
    if request.method == 'POST':
        name = request.form['name']
        gender = request.form['gender']
        martialStatus = request.form['martialStatus']
        mobileno = request.form['mobileno']
        address = request.form['address']
        city = request.form['city']
        pincode = request.form['pincode']
        
        account_details_data(name, gender, martialStatus, mobileno, address, city, pincode)

    return render_template('account_details.html')

@app.route('/bookdetail', methods=['GET', 'POST'])
def book_details():
    if request.method == 'POST':
        place_from = request.form['place_from']
        place_to = request.form['place_to']
        travel_date = request.form['travel_date']
        NoOfSeats = request.form['NoOfSeats']
        
        booking_details_data(place_from, place_to, travel_date, NoOfSeats)

        return render_template('confirmed.html')
        
    return render_template('bookingdetails.html')

if __name__ == '__main__':
    app.run(debug=True)