from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo_users = [
    User(username='DemoChef', email='homechef@aa.io', first_name='Demo', last_name = 'User', password='password'),
    User(username='MasterChef', email='masterchef@aa.io', first_name='Gordon', last_name = 'Ramsay', password='password'),
    User(username='WolfgangPuck', email='wolfgangpuck@aa.io', first_name='Wolfgang', last_name = 'Puck', password='password'),
    User(username='Flavortown', email='flavortown@aa.io', first_name='Guy', last_name = 'Fieri', password='password'),
    User(username='RachaelRay', email='rachaelray@aa.io', first_name='Rachael', last_name = 'Ray', password='password'),
    User(username='UglyDelicious', email='uglydelicious@aa.io', first_name='David', last_name = 'Chang', password='password'),
    User(username='Wahlburgers', email='wahlburgers@aa.io', first_name='Mark', last_name = 'Wahlberg', password='password'),
    User(username='BettyCrocker', email='bettycrocker@aa.io', first_name='Betty', last_name = 'Crocker', password='password'),
    User(username='CakeBoss', email='cakeboss@aa.io', first_name='Buddy', last_name = 'Valastro', password='password'),
    User(username='ThomasKeller', email='thomaskeller@aa.io', first_name='Thomas', last_name = 'Keller', password='password'),
    ]

    for user in demo_users:
        db.session.add(user)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
