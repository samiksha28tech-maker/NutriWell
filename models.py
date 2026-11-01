from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import date, datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    mobile = db.Column(db.String(10), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    current_weight = db.Column(db.Float, nullable=False)
    profession = db.Column(db.String(20), nullable=False)
    goal = db.Column(db.String(20), nullable=False)
    target_kg = db.Column(db.Integer, nullable=True)
    food_preference = db.Column(db.String(20), nullable=False)
    health_condition = db.Column(db.String(40), default='none', nullable=False)
    flexible_day = db.Column(db.String(12), default='Sunday', nullable=False)

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    day = db.Column(db.Date, default=date.today, nullable=False, index=True)
    recorded_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    steps = db.Column(db.Integer, nullable=False, default=0)
    source = db.Column(db.String(20), default='manual')

class WaterLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    day = db.Column(db.Date, default=date.today, nullable=False, index=True)
    recorded_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    amount_ml = db.Column(db.Integer, nullable=False)

class WeightLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    day = db.Column(db.Date, default=date.today, nullable=False, index=True)
    weight_kg = db.Column(db.Float, nullable=False)

class MealLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    day = db.Column(db.Date, default=date.today, nullable=False, index=True)
    meal_key = db.Column(db.String(40), nullable=False)
    completed = db.Column(db.Boolean, default=True, nullable=False)
