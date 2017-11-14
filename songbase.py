from flask import Flask, session, render_template, request, flash, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    #return '<h1>Welcome to James first server. Thanks for checking it out.</h1>'
    return render_template('index.html')

@app.route('/form-demo', methods=['GET', 'POST'])
def form_demo():
    # how to get form data is different for GET vs. POST
    if request.method == 'GET':
        first_name = request.args.get('first_name')
        if first_name:
            return render_template('form-demo.html', first_name=first_name)
        else:
            return render_template('form-demo.html', first_name=session.get('first_name'))
    if request.method == 'POST':
        session['first_name'] = request.form['first_name']
        # return render_template('form-demo.html', first_name=first_name)
        return redirect(url_for('form_demo'))

@app.route('/songs')
def get_all_songs():
    songs = [
        'Free Fall',
        'Sound of Walking Away',
        'Feel Good'
    ]
    return render_template('songs.html', songs=songs)


@app.route('/user/<string:name>')
def get_user(name):
    #return '<h1>hello %s your age is %d</h1>' % (name, 3)
    return render_template('user.html', user_name=name)




if __name__ == "__main__":
    app.run(debug=True);
