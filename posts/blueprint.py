from flask import Blueprint
from flask import render_template
from models import Blog, Tag
from flask import request
from .forms import PostForm
from app import db
from flask import redirect
from flask import url_for

posts = Blueprint('posts', __name__, template_folder='templates')



@posts.route('/create', methods=['POST', 'GET'])
def create_post():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']

        try:
            if title:
                post = Blog(title=title, body=body)
                db.session.add(post)
                db.session.commit()
            else:
                return redirect(url_for("posts.create_post"))
        except:
            print("error")

        return redirect(url_for("posts.index"))

    form = PostForm()
    return render_template('create_post.html', form=form)


@posts.route('/')
def index():
    q = request.args.get('q')
    if q:
        posts = Blog.query.filter(Blog.title.contains(q) | Blog.body.contains(q)).all()
    else:
        posts = Blog.query.all()
    return render_template('index_blueprint.html', posts=posts, q=q)

@posts.route('/<slug>')
def post_detail(slug):
    post = Blog.query.filter(Blog.slug==slug).first()
    tags = Blog.tags
    return render_template('post_detail.html', post=post,tags=tags)


@posts.route('/tag/<slug>')
def tag_detail(slug):
    tag = Tag.query.filter(Tag.slug==slug).first()
    posts = tag.posts.all()
    return render_template('tag_detail.html', tag=tag, posts=posts)
