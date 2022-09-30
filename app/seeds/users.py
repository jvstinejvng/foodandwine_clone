from app.models import db, User


# Adds a demo user, you can add other users here if you want
def seed_users():
    demo = User(
        first_name='Demo', last_name='User', username='DemoChef', email='homechef@aa.io', password='password'),
    gordon = User(
        first_name='Gordon', last_name='Ramsay', username='MasterChef', email='masterchef@aa.io', password='password'),
    wolfgang = User(
        first_name='Wolfgang', last_name='Puck', username='WolfgangPuck', email='wolfgangpuck@aa.io', password='password'),
    guy = User(
        first_name='Guy', last_name='Fieri', username='Flavortown', email='flavortown@aa.io', password='password'),
    rachael = User(
        first_name='Rachael', last_name='Ray',username='RachaelRay', email='rachaelray@aa.io', password='password'),
    david = User(
        first_name='David', last_name='Chang', username='UglyDelicious', email='uglydelicious@aa.io', password='password'),
    mark = User(
        first_name='Mark', last_name='Wahlberg', username='Wahlburgers', email='wahlburgers@aa.io', password='password'),
    betty = User(
        first_name='Betty', last_name='Crocker', username='BettyCrocker', email='bettycrocker@aa.io', password='password'),
    buddy = User(
        first_name='Buddy', last_name='Valastro', username='CakeBoss', email='cakeboss@aa.io', password='password'),
    thomas = User(
        first_name='Thomas', last_name='Keller', username='ThomasKeller', email='thomaskeller@aa.io', password='password'),
    

    db.session.add(demo)
    db.session.add(gordon)
    db.session.add(wolfgang)
    db.session.add(guy)
    db.session.add(rachael)
    db.session.add(david)
    db.session.add(mark)
    db.session.add(betty)
    db.session.add(buddy)
    db.session.add(thomas)
    

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE;')
    db.session.commit()
