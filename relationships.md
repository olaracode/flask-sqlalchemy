# data types
Integer: Represents integer values.
String: Represents text data.
Boolean: Represents Boolean values (True or False).
Float: Represents floating-point numbers.
Date: Represents date values.
DateTime: Represents date and time values.
Text: Represents large text data.
JSON: Represents JSON data (requires additional configuration).
Numeric: Represents numeric data with configurable precision and scale.
Enum: Represents enumerated types with a predefined set of allowed values.
BIGINT: Represents large integer values.

ARRAY: Represents an array of values.
BINARY: Represents binary data.
BLOB: Represents large binary objects.
CHAR: Represents fixed-length character strings.
CLOB: Represents large character objects.
TIME: Represents time values.
TIMESTAMP: Represents date and time values (potentially with higher precision than DateTime).
INTERVAL: Represents time intervals.

# Relationships

## One to One

```python
class User(db.Model):
  id = db.Column(Integer, primary_key=True)
  username = db.Column(String(80), unique=True, nullable=False)
  email = db.Column(String(120), unique=True, nullable=False)
  address_id = db.Column(Integer, ForeignKey('address.id'))
  address = db.relationship('Address', uselist=False, backref='user')

class Address(db.Model):
  id = db.Column(Integer, primary_key=True)
  street = db.Column(String(80), nullable=False)
  city = db.Column(String(80), nullable=False)
  state = db.Column(String(50), nullable=False)
```

## One to Many

```python
class User(db.Model):
  id = db.Column(Integer, primary_key=True)
  username = db.Column(String(80), unique=True, nullable=False)
  email = db.Column(String(120), unique=True, nullable=False)
  posts = db.relationship('Post', backref='author')

class Post(db.Model):
  id = db.Column(Integer, primary_key=True)
  title = db.Column(String(80), nullable=False)
  content = db.Column(Text, nullable=False)
  author_id = db.Column(Integer, ForeignKey('user.id'), nullable=False)
```

## Many to Many

```python
class User(db.Model):
  id = db.Column(Integer, primary_key=True)
  username = db.Column(String(80), unique=True, nullable=False)
  email = db.Column(String(120), unique=True, nullable=False)
  courses = db.relationship('Course', secondary='enrollment', backref='students')

class Course(db.Model):
  id = db.Column(Integer, primary_key=True)
  title = db.Column(String(80), nullable=False)
  description = db.Column(Text, nullable=False)

class Enrollment(db.Model):
  __tablename__ = 'enrollment'
  user_id = db.Column(Integer, ForeignKey('user.id'), primary_key=True)
  course_id = db.Column(Integer, ForeignKey('course.id'), primary_key=True)

```