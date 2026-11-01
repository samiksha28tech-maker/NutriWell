# NutriWell starter project

## Run locally (Windows PowerShell)

```powershell
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000 in your browser.

## Included
- Sign up/sign in with mobile number and hashed password
- Server-side validation for age, goal, food preference and target
- SQLite storage using Flask-SQLAlchemy
- Dashboard, example diet plan, exercise guide and profession schedule
- Manual step, water and weight logs
- Seven-day summary and downloadable PDF

## Important limitations
- Meal plans and exercise examples are educational placeholders, not clinically validated personalized recommendations.
- Health condition selection only displays a caution. It does not automatically determine safe diet/exercise prescriptions.
- Step entries are manual. Background phone step tracking requires a supported mobile app/device integration and permission.
- Before deployment, set a strong `NUTRIWELL_SECRET` environment variable, enable HTTPS, add CSRF protection and privacy controls, and conduct security and clinical review.
- If you modify the database schema during development, delete `instance/nutriwell.db` only if you are happy to lose the local test data; `db.create_all()` does not migrate existing tables.
