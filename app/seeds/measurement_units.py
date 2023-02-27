from app.models import db, MeasurementUnit


def seed_measurement_units():
    # metric
    g = MeasurementUnit(
        unit='gram (g)'
        )
    kg = MeasurementUnit(
        unit='kilogram (kg)'
        )
    l = MeasurementUnit(
        unit='liter (L)'
        )
    ml = MeasurementUnit(
        unit='milliliters (mL)'
        )

    # imperial
    oz = MeasurementUnit(
        unit='once (oz.)'
        )
    floz = MeasurementUnit(
        unit='fluid ounce (fl.oz)'
        )
    tsp = MeasurementUnit(
        unit='teaspoon (tsp.)'
        )
    tbsp = MeasurementUnit(
        unit='tablespoon (tbsp.)'
        )
    c = MeasurementUnit(
        unit='cup (C.)'
        )
    pt = MeasurementUnit(
        unit='pint (pt.)'
        )
    qt = MeasurementUnit(
        unit='quart (qt.)'
        )
    gal = MeasurementUnit(
        unit='gallon (gal.)'
        )
    lb = MeasurementUnit(
        unit='pound (lb.)'
        )



    db.session.add(g)
    db.session.add(kg)
    db.session.add(l)
    db.session.add(ml)
    db.session.add(oz)
    db.session.add(floz)
    db.session.add(tsp)
    db.session.add(tbsp)
    db.session.add(c)
    db.session.add(pt)
    db.session.add(qt)
    db.session.add(gal)
    db.session.add(lb)

    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_measurement_units():
    db.session.execute('TRUNCATE measurement_units RESTART IDENTITY CASCADE;')
    db.session.commit()
