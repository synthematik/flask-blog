from datetime import datetime
import re
from app import db


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Blog, self).__init__(*args, **kwargs)
        self.generate_slug()

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Blog id: {}, title: {}>'.format(self.id, self.title)
