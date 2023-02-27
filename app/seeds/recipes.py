from app.models import db, Recipe

def seed_recipes():
    r1 = Recipe(
        user_id=1,
        title='Caesar Salad with Crispy Tofu Croutons',
        description='In this creative remix of a classic Caesar, we pan-fry tofu cubes until they become crisp and crouton-like. Plus, the blend of soft tofu with olive oil, lemon juice, and anchovy makes a terrific caesar-style dressing without the standard raw egg yolks.',
        image_url='https://www.foodandwine.com/thmb/TNp-RFiTfO1ir8z9HBp0xS8uaOo=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201005-r-xl-caesar-salad-with-crispy-tofu-croutons-27f3f820efcf41d584bf968afa587461.jpg',
        total_time='30 minutes',
        servings='4 servings',
        # ingredients='6 ounces soft silken drained tofu, 1 1/2 tablespoons extra-virgin olive oil, 1 1/2 tablespoons fresh lemon juice, 1 1/2 tablespoons freshly grated Parmigiano-Reggiano cheese plus more for serving, 1 oil-packed anchovy drained fillet, 1 small garlic clove, 1/2 teaspoon Worcestershire sauce, 1/2 teaspoon Dijon mustard, Salt and freshly ground pepper, One 14-ounce package firm drained tofu cut into 3/4-inch cubes, Vegetable oil for frying, 1/2 cup cornstarch, 2 romaine hearts torn into bite-size pieces',
        # directions='In a blender, puree the silken tofu with the olive oil, lemon juice, the 1 1/2 tablespoons of Parmigiano, the anchovy, garlic, Worcestershire and mustard; season the dressing with salt and pepper. Wrap the firm tofu in paper towels and press out some of the water. In a large skillet, heat 1/4 inch of vegetable oil until shimmering. In a bowl, toss the tofu with the cornstarch until coated. Add the cubes to the oil and fry over moderately high heat, turning once, until crisp, about 8 minutes. Using a slotted spoon, transfer the croutons to a paper towel lined plate; season with salt. In a large bowl, toss the romaine with the dressing and two-thirds of the croutons. Transfer the salad to plates and top with the remaining croutons. Sprinkle with Parmigiano and serve.',
    )
    r2 = Recipe(
        user_id=1,
        title='Smoked-Salmon Deviled Eggs',
        description='"Deviled eggs are fun because you can dress them up or down," says Michael Mina, who dresses them up with chopped smoked salmon here.',
        image_url='https://www.foodandwine.com/thmb/J0CnSi6g8zVxIWp1u9XZE-0Mq7o=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201204-xl-smoked-salmon-deviled-eggs-2000-c17a8c7c5c7648029b2091b301836773.jpg',
        total_time='30 minutes',
        servings='makes 8 deviled eggs (16 halves)',
        # ingredients='8 large eggs, 1/2 cup finely chopped smoked salmon (2 ounces), 1/3 cup mayonnaise, 2 cornichons cut into 1/4-inch dice, 2 teaspoons pickling liquid from the cornichons jar, 2 teaspoons Dijon mustard, Salt, Old Bay seasoning',
        # directions='Cover the eggs with water in a large saucepan and bring to a vigorous boil. Cover the saucepan, remove the heat and let stand for 10 minutes. Drain off the water and shake the pan gently to crack the eggs. Cool the eggs slightly under cold running water, then peel them under running water. Pat dry. Cut the eggs in half lengthwise and carefully remove the yolks. Transfer the yolks to a bowl and mash well with a fork. Stir in the salmon, mayonnaise, cornichons, cornichon liquid, and Dijon mustard. Season with salt. Mound the filling in the egg-white halves and sprinkle with Old Bay. Serve lightly chilled.',
    )
    r3 = Recipe(
        user_id=1,
        title='Chicken and Wild Rice Soup',
        description='Let\'s use leftover chicken or turkey, and wild rice to make this lovely chicken and rice soup. Thyme and garlic add aromatic depth to the soup and the classic base of onions, carrots, and celery. After simmering the soup, finish it with a drizzle of cream to add a touch of richness. ',
        image_url='https://www.foodandwine.com/thmb/8Igqyn3l2LeLDcXRN8Ll1FIglrA=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/HD-201411-r-chicken-and-wild-rice-soup-2f493a1de2a6462286391ea214601acf.jpg',
        total_time='1 hour 15 minutes',
        servings='8 servings',
        # ingredients='4 tablespoons unsalted butter, 3 celery ribs cut into 1/2-inch pieces, 2 carrots cut into 1/2-inch pieces, 1 medium chopped onion, 2 garlic cloves minced, 1 1/2 teaspoons finely chopped thyme, Salt, Pepper, 1/4 cup all-purpose flour, 1 cup wild rice (5 ounces), 2 quarts chicken stock or low-sodium broth, 2 cups water, 4 cups bite-size pieces of roasted chicken or turkey,1 cup heavy cream',
        # directions='In a large saucepan, melt the butter. Add the celery, carrots, onion, garlic, thyme, and a generous pinch each of salt and pepper and cook over moderate heat, stirring occasionally, until the vegetables just start to soften, about 10 minutes. Sprinkle the flour over the vegetables and cook, stirring, until evenly coated and lightly browned, about 3 minutes.Add the wild rice to the saucepan and gradually stir in the stock and water. Bring to a boil, then simmer over moderately low heat, stirring occasionally, until the vegetables are tender, about 30 minutes. Add the chicken and simmer, stirring occasionally, until the wild rice is tender, 10 to 15 minutes longer. Stir in the cream and season with salt and pepper. Ladle the soup into bowls and serve.',
    )
    r4 = Recipe(
        user_id=1,
        title='Grilled Apricots with Burrata, Country Ham and Arugula',
        description='Depending on the season, you can also make this salad with plums, peaches, and pears.',
        image_url='https://www.foodandwine.com/thmb/GlixT3MbhbFtQ2uLg-g9ImLDxBw=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201109-xl-grilled-apricots-with-burrata-country-ham-and-arugula-ce006a480c0e417cac2190c981b72ab3.jpg',
        total_time='30 minutes',
        servings='8 servings',
        # ingredients='1 1/4 pounds apricots, halved and pitted, 1/4 cup extra-virgin olive oil plus more for brushing, Sea salt, freshly ground pepper, 1 1/2 tablespoons fresh lemon juice, 1 small head  cored and thinly sliced radicchio,5 ounces baby arugula, 1/2 pound of shredded burrata cheese, 4 ounces shaved country ham, 1 tablespoon aged balsamic vinegar',
        # directions='Light a grill or preheat a grill pan. Brush the apricots with oil and season with salt and pepper. Grill over high heat, cut sides down, just until lightly charred, 5 minutes. Let cool. In a bowl, whisk the lemon juice with 1/4 cup of oil and season with salt and pepper. Gently toss in the apricots, radicchio, and arugula. Transfer to a platter and top with the burrata, ham and vinegar. Serve.',
    )
    r5 = Recipe(
        user_id=1,
        title='Honey Mustard Chicken Wings',
        description='Sweet honey and tangy mustard make these classic chicken wings extraordinary.',
        image_url='https://www.foodandwine.com/thmb/_8iiizCxNY_AnWFrM_MXOqXPNOg=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201403-xl-honey-mustard-chicken-wings-6e55beb535df4d2995108b67b7091f6d.jpg',
        total_time='45 minutes',
        servings='4 servings',
        # ingredients='1/2 cup butter, 4 cloves garlic (minced), 1/2 cup mustard, 1/3 cup honey, 1 tablespoon Worcestershire sauce, 1 teaspoon apple cider vinegar, 1/2 teaspoon kosher or sea salt (plus more for seasoning), 1/2 teaspoon black pepper (plus more for seasoning), 2 pounds chicken wings (split), 1 cup all-purpose flour (for dredging), Vegetable oil (or other high flashpoint oil used for frying)',
        # directions='Heat a saucepan over medium heat. Melt the butter, and then stir in the garlic. Cook for 1 to 2 minutes, or until the garlic is lightly browned. Whisk in the mustard and honey. Stir in the Worcestershire sauce, apple cider vinegar, and season with salt and pepper. Reduce heat to low and simmer the sauce for about 3 to 5 minutes or until thickened. Set aside. Rinse the chicken wings and pat them dry. Generously season the chicken with salt and black pepper. Dredge the wings in flour, shaking off any excess flour, and set aside. In a large saucepan or deep fryer, heat the oil to about 375°. Fry the chicken wings in small batches until golden brown, 8 to 10 minutes. Shake off any excess oil and place on paper towels to drain. Continue frying the chicken in batches until all of the wings are cooked. Toss the wings with the honey mustard sauce and serve warm with leftover sauce for dipping.',
    )
    r6 = Recipe(
        user_id=2,
        title='Apple Cider Glazed Ham',
        description='Pulling off an impressive holiday ham at home takes just a few simple steps. Start with a good-quality, bone-in spiral-cut ham — make sure it is unglazed. Coat it with this deliciously sweet apple cider glaze featuring light brown sugar, honey, and Dijon mustard. Brushing the glaze onto the ham in 15-minute intervals during the last 30 minutes of baking creates a wonderfully sticky and caramelized crust. Serve any leftovers on biscuits with a slather of mustard.',
        image_url='https://www.foodandwine.com/thmb/cNAPJA1VVVfmkxBvC5iOKuKzii4=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/diy-honeybaked-ham-FT-RECIPE2019-e2a596b5bec34d419924c6153eae2b4c.jpg',
        total_time='2 hours 35 minutes',
        servings='10 servings',
        # ingredients='1 1/2 cups packed light brown sugar, 1/2 cup honey, 1/4 cup Dijon mustard, 1/2 teaspoon kosher salt, 1/2 teaspoon black pepper, 1 cup apple cider, divided, 1 (8 to 9lb.) fully cooked bone-in spiral-cut ham half',
        # directions='Preheat oven to 350°F. Line a roasting pan with heavy-duty aluminum foil. Stir together brown sugar, honey, mustard, salt, pepper, and 1/2 cup of the cider in a medium bowl. Place ham in prepared pan so that individual ham slices are perpendicular to pan bottom. Brush ham with 3/4 cup glaze, gently pushing glaze in between slices. Turn ham over so that bottoms of slices are now facing up; brush an additional 3/4 cup glaze in between slices. Turn ham so that the large, flat, cut side is facing down in pan.Pour remaining 1/2 cup cider into bottom of pan. Cover tightly with foil. Bake in preheated oven 1 1/2 hours. Remove from oven; remove and discard foil. Brush ham evenly with 1/3 cup glaze; return to oven, and bake 15 minutes. Remove from oven. Brush with 1/3 cup glaze; return to oven, and bake until a thermometer inserted in thickest portion of ham registers 140°F, about 15 minutes. Remove from oven; brush with remaining 1/3 cup glaze and pan drippings. Let stand 15 minutes. Serve warm or at room temperature.',
    )
    r7 = Recipe(
        user_id=2,
        title='Lemon-and-Garlic-Marinated Flat Iron Steak',
        description='The flat iron steak, which sits on the shoulder blade next to the teres major, is great for marinating and grilling.',
        image_url='https://www.foodandwine.com/thmb/mZCOibKXSTOFAGW06jyjqVht8Pc=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201205-xl-lemon-and-garlic-marinated-flat-iron-steak-a66515005cf54031815b943eaef4b3c6.jpg',
        total_time='30 minutes',
        servings='2 servings',
        # ingredients='One 1-pound beef flat iron steak, Salt, Freshly ground pepper, 2 tablespoons extra-virgin olive oil, 6 garlic cloves, minced, 4 scallions, chopped, 4 bay leaves, broken into pieces, 2 lemons, very thinly sliced, Vegetable oil for brushing',
        # directions='Season the steak with salt and pepper in a glass baking dish and rub with the olive oil. Spread the garlic, scallions and bay leaves all over the steak. Cover both sides of the steak with lemon slices. Cover and refrigerate for 24 hours. Light a grill and brush with vegetable oil. Scrape off the seasonings and bring the steak to room temperature. Season with salt and pepper and grill over moderately high heat until medium-rare within, 3 1/2 minutes per side. Transfer to a carving board and let rest for 5 minutes. Thinly slice across the grain and serve.',
    )
    r8 = Recipe(
        user_id=2,
        title='Salmon and Cherry Tomato Skewers with Rosemary Vinaigrette',
        description='Cook these simple salmon-and-tomato kebabs on skewers or even on sturdy rosemary sprigs.',
        image_url='https://www.foodandwine.com/thmb/Dh8xN0JoJEwadeaQoLo9aKcEV-A=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/recipe1015-xl-salmon-tomato-skewers-10bc4ce3221746e39d14f2b8bd2188af.jpg',
        total_time='40 minutes',
        servings='4 skewers',
        # ingredients='1/4 cup extra-virgin olive oil plus more for brushing, 3 tablespoon fresh lemon juice, 2 teaspoons Dijon mustard, 2 teaspoons finely chopped rosemary, Kosher salt, Pepper, 16 cherry tomatoes , 1 1/2 pounds salmon fillet cut into 1 1/2-inch cubes, 4 long metal skewers or 4 wooden skewers soaked in water for 1 hour',
        # directions='In a small bowl, whisk the 1/4 cup of olive oil with the lemon juice, mustard and rosemary. Season the vinaigrette with salt and pepper. Light a grill or heat a grill pan. Thread the salmon and cherry tomatoes onto the skewers, brush with olive oil and season all over with salt and pepper. Grill over moderately high heat, turning once, until the salmon is just cooked through, about 6 minutes. Transfer the skewers to a platter and drizzle with some of the vinaigrette. Serve right away, passing additional vinaigrette at the table.',
    )
    r9 = Recipe(
        user_id=3,
        title='Lemony Crêpe Casserole',
        description='Reminiscent of a classic bread pudding, this sweet-tart crêpe casserole has a beautiful lacy top and tender-but-sliceable center.',
        image_url='https://www.foodandwine.com/thmb/VzRB80cpbqpKakUBwl2wls2Fe0Q=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/lemony-crepe-casserole-ft-RECIPE0119-07a35dd254394be6bb6ecb676da1b0bd.jpg',
        total_time='55 minutes',
        servings='8 servings',
        # ingredients='2 (8-ounce) packages cream cheese, at room temperature, 3/4 cup store-bought lemon curd, 1/4 teaspoon kosher salt(divided), 1/4 cup unsalted butter, plus more for greasing, 24 (10-inch) store-bought crêpes, 1 medium Meyer lemon, very thinly sliced and seeded, 1/4 cup pure maple syrup, 1 tablespoon powdered sugar',
        # directions='Preheat oven to 350°F. Beat cream cheese, lemon curd, and 1/8 teaspoon salt with an electric mixer on medium speed until smooth, about 3 minutes. Grease a 13- x 9-inch baking dish with butter. Arrange 1 crêpe on a work surface. Using a small offset spatula, spread 1 1/2 tablespoons cream cheese mixture evenly over crêpe, leaving a 1-inch border. Fold crêpe in half, and then fold in half again. Place folded crêpe in prepared baking dish. Repeat with remaining crêpes and remaining cream cheese mixture, overlapping folded crêpes in baking dish. Bake in preheated oven until crêpes are heated through and edges are golden brown, 15 to 20 minutes. Meanwhile, melt butter in a large nonstick skillet over medium-low. Add lemon slices, sprinkle with remaining 1/8 teaspoon salt, and cook, stirring occasionally, until lemon peel is softened, about 7 minutes. Stir in maple syrup, and remove from heat. Spoon lemon sauce over casserole. Dust with powdered sugar, and serve.',
    )
    r10 = Recipe(
        user_id=4,
        title='Stuffed Jalapeños',
        description='Perfect served with cold beers, these stuffed jalapeños are the perfect game-day or movie-night snack. Halved jalapeños are packed with a cheddar and cream cheese filling flavored with garlic, cilantro and scallions.',
        image_url='https://www.foodandwine.com/thmb/lLKDW8OCi0a4jM6B651njJOA81k=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/stuffed-jalapenos-xl-recipe2016-8aa1de0a28af4e4d85d954d02ce207d5.jpg',
        total_time='1 hour',
        servings='24 pieces',
        # ingredients='1 small garlic clove, Kosher salt, 12 ounces cream cheese(softened), 2 minced scallions, 1 large egg yolk, 1/2 teaspoon ground cumin, 1/2 teaspoon Dijon mustard, 1/3 cup minced cilantro plus more for garnish, Pepper, 6 ounces sharp cheddar cheese, coarsely grated (1 3/4 cups), 12 large jalapeños halved lengthwise with seeded stems left intact, 1 tablespoon extra-virgin olive oil, Lime wedges for serving',
        # directions='Preheat the oven to 375°. Using the flat side of a chef\'s knife, crush the garlic and 1/2 teaspoon of salt to a paste. Scrape the garlic paste into a medium bowl and add the cream cheese, scallions, egg yolk, cumin, mustard and 1/3 cup of cilantro. Stir with a rubber spatula until well combined. Season with a generous pinch each of salt and pepper, then fold the cheddar into the filling. On a rimmed baking sheet, toss the jalapeños with the olive oil and a pinch each of salt and pepper until well coated. Arrange them cut side up and spoon 1 1/2 to 2 tablespoons of filling into each one. Bake for about 20 minutes, rotating the sheet from front to back halfway through, until the filling is puffed and bubbling and the jalapeños are tender. Garnish with minced cilantro and serve with lime wedges.',
    )
    r11 = Recipe(
        user_id=4,
        title='Garlic-Crusted Roast Rack of Lamb',
        description='Rack of lamb is a brilliant roast centerpiece dish because it\'s impressive and surprisingly easy to make. This lamb recipe includes just five ingredients and 10 minutes of active cooking time. It\'s one of our favorite ways to prepare a rack of lamb because it\'s simply rubbed with plenty of garlic, rosemary, olive oil, and salt before roasting. Since the seasoning is so simple, the dish pairs well with a range of sides, from risotto to green salads to roasted vegetables.',
        image_url='https://www.foodandwine.com/thmb/4ryFSLczBRBc5580uLBrF8g5VlU=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/HD-201104-r-garlic-rack-of-lamb-04f38936aeb147e0ac3798d530a3722c.jpg',
        total_time='1 hour 45 minutes',
        servings='8 servings',
        # ingredients='1 head of garlic (cloves peeled), 1/4 cup rosemary leaves, 1/4cup extra-virgin olive oil, 2 racks of lamb, frenched (2 pounds each), Kosher salt and freshly ground black pepper',
        # directions='In a mini food processor, combine the garlic, rosemary and olive oil and process until the garlic is finely chopped. Season the lamb racks with salt and pepper and rub the garlic-rosemary oil all over them. Set the racks fat side up on a large rimmed baking sheet and let stand for 1 hour. Preheat the oven to 450°. Roast the lamb in the upper third of the oven for 15 minutes. Turn the racks and roast for 10 minutes longer for medium-rare meat. Transfer the racks to a carving board, stand them upright and let rest for 10 minutes. Carve the racks in between the rib bones and transfer to plates. Serve right away.',
    )
    r12 = Recipe(
        user_id=5,
        title='Grilled Ham and Cheese with Strawberry-Red-Wine Jam',
        description='The secret to this delectable sandwich is the jam spiked with Pinot Noir.',
        image_url='https://www.foodandwine.com/thmb/r6X9Fr6kys1zLgPWrNsq_DudBTo=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201004-xl-grilled-ham-and-cheese-2000-f18d283af5e848efb4ac53b970d60f02.jpg',
        total_time='30 minutes',
        servings='10 sandwiches',
        # ingredients='Twenty 1/4-inch-thick slices of brioche, 1/2 cup strawberry jam mixed with 2 tablespoons of Pinot Noir, 10 thin slices of baked ham, 10 thin slices of Gruyère cheese, Softened unsalted butter',
        # directions='Heat a large griddle. Spread 10 of the brioche slices with the jam. Top with the ham and Gruyère and close the sandwiches. Lightly butter the outside of the sandwiches and cook over moderate heat until toasted and the cheese is melted, 2 minutes per side. Cut in half and serve right away.',
    )
    r13 = Recipe(
        user_id=6,
        title='Pink Grapefruit and Avocado Salad',
        description='This pretty salad is best in the winter when grapefruit is at its prime.',
        image_url='https://www.foodandwine.com/thmb/9E3pMYDbNKrzksE5W1ld9rphvSw=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201011-xl-pink-grapefruit-and-avocado-salad-bc58a373e6b24f998baa36b1d6de65d1.jpg',
        total_time='30 minutes',
        servings='4 servings',
        # ingredients='2 medium ruby grapefruits, 1 teaspoon finely grated grapefruit zest, 1 medium shallot, minced, 1 teaspoon white wine vinegar, 2 medium Hass avocados sliced 1/4 inch thick. Salt, 2 tablespoons extra-virgin olive oil, Freshly ground pepper, Chervil leaves for garnish',
        # directions='Using a sharp knife, cut the skin and all of the bitter white pith off of the grapefruits. Working over a bowl, cut in between the membranes to release the sections. Squeeze the juice from the membranes into the bowl. Transfer 2 tablespoons of the juice to another bowl. Add the zest, shallot and vinegar; let the dressing stand for 10 minutes. Season the avocado with salt and arrange on plates with the grapefruit sections. Stir the oil into the dressing; season with salt and pepper. Drizzle onto the grapefruit and avocado, garnish with the chervil and serve.',
    )
    r14 = Recipe(
        user_id=6,
        title='Herbed Ricotta with Grilled Bread',
        description=' Make this simple herbed ricotta for all your parties because it\'s such a crowd-pleaser. It\'s delicious spread on toasted bread but is also perfect served with crudités',
        image_url='https://www.foodandwine.com/thmb/d6IrEem0MfEWdekwp1KYkFPJVNI=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/herbed-ricotta-with-grilled-bread-XL-RECIPE0517-2e46c3952128480d821537c3ecfc0cb2.jpg',
        total_time='30 minutes',
        servings='8 servings',
        # ingredients='1 pound fresh ricotta, 1 teaspoon finely grated lemon zest plus 3 tablespoons fresh lemon juice, 1 garlic clove finely grated, 1/4 cup extra-virgin olive oil, plus more for brushing and drizzling, 1 cup finely chopped mixed chives, parsley, mint and tarragon, plus more for garnish, Kosher salt, Pepper, 2 baguettes split lengthwise',
        # directions='In a food processor, puree the ricotta, lemon zest, lemon juice, garlic and the 1/4 cup of olive oil until smooth. Scrape into a medium bowl, stir in the herbs and season generously with salt and pepper. Light a grill. Brush the baguettes with olive oil. Grill over moderately high heat, turning once, until lightly charred, 3 minutes. Drizzle the herbed ricotta with olive oil and garnish with herbs and cracked pepper. Serve with the bread.',
    )
    r15 = Recipe(
        user_id=7,
        title='Bacon Candy',
        description='Crispy, sweet and salty, this three-ingredient snack is the ultimate cocktail party hors d\'oeuvre',
        image_url='https://www.spendwithpennies.com/wp-content/uploads/2019/11/Candied-Bacon-3.jpg',
        total_time='25 minutes',
        servings='20 strips',
        # ingredients='1/2 cup packed light brown sugar, 1 1/2 teaspoons chile powder, 20 slices of thick-cut bacon (1 1/2 pounds)',
        # directions='Preheat the oven to 400°. Line 2 rimmed baking sheets with foil. In a small bowl, whisk the brown sugar with the chile powder. Arrange the bacon strips on the foil and coat the tops with the chile sugar. Bake for 20 to 25 minutes, until caramelized and almost crisp. Transfer the bacon to a rack set over a sheet of foil to cool completely; serve.',
    )
    r16 = Recipe(
        user_id=7,
        title='Pappardelle with Chicken and Pistachio-Mint Pesto',
        description='Let\'s make a bright and nutty mint-and-pistachio pesto as the sauce for this fresh and summery warm pasta dish.',
        image_url='https://www.foodandwine.com/thmb/hEHd08HOo_UcpEtDxmw2bwFbd5E=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/pappardelle-with-chicken-and-pistachio-mint-pesto-XL-RECIPE1017-ffd1b2c4ef334d36a45a168b8cb0197d.jpg',
        total_time='30 minutes',
        servings='4 to 6 servings',
        # ingredients='1 1/2 cups lightly packed mint leaves plus more for garnish, 1/2 cup shelled unsalted pistachios, 1/4 cup fresh lemon juice, 1/2 cup extra-virgin olive oil, Kosher salt, Pepper, 8 ounces pappardelle pasta, 12 ounces shredded rotisserie chicken (3 cups), 1 small zucchini, very thinly sliced or shaved, 1 small yellow squash (very thinly sliced or shaved), 1 1/2 cups mixed cherry tomatoes(halved or quartered if large)',
        # directions='In a food processor, combine the 1 1/2 cups of mint with the pistachios and lemon juice and pulse until finely chopped. With the machine on, gradually add the olive oil until incorporated and the pesto is nearly smooth. Scrape into a large bowl and season generously with salt and pepper. Meanwhile, in a large saucepan of salted boiling water, cook the pasta until al dente. Drain well, reserving 1 cup of the cooking water. Add the pasta, chicken, zucchini, yellow squash, tomatoes and reserved cooking water to the pesto and toss well. Season generously with salt and pepper and toss again. Garnish with mint leaves and serve right away.',
    )
    r17 = Recipe(
        user_id=8,
        title='Pineapple-Coconut Soft Serve',
        description='With just five ingredients, this fluffy, effortless dessert comes together in minutes with a flavor reminiscent of a tiki cocktail. For an adult version, swap 1/4 cup of the coconut cream for the same amount of your favorite rum.',
        image_url='https://www.foodandwine.com/thmb/Cst4Mpbat3QNS9DDEO_t6dMgmnY=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/pineapple-coconut-soft-serve-FT-RECIPE0620-aafa228e086c4d6f86ece751241160e4.jpg',
        total_time='15 minutes',
        servings='12 servings',
        # ingredients='2 cups all purpose flour, 1 1/2 teaspoons kosher salt, 2 sticks unsalted butter (softened), 1 cup packed light brown sugar, 1/3 cup granulated sugar, 2 tablespoons whole milk, 1 teaspoon pure vanilla extract, 1 cup bittersweet chocolate chips',
        # directions='In a medium bowl, whisk the flour with the salt. In a large bowl, using a hand mixer, beat the butter with both sugars at medium speed until blended, about 2 minutes. At low speed, beat in the milk and vanilla until just combined. Add the dry ingredients and mix until just combined. Using a rubber spatula, fold in the chocolate chips. Eat the cookie dough straight out of the bowl or refrigerate in an airtight container for up to 2 weeks.',
    )
    r18 = Recipe(
        user_id=8,
        title='Edible Cookie Dough',
        description='There are so many reasons to make edible cookie dough. The weather is hot, the oven is broken or you have a fierce cookie dough craving. Perhaps all of the above. Enter edible cookie dough: Unburdened by leaveners or raw eggs, it can be enjoyed straight from the bowl with a spoon.We like classic chocolate chip dough, but the variations are endless. A couple of suggestions: Swap M&Ms, crushed Oreos or milk chocolate chips in for the bittersweet chips. Beat in 3 tablespoons of peanut butter with the butter, then fold in 1/2 cup each of chopped salted peanuts and chocolate chips.',
        image_url='https://www.foodandwine.com/thmb/g-JJMTQuptjfQg_f6GcexIJmtco=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/edible-cookie-dough-XL-RECIPE2016-e7c8d47454984f37bc743406f28f224c.jpg',
        total_time='10 minutes',
        servings='4 cups',
        # ingredients='1 1/2 pounds fresh pineapple chunks cut into 1/2-inch pieces (about 6 cups), 1 1/4 cups unsweetened coconut cream, 1/4 cup light agave nectar, Pinch of kosher salt, Toasted unsweetened flaked coconut for garnish',
        # directions='Spread pineapple in an even layer on a baking sheet lined with parchment paper. Freeze at least 8 hours or up to overnight. Place frozen pineapple, coconut cream, agave, and salt in a food processor; pulse until finely chopped, about 40 times. Process until smooth and airy, 3 to 4 minutes, stopping to scrape down sides of bowl as needed. Serve soft, or transfer to an airtight container, and freeze until just firm, about 1 hour. Garnish with flaked coconut.',
    )
    r19 = Recipe(
        user_id=9,
        title='Ricotta-Orange Pound Cake with Prosecco Strawberries',
        description='This is one cake that doesn\'t require any icing. Enjoy it with a cup of coffee or dessert wine.',
        image_url='https://www.foodandwine.com/thmb/L85DlVyqefV1gYJMN3BJsSqTR4g=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201405-xl-ricotta-orange-pound-cake-with-prosecco-strawberries-2000-bab153f0277b43f7aeed0c7f8913716d.jpg',
        total_time='2 hours 15 minutes',
        servings='8 servings',
        # ingredients='1 1/2 sticks unsalted butter, at room temperature plus more for greasing, 1 1/2 cups cake flour, 2 1/2 teaspoons baking powder, 1 teaspoon kosher salt, 1 1/2 cups fresh ricotta cheese, 1 1/2 cups plus 2 tablespoons granulated sugar, 3 large eggs, 2 tablespoons amaretto liqueur, 1 teaspoon pure vanilla extract, 1 teaspoon finely grated orange zest, 1 pound strawberries cut into quarters, 2 tablespoons Prosecco, Confectioners\' sugar for dusting, Lightly sweetened whipped cream for serving',
        # directions='Preheat the oven to 350°. Butter a deep, 9-inch round cake pan. In a bowl, whisk the cake flour, baking powder and salt. In another bowl, beat the ricotta, 1 1/2 sticks of butter and 1 1/2 cups of the sugar at medium-high speed until smooth. Beat in the eggs one at a time until just incorporated, then beat in the amaretto, vanilla and orange zest. Beat in the dry ingredients in 3 batches just until incorporated. Scrape the batter into the prepared pan and bake for 50 minutes, until a toothpick inserted in the center comes out with a few crumbs. Transfer to a rack to cool for 20 minutes; unmold and let cool completely. In a bowl, toss the strawberries with the Prosecco and remaining 2 tablespoons of sugar and let stand at room temperature until juicy, about 30 minutes. Dust the pound cake with confectioners\' sugar. Cut into wedges and serve with the strawberries and whipped cream.',
    )
    r20 = Recipe(
        user_id=10,
        title='Avocado Hollandaise',
        description='Luscious, rich, and lemony hollandaise gets completely re-imagined here in a light, supremely creamy puree of avocado, lemon juice, and olive oil.',
        image_url='https://www.kitchentreaty.com/wp-content/uploads/2018/03/avocado-hollandaise-8-700x980.jpg',
        total_time='10 minutes',
        servings='4 servings',
        # ingredients='1/2 very ripe medium Hass avocado peeled and chopped, 2 teaspoons fresh lemon juice, 2 tablespoons extra-virgin olive oil, Kosher salt, Freshly ground pepper, Poached eggs for serving',
        # directions='In a blender, combine the avocado and lemon juice with 1/3 cup of hot water. Puree until smooth and light in texture, about 2 minutes, scraping down the side of the bowl occasionally. With the machine on, drizzle in the olive oil and puree until combined. Season with salt and pepper. Serve the hollandaise over poached eggs.',
    )
    r21 = Recipe(
        user_id=10,
        title='Egg in a Bagel Hole',
        description='Adding water to the skillet helps cook the eggs evenly without burning the bagel halves, resulting in a lightly toasted bagel wrapped around a perfectly runny yolk. Savory smoked salmon and creamy avocado complete this classic breakfast.',
        image_url='https://www.foodandwine.com/thmb/pJ9JU-nv1VPTvyy1wkGvgsDLS8Q=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/egg-in-a-bagel-hole-FT-RECIPE0320-c1854893ac4f4b3385994a276de05873.jpg',
        total_time='10 minutes',
        servings='2 servings',
        # ingredients='1 everything bagel split, 2 tablespoons unsalted butter (softened), 2 large eggs, 1 tablespoon water, Kosher salt to taste, Black pepper to taste, 2 ounces cold-smoked salmon for serving, Caviar or sliced avocado for serving',
        # directions='If needed, carefully widen holes in bagel halves to 1 3/4 inches in diameter using a paring knife. Spread bagel halves evenly on both sides with butter. Heat a 12-inch skillet over medium. Place bagel halves, cut sides up, in skillet. Cook until golden brown, 2 to 3 minutes .Flip bagel halves cut sides down. Reduce heat to low; crack eggs into bagel holes. Pour 1 tablespoon water around edge of skillet, and immediately cover skillet. Cook until egg whites are set and yolks are cooked to desired degree of doneness, 5 to 8 minutes. Transfer bagel halves to a plate; season with salt and pepper. Serve with smoked salmon and caviar or sliced avocado.',
    )
    r22 = Recipe(
        user_id=2,
        title='Charred Shishito Peppers with Furikake',
        description='Whether eaten as a snack or incorporated into a main dish, crunchy, sweet shishito peppers are delicious and occasionally pack a punch — one in ten are super spicy!',
        image_url='https://www.foodandwine.com/thmb/G9jRJ_evJKG-Ogd_vvTLjJJ3TMw=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/charred-shishito-peppers-with-furikake-XL-RECIP0717_0-190ad594a07049f389b3da12a4d8a69b.jpg',
        total_time='15 minutes',
        servings='4 servings',
        # ingredients='2 teaspoons grapeseed or canola oil, 1 pound shishito peppers, 1 tablespoon furikake (see Note) plus more for garnish, 1 tablespoon fresh lime juice, 1 teaspoon shoyu or other soy sauce, Flaky sea salt, Lime wedges for serving',
        # directions='In a large cast-iron skillet, heat 1 teaspoon of the grapeseed oil. Add half of the peppers and cook over moderately high heat, turning occasionally, until charred and tender, about 4 minutes. Transfer to a large bowl. Repeat with the remaining oil and peppers. Add the 1 tablespoon of furikake, the lime juice and shoyu to the shishitos and toss to combine; season with flaky sea salt. Transfer to a platter; garnish with more furikake. Serve immediately with lime wedges.',
    )
    r23 = Recipe(
        user_id=3,
        title='Fig Jam',
        description='This supersimple fig jam recipe—just figs, sugar and lemon juice—can be easily upgraded with white port and rosemary for an extra special treat.',
        image_url='https://www.foodandwine.com/thmb/fEFCudK89VLOnrUqcSo5OG_cNik=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/fig-jam-FT-RECIPE0909-6c7a8cd04a8247e69b79398511173d92.jpg',
        total_time='45 minutes',
        servings='Makes three 1/2-pint jars',
        # ingredients='2 pounds green or purple figs, stemmed and cut into 1/2-inch pieces, 1 1/2 cups sugar, 1/4 cup plus 2 tablespoons fresh lemon juice, 1/2 cup water',
        # directions='In a large, nonreactive saucepan, toss the fig pieces with the sugar and let stand, stirring occasionally, for about 15 minutes, until the sugar is mostly dissolved and the figs are juicy. Add the lemon juice and water and bring to a boil, stirring until the sugar is completely dissolved. Simmer the fig jam over moderate heat, stirring occasionally, until the fruit is soft and the liquid runs off the side of a spoon in thick, heavy drops, about 20 minutes. Spoon the jam into three 1/2-pint jars, leaving 1/4 inch of space at the top. Close the jars and let cool to room temperature. Store the jam in the refrigerator for up to 3 months.',
    )
    r24 = Recipe(
        user_id=4,
        title='Sunflower-Seed Brittle',
        description='Pair this delightful crunchy sunflower-seed brittle with 5 Spoke Creamery Tumbleweed cheese or other semi-firm cow\'s milk cheese, like sharp cheddar!',
        image_url='https://www.foodandwine.com/thmb/BdIy-9AAQUiteT5OL5DO5myqu9A=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/200812-r-xl-sunflower-seed-brittle-1687040503e84dc1bb71ebdf894463c6.jpg',
        total_time='30 minutes',
        servings='1 pound',
        # ingredients='1 cup sugar, 1/2 cup water, 1/2 cup light corn syrup, 1 1/2 tablespoons unsalted butter (at room temperature), 1 teaspoon kosher salt, ½ teaspoon baking soda, 2 cups raw sunflower seeds',
        # directions='Line a large, rimmed baking sheet with parchment paper and lightly oil the paper. In a medium saucepan, combine the sugar, water and corn syrup and bring to a boil. Boil over moderate heat until the caramel is golden and registers 320° on a candy thermometer, about 10 minutes. Remove from the heat and stir in the butter, salt and baking soda. Stir in the sunflower seeds and quickly spread the mixture on the prepared baking sheet in a thin layer. Let the brittle stand until completely cool, then break into pieces.',
    )
    r25 = Recipe(
        user_id=5,
        title='Caramelized Broccoli with Garlic',
        description='Slowly caramelizes broccoli to bring out its sweetness, then revitalizes it with a squeeze of lemon and a pinch of crushed red pepper. The resulting broccoli is tender, flavorful, and makes an easy side dish.',
        image_url="https://www.foodandwine.com/thmb/s9UPydFVtFfy8nPJ2XhpNl4V1Vs=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Caramelized-Broccoli-with-Garlic-FT-RECIPE0822-2000-926848df43b3456ba0d4aa6dfb6766e9.jpg",
        total_time='35 minutes',
        servings='4 servings',
        # ingredients='3 tablespoons extra-virgin olive oil, 2 heads of broccoli (1 1/4 pounds total) stems peeled and heads halved lengthwise, 1/2 cup water, 3 cloves garlic (thinly sliced), Pinch of crushed red pepper, 2 tablespoons fresh lemon juice, Salt and freshly ground black pepper',
        # directions='In a large, deep skillet, heat 2 tablespoons of the olive oil. Add the broccoli, cut side down, cover, and cook over moderate heat until richly browned on the bottom, about 8 minutes. Add the water, cover, and cook until the broccoli is just tender and the water has evaporated, about 7 minutes. Add the remaining 1 tablespoon of olive oil along with the garlic and the crushed red pepper and cook uncovered until the garlic is golden brown, about 3 minutes. Drizzle with the lemon juice, season the broccoli with salt and black pepper, and serve.',
    )
    r26 = Recipe(
        user_id=6,
        title='Thanksgiving Leftovers Nachos',
        description='Make next-level nachos with leftovers from your Thanksgiving meal. These leftovers include diced turkey, chopped roasted vegetables, and whole cranberry sauce, but any leftovers you have can be used because gooey Monterey Jack cheese brings them all together.',
        image_url='https://www.foodandwine.com/thmb/fWr9ev8VxVxbPnkaGicfBOySDAE=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/thanksgiving-leftover-nachos-ft-blog1119-1-17ca813a83ee4cc099a9f69a30888161.jpg',
        total_time='30 mins',
        servings='6 to 8 servings',
        # ingredients='Extra-virgin olive oil for brushing, 13 ounces thick tortillas chips, 2 pounds shredded Pepper Jack cheese, 3 cups diced roasted vegetables, 12 ounces shredded or diced roasted turkey, 3/4 cup whole cranberry sauce, Cilantro sprigs (thinly sliced), jalapeños and pickled red onion for topping, Sour cream and hot sauce for serving',
        # directions='Preheat the oven 400°. Brush a large rimmed baking sheet with olive oil. Spread half of the tortilla chips on the sheet and top with half each of the cheese, vegetables, turkey, and cranberry sauce. Repeat the layering with the remaining chips, cheese, vegetables, turkey, and cranberry sauce. Bake for 12 to 15 minutes, until the cheese is melted. Top the nachos with cilantro, jalapeños, and pickled red onion; serve right away with sour cream and hot sauce.',
    )
    r27 = Recipe(
        user_id=7,
        title='Garlic Confit',
        description='Although garlic is available year-round, fresh summer garlic has large cloves that are especially sweet and juicy. To preserve it, just simmer the cloves with dried red chiles and fresh thyme in olive oil until tender then packs them in the oil. Mash the garlic confit in butter and spread it on bread or slip it under chicken skin before roasting.',
        image_url='https://www.foodandwine.com/thmb/cJYRlmkRz92GQvHCbcqk6lKufwM=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/201110-xl-garlic-confit-36c97e3336bc44e496925b4f78cf2f3d.jpg',
        total_time='1 hour',
        servings='Makes 1 1/2 pints',
        # ingredients='6 heads of garlic, cloves peeled (2 cups), 6 thyme sprigs, 3 small bay leaves, 3 dried red chiles such as chiles de arbol, 2 cups pure olive oil',
        # directions='Combine all of the ingredients in a medium saucepan and simmer over low heat until the garlic is tender but not browned, about 30 minutes. Let cool. Using a slotted spoon, transfer the garlic, herbs and chiles to three 1/2-pint canning jars. Pour the cooking oil on top, seal and refrigerate for up to 4 months.',
    )
    r28 = Recipe(
        user_id=8,
        title='Apple-Pomegranate Cobbler',
        description='This juicy and bright apple cobbler is just the right amount of sweet, with an irresistibly tender and crunchy crust on top',
        image_url='https://www.foodandwine.com/thmb/BFk1o6eRsWwsH4B2n9MJNwPQOQM=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/apple-pomegranate-cobbler-XL-RECIPE1017-311bded52afb441d8a506b161eb86df6.jpg',
        total_time='2 hrs',
        servings='8 to 10 servings',
        # ingredients='2 cups pomegranate juice, 6 peeled Granny Smith apples (3 pounds) sliced 1/2 inch thick, 1 cup sugar plus more for sprinkling, 2 1/4 cups all-purpose flour, Kosher salt, 2 teaspoons baking powder, 1 stick cold unsalted butter cut into small pieces, 1 cup cold heavy cream plus more for brushing, Pomegranate seeds, Vanilla ice cream for serving',
        # directions='Preheat the oven to 375°. Place an 8-by-8-inch glass baking dish on a foil-lined rimmed baking sheet. In a small saucepan, bring the pomegranate juice to a boil over moderately high heat until reduced to 1/3 cup, about 15 minutes. Pour the juice into a large bowl and fold in the apples, 3/4 cup of the sugar, 1/4 cup of the flour and 1/2 teaspoon of salt. Scrape the mixture into the baking dish. In another large bowl, whisk the remaining 2 cups of flour with the remaining 1/4 cup of sugar, the baking powder and 1/2 teaspoon of salt. Add the butter and, using a pastry cutter or 2 knives, cut the butter into the dry ingredients until the mixture resembles very coarse crumbs, with some pieces the size of small peas. Gently stir in the 1 cup of cream just to combine. Gather the topping into small clumps and scatter over the apple filling. Brush the topping with cream and sprinkle generously with sugar. Bake the cobbler for 60 to 70 minutes, or until the filling is bubbling and the topping is golden. Tent with foil if the crust browns too quickly. Let cool for 20 minutes. Serve sprinkled with pomegranate seeds and topped with vanilla ice cream.',
    )
    r29 = Recipe(
        user_id=9,
        title='Carrot Cake Marmalade with Yogurt and Fresh Fruit',
        description='Everyone is raving about this yogurt bowl topped with sunny roasted carrot marmalade. The marmalade gets a big flavor from stewing carrots and apple with cinnamon, cardamom, and star anise for a warmly spiced result.',
        image_url='https://www.foodandwine.com/thmb/gae981F-9W4O3_NCudbSZMSvADM=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/carrot-cake-marmalade-with-yogurt-and-fresh-fruit-FT-RECIPE0221-1867851526da4613abbf4e863f51e224.jpg',
        total_time='1 hours 40 minutes',
        servings='Makes 2 1/3 Cups',
        # ingredients='1 pound carrots, shredded (about 3 1/2 cups or 12 ounces), 2 cups water plus more if needed, 1 medium-size peeled Honeycrisp apple (about 7 ounces),  1 cup shredded Honeycrisp apple, 1 cup granulated sugar, 2 teaspoons grated lemon zest plus 1/4 cup fresh lemon juice, 3 cardamom pods (lightly smashed), 2 whole star anise, 2 cinnamon sticks, 3/4 teaspoon kosher salt, 2 tablespoons honey, yogurt, blueberries, clementine segments, granola for serving',
        # directions='Place carrots, 2 cups water, apple, sugar, lemon zest and juice, cardamom pods, star anise, cinnamon sticks, and salt in a large heavy-bottomed saucepan; bring to a boil over medium-high, stirring occasionally. Cover and reduce heat to medium; cook, stirring occasionally, until carrots are crisp-tender, about 15 minutes. Uncover and cook, stirring occasionally, until carrots are tender and liquid has reduced to a thin, syrupy consistency, 20 to 25 minutes. Remove from heat, and discard whole spices. Transfer carrot mixture to a blender; add honey. Blend on low speed 1 minute. Continue blending, gradually increasing speed to medium-high, until smooth, about 1 minute, adding additional water, 1 tablespoon at a time, if necessary to keep puree moving. Transfer mixture to a small bowl; refrigerate 20 minutes.',
    )
    r30 = Recipe(
        user_id=1,
        title='Blueberry Scones with Lemon Glaze',
        description='These better-than-the-bakery blueberry scones are bursting with juicy blueberries. These scones are crunchy and golden on the outside, soft and moist in the middle, with a drizzle of lemon glaze on top. Perfect for your next brunch! Making scones from scratch is easy and rewarding. The baking process is quick and simple.',
        image_url='https://www.aheadofthyme.com/wp-content/uploads/2018/08/glazed-lemon-blueberry-scones-7-1.jpg',
        total_time='33 minutes',
        servings='12 scones',
        # ingredients='2 cups all-purpose flour(plus more for dusting), 2 tablespoons sugar, 1 ½ teaspoons baking powder, ¾ teaspoon salt, ¼ teaspoon ground cinnamon, 5 tablespoons unsalted butter ( cold & cut into cubes) , 1 cup fresh blueberries, ½ cup buttermilk, ½ cup  & 1 tablespoon heavy cream (divided),  1 egg (beaten),  ½ cup confectioner sugar, juice from 1 lemon',
        # directions='1. Preheat oven to 400 F. In a large bowl, sift together flour, sugar, baking powder, salt, and cinnamon. Add butter and using your hands or a pastry cutter, cut the butter into the flour until the size of peas, working quickly so the butter stays cold. Carefully fold in blueberries so they don’t burst. In a small bowl, combine buttermilk and ½ cup heavy cream. Make a well in the center of the flour mixture, then pour in the liquid mixture. Use a rubber spatula to carefully fold the ingredients until the liquid is just incorporated.  Roll the dough out onto a lightly floured surface, adding more flour as needed if too sticky to work with. Press down into a small rectangle, about 6-inches by 8-inches. Cut the dough in half once horizontally and twice vertically to create 6 equal rectangles. Slice each rectangle in half diagonally to form 12 triangle-shaped scones. Carefully transfer scones to a large half sheet baking pan lined with a silpat baking mat or parchment paper. In a small bowl, whisk together egg and 1 tablespoon heavy cream. Brush the tops of the scones with egg wash, then bake for 16-18 minutes, or until scones are lightly golden brown. Let cool 5 minutes in pan, then transfer to a wire rack to cool completely. While scones are cooling, combine confectioner’s sugar and half the lemon juice in in a small bowl. Whisk until combined, adding more lemon juice as needed to reach desired glaze consistency. When scones are cool, drizzle lemon glaze on top.',
    )
    r31 = Recipe(
        user_id=2,
        title='Seared Scallops With Brown Butter and Lemon Pan Sauce',
        description='Fresh scallops are bathed in a pan-sauce of nutty brown butter that is flavored with fresh lemon, capers and chives. Ridiculously easy to make, an ideal dish for a busy weeknight meal or to serve as a starter at your next dinner party. You’ll fall in love with the rich and zesty taste of this dish.',
        image_url='https://assets.epicurious.com/photos/5a3002b504847a34b821cb4a/1:1/w_2240,c_limit/seared-scallops-with-brown-butter-and-lemon-pan-sauce-recipe-BA-121217.jpg',
        total_time='20 minutes',
        servings='4 servings',
        # ingredients='3 lemons, Small handful of chives, 12 large dry sea scallops, Kosher salt, freshly ground pepper, Extra-virgin olive oil or vegetable oil, 3 tablespoons unsalted butter (cut into pieces), 2 teaspoons drained capers',
        directions='Cut 2 lemons in half and squeeze juice into a measuring glass or small bowl; you should have 1/4 cup juice. Set aside. Using a paring knife, cut ends off remaining lemon to expose flesh. Upend lemon on a cut end and remove peel and white pith from lemons; discard. Cut between membranes to release segments into bowl with juice; squeeze membranes to get any last drops of juice. Fish out any seeds; set aside. Thinly slice chives and place in a small bowl; set aside. Pull side muscle off scallops, if needed; pat dry. Season lightly on both sides with salt and pepper. Heat a large skillet, preferably stainless steel, over medium-high. Pour in oil to lightly coat surface (2–3 Tbsp.); heat until it shimmers and you see first wisps of smoke. Swiftly place scallops into skillet, flat side down, and cook without touching, tossing, or fussing until underside is deep golden brown, 3–4 minutes. Use a thin spatula or tongs to gently turn over; if they resist, cook another 30 seconds and try again. Cook on second side until flesh at top and bottom looks opaque but there is still a faintly translucent strip in the middle, 1–2 minutes, depending on size. Transfer scallops to a plate. Pour off any oil in skillet and set over medium heat. Add butter and cook, swirling, until butter foams, then browns, about 2 minutes. Add reserved lemon juice and segments; energetically stir and swirl pan to emulsify sauce. Mix in capers and reserved chives and spoon pan sauce around and over scallops.',
    )
    r32 = Recipe(
        user_id=3,
        title='Kale Pesto With Whole Wheat Pasta',
        description='This is one of our most feel-good easy pasta recipes. What more delicious way is there to eat your greens than blended with Parmesan cheese into a pesto and coating warm noodles?',
        image_url='https://assets.bonappetit.com/photos/5df7e83c95932c0008b0d4f4/1:1/w_2580%2Cc_limit/HLY-FGFP-Kale-Pesto-16x9.jpg',
        total_time='30 minutes',
        servings='4 servings',
        # ingredients='1 large bunch Tuscan kale, ribs and stems removed, Kosher salt, 12 oz. farro pasta or whole wheat pasta, ⅓ cup raw pistachios, ¼ cup extra virgin olive oil, 1 garlic clove, 1 oz. Parmesan, finely grated, plus more for serving, 2 Tbsp. unsalted butter, Freshly ground black pepper',
        # directions='Cook kale leaves in a large pot of boiling salted water until bright green and wilted, about 30 seconds. Transfer to a rimmed baking sheet with tongs; keep water boiling. Let kale cool slightly; wring out excess water with your hands. Cook pasta in pot of boiling water, stirring occasionally, until al dente. Blend nuts, oil, garlic, and ⅓ cup water in a blender or food processor until very smooth. Add kale and 1 oz. Parmesan. Purée, adding water 1 Tbsp. at a time as needed, until smooth. Transfer pesto to a large bowl. Using tongs, transfer pasta to bowl with pesto; add butter and ⅓ cup pasta cooking liquid. Toss, adding more pasta cooking liquid by the tablespoonful if needed, until sauce coats pasta. Divide among bowls; top with more Parmesan and a few grinds of pepper.'
    )
    r33 = Recipe(
        user_id=4,
        title='Upside Down Winter Citrus Cake',
        description="Instead of peeling the citrus and then slicing it, slice it with the skin on and use the tip of your knife to cut off the outer layer of skin. This will ensure that the citrus fruit slices properly and doesn't fall apart or lose its juice when you slice it. Grapefruits, pomelos, tangerines, oranges, any types of citrus fruits would all work for this citrus cake recipe. I like using a blend of sweet and tart citrus fruits, but follow your heart on this one!",
        image_url='https://bromabakery.com/wp-content/uploads/2017/01/Upside-Down-Winter-Citrus-Cake-L-P-7.jpg',
        total_time='1 hour 15 minutes',
        servings='6 servings',
        # ingredients='2 blood oranges, 2 navel oranges, 1 tangelo, small grapefruit, or other citrus of choice, 1/2 cup granulated sugar, 1/4 cup water, 1/2 cup butter, (room temperature), 1/3 cup white sugar, 1/3 cup brown sugar, 2 large eggs (room temperature), 3 tablespoons freshly squeezed orange juice (from any type of orange), 1 tablespoon orange zest (from any type of orange), 1 tablespoon vanilla extract, 1 1/2 cups plus 1 tablespoon all purpose flour, 1 teaspoon baking powder, 1/4 teaspoon baking soda, 1/2 teaspoon salt, 2/3 cup plain non- or low-fat yogurt',
        # directions='Preheat oven to 350°F. Line a 9 inch cake pan pan with parchment paper so that it covers the bottom and goes up the sides of the pan. Fold parchment paper so that it hugs the sides of the pan, like an upside down hat. Spray with non-stick spray. With the skin still on, slice citrus 1/2 inch thick. Use a paring knife to carefully remove the skin from the citrus slices (like cutting off the outer ring). Doing it this way will ensure your oranges citrus stays intact and does not break apart when you slice it. Microwave the sugar and water together until the sugar dissolves completely, about 45 seconds. Pour half of the sugar-water into the bottom of the prepared cake pan, then line the bottom with prepared citrus fruits. Once arranged, pour the remaining sugar-water over the citrus. Set aside. In a large bowl, beat the butter and sugars together until light and fluffy. Add in the eggs, orange juice, orange zest, and vanilla extract. In a separate bowl, combine the flour, baking powder, baking soda, and salt, whisking to combine. Slowly alternate folding in the flour mixture and the yogurt into the wet ingredients until everything is combined. Mixture will be thick. Pour the batter over the prepared citrus slices, spreading it evenly to the edges. Bake for 35 minutes, then allow to cool completely before inverting onto a serving tray.',
    )
    r34 = Recipe(
        user_id=5,
        title='Lemongrass Ginger Steamed Mussels in Coconut Broth',
        description="This tropical twist on the French classic moules marinières serves up briny mussels in a tangy coconut broth enhanced by ginger and lemongrass. You'll find the pretty green stalks of fresh lemongrass in the produce section of many fine supermarkets and specialty-food shops, alongside the brown knobby fresh ginger rhizomes, or roots. Both aromatics need to be peeled before using, and both have dense, stringy flesh that can be difficult to mince. Grating is a good solution for ginger; include the juices that are extruded when you scrape. For lemongrass, peel and use only the tender midsection of the slender, bulblike stalk. Smash it with the flat side of a chef's knife to make mincing easier. Increase your dining pleasure by sipping, as an accompaniment, any bright, fresh white wine that offers good acidity. Think sparkling wine, unoaked Chardonnay, Pinot Grigio, or Sauvignon Blanc.",
        image_url='https://lepetiteats.com/wp-content/uploads/2021/10/IMG_9352-1.jpg',
        total_time='30 minutes',
        servings='4 servings',
        # ingredients='1 tablespoon coconut oil, 1 clove garlic thinly sliced, 1 stalk lemongrass trimmed and finely chopped, 1 Thai chile diced, plus more for serving, 1 teaspoon freshly grated ginger, 1 cup unsweetened coconut milk, 1 cup vegetable broth or fish broth, 1 teaspoon fish sauce, 1 teaspoon coconut sugar, 1 1/2 pounds mussels scrubbed, 1 tablespoon fresh lime juice, 1 teaspoon lime zest, Handful fresh cilantro leaves',
        # directions='Heat coconut oil in a Dutch oven on medium-low heat. Add garlic, lemongrass and chile and cook until softened, about 2 minutes. Add ginger and cook for 1 minute more, then stir in coconut milk, broth, fish sauce and coconut sugar. Bring mixture to a simmer, then add mussels. Cover and simmer, stirring occasionally, until the shells open, 5 to 6 minutes (discard any mussels that failed to open). Remove from heat and stir in lime juice. Divide mussels and broth evenly into four bowls. Garnish with lime zest, cilantro and chile.',
    )
    r35 = Recipe(
        user_id=6,
        title='Pineapple Fried Rice',
        description="If you want to turn your leftover rice into a dish with multiple layers of flavor, look no further! Ready in 30 minutes, this pineapple fried rice is crisp and delicious with sweet, juicy pineapple bites and crunchy, salty cashews. Serve as a side or enjoy as a full entree. I like to top my pineapple fried rice with some sesame seeds, more green onions, and some sriracha for a little more spice. I’m also a huge fan of fresh lime, so I like to squeeze a wedge over the top!",
        image_url='https://images.squarespace-cdn.com/content/v1/5bff85572971146fb81d6d24/1666052157377-UDFRNXYILSKQS9EV9Q3W/8O7A9734-2.jpg',
        total_time='30 minutes',
        servings='4 servings',
        # ingredients='2 cups fresh pineapples (cut into ½ inch chunks), ½ a bell pepper (diced), 1 stalk green onion, 2 cloves garlic (minced), 1 teaspoon red curry paste, 1 cup protein of choice, 3 cups (day-old) rice, 1 tablespoon fish sauce, 2 teaspoons soy sauce, ¼ cup roasted cashews',
        # directions='In a large wok, heat up with a drizzle of oil. Let it get hot and add in the curry paste. If cooking with chicken, add the chicken cut into small pieces, and stir fry for 4-5 minutes until cooked through. If using shrimp, cook for a minute until pink and remove / set aside. If cooking shrimp and chicken, then leave in and add the pineapples, bell pepper, garlic, and green onion. Nestle the shrimp on top of the veggies to slow down the cooking process. Once the pineapple starts to caramelize for (about 3 minutes), add the cold rice and break it up a bit. Add the fish sauce and soy sauce, the cashews, mix well and serve.',
    )
    r36 = Recipe(
        user_id=7,
        title='Japanese-Style Chili Burgers with Yuzu Mayo',
        description='This burger is a two-hander, topped with Japanese-spiced chili, tomatoes, and shredded iceberg lettuce. Be careful not to overmix the beef before shaping it into patties; a light hand yields tender burgers',
        image_url='https://www.foodandwine.com/thmb/h_oC7W8DwN9MaFBut-KbnMwhepE=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/japanese-style-chili-burgers-with-yuzu-mayo-FT-RECIPE0620-2f8384135fc042e79cc256d17ad672f9.jpg',
        total_time='50 minutes',
        servings='8 servings',
        # ingredients='1 cup Kewpie mayonnaise, 1/2 cup ketchup, 1 tablespoon bottled yuzu juice, 1 (28-ounce) can whole peeled tomatoes, 1 tablespoon olive oil, 4 pounds ground beef, divided, 1 cup finely diced yellow onion, 4 teaspoons kosher salt, divided, 1/4 cup tonkatsu sauce, 2 teaspoons gochugaru, 2 teaspoons turbinado sugar, 1 1/2 teaspoons ground coriander, 1 1/2 teaspoons ground cumin, 1/2 cup (4 ounces) sake, 1/4 cup cold water, 2 tablespoons all-purpose flour, 1 teaspoon smoked paprika, 1 1/2 teaspoons black pepper, divided, 8 sesame seed hamburger buns, buttered and toasted, 8 fresh tomato slices, 2 cups shredded iceberg lettuce',
        # directions='Stir together Kewpie mayonnaise, ketchup, and yuzu juice in a bowl. Refrigerate until ready to serve. Process canned tomatoes in a food processor until smooth, about 1 minute. Set processed tomatoes aside. Heat oil in a small saucepan over medium-high. Add 1 pound ground beef, onion, and 2 teaspoons salt; cook, stirring occasionally, until meat is no longer pink and onion is lightly browned, about 7 minutes. Add processed tomatoes, tonkatsu, gochugaru, sugar, coriander, and cumin; stir in sake. Bring to a simmer. Stir together 1/4 cup cold water and flour in small bowl; add to ground beef mixture, and stir to combine. Stir in smoked paprika and 1/2 teaspoon black pepper. Reduce heat to medium-low, and return to a simmer. Cook, stirring often, 10 minutes. Remove from heat. Preheat grill or griddle to medium (350°F to 450°F). Gently stir together remaining 3 pounds ground beef, remaining 2 teaspoons salt, and remaining 1 teaspoon black pepper in a large bowl until just combined. Shape mixture into 8 (6-ounce) patties, pressing to 1/2-inch thickness. Place on oiled grates, and grill, covered, to desired degree of doneness, about 5 minutes per side for medium. Place patties on buns. Top each with 1/3 cup chili, 1 tomato slice, 1/4 cup lettuce, and 1 tablespoon mayonnaise mixture.',
    )
    r37 = Recipe(
        user_id=8,
        title='Cheesecake-Topped Brownies',
        description='These excellent cheesecake brownies consist of a rich fudge brownie layer topped with an ultra-simple cheesecake that uses sweetened condensed milk.',
        image_url='https://images.food52.com/dhdsppI7wle5RaHieDp5H9BtpE8=/2016x1344/filters:format(webp)/ac2bbe69-7288-478d-9010-a834d5efec09--DSC_0333.JPG',
        total_time='50 minutes',
        servings='one pan',
        # ingredients='4 eggs, 1 1/4 cups Dutch-processed cocoa, 1 teaspoon salt, 1 teaspoon baking powder, 1 teaspoon espresso powder (optional),1 tablespoon vanilla, 1 cup (2 sticks) unsalted butter, 2 cups sugar, 1 1/2 cups flour, 1 3/4 cups semisweet chocolate chips (or bittersweet chocolate chips), 8 ounces cream cheese (softened), 2 tablespoons unsalted butter (softened), 1 tablespoon cornstarch, 14 ounces sweetened condensed milk, 1 egg, 1 tablespoon vanilla',
        # directions="Preheat your oven to 350° F. Grease an 9x9 pan (if you want less thick brownies, use a 9x13 pan). Make the brownies: In a medium bowl, beat the eggs with the cocoa powder, salt, baking powder, espresso powder (if using), and vanilla. Beat for a few minutes until well combined. In the microwave or in a saucepan over medium heat, melt the butter with the sugar and stir until the sugar dissolves. Add the hot sugar and butter mixture to the bowl with the cocoa mixture. Stir to combine well. Add the flour and chocolate chips and mix well until shiny. Pour the brownie batter into the prepared pan and bake for 20 to 25 minutes—the crust should be just set, but the brownies shouldn't be cooked through. While the brownies bake, make the cheesecake layer. In a large bowl or stand mixer, beat together the cream cheese, softened butter, and cornstarch. Slowly add the condensed milk, egg, and vanilla and mix until very well combined. When the brownies have finished their first bake, remove them from the oven and pour the cheesecake batter over the top. Return the pan to the oven and bake for 25 to 30 minutes, or until the top is just beginning to brown. Let cool, then slice.",
    )
    r38 = Recipe(
        user_id=9,
        title='Clementine Chocolate Lava Cakes',
        description='These gooey, single-serving chocolate cakes are just set and scented with winter citrus. I like to serve these individual chocolate cakes for dessert at the end of long dinner parties (everyone loves chocolate). But more often than not I just end up making a batch, baking one ramekin off for myself right there, and stashing the rest, covered, in the fridge for the next three nights. This recipe is easily divisible by half if you wish to only make two ramekins, which I often do when I have a date coming over for dinner.',
        image_url='https://images.food52.com/XQ7FmMZZzjTMbgykFf4ORrizVOs=/2016x1344/filters:format(webp)/0c422583-0aa6-4762-a831-cad8a37833f9--2018-1211_clementine-chocolate-lava-cakes_3x2_bobbi-lin_17709.jpeg',
        total_time='15 minutes',
        servings='4 servings',
        # ingredients='4 ounces dark bittersweet chocolate (60 percent or more cacao), 2 large eggs, 1/2 cup (scant) granulated sugar, 1 pinch kosher salt, 1 teaspoon vanilla extract, Zest of 1 clementine or satsuma mandarin, 1/4 cup plus 2 tablespoons olive oil, Confectioner sugar for garnish (optional), Vanilla ice cream for serving (optional)',
        # directions="Preheat the oven to 400°F. Grease four 6-ounce ramekins and place them on a sheet pan. Melt the chocolate in the microwave and set aside to cool slightly. In a separate bowl, whisk together the eggs, sugar, salt, vanilla, clementine zest, and olive oil until light and fluffy (you don't have to go overboard here; just incorporate all of the ingredients—though, if you have the wherewithal in you, a little air in the eggs now will result in a deliciously chewy-edged lava cake later). Fold in the chocolate. Pour batter into the ramekins and bake for 10 to 15 minutes, or until just cooked. (The tops should be slightly cracked, the insides hot and gooey.) Dust with powdered sugar before serving, or top with vanilla ice cream.",
    )
    r39 = Recipe(
        user_id=10,
        title='Grilled Pork Chop with Bourbon Peach Sauce',
        description="A good pork chop dinner just warms the soul! This dish is part American Southern, with its peaches and bourbon, part French country cuisine, with its shallots and Dijon, and 100 percent delicious.",
        image_url='https://challengedairy.com/sites/default/files/recipe/images/recipe_grilled_pork_chop_with_bourbon_peach_sauce_2280.jpg',
        total_time='30 minutes',
        servings='4 servings',
        # ingredients='2 Tablespoons Challenge Dairy Butter, 1 shallot, minced, ⅓ cup brown sugar, 2 Tablespoons bourbon, 2 Tablespoons apple cider vinegar, 1 teaspoon Dijon mustard, Kosher salt, 3 peaches (pitted, peeled and roughly chopped - about 2 cups), ¼ cup brown sugar, 1 ½ teaspoon ground ginger, 2 teaspoon Kosher salt, ½ teaspoon black pepper, 3 pounds bone-in pork chops (each 1 ½ inches thick), ¼ cup & 4 Tablespoons butter(melted)',
        # directions='For the Bourbon Peach Sauce: Melt butter in a small saucepan over medium heat. Add shallot and cook until softened, about 3 minutes. Stir in brown sugar, bourbon, vinegar, mustard, 1/2 teaspoon kosher salt and chopped peaches. Bring to a gentle simmer and cook, stirring occasionally, until peaches are soft and the sauce has thickened, 15-20 minutes. Keep warm. For the Grilled Pork Chops: Turn all burners on gas grill to high, cover, and heat until hot, about 15 minutes. Leave primary burner on high and turn other burners to medium. Combine brown sugar, ginger, salt and pepper in a small bowl. Pat pork chops dry and coat all over with sugar mixture. Oil grates and place chops on hot side of grill. Cook 8-10 minutes, flipping halfway, until browned on both sides. Move to cooler side of grill and brush with melted butter. Continue to cook, turning once and brushing with more butter, until an instant read thermometer registers 145°F when inserted into the center of the chop, about 5 more minutes. Transfer to a platter and spoon warm bourbon peach sauce over the meat.',
    )
    r40 = Recipe(
        user_id=5,
        title='Ricotta-Rosemary Cake With Fresh Figs',
        description="Serving a single-layer cake is the ultimate way to seem effortlessly cool. They don’t require frosting or fancy decorations to make a splash. As long as the top has something exciting going on—in this case, fresh figs, whipped cream, and crunchy rosemary sugar—you don’t need anything else. This one is made in just two bowls, and you don’t have to struggle with creaming butter and sugar together. It’s also flexible, so feel free to use whatever fruit is in season in place of fresh figs.",
        image_url='https://images.food52.com/d1ZLpS7HWfNQ7YmBJuQcHfemjwk=/2016x1344/filters:format(webp)/4371361e-3dfe-4a59-8e84-6ff9e1c0c1cc--2018-0914_fig-cake_3x2_jenny-huang_32694.jpg',
        total_time='1 hour',
        servings='One 9-inch cake',
        # ingredients='1 stick unsalted butter - melted and slightly cooled (plus more for greasing pan), 2 tablespoons turbinado sugar, 2 teaspoons finely chopped fresh rosemary, 1 1/2 cups pastry flour, 1 cup plus 2 tablespoons granulated sugar (divided), 2 teaspoons baking powder, 1 teaspoon kosher salt, 3 large eggs (room temperature), 1 1/2 cups whole milk ricotta cheese, 2 teaspoons vanilla extract, 1/2 teaspoon lemon zest, 2 cups fresh figs (quartered and divided), 1 cup heavy whipping cream',
        # directions='Preheat oven to 350° F. Grease a 9-inch round cake pan with butter and line the bottom with parchment paper. Combine turbinado sugar and chopped rosemary in a small bowl. Using your fingers, gently massage the rosemary into the sugar. Set aside. Sift flour, 1 cup of granulated sugar, baking powder, and salt into a large bowl. In a separate bowl, whisk together eggs, ricotta, vanilla extract, lemon zest, and melted butter. Add cheese mixture to flour mixture and stir until smooth. (Batter will be very thick.) Transfer batter into prepared pan, smooth out the top with a spatula. Sprinkle with half of the prepared rosemary sugar and scatter half of the figs over top. Bake until a toothpick comes out clean, about 45 minutes. Let cool completely. As the cake is cooling, combine remaining 2 teaspoons granulated sugar and heavy cream in the bowl of a stand mixer fitted with a whisk attachment. Whip on medium speed until cream is light and airy, about 45 seconds. Dollop whipped cream in the center of the cake and top with remaining figs and rosemary sugar.'
    )
    r41 = Recipe(
        user_id=2,
        title='Honey Butter',
        description="Honey butter is creamy and utterly irresistible. It’s sweet and a little bit salty, which always sends me back for more. It looks dazzling on the table, and it makes everyone’s eyes light up. This recipe tastes extra-special thanks to a little sprinkle of cinnamon. Finish it with a little drizzle of honey and a light sprinkle of salt for bonus points in flavor and visual appeal.",
        image_url='https://cookieandkate.com/images/2022/04/honey-butter-recipe-3-768x1155.jpg',
        total_time='5 minutes',
        servings='3/4 cup',
        # ingredients='One stick of softened unsalted butter (4 ounces or 8 tablespoons), 3 tablespoons honey, ¼ teaspoon ground cinnamon,⅛ teaspoon fine salt , For garnish: Drizzle of honey and a sprinkle of flaky sea salt or kosher salt',
        # directions='In a 2-cup liquid measuring cup (or other small, shatter-proof mixing bowl with tall sides), combine the softened butter, honey, cinnamon and salt. Using a hand mixer, whip the ingredients together until the butter is light and fluffy. Transfer the mixture to a small serving bowl. Lightly drizzle honey on top, followed by a little sprinkle of flaky salt or kosher salt.  Serve promptly, or refrigerate for later (let the mixture come back to room temperature before serving). Leftovers keep well in the refrigerator, covered, for up to 5 days.',
    )
    r42 = Recipe(
        user_id=12,
        title='Creamy Mashed Potato Soup with Dashi',
        description="Dashi and soy sauce add umami to buttery leftover mashed potatoes in this cozy soup.Add milk for a creamier texture, or more dashi for a thinner consistency. Substitute any mashed vegetable you have on hand, such a cauliflower or sweet potato, but be sure to finish the soup with generous pats of melting butter and an extra drizzle of soy.",
        image_url='https://www.foodandwine.com/thmb/hgK1MkNfJdr0ngAd8s3UDwyX7Lw=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/creamy-mashed-potato-soup-with-dashi-FT-RECIPE1120-aadb2f951a6c4bf4a75187423694a96a.jpg',
        total_time='4 hours',
        servings='4 servings',
        # ingredients='1 medium-size yellow onion (finely chopped), 2 large celery stalks, finely chopped, 2 1/2 to 3 1/2 cups dashi or chicken stock, 3 cups leftover mashed potatoes, 1/4 cup whole milk (optional), 1/2 teaspoon kosher salt or to taste, 1/4 teaspoon black pepper or to taste, Unsalted butter and soy sauce for serving, Chopped mitsuba or celery leaves for garnish',
        # directions='Combine onion, celery, and 2 1/2 cups dashi in a small Dutch oven. Bring to a boil over medium-high. Reduce heat to medium-low, and simmer, uncovered, stirring occasionally, until vegetables are tender, 35 to 40 minutes. Add leftover mashed potatoes to dashi mixture, and whisk until well combined. Stir in milk, if desired, for a creamier texture. Stir in remaining 1 cup dashi, 1/4 cup at a time, to thin soup to desired consistency. Cook over medium-low, stirring occasionally, until warm, 4 to 6 minutes. Season with salt and pepper. Top servings with butter and drizzle with soy sauce. Garnish with mitsuba or celery leaves.',
    )
    r43 = Recipe(
        user_id=11,
        title='Tofu Avocado Salad',
        description="Quick recipes like this tofu avocado salad are quick and easy, and require no cooking at all! Not to mention the fact that it’s healthy (with protein and healthy fats) and can easily be made totally vegan. I love it as a side dish, or as a light meal with steamed rice.",
        image_url='https://thewoksoflife.com/wp-content/uploads/2020/06/tofu-avocado-cold-dish-9.jpg',
        total_time='10 minutes',
        servings='2 servings',
        # ingredients='7 ounces silken tofu (200g, or about half a package), 1 ripe avocado, 2 cloves garlic (grated), 1 teaspoon ginger (grated), 2 tablespoons light soy sauce, 1 teaspoon sesame oil, 1/2 teaspoon sugar, 1/2 teaspoon Chinese black vinegar (can substitute rice wine vinegar, lime juice, yuzu, etc.), 1/4 teaspoon white pepper, 2 teaspoons water, salt (to taste; you may not need any), 1 scallion (finely chopped)',
        # directions='Start by thinly slicing your silken tofu into small squares. Also cut your avocado in half. Thinly slice it crosswise so you get pieces similarly sized to the tofu slices. Arrange alternating slices of silken tofu and avocado on a serving platter. In a small bowl, combine the minced garlic and ginger, soy sauce, sesame oil, sugar, vinegar, white pepper, water, and salt to taste. Mix well to combine, and drizzle over the tofu and avocado. Garnish with chopped scallions and serve.',
    )
    r44 = Recipe(
        user_id=12,
        title='Double-Cut Lamb Chops with Garlic-Caper Rub',
        description="Punchy anchovies and garlic mellow during their short cook time, adding umami to double-cut lamb chops. Reverse-searing using the broiler results in perfectly cooked lamb with a crispy exterior; use a probe thermometer to monitor the internal temperature for best results. Serve the carved chops over cooked orzo to balance out the meal.",
        image_url='https://www.foodandwine.com/thmb/U-60bk7EsOYDaxdrpUrgfn9d9as=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/double-cut-lamb-chops-with-garlic-caper-rub-FT-RECIPE0421-eafe9b0d835a4d809546e4caf4b3c8d0.jpg',
        total_time='55 minutes',
        servings='4 servings',
        # ingredients='1/2 cup finely chopped mixed tender fresh herbs (such as flat-leaf parsley or chives or mint) plus more for garnish, 6 tablespoons extra-virgin olive oil (divided), ¼ cup drained and rinsed capers (divided), 1 tablespoon & 1 teaspoon grated lemon zest, 2 tablespoon fresh lemon juice plus lemon wedges for serving, ¼ teaspoon black pepper, ¼ teaspoon crushed red pepper (divided), Kosher salt for taste, 8 medium garlic cloves, 4 anchovy fillets (drained), 2 pounds double-cut lamb chops (about 8 double-cut chops from 2 racks)- frenched',
        # directions='Preheat oven to 400°F with 1 rack in middle position and 1 rack positioned 4 inches from broiler. Whisk together chopped herbs, 1/4 cup oil, 2 tablespoons capers, lemon zest and juice, black pepper, and 1/8 teaspoon crushed red pepper in a medium bowl until combined. Season with salt to taste; set aside. Process garlic, anchovies, remaining 2 tablespoons capers, and remaining 1/8 teaspoon crushed red pepper in a mini food processor until a coarse paste forms, about 10 seconds. Add remaining 2 tablespoons oil, and process until creamy and mostly smooth, about 40 seconds. (Alternatively, pound and mash garlic, anchovies, capers, and crushed red pepper using a mortar and pestle until a coarse paste forms, about 1 minute and 30 seconds. Add remaining 2 tablespoons oil, and continue to pound and mash until creamy and mostly smooth, about 2 minutes. Arrange lamb on a large baking sheet lined with parchment paper. Rub lamb evenly with garlic-caper paste. Roast in preheated oven on middle rack until a thermometer inserted in thickest portion of chops registers 110°F, 12 to 16 minutes. Remove lamb from oven; let rest until temperature stops rising and begins to fall, 5 to 10 minutes. Increase oven temperature to high broil; preheat 5 minutes. Return lamb to oven on top rack. Broil until lamb is golden and sizzling and a thermometer inserted in thickest portion of chops registers 120°F, 2 to 3 minutes. Remove from oven; transfer lamb to a cutting board, and let rest 5 minutes. Cut each lamb chop in half between ribs; serve with herb mixture and lemon wedges. Garnish with additional fresh herbs.'
    )
    r45 = Recipe(
        user_id=11,
        title='Char Siu-Style Oven Baked Ribs',
        description="These oven baked ribs are made with a Chinese BBQ Pork (Char Siu) marinade. It's better than any BBQ sauce you've ever tasted. The ribs cook in just 1 hour. Char siu is a type of Cantonese roast meat. A fusion of East and West, these char siu ribs echo what we love about two different food cultures. We’re combining our love for sweet, savory Chinese BBQ Pork (char siu) and saucy, finger-lickin’-good, can’t-have-too-many-napkins BBQ ribs. This recipe uses some Chinese ingredients, including five spice powder, sesame oil, Shaoxing rice wine, soy sauce, and hoisin sauce. Luckily, in the grand scheme of difficult-to-find Chinese ingredients, these aren’t that difficult to find! We have seen five spice, sesame oil, soy sauce, and hoisin sauce at many regular grocery stores, so you may not even have to venture into an Asian market. The one ingredient you may have difficulty locating is the Shaoxing rice wine. Grocery stores rarely carry it, but you can easily substitute a dry sherry cooking wine or mirin (a Japanese rice wine that is more commonly stocked in some Western grocery stores.)",
        image_url='https://thewoksoflife.com/wp-content/uploads/2019/05/char-siu-ribs-10.jpg',
        total_time='2 hours',
        servings='6 servings',
        # ingredients='3 pounds baby back ribs(1.4 kg), 1/4 cup sugar (50g), 2 teaspoons salt, 1/2 teaspoon five spice powder, 1/4 teaspoon white pepper, 1/2 teaspoon sesame oil, 1 tablespoon shaoxing wine, 1 tablespoon soy sauce, 1 tablespoon hoisin sauce, 2 teaspoons molasses, 1/8 teaspoon red food coloring (optional), 3 cloves garlic (finely minced)',
        # directions='Rinse the ribs and thoroughly pat them dry with paper towels. Mix the rest of the ingredients in a bowl to make the marinade. Reserve about ⅓ of the marinade, and rub the ribs with the rest of it. Allow the ribs to marinate for at least 2 hours. For best results, allow to marinate overnight.  Preheat your oven to 400 degrees, and put the ribs on a rack resting on a baking sheet. Pour 1 cup water into the pan, and transfer to the oven. Roast for 30 minutes. Remove the ribs from the oven and baste with the marinade. Return to the oven and roast for another 30 minutes. Allow the ribs to rest for 5 minutes. Slice and serve.',
    )
    r46 = Recipe(
        user_id=12,
        title='Baked French Toast with Cream and Eggs (Oeufs au Plat Bressanne)',
        description="The no-brainer brunch you’ve been searching for. This savory French breakfast of baked, cream-soaked toast and eggs is deceptively simple (and scalable) but lavish. The cream soaks into the garlic-rubbed bread and thickens to a rich sauce right in the skillet resulting in a savory French toast. Inspired by the great English food writer Elizabeth David’s 1955 collection of seasonal French fare, Summer Cooking. She advises using day-old bread.",
        image_url='https://www.saveur.com/uploads/2018/11/20/DQSKB3ZQJ5FLRK7VY7HIPBY4VA.jpg',
        total_time='30 minutes',
        servings='2 serving',
        # ingredients='2 tablespoon softened unsalted butter and bacon fat or duck fat (divided), Two ½-inch-thick slices of good-quality white bread, 1 garlic clove (peeled and halved), ½ cups heavy cream, Salt and freshly ground black pepper, 4 large eggs, 2 teaspoon finely chopped chives',
        # directions='Position a rack in the center of the oven and preheat to 375°F. Meanwhile, spread 1 tablespoon of the butter on both sides of each slice of bread. Heat a medium cast-iron skillet over medium-high heat until hot, then add the bread and cook, turning once, until evenly toasted and browned, 1–2 minutes per side. Transfer to a plate to cool slightly, then rub each slice all over with the cut side of the garlic clove. Discard any leftover garlic. To the empty skillet, add the cream and remaining butter and bring to a simmer over medium-low heat. Season to taste with salt and black pepper. Pour the liquid into a small bowl. To the empty skillet, add the bread slices 1 inch apart. Pour 2 tablespoons of the hot cream mixture over each slice. Gently crack 1 egg into a small bowl, making sure not to break the yolk. Tilt it onto one of the toast slices so that the yolk rests atop the bread. Repeat with the remaining eggs, topping each slice with 2 eggs. (It’s fine if the whites spill over the sides.) Pour the rest of the hot cream over the eggs and transfer the skillet to the oven. Bake until the whites are set and the yolks are cooked to your desired doneness, about 13 minutes for runny. Top with the chives and more black pepper, then serve immediately.',
    )
    r47 = Recipe(
        user_id=11,
        title='Steamed Egg',
        description="You would never think to steam eggs but this is one of those easy Chinese comfort foods that you can never go wrong with. It’s so easy to make and looks super delicate and elegant. Instead of using just water, I added some chicken stock for extra flavor and nutrients. You can also use vegetable stock if you want to keep it vegetarian.",
        image_url='https://thewoksoflife.com/wp-content/uploads/2015/01/steamed-egg-5.jpg',
        total_time='20 minutes',
        servings='4 servings',
        # ingredients='3 eggs, Water (same volume as eggs), Vegetable or chicken stock (same volume as eggs), Salt (to taste), 1 teaspoon sesame oil, Chopped scallion',
        # directions="Crack 3 eggs in a liquid measuring cup and note the volume. Pour the eggs into a large bowl, add salt, and beat for at least 1 minute. Now measure out water at the same volume as the eggs, and add it to the bowl. Do the same with the broth. Whisk in the sesame oil, and make sure everything's well combined. Place 4 empty ramekins in a steamer over high heat. Be sure the water will not bubble and touch the ramekins during steaming. Once the water boils, turn the heat down to a slow simmer. Then, divide the egg mixture into the ramekins, pouring it through a fine mesh strainer. Cover the steamer, turn up the heat to high, and steam for 3 minutes. After 3 minutes have elapsed, shut off the heat but keep the steamer covered. Let stand for 14 minutes with the lid firmly covered. Remove from the steamer, sprinkle with scallions, and serve.",
    )
    r48 = Recipe(
        user_id=12,
        title='Oven-Roasted Whole Fish with Tomatoes and Fennel',
        description="This dainty and sustainable species makes an easy sheet-pan supper. The best way to cook mild-­flavored, itty-bitty Atlantic butterfish is to liberally seasoned with dried herbs, then roasted in a hot oven over a bed of ­tomatoes, fennel, and garlic. This method works well with any small, white-fleshed fish.",
        image_url='https://www.saveur.com/uploads/2020/09/29/GKJAAHLRFFFIXAGQUSQHWIIJWU.jpg',
        total_time='40 minutes',
        servings='4 servings',
        # ingredients='1 teaspoon dried oregano, 1 teaspoon dried thyme, 1 tsp. kosher salt, ¼ teaspoon freshly ground black pepper, 1½ cups halved cherry tomatoes, 1 large fennel bulb (cored and cut into ½ inch slices), 6 large garlic cloves - thinly sliced (about ¼ cup), ½ cups plus 2 tablespoon robust extra-virgin olive oil (divided), 8 whole Atlantic butterfish (1½ pound - cleaned and fins removed), ¼ cups dry vermouth, 2 tablespoon coarsely chopped Italian parsley,  Crusty Italian bread for serving',
        # directions='Position a rack in the center of the oven and preheat to 500°F. Line a large rimmed baking sheet with parchment paper. In a small bowl, combine the oregano, thyme, salt, and black pepper. In a large bowl, toss the tomatoes, fennel, and garlic with ½ cup olive oil. Transfer the tomato mixture to the prepared baking sheet. Rinse the fish inside and out and pat dry with paper towels. Rub the remaining 2 tablespoons of olive oil over the exterior of the fish, then place a generous pinch of the herb seasoning into each cavity. Arrange the fish atop the tomato mixture, and sprinkle with the remaining seasoning. Cook until the vegetables are soft, 18–20 minutes. Pour the vermouth over the fish, then cook for 10 additional minutes. Garnish with parsley, and serve with crusty bread for ­sopping up the juices.'
    )
    r49 = Recipe(
        user_id=11,
        title='Cheesy Kale Sweet Potato Tart',
        description="A somewhat new way to use the antioxidant-rich veg, paired with sweet potatoes, cheese, and lovely pastry. This kale sweet potato tart is the perfect lunch with a green salad or even a great Thanksgiving side dish.",
        image_url='https://thewoksoflife.com/wp-content/uploads/2014/11/kale-sweet-potato-tart-15.jpg',
        total_time='2 hours 30 minutes',
        servings='8 serving',
        # ingredients='1 ¼ cups all-purpose flour, ¼ cup sugar, ¼ teaspoon salt, 1 stick butter (cold, cut into small cubes), 1 egg yolk, 1 tablespoon cold water, 2 tablespoons butter, ½ cup leeks (finely chopped), 1 bunch kale (stemmed and chopped), ½ teaspoon crushed red pepper flakes, olive oil, salt and pepper, 1 small sweet potato, 2 sprigs fresh thyme plus more for garnish, 1 cup ricotta (or softened cream cheese), 1/2 cup shredded cheese (gruyere, aged cheddar, or manchego work great for this)',
        # directions='Start by making the crust. In a large mixing bowl, combine the flour, sugar, and salt. Cut in the butter with a pastry cutter or two knives until the mixture resembles coarse crumbs. Whisk together the egg yolk and water, and add it to the flour mixture. Mix everything together with a fork until the dough comes together. Flatten into a disk, cover tightly with plastic wrap, and place in the refrigerator to chill for at least an hour. Take out of the refrigerator about a few minutes before you’re ready to roll it out. Roll out the dough and fit it to your tart pan. You may have to patch it up a bit, but don’t worry, it’ll turn out great. Pierce the dough all over with a fork and place the tart shell in the freezer for 30 minutes. Meanwhile, melt 2 tablespoons of butter in a large skillet over medium heat. Add the chopped leeks and cook for about 10 minutes. Add the kale, crushed red pepper flakes, and a couple drizzles of olive oil. Season with salt and pepper to taste. Cook for another couple minutes, just until the kale is wilted. Remove from the heat. Preheat the oven to 375 degrees F (210 degrees C). Blind bake the tart shell for 10 minutes, and remove from the oven. If you see it starting to puff up at all, poke the dough with a fork again! Prep your potato by peeling it and slicing it paper-thin. A mandolin helps, but a sharp knife will do the job. Add the thyme and ricotta (or cream cheese) to the kale mixture. Place a layer of sweet potato slices in the bottom of the tart shell. Spread the kale and cheese mixture evenly over that, and top with another layer of sweet potato slices. Brush the top thoroughly with olive oil and sprinkle the cheese over the tart. Bake for about 20 minutes, until golden brown.',
    )
    r50 = Recipe(
        user_id=12,
        title='Chutney Cheese Brioche Rolls',
        description="There's absolutely no way to go wrong with this soft, buttery brioche bread filled with cilantro-mint chutney and cheese! Chutney Cheese Brioche Rolls are about to be the new family favorite! The rolls are fluffy, buttery, and incredibly soft. They're filled with a green chutney made with a base of cilantro and mint that's tangy, spicy, and super herby. The brioche dough has cheese mixed into it, and is topped with even more cheese! These rolls are absolutely delicious and super savory! They can be customized with whatever cheese and seasonings you have on hand.",
        image_url='https://masalaandchai.com/wp-content/uploads/2020/11/Chutney-Cheese-Brioche-Rolls-in-Lodge.jpg',
        total_time='3 Hours',
        servings='makes 8 rolls',
        # ingredients='3 cups all-purpose flour, 2¼ teaspoon instant yeast, 1 tablespoon sugar, 1 cup grated parmesan cheese, ½ teaspoon salt, ⅓ cup warm whole milk, 1 teaspoon honey, 4 eggs, 1 yolk, 4 oz unsalted butter, 1 jar chutney (remove the water), 4 oz grated sharp cheddar cheese',
        # directions="In a bowl, whisk together the flour, instant yeast, sugar, parmesan, and salt. Add the warm milk, honey, 3 eggs, and yolk. Using a dough hook on a stand mixer, mix together at a low to medium speed until a shaggy dough forms. Mix the dough together for another minute or so until the dough is combined. Split the butter into four portions. Add the first portion into the dough, and knead for about two minutes until fully incorporated. Scrape down the sides of the bowl, and add in the second portion. Continue this for the next few portions. The batter will resemble cake batter at this point. Increase the mixer speed to medium and knead for an additional 8-10 minutes, or until the dough is completely smooth and velvety. It'll come off the sides of the bowl cleanly when done. Turn the dough out on to a lightly floured surface. Fold each side into the center and repeat 3 times. Flip the dough over and you'll have a smooth surface. Transfer the dough to a bowl for the first proofing. Cover the bowl and allow it to proof for about an hour, or until it doubles in size. While the dough rests, toss together all the ingredients for Mom's Green Chutney into the blender, removing the water from the recipe, until a thick chutney forms. Layer parchment paper in a 10-inch cast iron or spring form pan and butter it. Once the dough has risen, punch it down and turn out the dough onto a lightly floured surface. Roll the dough out into a 12 x 18 inches rectangle. Spread the chutney all over the dough, being sure to go all the way up to the edges. Top with shredded cheese. Roll the edge of the dough into itself and continue rolling to form a log. Pinch the seals together. Cut the log into 8 rolls. Carefully transfer the rolls into the cast iron. Cover and let rise for another 1-2 hours. Check if the dough is done proofing by poking it. If it leaves an indentation, it's done. Preheat the oven to 450°F. Brush the top of the rolls with a beaten egg. Bake for 25 minutes until the top begins to brown. Then, reduce the oven temperature to 350°F and bake for another 30-35 minutes until the internal temperature reaches 180°F. Sprinkle additional cheese on warm rolls and serve with additional chutney.",
    )
    r51 = Recipe(
        user_id=11,
        title='Miso Banana Bread',
        description="The miso in this supremely delicious banana bread adds deeper, robust flavor. The bread is fantastic the day it's made, but it tastes even better the following day.",
        image_url='https://www.foodandwine.com/thmb/N5Tk3WMnrkSaPpf3nD5mhAnROQA=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/miso-banana-bread-XL-RECIPE0716-92f1fe2e041a4c459d193687c13c8bc6.jpg',
        total_time='2 hours',
        servings='1 10-by-5-inch loaf',
        # ingredients,
        # directions,
    )
    r52 = Recipe(
        user_id=12,
        title='Kiwi, Dill, and Yogurt Pavlova',
        description="Swap the kiwi out for any seasonal fresh fruit in this casual yet elegant dessert.If you prefer a family-style presentation, arrange the meringues on a serving platter or bowl and layer with the fruit and yogurt cream. Stored in an airtight container, leftover meringues will keep for up to 2 weeks.",
        image_url='https://www.saveur.com/uploads/2021/04/18/IMG_2545-scaled.jpeg?',
        total_time='55 minutes',
        servings='8 servings',
        # ingredients='3 large egg whites, 1 cup plus 1 tablespoon superfine sugar (divided),  1/2 cup plus 2 tablespoon confectioners sugar,  1 1⁄2 teaspoon potato starch, 1 1⁄2 cups heavy cream, 3 1⁄4 cups plain full-fat yogurt, 8 medium kiwis (2 lb. 4 oz.) -peeled and coarsely chopped, Fresh dill for garnish, Extra-virgin olive oil for drizzling',
        # directions="Preheat the oven to 250°F. Line 2 large rimmed baking sheets with parchment paper and set aside. In the bowl of a stand-mixer fitted with a whip attachment, beat the egg whites on high speed just to medium-stiff peaks, about 2 minutes. With the mixer still running, gradually add ⅓ cup plus 1 tablespoon superfine sugar, and continue beating on high speed until the meringue is smooth and glossy, about 1 minute more. Turn the mixer off and remove the whip attachment. Sift the confectioners’ sugar and potato starch over the meringue and use a silicone spatula to gently fold together. Fill a piping bag or a large, zip-top freezer bag with the meringue, cut off the tip, then pipe 2-inch circles onto the lined baking sheet, leaving at least 2 inches between each circle.Transfer to the oven and bake until puffed and slightly golden, about 35 minutes. Set aside to cool to room temperature. Meanwhile, in a medium bowl, whisk together the cream and the remaining ⅔ cup superfine sugar to soft peaks. Add the yogurt and whisk just to combine. Immediately before serving, break or slice 8 meringues in half, reserving the rest in an airtight container for another use. Divide the pieces among 8 dessert plates; add a generous dollop of yogurt cream in the center of each plate, top with some of the kiwi and a few sprigs of fresh dill, drizzle with olive oil, and serve."
    )
    r53 = Recipe(
        user_id=2,
        title='Honey-Tomato Bruschetta with Ricotta',
        description="In this amazing appetizer, two types of honey serve two distinct purposes: Mellow, slightly spicy clover honey intensifies the sweetness of the tangy tomatoes as they slowly roast. After the bruschetta is assembled, a drizzle of robust buckwheat honey balances the creamy ricotta cheese.",
        image_url='https://www.foodandwine.com/thmb/zLBEo664xfy8jA8M99qJfYXtvVo=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/200808xl-honey-tomato-bruschetta-with-ricotta_0-5258b97b0eaf40c188c9e57d7148dc7c.jpg',
        total_time='1 hour 45 minutes',
        servings='6',
        # ingredients,
        # directions,
    )
    r54 = Recipe(
        user_id=3,
        title='Asparagus & Brie Parcel Pies',
        description="This recipe came about one spring night when I wanted an excuse to eat pie for dinner, and this easy method has been the source of inspiration for many dinner pies (and breakfast pies and lunch pies) ever since. The best part of these pastries is that they reheat particularly well, making them perfect to make ahead and take for lunch or on a picnic.",
        image_url='https://images.food52.com/tsczM4kaWT-ayOEd_fWOd1yd_Ck=/1008x672/filters:format(webp)/36239977-8c00-4a38-a71b-e583709d2060--2021-1215_brie-asparagus-parcel-pies_3x2_julia-gartland_056.jpg',
        total_time='1 hour',
        servings='8 individual pastries',
        # ingredients,
        # directions,
    )
    r55 = Recipe(
        user_id=4,
        title='Sheet-Pan Breaded Alaska Cod With Sweet Potato Wedges',
        description="On busy nights when cooking a multi-dish meal feels like a stretch, nothing beats an easy sheet-pan dinner. The following recipe is a loose twist on a classic comfort food: fish and chips. Here, Alaska cod fillets are lightly breaded (not battered!) and baked in the oven with sweet potato wedges until everything is deliciously crisp. The method is straightforward and can be broken up into simple steps for a low effort, time-saving meal that won’t leave you with a big pot of oil. My favorite part of this dish is the variety of textures and flavors on display: flavorful Alaska cod with earthy roasted sweet potatoes, and a creamy spiced dip for dunking. Whether you put together individual plates or invite diners to take their meal directly from the tray, this dinner hack is a fun, unfussy weeknight meal that’s as satisfying to eat as it is easy to make. ",
        image_url='https://images.food52.com/qM28O2FY8LHxp6CPlh6y-yZcs2g=/1008x672/filters:format(webp)/795bd269-b72d-4bce-8fc8-bc56ebf83a54--2022-0107_sponsored_alaska-seafood_recipe_herb-breaded-cod_not-branded_3x2_rocky-luten_017.jpg',
        total_time='45 minutes',
        servings='4',
        # ingredients,
        # directions,
    )
    r56 = Recipe(
        user_id=5,
        title='Bacon, Lettuce & Strawberry Sandwich',
        description="A classic BLT, but instead of summery tomatoes, springtime strawberries. Call it an easy excuse to start BLT—er, BLS—season a few months early. If you’re raising your eyebrows at strawberries in a savory application, think of it this way: Tomatoes are a fruit; strawberries are a fruit. Tomatoes are red, juicy, sweet; strawberries are red and juicy and sweet. Tomatoes are delicious; strawberries are delicious. Beyond the strawberries, the rest of the ingredients are up to you. My dream sandwich has crisp-but-chewy bacon, grainy-seedy bread, and an ungodly amount of mayonnaise. But maybe instead you want cracker-crisp bacon, sourdough bread, and a mere wisp of mayonnaise. It’s all good. I like iceberg lettuce here for its watery crunch and neutral flavor. If you only have romaine, butterhead, or even baby arugula around, though, why not give that a go? Don’t skip this step: Salting the strawberries before starting the rest of the sandwich draws out their juices, concentrates their flavor, and mingles with the mayo to form a pseudo-dressing. If you can only find smaller strawberries (often these are the sweetest), increase the quantity as needed. You want an uninterrupted layer of berries on the bread.",
        image_url='https://images.food52.com/dL632hmxtA9YTvQhyyT5oCWo6rc=/1008x672/filters:format(webp)/b8d92c74-c961-4790-b0c4-d6724e8d03a4--2020-0327_bacon-lettuce-strawberry-sandwich_3x2_ty-mecham.jpg',
        total_time='10  minutes',
        servings='1 sandwich',
        # ingredients,
        # directions,
    )  
    r57 = Recipe(
        user_id=6,
        title='Raspberry Fruit Roll-Ups (Fruit Leather)',
        description="Now you can make your own roll-ups at home and, dare I say it, they are actually kind of good for you (or at least a whole lot better then their grocery store counterpart). Homemade roll-ups are packed with fruit—and there's no artificial color in sight. All you need is fresh fruit (in-season produce makes the best tasting roll ups), a squirt of honey, some lemon juice, and a bit of patience. You can swap in just about any fruit you like, so go with what’s in season near you. Tip: You can use all different types of fruit. Try peach roll-ups with 6 peaches (about 1 pound) or blueberry roll-ups using 4 cups fresh blueberries",
        image_url='https://images.food52.com/MGl57TOXsEDYx5VKlPUOTxYd0hs=/1008x672/filters:format(webp)/11e88abf-1508-4a48-bacf-4b9962968995--Fruit_Roll-Ups_1.jpg',
        total_time='4 hours',
        servings='10 - 12 Roll ups',
        # ingredients,
        # directions,
    )
    r58= Recipe(
        user_id=7,
        title='Barbecued Oysters with Smoky Uni Butter',
        description="Briny uni and acidic lemon, mixed with smoky paprika and rich butter, combine to make an extraordinary flavored butter to top oysters before roasting. If shucking oysters isn't your thing, you can ask your fishmonger to do the job for you.",
        image_url='https://www.foodandwine.com/thmb/C-EWh9_TysmITrF-KHr0ID4c9lE=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/bbq-oysters-with-uni-butter-FT-RECIPE0521-b85132723c58463f839ffbd32686613b.jpg',
        total_time='20 minutes',
        servings='1 dozen oysters',
        # ingredients,
        # directions,
    )
    r59= Recipe(
        user_id=8,
        title='Scalloped Potatoes With Caramelized Onions',
        description="These scal­loped pota­toes were a hit on Easter Sun­day with friends and fam­ily, so why not Thanksgiving? These are not your aver­age scal­loped pota­toes, as there are deli­cious caramelized onions lay­ered in between the sliced pota­toes and cheese. A lighter ver­sion can be made with milk and a béchamel sauce instead of the whip­ping cream; see the direc­tions at the end of the recipe. You can also double the recipe if you have lots of guests, making the potatoes in 2 (12x8-inch) casseroles.",
        image_url='https://images.food52.com/G9Y1rwI0c6fRPG8M2hvJxyIMtTY=/1008x672/filters:format(webp)/b18f8c99-dfce-4fc0-8c79-3fafc8a28b9a--2020-1013_scalloped-potatoes-caramelized-onions_3x2_julia-gartland_269.jpg',
        total_time='3 hours',
        servings='6 - 8',
        # ingredients,
        # directions,
    )
    r60= Recipe(
        user_id=9,
        title='Bananas Foster',
        description="These bananas cooked with a citrusy brown sugar and rum sauce and topped with crispy pecans are so good, we eat this dessert straight from the pan. If you are looking for a decadent and rich dessert for two that comes together in just minutes, this is it. The rum, cinnamon, orange, and brown sugar will make your kitchen smell heavenly as you cook the sauce. The bananas are tender, but aren’t so soft that they fall apart in the pan, and the sweet spiced glaze on the pecans makes them extra crunchy after they are toasted. You will have leftover pecans, but they make a nice bar snack or topping on a salad, and will keep in an airtight container for up to a week. Once you start cooking the sauce, things go very quickly, so have all your ingredients prepped and ready to go into the skillet before you start — you’ll even want your ice cream out and ready to go in the pan. ",
        image_url='https://www.foodandwine.com/thmb/f9nMpgroknoESROjEWWnHrrcre8=/750x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Bananas-Foster-FT-RECIPE0223-2df5e8bc420b42bab6bd5f050d68d51f.jpg',
        total_time='55 minutes',
        servings='2 servings',
        # ingredients,
        # directions,
    )
    # r60= Recipe(
    #     user_id=,
    #     title='',
    #     description="",
    #     image_url=,
    #     total_time='',
    #     servings='',
    #     # ingredients,
    #     # directions,
    # )

    db.session.add(r1)
    db.session.add(r2)
    db.session.add(r3)
    db.session.add(r4)
    db.session.add(r5)
    db.session.add(r6)
    db.session.add(r7)
    db.session.add(r8)
    db.session.add(r9)
    db.session.add(r10)
    db.session.add(r11)
    db.session.add(r12)
    db.session.add(r13)
    db.session.add(r14)
    db.session.add(r15)
    db.session.add(r16)
    db.session.add(r17)
    db.session.add(r18)
    db.session.add(r19)
    db.session.add(r20)
    db.session.add(r21)
    db.session.add(r22)
    db.session.add(r23)
    db.session.add(r24)
    db.session.add(r25)
    db.session.add(r26)
    db.session.add(r27)
    db.session.add(r28)
    db.session.add(r29)
    db.session.add(r30)
    db.session.add(r31)
    db.session.add(r32)
    db.session.add(r33)
    db.session.add(r34)
    db.session.add(r35)
    db.session.add(r36)
    db.session.add(r37)
    db.session.add(r38)
    db.session.add(r39)
    db.session.add(r40)
    db.session.add(r41)
    db.session.add(r42)
    db.session.add(r43)
    db.session.add(r44)
    db.session.add(r45)
    db.session.add(r46)
    db.session.add(r47)
    db.session.add(r48)
    db.session.add(r49)
    db.session.add(r50)
    db.session.add(r51)
    db.session.add(r52)
    db.session.add(r53)
    db.session.add(r54)
    db.session.add(r55)
    db.session.add(r56)
    db.session.add(r57)
    db.session.add(r58)
    db.session.add(r59)
    db.session.add(r60)

    db.session.commit()    

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_recipes():
    db.session.execute('TRUNCATE recipes RESTART IDENTITY CASCADE;')
    db.session.commit()
