from todo import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    complete = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id} - {self.title}, Completed: {self.complete}>'

