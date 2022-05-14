from flask import  render_template, request, Blueprint

main = Blueprint('main',__name__)

@main.route("/")
@main.route("/home")
def home():
    # return "<h1>Home Page!</h1>"
    page = request.args.get('page', 1, type=int)
    return render_template('home.html')#, posts=posts)

@main.route("/about")
def about():
    return render_template('about.html', title ='About')