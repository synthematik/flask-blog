from flask import Blueprint
from flask import render_template
from models import Blog, Tag

posts = Blueprint('posts', __name__, template_folder='templates')



@posts.route('/')
def index():
    posts = Blog.query.all()
    return render_template('index_blueprint.html', posts=posts)

@posts.route('/<slug>')
def post_detail(slug):
    post = Blog.query.filter(Blog.slug==slug).first()
    tags = blog.tags
    return render_template('post_detail.html', post=post,tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('tag_detail.html', tag=tag, posts=posts)