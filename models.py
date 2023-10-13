from datetime import datetime
import re
from app import db


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

post_tags = db.Table('post_tags',
                     db.Column('post_id', db.Integer, db.ForeignKey('blog.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')))


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Blog, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary='post_tags', backref=db.backref('posts', lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)

    def __repr__(self):
        return '<Blog id: {}, title: {}>'.format(self.id, self.title)


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(100))

    def __int__(self, *args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '<Tag id: {}, name: {}>'.format(self.id, self.name)


