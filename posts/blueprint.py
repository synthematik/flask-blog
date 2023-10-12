from flask import Blueprint
from flask import render_template
from models import Blog

posts = Blueprint('posts', __name__, template_folder='templates')



@posts.route('/')
def index():
    posts = Blog.query.all()
    return render_template('index_blueprint.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Blog.query.filter(Blog.slug==slug).first()
    return render_template('post_detail.html', post=post)

