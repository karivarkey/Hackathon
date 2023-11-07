from flask import Blueprint , render_template,request

login_bp = Blueprint('login',__name__)

@login_bp.route('/login')
def login():
    return render_template('login.html')


@login_bp.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        user_name = request.form['user_name']
        user_password = request.form['user_password']
        # Do something with the user_input, for example, print it
        

        return f"You entered: {user_name}\n passwd: {user_password}"