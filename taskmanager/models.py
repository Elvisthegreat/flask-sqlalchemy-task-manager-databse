"""
If you recall from the last few lessons, we had to specifically import 
each column type at the top of the file e.g Integer, Float, String etc.
However, with Flask-SQLAlchemy, the 'db' variable contains each of those already, and we can
simply use dot-notation to specify the data-type for our columns.

"""
from taskmanager import db


class Category(db.Model):
    # schema for the Category models
    id = db.Column(db.Integer, primary_key=True)
    """
    It stores strings of up to 25 characters (db.String(25)).
    It does not allow duplicate values (unique=True).
    It does not allow missing values (nullable=False).
    """
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    tasks = db.relationship("Task", backref="category", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Task: {1} | Urgent: {2}".format(
            self.id, self.task_name, self.is_urgent
        )


class Task(db.Model):
    # schema for the Task models
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False) # db.Text allows longer strings to be used
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.Date, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self
