from app import app
from app import db
import view
from posts.blueprint import posts

app.register_blueprint(posts, url_prefix='/blog')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()