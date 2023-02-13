from app.models.user import db, User


def seed_users():
    demo = User(
         username='DemoChef', email='DemoChef@aa.io', first_name='Demo', last_name='User',  password='password')
    gordon = User(
        username='MasterChef', email='masterchef@aa.io', first_name='Gordon', last_name='Ramsay', password='password')
    wolfgang = User(
        username='WolfgangPuck', email='wolfgangpuck@aa.io', first_name='Wolfgang', last_name='Puck', password='password')
    guy = User(
        username='Flavortown', email='flavortown@aa.io',  first_name='Guy', last_name='Fieri',  password='password')
    rachael = User(
       username='RachaelRay', email='rachaelray@aa.io', first_name='Rachael', last_name='Ray', password='password')
    david = User(
        username='UglyDelicious', email='uglydelicious@aa.io', first_name='David', last_name='Chang',  password='password')
    mark = User(
       username='Wahlburgers', email='wahlburgers@aa.io', first_name='Mark', last_name='Wahlberg', password='password')
    betty = User(
       username='BettyCrocker', email='bettycrocker@aa.io', first_name='Betty', last_name='Crocker',  password='password')
    buddy = User(
       username='CakeBoss', email='cakeboss@aa.io', first_name='Buddy', last_name='Valastro', password='password')
    thomas = User(
       username='ThomasKeller', email='thomaskeller@aa.io', first_name='Thomas', last_name='Keller', password='password')
    bobby = User(
       username='IronChefFlay', email='bobbyflay@aa.io', first_name='Bobby', last_name='Flay',  password='password')
    martin = User(
       username='YanCanCook', email='martinyan@aa.io', first_name='Martin', last_name='Yan',  password='password')
    

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


    users = [demo, gordon, wolfgang, guy, rachael, david, mark, betty, buddy, thomas, bobby, martin]
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
