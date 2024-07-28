from flask import Flask, render_template

skills_app = Flask(__name__)

@skills_app.route('/')
def homePage():
    return render_template('homepage.html', pagetitle='H')

@skills_app.route('/about')
def about():
    return render_template('about.html', pagetitle='A')

if __name__ == "__main__":
    skills_app.run(debug=True, port=9000)
