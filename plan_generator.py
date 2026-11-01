"""Goal-, food-preference- and health-aware educational wellness examples.

These examples are not medical prescriptions. Health-condition notes are conservative
safety prompts and do not replace individualized advice from a clinician/dietitian.
"""

FOOD_LABELS = {
    'veg': 'Vegetarian',
    'nonveg': 'Non-vegetarian',
    'both': 'Vegetarian and non-vegetarian',
    'eggen': 'Egg-only preference (eggs plus vegetarian foods)',
}

GOAL_INFO = {
    'weight_loss': {
        'title': 'Weight-loss meal ideas',
        'range': 'Illustrative example: around 1,500–1,700 calories/day for some adults; not a personal target.',
        'goal': 'Use balanced portions, vegetables, fibre-rich foods and protein-containing foods. Avoid crash diets.',
    },
    'weight_gain': {
        'title': 'Weight-gain meal ideas',
        'range': 'Illustrative example: around 2,800–3,000 calories/day for some adults; not a personal target.',
        'goal': 'If appropriate for you, add nourishing snacks and energy-dense foods gradually. Include protein-containing foods across the day.',
    },
    'maintain': {
        'title': 'Weight-maintenance meal ideas',
        'range': 'No fixed calorie range: energy needs vary by person.',
        'goal': 'Aim for regular, balanced meals and adjust portions based on your needs and longer-term weight trend.',
    },
}

# Each food preference has alternatives for every meal. Egg-only means eggs plus
# vegetarian foods; it does not include meat or fish.
MEAL_OPTIONS = {
    'weight_gain': {
        'breakfast': {
            'veg': 'Paneer bhurji (about 100 g) or tofu, 2 whole-grain toasts, 1 banana and 1 glass of milk/fortified alternative.',
            'nonveg': '2 eggs, 2 whole-grain toasts, 1 banana and 1 glass of milk/fortified alternative.',
            'both': 'Choose paneer/tofu (about 100 g) OR 2 eggs; serve with 2 whole-grain toasts and 1 banana.',
            'eggen': '2 eggs, 2 whole-grain toasts, 1 banana and 1 glass of milk/fortified alternative.',
        },
        'snack': {
            'veg': 'Smoothie with 1 cup milk/fortified alternative, ½ cup oats, 1 tbsp peanut butter and 1 small banana.',
            'nonveg': 'Smoothie with 1 cup milk, ½ cup oats, 1 tbsp peanut butter and 1 small banana; protein powder only if suitable and approved for you.',
            'both': 'Smoothie with 1 cup milk/fortified alternative, ½ cup oats, 1 tbsp peanut butter and 1 small banana.',
            'eggen': 'Smoothie with 1 cup milk/fortified alternative, ½ cup oats, 1 tbsp peanut butter and 1 small banana.',
        },
        'lunch': {
            'veg': 'Paneer or tofu (about 150 g), 1–1½ cups cooked rice, 1 cup vegetables and 1 tsp oil used in cooking.',
            'nonveg': 'Cooked chicken/fish (about 120–150 g), 1–1½ cups cooked rice and 1 cup vegetables.',
            'both': 'Choose paneer/tofu (about 150 g) OR cooked chicken/fish (about 120–150 g), with 1–1½ cups rice and 1 cup vegetables.',
            'eggen': '2 eggs or egg bhurji, 1–1½ cups cooked rice, 1 cup vegetables and curd if suitable.',
        },
        'dinner': {
            'veg': '1 bowl dal or beans, 2 medium chapatis, 1 cup vegetables and curd/paneer if suitable.',
            'nonveg': 'Cooked chicken/fish (about 120–150 g) OR 2 eggs, 2 medium chapatis and 1 cup vegetables.',
            'both': 'Choose dal/paneer OR chicken/fish/eggs, with 2 medium chapatis and 1 cup vegetables.',
            'eggen': '2 eggs or egg curry, 2 medium chapatis and 1 cup vegetables; add dal if desired.',
        },
    },
    'weight_loss': {
        'breakfast': {
            'veg': '½ cup oats cooked in water or milk, 1 tbsp chia/flax seeds and 1 small fruit; add plain curd if suitable.',
            'nonveg': '1 egg with ½ cup oats and 1 small fruit; use little or no added sugar.',
            'both': 'Choose 1 egg OR plain curd with ½ cup oats, 1 tbsp chia/flax seeds and 1 small fruit.',
            'eggen': '1–2 eggs with ½ cup oats and 1 small fruit.',
        },
        'snack': {
            'veg': '1 medium apple/pear OR 1 small bowl roasted chana; choose one based on hunger.',
            'nonveg': '1 medium apple/pear and a small handful of unsalted nuts, or plain curd if preferred.',
            'both': '1 medium apple/pear OR a small bowl roasted chana; optional plain curd if needed.',
            'eggen': '1 medium apple/pear OR a small bowl roasted chana; eggs are optional if they fit your usual meals.',
        },
        'lunch': {
            'veg': '1 bowl dal or tofu/paneer (about 100–120 g), 1–2 medium chapatis OR ½–¾ cup cooked rice, and 2 cups salad/vegetables.',
            'nonveg': 'Cooked chicken/fish (about 100–120 g), 1 medium chapati OR ½–¾ cup cooked rice, and 2 cups salad/vegetables.',
            'both': 'Choose dal/tofu/paneer OR cooked chicken/fish (about 100–120 g), with 1 medium chapati or ½–¾ cup rice and vegetables.',
            'eggen': '2 eggs or egg bhurji, 1 medium chapati OR ½–¾ cup cooked rice, plus 2 cups salad/vegetables.',
        },
        'dinner': {
            'veg': '1 bowl dal/beans or tofu, 1–2 cups cooked vegetables and 1 medium chapati if needed.',
            'nonveg': 'Cooked chicken/fish (about 100–120 g), 1–2 cups vegetables and 1 medium chapati if needed.',
            'both': 'Choose dal/tofu/paneer OR chicken/fish, with 1–2 cups vegetables and a modest portion of rice/chapati.',
            'eggen': '1–2 eggs, 1–2 cups vegetables and 1 medium chapati if needed.',
        },
    },
    'maintain': {
        'breakfast': {
            'veg': 'Vegetable poha/upma (1 medium bowl) with plain curd, OR oats with milk and fruit.',
            'nonveg': '2 eggs with whole-grain toast and 1 fruit, OR oats with milk and fruit.',
            'both': 'Choose vegetable poha/upma with curd OR eggs with whole-grain toast and fruit.',
            'eggen': '1–2 eggs with whole-grain toast and 1 fruit, OR oats with milk and fruit.',
        },
        'snack': {
            'veg': '1 fruit with a small handful of unsalted nuts OR plain curd.',
            'nonveg': '1 fruit with a small handful of unsalted nuts OR plain curd.',
            'both': '1 fruit with a small handful of unsalted nuts OR plain curd.',
            'eggen': '1 fruit with a small handful of unsalted nuts OR plain curd.',
        },
        'lunch': {
            'veg': '2 medium chapatis OR 1 cup cooked rice, 1 bowl dal/beans, 1 cup vegetables and salad.',
            'nonveg': '2 medium chapatis OR 1 cup cooked rice, cooked chicken/fish or eggs, vegetables and salad.',
            'both': 'Choose dal/paneer OR chicken/fish/eggs, with 2 chapatis or 1 cup rice, vegetables and salad.',
            'eggen': 'Egg curry or 2 eggs, 2 medium chapatis OR 1 cup rice, vegetables and salad.',
        },
        'dinner': {
            'veg': '1 bowl dal/paneer/tofu, 1–2 medium chapatis and 1 cup vegetables.',
            'nonveg': 'Cooked chicken/fish or eggs, 1–2 medium chapatis and 1 cup vegetables.',
            'both': 'Choose dal/paneer/tofu OR chicken/fish/eggs, with chapati/rice and vegetables.',
            'eggen': 'Egg bhurji/egg curry, 1–2 medium chapatis and 1 cup vegetables.',
        },
    },
}

HEALTH_DIET_NOTES = {
    'none': 'No health condition was selected. Choose varied foods and adjust portions to your individual needs.',
    'diabetes': 'Diabetes selected: carbohydrate needs and medication matter. Prefer regular balanced meals, fibre-rich carbohydrates and unsweetened drinks; do not use this example as a diabetes prescription. Confirm your plan with your diabetes clinician/dietitian.',
    'bp': 'High blood pressure selected: favour fresh foods and limit salty packaged foods, pickles and excess added salt. Confirm individual sodium and medication advice with your clinician.',
    'thyroid': 'Thyroid condition selected: needs vary by diagnosis and medication. Do not start supplements or make major dietary changes from this example; confirm with your clinician/dietitian.',
    'heart': 'Heart-related condition selected: diet requirements can depend on your diagnosis and medicines. This app cannot safely personalize a heart-condition diet; seek your clinician/dietitian’s guidance before following the sample plan.',
    'lung': 'Asthma/lung condition selected: this sample does not treat the condition. Avoid known food allergies/triggers and follow your clinician’s care plan.',
    'joint': 'Joint/back problem selected: use foods that fit your general needs, but seek clinical advice if you have a condition-specific diet or medicines.',
    'other': 'Other or multiple health conditions selected: this app cannot safely tailor a medical diet to an unspecified condition. Ask your clinician/dietitian to review the plan before using it.',
}

HEALTH_EXERCISE_NOTES = {
    'none': 'Start at a comfortable level and increase gradually. Stop if you feel unwell.',
    'diabetes': 'Diabetes selected: activity may affect blood glucose and medication needs. Follow your care team’s advice about timing, glucose monitoring and foot care.',
    'bp': 'High blood pressure selected: avoid sudden maximal effort and breath-holding. Ask your clinician what intensity is suitable, especially if blood pressure is uncontrolled.',
    'thyroid': 'Thyroid condition selected: choose intensity based on symptoms and medical advice; this app cannot determine safe intensity for you.',
    'heart': 'Heart-related condition selected: do not start a new exercise routine based on this app alone. Get clinician clearance and an individualized activity plan first.',
    'lung': 'Asthma/lung condition selected: follow your prescribed action plan and clinician’s exercise advice. Keep any prescribed reliever available as directed.',
    'joint': 'Joint/back problem selected: avoid movements that increase pain; a physiotherapist or clinician can advise on safe modifications.',
    'other': 'Other or multiple health conditions selected: ask your clinician which movements and intensity are safe before following an exercise routine.',
}


def _normalize_food(food):
    food = (food or 'veg').strip().lower()
    aliases = {'vegetarian': 'veg', 'non-vegetarian': 'nonveg', 'non_veg': 'nonveg', 'eggs': 'eggen', 'egg': 'eggen', 'egg-only': 'eggen', 'both': 'both'}
    food = aliases.get(food, food)
    return food if food in ('veg', 'nonveg', 'both', 'eggen') else 'veg'


def _normalize_goal(goal):
    goal = (goal or 'maintain').strip().lower()
    aliases = {'loss': 'weight_loss', 'gain': 'weight_gain', 'maintenance': 'maintain', 'weight_maintain': 'maintain'}
    goal = aliases.get(goal, goal)
    return goal if goal in GOAL_INFO else 'maintain'


def get_meals(food, goal, condition='none', flexible_day='Sunday'):
    food = _normalize_food(food)
    goal = _normalize_goal(goal)
    plan = MEAL_OPTIONS[goal]
    names = [('breakfast', 'Breakfast', '8:00 AM'), ('snack', 'Mid-morning / afternoon snack', '11:00 AM / 4:30 PM'), ('lunch', 'Lunch', '1:00 PM'), ('dinner', 'Dinner', '7:30 PM')]
    meals = []
    for key, name, time in names:
        meals.append({'key': key, 'name': name, 'time': time, 'food': plan[key][food], 'note': GOAL_INFO[goal]['goal']})
    flexible_day = flexible_day if flexible_day in ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday') else 'Sunday'
    condition = (condition or 'none').strip().lower()
    for meal in meals:
        meal['flexible_day'] = flexible_day
        if condition == 'diabetes':
            meal['food'] += ' Prefer unsweetened drinks and whole fruit; keep carbohydrate portions consistent and follow your clinician’s individual advice.'
        elif condition == 'bp':
            meal['food'] += ' Prepare with little added salt; limit salty sauces, pickles and packaged foods.'
        elif condition == 'thyroid':
            meal['food'] += ' Avoid starting iodine/thyroid supplements or restrictive diets without medical advice.'
    return meals


def get_exercises(goal='maintain', condition='none'):
    goal = _normalize_goal(goal)
    condition = (condition or 'none').strip().lower()
    if condition in ('heart', 'other'):
        return [{'name': 'Clinician-approved activity only', 'duration': 'Wait for individualized advice before starting a new routine', 'steps': ['Ask your healthcare professional which activities are safe for your condition.', 'Follow any restrictions and prescribed care plan.', 'Do not use this app to replace rehabilitation or medical advice.'], 'video': 'https://www.youtube.com/results?search_query=gentle+exercise+education'}]

    if condition == 'joint':
        items = [
            ('Gentle seated movement', 'Try 3–5 minutes only if pain-free', ['Sit on a stable chair with feet supported.', 'Gently march your feet or move your ankles within a comfortable range.', 'Stop if pain increases; ask a physiotherapist about suitable options.'], 'gentle+seated+exercise+joint+pain'),
            ('Easy flat-surface walking', 'Only if walking is comfortable and approved for you', ['Choose a flat, uncluttered surface.', 'Use supportive footwear or your usual mobility aid.', 'Stop if pain or instability increases.'], 'low+impact+walking+joint+pain'),
        ]
    elif condition == 'lung':
        items = [
            ('Gentle seated movement', 'Start with 2–5 minutes if comfortable', ['Sit upright and relax your shoulders.', 'Move your arms and feet gently while breathing normally.', 'Follow your asthma/lung action plan and stop if symptoms worsen.'], 'gentle+seated+exercise+breathing'),
            ('Easy walking', 'Only at a pace allowed by your care plan', ['Choose a safe, flat route.', 'Keep the pace easy and take breaks.', 'Follow your clinician’s advice about prescribed inhalers.'], 'gentle+walking+asthma+exercise'),
        ]
    elif condition == 'diabetes':
        items = [
            ('Easy walking', 'Start with 5–10 minutes if suitable', ['Choose a safe, flat route.', 'Follow your care team’s advice about glucose checks and medication timing.', 'Wear suitable footwear and check your feet as advised.'], 'walking+for+people+with+diabetes'),
            ('Gentle chair-based movement', 'Try a few comfortable minutes', ['Sit on a stable chair.', 'Move your arms and legs gently.', 'Stop if you feel unwell and follow your diabetes care plan.'], 'chair+exercise+for+diabetes'),
        ]
    elif condition == 'bp':
        items = [
            ('Easy-paced walking', 'Start with 5–10 minutes if your clinician says it is suitable', ['Choose a flat, safe route.', 'Keep an easy pace and breathe normally.', 'Avoid breath-holding and stop if you feel unwell.'], 'beginner+walking+high+blood+pressure'),
            ('Gentle seated movement', 'Try a few comfortable minutes', ['Sit upright on a stable chair.', 'Move slowly and keep breathing normally.', 'Avoid straining or breath-holding.'], 'gentle+chair+exercise+high+blood+pressure'),
        ]
    elif goal == 'weight_loss':
        items = [
            ('Comfortable-paced walking', 'Begin with 5–10 minutes if comfortable', ['Walk on a flat, safe route.', 'Use a pace that lets you speak in sentences.', 'Increase time gradually only if comfortable.'], 'beginner+walking+exercise'),
            ('Chair sit-to-stand', 'Try 5 comfortable repetitions if suitable', ['Use a stable chair placed against a wall.', 'Stand up slowly and sit down with control.', 'Use your hands for support if needed.'], 'chair+sit+to+stand+exercise'),
            ('Wall push-ups', 'Try 5 comfortable repetitions if suitable', ['Face a wall and place hands at shoulder height.', 'Bend elbows gently toward the wall.', 'Push away without holding your breath.'], 'wall+push+up+exercise'),
        ]
    elif goal == 'weight_gain':
        items = [
            ('Gentle strength practice', 'Start with 1 set of 5–8 easy repetitions if suitable', ['Choose a stable chair or wall-supported movement.', 'Move slowly and maintain comfortable breathing.', 'Increase resistance only when technique feels easy and safe.'], 'beginner+strength+training'),
            ('Wall push-ups', 'Try 1 set of 5–8 comfortable repetitions', ['Face a wall and place hands at shoulder height.', 'Bend elbows gently toward the wall.', 'Push away without holding your breath.'], 'wall+push+up+exercise'),
            ('Easy walking', 'Try 5–10 minutes if comfortable', ['Choose a flat, safe route.', 'Keep a comfortable pace.', 'Rest whenever needed.'], 'easy+walking+exercise'),
        ]
    else:
        items = [
            ('Comfortable-paced walking', 'Try 5–15 minutes if suitable', ['Walk on a flat, safe route.', 'Use a pace that feels comfortable.', 'Increase time gradually if you feel well.'], 'beginner+walking+exercise'),
            ('Wall push-ups', 'Try a few comfortable repetitions', ['Face a wall and place hands at shoulder height.', 'Bend elbows gently toward the wall.', 'Push away without holding your breath.'], 'wall+push+up+exercise'),
            ('Seated knee extensions', 'Try 5 gentle repetitions per side if suitable', ['Sit upright on a stable chair.', 'Straighten one knee without forcing it.', 'Lower slowly and stop if there is pain.'], 'seated+knee+extension+exercise'),
        ]
    return [{'name': name, 'duration': duration, 'steps': steps, 'video': 'https://www.youtube.com/results?search_query=' + query} for name, duration, steps, query in items]


def get_schedule(profession):
    schedules = {
        'student': [('7:00 AM','Wake up and morning routine'),('8:00 AM','Breakfast'),('9:00 AM','Classes or focused study'),('1:00 PM','Lunch'),('4:00 PM','Study break / snack'),('6:00 PM','Leisure movement if suitable'),('8:00 PM','Dinner'),('10:30 PM','Wind down for sleep')],
        'employee': [('6:30 AM','Wake up'),('7:00 AM','Morning routine / movement if suitable'),('8:00 AM','Breakfast'),('9:00 AM','Work; take breaks when possible'),('1:00 PM','Lunch'),('4:30 PM','Snack / stretch break'),('7:00 PM','Personal time'),('8:00 PM','Dinner'),('10:30 PM','Wind down for sleep')],
        'housewife': [('6:30 AM','Wake up and plan the day'),('7:30 AM','Breakfast'),('9:00 AM','Household tasks with breaks'),('11:00 AM','Rest or snack'),('1:00 PM','Lunch'),('3:00 PM','Personal time / errands'),('5:00 PM','Leisure movement if suitable'),('8:00 PM','Dinner'),('10:30 PM','Wind down for sleep')]
    }
    return schedules.get(profession, schedules['student'])
