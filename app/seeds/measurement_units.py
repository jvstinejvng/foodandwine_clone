from app.models import db, MeasurementUnit


def seed_measurement_units():

    none1 = MeasurementUnit(
        unit='none'
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

    db.session.commit(none1)
    db.session.commit(c2)
    db.session.commit(pt3)
    db.session.commit(qt4)
    db.session.commit(gal5)
    db.session.commit(lb6)
    db.session.commit(oz7)
    db.session.commit(floz8)
    db.session.commit(tsp9)
    db.session.commit(tbsp10)
    db.session.commit(g11)
    db.session.commit(kg12)
    db.session.commit(mg13)
    db.session.commit(l14)
    db.session.commit(ml15)
    db.session.commit(bar16)
    db.session.commit(bottle17)
    db.session.commit(bunch18)
    db.session.commit(can19)
    db.session.commit(drop20)
    db.session.commit(handful21)    
    db.session.commit(head22)
    db.session.commit(large23)
    db.session.commit(medium24)
    db.session.commit(package25)
    db.session.commit(piece26)
    db.session.commit(pinch27)
    db.session.commit(sheet28)
    db.session.commit(slice29)
    db.session.commit(small30)
    db.session.commit(sprig31)
    db.session.commit(stalk32)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_measurement_units():
    db.session.execute('TRUNCATE measurement_units RESTART IDENTITY CASCADE;')
    db.session.commit()
