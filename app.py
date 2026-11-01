import os
from datetime import date, datetime, timedelta
from flask import Flask, render_template, redirect, url_for, flash, request, send_file
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from models import db, User, ActivityLog, WaterLog, WeightLog, MealLog
from plan_generator import get_meals, get_exercises, get_schedule, GOAL_INFO, HEALTH_DIET_NOTES, HEALTH_EXERCISE_NOTES, FOOD_LABELS
from pdf_generator import make_weekly_pdf

app = Flask(__name__, instance_relative_config=True)
app.config['SECRET_KEY'] = os.environ.get('NUTRIWELL_SECRET', 'change-this-secret-before-deployment')
os.makedirs(app.instance_path, exist_ok=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'nutriwell.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'signin'
login_manager.login_message_category = 'info'

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))

with app.app_context():
    db.create_all()
    # Safe SQLite migration for existing installations created before flexible_day existed.
    from sqlalchemy import inspect, text
    inspector = inspect(db.engine)
    if 'user' in inspector.get_table_names():
        user_columns = [column['name'] for column in inspector.get_columns('user')]
        if 'flexible_day' not in user_columns:
            db.session.execute(text("ALTER TABLE user ADD COLUMN flexible_day VARCHAR(12) NOT NULL DEFAULT 'Sunday'"))
            db.session.commit()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        mobile = request.form.get('mobile', '').strip()
        password = request.form.get('password', '')
        try:
            age = int(request.form.get('age', ''))
            weight = float(request.form.get('weight', ''))
        except (ValueError, TypeError):
            flash('Enter a valid age and current weight.', 'error')
            return redirect(url_for('signup'))
        profession = request.form.get('profession', '')
        goal = request.form.get('goal', '')
        food = request.form.get('food', '')
        condition = request.form.get('condition', 'none')
        flexible_day = request.form.get('flexible_day', 'Sunday')
        target_raw = request.form.get('target_kg', '')
        target = None
        if goal in ('weight_loss', 'weight_gain'):
            try:
                target = int(target_raw)
            except ValueError:
                target = 0
        if not username or not mobile.isdigit() or len(mobile) != 10:
            flash('Enter a username and a valid 10-digit mobile number.', 'error')
        elif not 18 <= age <= 60:
            flash('Age must be between 18 and 60.', 'error')
        elif weight <= 0 or weight > 350:
            flash('Enter a valid current weight in kilograms.', 'error')
        elif profession not in ('student', 'housewife', 'employee'):
            flash('Choose a valid profession.', 'error')
        elif goal not in ('weight_loss', 'weight_gain', 'maintain'):
            flash('Choose a valid goal.', 'error')
        elif food not in ('veg', 'nonveg', 'eggen', 'both'):
            flash('Choose a valid food preference.', 'error')
        elif condition not in ('none', 'lung', 'diabetes', 'bp', 'thyroid', 'heart', 'joint', 'other'):
            flash('Choose a valid health condition.', 'error')
        elif flexible_day not in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
            flash('Choose a valid weekly flexible day.', 'error')
        elif goal != 'maintain' and not 1 <= (target or 0) <= 10:
            flash('Choose a target from 1 to 10 kg.', 'error')
        elif len(password) < 8:
            flash('Password must contain at least 8 characters.', 'error')
        elif User.query.filter_by(mobile=mobile).first():
            flash('That mobile number is already registered.', 'error')
        else:
            user = User(username=username, mobile=mobile, password_hash=generate_password_hash(password),
                        age=age, current_weight=weight, profession=profession, goal=goal,
                        target_kg=target if goal != 'maintain' else None,
                        food_preference=food, health_condition=condition, flexible_day=flexible_day)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            flash('Welcome to NutriWell! Your profile has been saved.', 'success')
            return redirect(url_for('dashboard'))
    return render_template('signup.html')

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        mobile = request.form.get('mobile', '').strip()
        password = request.form.get('password', '')
        user = User.query.filter_by(mobile=mobile).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Incorrect mobile number or password.', 'error')
    return render_template('signin.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have signed out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    today = date.today()
    steps = sum(x.steps for x in ActivityLog.query.filter_by(user_id=current_user.id, day=today).all())
    water_ml = sum(x.amount_ml for x in WaterLog.query.filter_by(user_id=current_user.id, day=today).all())
    meals_done = MealLog.query.filter_by(user_id=current_user.id, day=today, completed=True).count()
    return render_template('dashboard.html', steps=steps, water_l=round(water_ml/1000, 2), meals_done=meals_done)

@app.route('/diet', methods=['GET', 'POST'])
@login_required
def diet():
    meals = get_meals(current_user.food_preference, current_user.goal, current_user.health_condition, current_user.flexible_day)
    if request.method == 'POST':
        if 'flexible_day' in request.form:
            chosen_day = request.form.get('flexible_day', '')
            if chosen_day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'):
                current_user.flexible_day = chosen_day
                db.session.commit()
                flash('Your weekly flexible day has been updated.', 'success')
            else:
                flash('Choose a valid weekday.', 'error')
            return redirect(url_for('diet'))
        meal_key = request.form.get('meal_key', '')
        if meal_key in [m['key'] for m in meals]:
            log = MealLog.query.filter_by(user_id=current_user.id, day=date.today(), meal_key=meal_key).first()
            if log:
                log.completed = not log.completed
            else:
                db.session.add(MealLog(user_id=current_user.id, day=date.today(), meal_key=meal_key, completed=True))
            db.session.commit()
        return redirect(url_for('diet'))
    logs = {x.meal_key: x.completed for x in MealLog.query.filter_by(user_id=current_user.id, day=date.today()).all()}
    return render_template('diet.html', meals=meals, logs=logs, goal_info=GOAL_INFO.get(current_user.goal, GOAL_INFO['maintain']), health_note=HEALTH_DIET_NOTES.get(current_user.health_condition, HEALTH_DIET_NOTES['other']), food_label=FOOD_LABELS.get(current_user.food_preference, current_user.food_preference), flexible_day=current_user.flexible_day, condition=current_user.health_condition)

@app.route('/exercise')
@login_required
def exercise():
    # Health notes are conservative safety prompts, not medical exercise prescriptions.
    return render_template('exercise.html', exercises=get_exercises(current_user.goal, current_user.health_condition), condition=current_user.health_condition, goal=current_user.goal, health_note=HEALTH_EXERCISE_NOTES.get(current_user.health_condition, HEALTH_EXERCISE_NOTES['other']))

@app.route('/schedule')
@login_required
def schedule():
    return render_template('schedule.html', items=get_schedule(current_user.profession))

@app.route('/tracker', methods=['GET', 'POST'])
@login_required
def tracker():
    if request.method == 'POST':
        kind = request.form.get('kind')
        try:
            if kind == 'steps':
                steps = int(request.form.get('steps', ''))
                if not 0 <= steps <= 100000:
                    raise ValueError
                db.session.add(ActivityLog(user_id=current_user.id, day=date.today(), recorded_at=datetime.now(), steps=steps, source='manual'))
            elif kind == 'water':
                amount = int(request.form.get('amount_ml', ''))
                if not 1 <= amount <= 5000:
                    raise ValueError
                db.session.add(WaterLog(user_id=current_user.id, day=date.today(), recorded_at=datetime.now(), amount_ml=amount))
            elif kind == 'weight':
                weight = float(request.form.get('weight', ''))
                if not 1 <= weight <= 350:
                    raise ValueError
                db.session.add(WeightLog(user_id=current_user.id, day=date.today(), weight_kg=weight))
            else:
                raise ValueError
            db.session.commit()
            flash('Your entry has been saved.', 'success')
        except (ValueError, TypeError):
            flash('Please enter a valid value.', 'error')
        return redirect(url_for('tracker'))
    today = date.today()
    step_logs = ActivityLog.query.filter_by(user_id=current_user.id).order_by(ActivityLog.recorded_at.desc()).limit(20).all()
    water_logs = WaterLog.query.filter_by(user_id=current_user.id).order_by(WaterLog.recorded_at.desc()).limit(10).all()
    weight_logs = WeightLog.query.filter_by(user_id=current_user.id).order_by(WeightLog.day.desc()).limit(10).all()
    return render_template('tracker.html', step_logs=step_logs, water_logs=water_logs, weight_logs=weight_logs)

@app.route('/report')
@login_required
def report():
    today = date.today()
    start = today - timedelta(days=6)
    activity = ActivityLog.query.filter(ActivityLog.user_id == current_user.id, ActivityLog.day >= start, ActivityLog.day <= today).all()
    water = WaterLog.query.filter(WaterLog.user_id == current_user.id, WaterLog.day >= start, WaterLog.day <= today).all()
    daily_steps = { (start + timedelta(days=i)).isoformat(): 0 for i in range(7) }
    for row in activity:
        daily_steps[row.day.isoformat()] += row.steps
    total_steps = sum(daily_steps.values())
    total_water = sum(row.amount_ml for row in water)
    return render_template('report.html', daily_steps=daily_steps, total_steps=total_steps,
                           avg_steps=round(total_steps/7), total_water=round(total_water/1000, 1), start=start, today=today)

@app.route('/report/pdf')
@login_required
def report_pdf():
    today = date.today()
    start = today - timedelta(days=6)
    activity = ActivityLog.query.filter(ActivityLog.user_id == current_user.id, ActivityLog.day >= start, ActivityLog.day <= today).all()
    water = WaterLog.query.filter(WaterLog.user_id == current_user.id, WaterLog.day >= start, WaterLog.day <= today).all()
    steps_by_day = { (start + timedelta(days=i)).isoformat(): 0 for i in range(7) }
    for row in activity:
        steps_by_day[row.day.isoformat()] += row.steps
    path = make_weekly_pdf(current_user.username, start, today, steps_by_day, sum(x.amount_ml for x in water))
    return send_file(path, as_attachment=True, download_name='NutriWell_weekly_report.pdf')

@app.route('/disclaimer')
def disclaimer():
    return render_template('disclaimer.html')

if __name__ == '__main__':
    app.run(debug=True)
