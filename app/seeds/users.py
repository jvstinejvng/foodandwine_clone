from app.models.user import db, User


def seed_users():
    demo = User(
         username='DemoChef', email='homechef@aa.io', first_name='Demo', last_name = 'Chef', password='password')
    gordon = User(
        username='MasterChef', email='masterchef@aa.io', first_name='Gordon', last_name = 'Ramsay',  password='password')
    wolfgang = User(
        username='WolfgangPuck', email='wolfgangpuck@aa.io', first_name='Wolfgang ', last_name = 'Puck', password='password')
    guy = User(
        username='Flavortown', email='flavortown@aa.io', first_name='Wolfgang ', last_name = 'Puck',  password='password')
    rachael = User(
       username='RachaelRay', email='rachaelray@aa.io', first_name='Wolfgang ', last_name = 'Puck', password='password')
    david = User(
        username='UglyDelicious', email='uglydelicious@aa.io',  first_name='Wolfgang ', last_name = 'Puck', password='password')
    mark = User(
       username='Wahlburgers', email='wahlburgers@aa.io',  first_name='Wolfgang ', last_name = 'Puck', password='password')
    betty = User(
       username='BettyCrocker', email='bettycrocker@aa.io',  first_name='Wolfgang ', last_name = 'Puck', password='password')
    buddy = User(
       username='CakeBoss', email='cakeboss@aa.io',  first_name='Wolfgang ', last_name = 'Puck', password='password')
    thomas = User(
       username='ThomasKeller', email='thomaskeller@aa.io',  first_name='Wolfgang ', last_name = 'Puck', password='password')
    

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
