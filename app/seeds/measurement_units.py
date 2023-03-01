from app.models import db, MeasurementUnit


def seed_measurement_units():

    none1 = MeasurementUnit(
        unit=' '
        )
    c2 = MeasurementUnit(
        unit='cup (C.)'
        )
    pt3 = MeasurementUnit(
        unit='pint (pt.)'
        )
    qt4 = MeasurementUnit(
        unit='quart (qt.)'
        )
    gal5 = MeasurementUnit(
        unit='gallon (gal.)'
        )
    lb6 = MeasurementUnit(
        unit='pound (lb.)'
        )
    oz7 = MeasurementUnit(
        unit='once (oz.)'
        )
    floz8 = MeasurementUnit(
        unit='fluid ounce (fl.oz)'
        )
    tsp9 = MeasurementUnit(
        unit='teaspoon (tsp.)'
        )
    tbsp10 = MeasurementUnit(
        unit='tablespoon (tbsp.)'
        )
    g11 = MeasurementUnit(
        unit='gram (g)'
        )
    kg12 = MeasurementUnit(
        unit='kilogram (kg)'
        )
    mg13 = MeasurementUnit(
        unit='milligram (mg)'
        )
    l14 = MeasurementUnit(
        unit='liter (L)'
        )
    ml15 = MeasurementUnit(
        unit='milliliters (mL)'
        )
    bar16 = MeasurementUnit(
        unit='bar(s)'
        )
    bottle17 = MeasurementUnit(
        unit='bottle(s)'
        )
    bunch18 = MeasurementUnit(
        unit='bunch(es)'
        )
    can19 = MeasurementUnit(
        unit='can(s)'
        )
    drop20 = MeasurementUnit(
        unit='drop(s)'
        )
    handful21 = MeasurementUnit(
        unit='handful(s)'
        )
    head22 = MeasurementUnit(
        unit='head(s)'
        )
    large23 = MeasurementUnit(
        unit='large'
        )
    medium24 = MeasurementUnit(
        unit='medium'
        )
    package25 = MeasurementUnit(
        unit='package(s)'
        )
    piece26 = MeasurementUnit(
        unit='piece(s)'
        )
    pinch27 = MeasurementUnit(
        unit='pinch(es)'
        )
    sheet28 = MeasurementUnit(
        unit='sheets(s)'
        )
    slice29 = MeasurementUnit(
        unit='slice(s)'
        )
    small30 = MeasurementUnit(
        unit='small'
        )
    sprig31 = MeasurementUnit(
        unit='sprig(s)'
        )
    stalk32 = MeasurementUnit(
        unit='stalk(s)'
        )

    db.session.add(none1)
    db.session.add(c2)
    db.session.add(pt3)
    db.session.add(qt4)
    db.session.add(gal5)
    db.session.add(lb6)
    db.session.add(oz7)
    db.session.add(floz8)
    db.session.add(tsp9)
    db.session.add(tbsp10)
    db.session.add(g11)
    db.session.add(kg12)
    db.session.add(mg13)
    db.session.add(l14)
    db.session.add(ml15)
    db.session.add(bar16)
    db.session.add(bottle17)
    db.session.add(bunch18)
    db.session.add(can19)
    db.session.add(drop20)
    db.session.add(handful21)    
    db.session.add(head22)
    db.session.add(large23)
    db.session.add(medium24)
    db.session.add(package25)
    db.session.add(piece26)
    db.session.add(pinch27)
    db.session.add(sheet28)
    db.session.add(slice29)
    db.session.add(small30)
    db.session.add(sprig31)
    db.session.add(stalk32)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_measurement_units():
    db.session.execute('TRUNCATE measurement_units RESTART IDENTITY CASCADE;')
    db.session.add()
