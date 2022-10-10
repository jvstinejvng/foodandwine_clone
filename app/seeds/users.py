from app.models.user import db, User


def seed_users():
    demo = User(
         username='DemoChef', email='homechef@aa.io', password='password')
    gordon = User(
        username='MasterChef', email='masterchef@aa.io',  password='password')
    wolfgang = User(
        username='WolfgangPuck', email='wolfgangpuck@aa.io', password='password')
    guy = User(
        username='Flavortown', email='flavortown@aa.io',  password='password')
    rachael = User(
       username='RachaelRay', email='rachaelray@aa.io', password='password')
    david = User(
        username='UglyDelicious', email='uglydelicious@aa.io',  password='password')
    mark = User(
       username='Wahlburgers', email='wahlburgers@aa.io',  password='password')
    betty = User(
       username='BettyCrocker', email='bettycrocker@aa.io',  password='password')
    buddy = User(
       username='CakeBoss', email='cakeboss@aa.io', password='password')
    thomas = User(
       username='ThomasKeller', email='thomaskeller@aa.io', password='password')
    

    # db.session.add(demo)
    # db.session.add(gordon)
    # db.session.add(wolfgang)
    # db.session.add(guy)
    # db.session.add(rachael)
    # db.session.add(david)
    # db.session.add(mark)
    # db.session.add(betty)
    # db.session.add(buddy)
    # db.session.add(thomas)


    users = [demo, gordon, wolfgang, guy, rachael, david, mark, betty, buddy, thomas]
    for user in users:
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
