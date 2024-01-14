from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

def save_user_data(user_id, password, phone_number, dob, address):
    # Create a string with user data
    user_data = f"{user_id},{password},{phone_number},{dob},{address}\n"

    try:
        # Append user data to a text file (users.txt)
        with open('C:\\Users\\AHIL\\Desktop\\ZZYVALORANT\\users.txt', 'a') as file:
            file.write(user_data)
        print(f"User data written successfully: {user_data}")
    except Exception as e:
        print(f"Error writing user data: {e}")

def check_user_credentials(user_id, password):
    # Read user credentials from the file and check for a match
    with open('C:\\Users\\AHIL\\Desktop\\ZZYVALORANT\\users.txt', 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) >= 2 and user_id == values[0] and password == values[1]:
                return True, "Login successful!"
    return False, "Invalid credentials. Please try again."

@app.route('/')
def index():
    return render_template('LoginZZYValorant.html')

@app.route('/signup', methods=['POST'])
def signup():
    # Retrieve user data from the form
    user_id = request.form.get('userId')
    password = request.form.get('password')
    phone_number = request.form.get('phoneNumber')
    dob = request.form.get('dob')
    address = request.form.get('address')

    # Print received user data for debugging
    print(f"Received user data: {user_id}, {password}, {phone_number}, {dob}, {address}")

    # Save user data to a text file
    save_user_data(user_id, password, phone_number, dob, address)

    # Redirect to the login page after signup
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = request.form.get('userId')
        password = request.form.get('password')

        success, message = check_user_credentials(user_id, password)
        if success:
            return render_template('LoginZZYValorant.html', success=message)
        else:
            return render_template('LoginZZYValorant.html', error=message)

    # Handle GET requests to render the login page
    return render_template('LoginZZYValorant.html', error=None, success=None)

@app.route('/create')
def create():
    return render_template('CreateZZYValorant.html')

@app.route('/user')
def user():
    return render_template('User.html')

if __name__ == '__main__':
    app.run(debug=True)
