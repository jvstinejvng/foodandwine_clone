from app.models.recipe import db, Recipe

def seed_recipes():
    r1 = Recipe(
        user_id=1,
        title='Caesar Salad with Crispy Tofu Croutons',
        description='In this creative remix of a classic Caesar, we pan-fry tofu cubes until they become crisp and crouton-like. Plus, the blend of soft tofu with olive oil, lemon juice, and anchovy makes a terrific caesar-style dressing without the standard raw egg yolks.',
        img_url='https://www.foodandwine.com/thmb/TNp-RFiTfO1ir8z9HBp0xS8uaOo=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201005-r-xl-caesar-salad-with-crispy-tofu-croutons-27f3f820efcf41d584bf968afa587461.jpg',
        total_time='30 minutes',
        servings='4 servings',
        ingredients='6 ounces soft silken drained tofu, 1 1/2 tablespoons extra-virgin olive oil, 1 1/2 tablespoons fresh lemon juice, 1 1/2 tablespoons freshly grated Parmigiano-Reggiano cheese plus more for serving, 1 oil-packed anchovy drained fillet, 1 small garlic clove, 1/2 teaspoon Worcestershire sauce, 1/2 teaspoon Dijon mustard, Salt and freshly ground pepper, One 14-ounce package firm drained tofu cut into 3/4-inch cubes, Vegetable oil for frying, 1/2 cup cornstarch, 2 romaine hearts torn into bite-size pieces',
        directions='In a blender, puree the silken tofu with the olive oil, lemon juice, the 1 1/2 tablespoons of Parmigiano, the anchovy, garlic, Worcestershire and mustard; season the dressing with salt and pepper. Wrap the firm tofu in paper towels and press out some of the water. In a large skillet, heat 1/4 inch of vegetable oil until shimmering. In a bowl, toss the tofu with the cornstarch until coated. Add the cubes to the oil and fry over moderately high heat, turning once, until crisp, about 8 minutes. Using a slotted spoon, transfer the croutons to a paper towel lined plate; season with salt. In a large bowl, toss the romaine with the dressing and two-thirds of the croutons. Transfer the salad to plates and top with the remaining croutons. Sprinkle with Parmigiano and serve.',
    )
    r2 = Recipe(
        user_id=1,
        title='Smoked-Salmon Deviled Eggs',
        description='"Deviled eggs are fun because you can dress them up or down," says Michael Mina, who dresses them up with chopped smoked salmon here.',
        img_url='https://www.foodandwine.com/thmb/J0CnSi6g8zVxIWp1u9XZE-0Mq7o=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201204-xl-smoked-salmon-deviled-eggs-2000-c17a8c7c5c7648029b2091b301836773.jpg',
        total_time='30 minutes',
        servings='makes 8 deviled eggs (16 halves)',
        ingredients='8 large eggs, 1/2 cup finely chopped smoked salmon (2 ounces), 1/3 cup mayonnaise, 2 cornichons cut into 1/4-inch dice, 2 teaspoons pickling liquid from the cornichons jar, 2 teaspoons Dijon mustard, Salt, Old Bay seasoning',
        directions='Cover the eggs with water in a large saucepan and bring to a vigorous boil. Cover the saucepan, remove the heat and let stand for 10 minutes. Drain off the water and shake the pan gently to crack the eggs. Cool the eggs slightly under cold running water, then peel them under running water. Pat dry. Cut the eggs in half lengthwise and carefully remove the yolks. Transfer the yolks to a bowl and mash well with a fork. Stir in the salmon, mayonnaise, cornichons, cornichon liquid, and Dijon mustard. Season with salt. Mound the filling in the egg-white halves and sprinkle with Old Bay. Serve lightly chilled.',
    )
    r3 = Recipe(
        user_id=1,
        title='Chicken and Wild Rice Soup',
        description='Let\'s use leftover chicken or turkey, and wild rice to make this lovely chicken and rice soup. Thyme and garlic add aromatic depth to the soup and the classic base of onions, carrots, and celery. After simmering the soup, finish it with a drizzle of cream to add a touch of richness. ',
        img_url='https://www.foodandwine.com/thmb/8Igqyn3l2LeLDcXRN8Ll1FIglrA=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/HD-201411-r-chicken-and-wild-rice-soup-2f493a1de2a6462286391ea214601acf.jpg',
        total_time='1 hour 15 minutes',
        servings='8 servings',
        ingredients='4 tablespoons unsalted butter, 3 celery ribs cut into 1/2-inch pieces, 2 carrots cut into 1/2-inch pieces, 1 medium chopped onion, 2 garlic cloves minced, 1 1/2 teaspoons finely chopped thyme, Salt, Pepper, 1/4 cup all-purpose flour, 1 cup wild rice (5 ounces), 2 quarts chicken stock or low-sodium broth, 2 cups water, 4 cups bite-size pieces of roasted chicken or turkey,1 cup heavy cream',
        directions='In a large saucepan, melt the butter. Add the celery, carrots, onion, garlic, thyme, and a generous pinch each of salt and pepper and cook over moderate heat, stirring occasionally, until the vegetables just start to soften, about 10 minutes. Sprinkle the flour over the vegetables and cook, stirring, until evenly coated and lightly browned, about 3 minutes.Add the wild rice to the saucepan and gradually stir in the stock and water. Bring to a boil, then simmer over moderately low heat, stirring occasionally, until the vegetables are tender, about 30 minutes. Add the chicken and simmer, stirring occasionally, until the wild rice is tender, 10 to 15 minutes longer. Stir in the cream and season with salt and pepper. Ladle the soup into bowls and serve.',
    )
    r4 = Recipe(
        user_id=1,
        title='rilled Apricots with Burrata, Country Ham and Arugula',
        description='Depending on the season, you can also make this salad with plums, peaches, and pears.',
        img_url='https://www.foodandwine.com/thmb/GlixT3MbhbFtQ2uLg-g9ImLDxBw=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201109-xl-grilled-apricots-with-burrata-country-ham-and-arugula-ce006a480c0e417cac2190c981b72ab3.jpg',
        total_time='30 minutes',
        servings='8 servings',
        ingredients='1 1/4 pounds apricots, halved and pitted, 1/4 cup extra-virgin olive oil plus more for brushing, Sea salt, freshly ground pepper, 1 1/2 tablespoons fresh lemon juice, 1 small head  cored and thinly sliced radicchio,5 ounces baby arugula, 1/2 pound of shredded burrata cheese, 4 ounces shaved country ham, 1 tablespoon aged balsamic vinegar',
        directions='Light a grill or preheat a grill pan. Brush the apricots with oil and season with salt and pepper. Grill over high heat, cut sides down, just until lightly charred, 5 minutes. Let cool. In a bowl, whisk the lemon juice with 1/4 cup of oil and season with salt and pepper. Gently toss in the apricots, radicchio, and arugula. Transfer to a platter and top with the burrata, ham and vinegar. Serve.',
    )
    r5 = Recipe(
        user_id=1,
        title='Honey Mustard Chicken Wings',
        description='Sweet honey and tangy mustard make these classic chicken wings extraordinary.',
        img_url='https://www.foodandwine.com/thmb/_8iiizCxNY_AnWFrM_MXOqXPNOg=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201403-xl-honey-mustard-chicken-wings-6e55beb535df4d2995108b67b7091f6d.jpg',
        total_time='45 minutes',
        servings='4 servings',
        ingredients='1/2 cup butter, 4 cloves garlic (minced), 1/2 cup mustard, 1/3 cup honey, 1 tablespoon Worcestershire sauce, 1 teaspoon apple cider vinegar, 1/2 teaspoon kosher or sea salt (plus more for seasoning), 1/2 teaspoon black pepper (plus more for seasoning), 2 pounds chicken wings (split), 1 cup all-purpose flour (for dredging), Vegetable oil (or other high flashpoint oil used for frying)',
        directions='Heat a saucepan over medium heat. Melt the butter, and then stir in the garlic. Cook for 1 to 2 minutes, or until the garlic is lightly browned. Whisk in the mustard and honey. Stir in the Worcestershire sauce, apple cider vinegar, and season with salt and pepper. Reduce heat to low and simmer the sauce for about 3 to 5 minutes or until thickened. Set aside. Rinse the chicken wings and pat them dry. Generously season the chicken with salt and black pepper. Dredge the wings in flour, shaking off any excess flour, and set aside. In a large saucepan or deep fryer, heat the oil to about 375°. Fry the chicken wings in small batches until golden brown, 8 to 10 minutes. Shake off any excess oil and place on paper towels to drain. Continue frying the chicken in batches until all of the wings are cooked. Toss the wings with the honey mustard sauce and serve warm with leftover sauce for dipping.',
    )
    r6 = Recipe(
        user_id=2,
        title='Apple Cider Glazed Ham',
        description='Pulling off an impressive holiday ham at home takes just a few simple steps. Start with a good-quality, bone-in spiral-cut ham — make sure it is unglazed. Coat it with this deliciously sweet apple cider glaze featuring light brown sugar, honey, and Dijon mustard. Brushing the glaze onto the ham in 15-minute intervals during the last 30 minutes of baking creates a wonderfully sticky and caramelized crust. Serve any leftovers on biscuits with a slather of mustard.',
        img_url='https://www.foodandwine.com/thmb/cNAPJA1VVVfmkxBvC5iOKuKzii4=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/diy-honeybaked-ham-FT-RECIPE2019-e2a596b5bec34d419924c6153eae2b4c.jpg',
        total_time='2 hours 35 minutes',
        servings='10 servings',
        ingredients='1 1/2 cups packed light brown sugar, 1/2 cup honey, 1/4 cup Dijon mustard, 1/2 teaspoon kosher salt, 1/2 teaspoon black pepper, 1 cup apple cider, divided, 1 (8 to 9lb.) fully cooked bone-in spiral-cut ham half',
        directions='Preheat oven to 350°F. Line a roasting pan with heavy-duty aluminum foil. Stir together brown sugar, honey, mustard, salt, pepper, and 1/2 cup of the cider in a medium bowl. Place ham in prepared pan so that individual ham slices are perpendicular to pan bottom. Brush ham with 3/4 cup glaze, gently pushing glaze in between slices. Turn ham over so that bottoms of slices are now facing up; brush an additional 3/4 cup glaze in between slices. Turn ham so that the large, flat, cut side is facing down in pan.Pour remaining 1/2 cup cider into bottom of pan. Cover tightly with foil. Bake in preheated oven 1 1/2 hours. Remove from oven; remove and discard foil. Brush ham evenly with 1/3 cup glaze; return to oven, and bake 15 minutes. Remove from oven. Brush with 1/3 cup glaze; return to oven, and bake until a thermometer inserted in thickest portion of ham registers 140°F, about 15 minutes. Remove from oven; brush with remaining 1/3 cup glaze and pan drippings. Let stand 15 minutes. Serve warm or at room temperature.',
    )
    r7 = Recipe(
        user_id=2,
        title='Lemon-and-Garlic-Marinated Flat Iron Steak',
        description='The flat iron steak, which sits on the shoulder blade next to the teres major, is great for marinating and grilling.',
        img_url='https://www.foodandwine.com/thmb/mZCOibKXSTOFAGW06jyjqVht8Pc=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201205-xl-lemon-and-garlic-marinated-flat-iron-steak-a66515005cf54031815b943eaef4b3c6.jpg',
        total_time='30 minutes',
        servings='2 servings',
        ingredients='One 1-pound beef flat iron steak, Salt, Freshly ground pepper, 2 tablespoons extra-virgin olive oil, 6 garlic cloves, minced, 4 scallions, chopped, 4 bay leaves, broken into pieces, 2 lemons, very thinly sliced, Vegetable oil for brushing',
        directions='Season the steak with salt and pepper in a glass baking dish and rub with the olive oil. Spread the garlic, scallions and bay leaves all over the steak. Cover both sides of the steak with lemon slices. Cover and refrigerate for 24 hours. Light a grill and brush with vegetable oil. Scrape off the seasonings and bring the steak to room temperature. Season with salt and pepper and grill over moderately high heat until medium-rare within, 3 1/2 minutes per side. Transfer to a carving board and let rest for 5 minutes. Thinly slice across the grain and serve.',
    )
    r8 = Recipe(
        user_id=2,
        title='Salmon and Cherry Tomato Skewers with Rosemary Vinaigrette',
        description='Cook these simple salmon-and-tomato kebabs on skewers or even on sturdy rosemary sprigs.',
        img_url='https://www.foodandwine.com/thmb/Dh8xN0JoJEwadeaQoLo9aKcEV-A=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/recipe1015-xl-salmon-tomato-skewers-10bc4ce3221746e39d14f2b8bd2188af.jpg',
        total_time='40 minutes',
        servings='4 skewers',
        ingredients='1/4 cup extra-virgin olive oil plus more for brushing, 3 tablespoon fresh lemon juice, 2 teaspoons Dijon mustard, 2 teaspoons finely chopped rosemary, Kosher salt, Pepper, 16 cherry tomatoes , 1 1/2 pounds salmon fillet cut into 1 1/2-inch cubes, 4 long metal skewers or 4 wooden skewers soaked in water for 1 hour',
        directions='In a small bowl, whisk the 1/4 cup of olive oil with the lemon juice, mustard and rosemary. Season the vinaigrette with salt and pepper. Light a grill or heat a grill pan. Thread the salmon and cherry tomatoes onto the skewers, brush with olive oil and season all over with salt and pepper. Grill over moderately high heat, turning once, until the salmon is just cooked through, about 6 minutes. Transfer the skewers to a platter and drizzle with some of the vinaigrette. Serve right away, passing additional vinaigrette at the table.',
    )
    r9 = Recipe(
        user_id=3,
        title='Lemony Crêpe Casserole',
        description='Reminiscent of a classic bread pudding, this sweet-tart crêpe casserole has a beautiful lacy top and tender-but-sliceable center.',
        img_url='https://www.foodandwine.com/thmb/VzRB80cpbqpKakUBwl2wls2Fe0Q=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/lemony-crepe-casserole-ft-RECIPE0119-07a35dd254394be6bb6ecb676da1b0bd.jpg',
        total_time='55 minutes',
        servings='8 servings',
        ingredients='2 (8-ounce) packages cream cheese, at room temperature, 3/4 cup store-bought lemon curd, 1/4 teaspoon kosher salt(divided), 1/4 cup unsalted butter, plus more for greasing, 24 (10-inch) store-bought crêpes, 1 medium Meyer lemon, very thinly sliced and seeded, 1/4 cup pure maple syrup, 1 tablespoon powdered sugar',
        directions='Preheat oven to 350°F. Beat cream cheese, lemon curd, and 1/8 teaspoon salt with an electric mixer on medium speed until smooth, about 3 minutes. Grease a 13- x 9-inch baking dish with butter. Arrange 1 crêpe on a work surface. Using a small offset spatula, spread 1 1/2 tablespoons cream cheese mixture evenly over crêpe, leaving a 1-inch border. Fold crêpe in half, and then fold in half again. Place folded crêpe in prepared baking dish. Repeat with remaining crêpes and remaining cream cheese mixture, overlapping folded crêpes in baking dish. Bake in preheated oven until crêpes are heated through and edges are golden brown, 15 to 20 minutes. Meanwhile, melt butter in a large nonstick skillet over medium-low. Add lemon slices, sprinkle with remaining 1/8 teaspoon salt, and cook, stirring occasionally, until lemon peel is softened, about 7 minutes. Stir in maple syrup, and remove from heat. Spoon lemon sauce over casserole. Dust with powdered sugar, and serve.',
    )
    r10 = Recipe(
        user_id=4,
        title='Stuffed Jalapeños',
        description='Perfect served with cold beers, these stuffed jalapeños are the perfect game-day or movie-night snack. Halved jalapeños are packed with a cheddar and cream cheese filling flavored with garlic, cilantro and scallions.',
        img_url='https://www.foodandwine.com/thmb/lLKDW8OCi0a4jM6B651njJOA81k=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/stuffed-jalapenos-xl-recipe2016-8aa1de0a28af4e4d85d954d02ce207d5.jpg',
        total_time='1 hour',
        servings='24 pieces',
        ingredients='1 small garlic clove, Kosher salt, 12 ounces cream cheese(softened), 2 minced scallions, 1 large egg yolk, 1/2 teaspoon ground cumin, 1/2 teaspoon Dijon mustard, 1/3 cup minced cilantro plus more for garnish, Pepper, 6 ounces sharp cheddar cheese, coarsely grated (1 3/4 cups), 12 large jalapeños halved lengthwise with seeded stems left intact, 1 tablespoon extra-virgin olive oil, Lime wedges for serving',
        directions='Preheat the oven to 375°. Using the flat side of a chef\'s knife, crush the garlic and 1/2 teaspoon of salt to a paste. Scrape the garlic paste into a medium bowl and add the cream cheese, scallions, egg yolk, cumin, mustard and 1/3 cup of cilantro. Stir with a rubber spatula until well combined. Season with a generous pinch each of salt and pepper, then fold the cheddar into the filling. On a rimmed baking sheet, toss the jalapeños with the olive oil and a pinch each of salt and pepper until well coated. Arrange them cut side up and spoon 1 1/2 to 2 tablespoons of filling into each one. Bake for about 20 minutes, rotating the sheet from front to back halfway through, until the filling is puffed and bubbling and the jalapeños are tender. Garnish with minced cilantro and serve with lime wedges.',
    )
    r11 = Recipe(
        user_id=4,
        title='Garlic-Crusted Roast Rack of Lamb',
        description='Rack of lamb is a brilliant roast centerpiece dish because it\'s impressive and surprisingly easy to make. This lamb recipe includes just five ingredients and 10 minutes of active cooking time. It\'s one of our favorite ways to prepare a rack of lamb because it\'s simply rubbed with plenty of garlic, rosemary, olive oil, and salt before roasting. Since the seasoning is so simple, the dish pairs well with a range of sides, from risotto to green salads to roasted vegetables.',
        img_url='https://www.foodandwine.com/thmb/4ryFSLczBRBc5580uLBrF8g5VlU=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/HD-201104-r-garlic-rack-of-lamb-04f38936aeb147e0ac3798d530a3722c.jpg',
        total_time='1 hour 45 minutes',
        servings='8 servings',
        ingredients='1 head of garlic (cloves peeled), 1/4 cup rosemary leaves, 1/4cup extra-virgin olive oil, 2 racks of lamb, frenched (2 pounds each), Kosher salt and freshly ground black pepper',
        directions='In a mini food processor, combine the garlic, rosemary and olive oil and process until the garlic is finely chopped. Season the lamb racks with salt and pepper and rub the garlic-rosemary oil all over them. Set the racks fat side up on a large rimmed baking sheet and let stand for 1 hour. Preheat the oven to 450°. Roast the lamb in the upper third of the oven for 15 minutes. Turn the racks and roast for 10 minutes longer for medium-rare meat. Transfer the racks to a carving board, stand them upright and let rest for 10 minutes. Carve the racks in between the rib bones and transfer to plates. Serve right away.',
    )
    r12 = Recipe(
        user_id=5,
        title='Grilled Ham and Cheese with Strawberry-Red-Wine Jam',
        description='The secret to this delectable sandwich is the jam spiked with Pinot Noir.',
        img_url='https://www.foodandwine.com/thmb/r6X9Fr6kys1zLgPWrNsq_DudBTo=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201004-xl-grilled-ham-and-cheese-2000-f18d283af5e848efb4ac53b970d60f02.jpg',
        total_time='30 minutes',
        servings='10 sandwiches',
        ingredients='Twenty 1/4-inch-thick slices of brioche, 1/2 cup strawberry jam mixed with 2 tablespoons of Pinot Noir, 10 thin slices of baked ham, 10 thin slices of Gruyère cheese, Softened unsalted butter',
        directions='Heat a large griddle. Spread 10 of the brioche slices with the jam. Top with the ham and Gruyère and close the sandwiches. Lightly butter the outside of the sandwiches and cook over moderate heat until toasted and the cheese is melted, 2 minutes per side. Cut in half and serve right away.',
    )
    r13 = Recipe(
        user_id=6,
        title='Pink Grapefruit and Avocado Salad',
        description='This pretty salad is best in the winter when grapefruit is at its prime.',
        img_url='https://www.foodandwine.com/thmb/9E3pMYDbNKrzksE5W1ld9rphvSw=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201011-xl-pink-grapefruit-and-avocado-salad-bc58a373e6b24f998baa36b1d6de65d1.jpg',
        total_time='30 minutes',
        servings='4 servings',
        ingredients='2 medium ruby grapefruits, 1 teaspoon finely grated grapefruit zest, 1 medium shallot, minced, 1 teaspoon white wine vinegar, 2 medium Hass avocados sliced 1/4 inch thick. Salt, 2 tablespoons extra-virgin olive oil, Freshly ground pepper, Chervil leaves for garnish',
        directions='Using a sharp knife, cut the skin and all of the bitter white pith off of the grapefruits. Working over a bowl, cut in between the membranes to release the sections. Squeeze the juice from the membranes into the bowl. Transfer 2 tablespoons of the juice to another bowl. Add the zest, shallot and vinegar; let the dressing stand for 10 minutes. Season the avocado with salt and arrange on plates with the grapefruit sections. Stir the oil into the dressing; season with salt and pepper. Drizzle onto the grapefruit and avocado, garnish with the chervil and serve.',
    )
    r14 = Recipe(
        user_id=6,
        title='Herbed Ricotta with Grilled Bread',
        description=' Make this simple herbed ricotta for all your parties because it\'s such a crowd-pleaser. It\'s delicious spread on toasted bread but is also perfect served with crudités',
        img_url='https://www.foodandwine.com/thmb/d6IrEem0MfEWdekwp1KYkFPJVNI=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/herbed-ricotta-with-grilled-bread-XL-RECIPE0517-2e46c3952128480d821537c3ecfc0cb2.jpg',
        total_time='30 minutes',
        servings='8 servings',
        ingredients='1 pound fresh ricotta, 1 teaspoon finely grated lemon zest plus 3 tablespoons fresh lemon juice, 1 garlic clove finely grated, 1/4 cup extra-virgin olive oil, plus more for brushing and drizzling, 1 cup finely chopped mixed chives, parsley, mint and tarragon, plus more for garnish, Kosher salt, Pepper, 2 baguettes split lengthwise',
        directions='In a food processor, puree the ricotta, lemon zest, lemon juice, garlic and the 1/4 cup of olive oil until smooth. Scrape into a medium bowl, stir in the herbs and season generously with salt and pepper. Light a grill. Brush the baguettes with olive oil. Grill over moderately high heat, turning once, until lightly charred, 3 minutes. Drizzle the herbed ricotta with olive oil and garnish with herbs and cracked pepper. Serve with the bread.',
    )
    r15 = Recipe(
        user_id=7,
        title='Bacon Candy',
        description='Crispy, sweet and salty, this three-ingredient snack is the ultimate cocktail party hors d\'oeuvre',
        img_url='https://www.spendwithpennies.com/wp-content/uploads/2019/11/Candied-Bacon-3.jpg',
        total_time='25 minutes',
        servings='20 strips',
        ingredients='1/2 cup packed light brown sugar, 1 1/2 teaspoons chile powder, 20 slices of thick-cut bacon (1 1/2 pounds)',
        directions='Preheat the oven to 400°. Line 2 rimmed baking sheets with foil. In a small bowl, whisk the brown sugar with the chile powder. Arrange the bacon strips on the foil and coat the tops with the chile sugar. Bake for 20 to 25 minutes, until caramelized and almost crisp. Transfer the bacon to a rack set over a sheet of foil to cool completely; serve.',
    )
    r16 = Recipe(
        user_id=7,
        title='Pappardelle with Chicken and Pistachio-Mint Pesto',
        description='Let\'s make a bright and nutty mint-and-pistachio pesto as the sauce for this fresh and summery warm pasta dish.',
        img_url='https://www.foodandwine.com/thmb/hEHd08HOo_UcpEtDxmw2bwFbd5E=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/pappardelle-with-chicken-and-pistachio-mint-pesto-XL-RECIPE1017-ffd1b2c4ef334d36a45a168b8cb0197d.jpg',
        total_time='30 minutes',
        servings='4 to 6 servings',
        ingredients='1 1/2 cups lightly packed mint leaves plus more for garnish, 1/2 cup shelled unsalted pistachios, 1/4 cup fresh lemon juice, 1/2 cup extra-virgin olive oil, Kosher salt, Pepper, 8 ounces pappardelle pasta, 12 ounces shredded rotisserie chicken (3 cups), 1 small zucchini, very thinly sliced or shaved, 1 small yellow squash (very thinly sliced or shaved), 1 1/2 cups mixed cherry tomatoes(halved or quartered if large)',
        directions='In a food processor, combine the 1 1/2 cups of mint with the pistachios and lemon juice and pulse until finely chopped. With the machine on, gradually add the olive oil until incorporated and the pesto is nearly smooth. Scrape into a large bowl and season generously with salt and pepper. Meanwhile, in a large saucepan of salted boiling water, cook the pasta until al dente. Drain well, reserving 1 cup of the cooking water. Add the pasta, chicken, zucchini, yellow squash, tomatoes and reserved cooking water to the pesto and toss well. Season generously with salt and pepper and toss again. Garnish with mint leaves and serve right away.',
    )
    r17 = Recipe(
        user_id=8,
        title='Pineapple-Coconut Soft Serve',
        description='With just five ingredients, this fluffy, effortless dessert comes together in minutes with a flavor reminiscent of a tiki cocktail. For an adult version, swap 1/4 cup of the coconut cream for the same amount of your favorite rum.',
        img_url='https://www.foodandwine.com/thmb/Cst4Mpbat3QNS9DDEO_t6dMgmnY=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/pineapple-coconut-soft-serve-FT-RECIPE0620-aafa228e086c4d6f86ece751241160e4.jpg',
        total_time='15 minutes',
        servings='12 servings',
        ingredients='2 cups all purpose flour, 1 1/2 teaspoons kosher salt, 2 sticks unsalted butter (softened), 1 cup packed light brown sugar, 1/3 cup granulated sugar, 2 tablespoons whole milk, 1 teaspoon pure vanilla extract, 1 cup bittersweet chocolate chips',
        directions='In a medium bowl, whisk the flour with the salt. In a large bowl, using a hand mixer, beat the butter with both sugars at medium speed until blended, about 2 minutes. At low speed, beat in the milk and vanilla until just combined. Add the dry ingredients and mix until just combined. Using a rubber spatula, fold in the chocolate chips. Eat the cookie dough straight out of the bowl or refrigerate in an airtight container for up to 2 weeks.',
    )
    r18 = Recipe(
        user_id=8,
        title='Edible Cookie Dough',
        description='There are so many reasons to make edible cookie dough. The weather is hot, the oven is broken or you have a fierce cookie dough craving. Perhaps all of the above. Enter edible cookie dough: Unburdened by leaveners or raw eggs, it can be enjoyed straight from the bowl with a spoon.We like classic chocolate chip dough, but the variations are endless. A couple of suggestions: Swap M&Ms, crushed Oreos or milk chocolate chips in for the bittersweet chips. Beat in 3 tablespoons of peanut butter with the butter, then fold in 1/2 cup each of chopped salted peanuts and chocolate chips.',
        img_url='https://www.foodandwine.com/thmb/g-JJMTQuptjfQg_f6GcexIJmtco=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/edible-cookie-dough-XL-RECIPE2016-e7c8d47454984f37bc743406f28f224c.jpg',
        total_time='10 minutes',
        servings='4 cups',
        ingredients='1 1/2 pounds fresh pineapple chunks cut into 1/2-inch pieces (about 6 cups), 1 1/4 cups unsweetened coconut cream, 1/4 cup light agave nectar, Pinch of kosher salt, Toasted unsweetened flaked coconut for garnish',
        directions='Spread pineapple in an even layer on a baking sheet lined with parchment paper. Freeze at least 8 hours or up to overnight. Place frozen pineapple, coconut cream, agave, and salt in a food processor; pulse until finely chopped, about 40 times. Process until smooth and airy, 3 to 4 minutes, stopping to scrape down sides of bowl as needed. Serve soft, or transfer to an airtight container, and freeze until just firm, about 1 hour. Garnish with flaked coconut.',
    )
    r19 = Recipe(
        user_id=9,
        title='Ricotta-Orange Pound Cake with Prosecco Strawberries',
        description='This is one cake that doesn\'t require any icing. Enjoy it with a cup of coffee or dessert wine.',
        img_url='https://www.foodandwine.com/thmb/L85DlVyqefV1gYJMN3BJsSqTR4g=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/201405-xl-ricotta-orange-pound-cake-with-prosecco-strawberries-2000-bab153f0277b43f7aeed0c7f8913716d.jpg',
        total_time='2 hours 15 minutes',
        servings='8 servings',
        ingredients='1 1/2 sticks unsalted butter, at room temperature plus more for greasing, 1 1/2 cups cake flour, 2 1/2 teaspoons baking powder, 1 teaspoon kosher salt, 1 1/2 cups fresh ricotta cheese, 1 1/2 cups plus 2 tablespoons granulated sugar, 3 large eggs, 2 tablespoons amaretto liqueur, 1 teaspoon pure vanilla extract, 1 teaspoon finely grated orange zest, 1 pound strawberries cut into quarters, 2 tablespoons Prosecco, Confectioners\' sugar for dusting, Lightly sweetened whipped cream for serving',
        directions='Preheat the oven to 350°. Butter a deep, 9-inch round cake pan. In a bowl, whisk the cake flour, baking powder and salt. In another bowl, beat the ricotta, 1 1/2 sticks of butter and 1 1/2 cups of the sugar at medium-high speed until smooth. Beat in the eggs one at a time until just incorporated, then beat in the amaretto, vanilla and orange zest. Beat in the dry ingredients in 3 batches just until incorporated. Scrape the batter into the prepared pan and bake for 50 minutes, until a toothpick inserted in the center comes out with a few crumbs. Transfer to a rack to cool for 20 minutes; unmold and let cool completely. In a bowl, toss the strawberries with the Prosecco and remaining 2 tablespoons of sugar and let stand at room temperature until juicy, about 30 minutes. Dust the pound cake with confectioners\' sugar. Cut into wedges and serve with the strawberries and whipped cream.',
    )
    r20 = Recipe(
        user_id=10,
        title='Avocado Hollandaise',
        description='Luscious, rich, and lemony hollandaise gets completely re-imagined here in a light, supremely creamy puree of avocado, lemon juice, and olive oil.',
        img_url='https://www.kitchentreaty.com/wp-content/uploads/2018/03/avocado-hollandaise-8-700x980.jpg',
        total_time='10 minutes',
        servings='4 servings',
        ingredients='1/2 very ripe medium Hass avocado peeled and chopped, 2 teaspoons fresh lemon juice, 2 tablespoons extra-virgin olive oil, Kosher salt, Freshly ground pepper, Poached eggs for serving',
        directions='In a blender, combine the avocado and lemon juice with 1/3 cup of hot water. Puree until smooth and light in texture, about 2 minutes, scraping down the side of the bowl occasionally. With the machine on, drizzle in the olive oil and puree until combined. Season with salt and pepper. Serve the hollandaise over poached eggs.',
    )
    r21 = Recipe(
        user_id=10,
        title='Egg in a Bagel Hole',
        description='Adding water to the skillet helps cook the eggs evenly without burning the bagel halves, resulting in a lightly toasted bagel wrapped around a perfectly runny yolk. Savory smoked salmon and creamy avocado complete this classic breakfast.',
        img_url='https://www.foodandwine.com/thmb/pJ9JU-nv1VPTvyy1wkGvgsDLS8Q=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/egg-in-a-bagel-hole-FT-RECIPE0320-c1854893ac4f4b3385994a276de05873.jpg',
        total_time='10 minutes',
        servings='2 servings',
        ingredients='1 everything bagel split, 2 tablespoons unsalted butter (softened), 2 large eggs, 1 tablespoon water, Kosher salt to taste, Black pepper to taste, 2 ounces cold-smoked salmon for serving, Caviar or sliced avocado for serving',
        directions='If needed, carefully widen holes in bagel halves to 1 3/4 inches in diameter using a paring knife. Spread bagel halves evenly on both sides with butter. Heat a 12-inch skillet over medium. Place bagel halves, cut sides up, in skillet. Cook until golden brown, 2 to 3 minutes .Flip bagel halves cut sides down. Reduce heat to low; crack eggs into bagel holes. Pour 1 tablespoon water around edge of skillet, and immediately cover skillet. Cook until egg whites are set and yolks are cooked to desired degree of doneness, 5 to 8 minutes. Transfer bagel halves to a plate; season with salt and pepper. Serve with smoked salmon and caviar or sliced avocado.',
    )
    r22 = Recipe(
        user_id=2,
        title='Charred Shishito Peppers with Furikake',
        description='Whether eaten as a snack or incorporated into a main dish, crunchy, sweet shishito peppers are delicious and occasionally pack a punch — one in ten are super spicy!',
        img_url='https://www.foodandwine.com/thmb/G9jRJ_evJKG-Ogd_vvTLjJJ3TMw=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/charred-shishito-peppers-with-furikake-XL-RECIP0717_0-190ad594a07049f389b3da12a4d8a69b.jpg',
        total_time='15 minutes',
        servings='4 servings',
        ingredients='2 teaspoons grapeseed or canola oil, 1 pound shishito peppers, 1 tablespoon furikake (see Note) plus more for garnish, 1 tablespoon fresh lime juice, 1 teaspoon shoyu or other soy sauce, Flaky sea salt, Lime wedges for serving',
        directions='In a large cast-iron skillet, heat 1 teaspoon of the grapeseed oil. Add half of the peppers and cook over moderately high heat, turning occasionally, until charred and tender, about 4 minutes. Transfer to a large bowl. Repeat with the remaining oil and peppers. Add the 1 tablespoon of furikake, the lime juice and shoyu to the shishitos and toss to combine; season with flaky sea salt. Transfer to a platter; garnish with more furikake. Serve immediately with lime wedges.',
    )
    r23 = Recipe(
        user_id=3,
        title='Fig Jam',
        description='This supersimple fig jam recipe—just figs, sugar and lemon juice—can be easily upgraded with white port and rosemary for an extra special treat.',
        img_url='https://www.foodandwine.com/thmb/fEFCudK89VLOnrUqcSo5OG_cNik=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/fig-jam-FT-RECIPE0909-6c7a8cd04a8247e69b79398511173d92.jpg',
        total_time='45 minutes',
        servings='Makes three 1/2-pint jars',
        ingredients='2 pounds green or purple figs, stemmed and cut into 1/2-inch pieces, 1 1/2 cups sugar, 1/4 cup plus 2 tablespoons fresh lemon juice, 1/2 cup water',
        directions='In a large, nonreactive saucepan, toss the fig pieces with the sugar and let stand, stirring occasionally, for about 15 minutes, until the sugar is mostly dissolved and the figs are juicy. Add the lemon juice and water and bring to a boil, stirring until the sugar is completely dissolved. Simmer the fig jam over moderate heat, stirring occasionally, until the fruit is soft and the liquid runs off the side of a spoon in thick, heavy drops, about 20 minutes. Spoon the jam into three 1/2-pint jars, leaving 1/4 inch of space at the top. Close the jars and let cool to room temperature. Store the jam in the refrigerator for up to 3 months.',
    )
    r24 = Recipe(
        user_id=4,
        title='Sunflower-Seed Brittle',
        description='Pair this delightful crunchy sunflower-seed brittle with 5 Spoke Creamery Tumbleweed cheese or other semi-firm cow\'s milk cheese, like sharp cheddar!',
        img_url='https://www.foodandwine.com/thmb/BdIy-9AAQUiteT5OL5DO5myqu9A=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/200812-r-xl-sunflower-seed-brittle-1687040503e84dc1bb71ebdf894463c6.jpg',
        total_time='30 minutes',
        servings='1 pound',
        ingredients='1 cup sugar, 1/2 cup water, 1/2 cup light corn syrup, 1 1/2 tablespoons unsalted butter (at room temperature), 1 teaspoon kosher salt, ½ teaspoon baking soda, 2 cups raw sunflower seeds',
        directions='Line a large, rimmed baking sheet with parchment paper and lightly oil the paper. In a medium saucepan, combine the sugar, water and corn syrup and bring to a boil. Boil over moderate heat until the caramel is golden and registers 320° on a candy thermometer, about 10 minutes. Remove from the heat and stir in the butter, salt and baking soda. Stir in the sunflower seeds and quickly spread the mixture on the prepared baking sheet in a thin layer. Let the brittle stand until completely cool, then break into pieces.',
    )
    r25 = Recipe(
        user_id=5,
        title='Caramelized Broccoli with Garlic',
        description='Slowly caramelizes broccoli to bring out its sweetness, then revitalizes it with a squeeze of lemon and a pinch of crushed red pepper. The resulting broccoli is tender, flavorful, and makes an easy side dish.',
        img_url="https://www.foodandwine.com/thmb/s9UPydFVtFfy8nPJ2XhpNl4V1Vs=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/Caramelized-Broccoli-with-Garlic-FT-RECIPE0822-2000-926848df43b3456ba0d4aa6dfb6766e9.jpg",
        total_time='35 minutes',
        servings='4 servings',
        ingredients='3 tablespoons extra-virgin olive oil, 2 heads of broccoli (1 1/4 pounds total) stems peeled and heads halved lengthwise, 1/2 cup water, 3 cloves garlic (thinly sliced), Pinch of crushed red pepper, 2 tablespoons fresh lemon juice, Salt and freshly ground black pepper',
        directions='In a large, deep skillet, heat 2 tablespoons of the olive oil. Add the broccoli, cut side down, cover, and cook over moderate heat until richly browned on the bottom, about 8 minutes. Add the water, cover, and cook until the broccoli is just tender and the water has evaporated, about 7 minutes. Add the remaining 1 tablespoon of olive oil along with the garlic and the crushed red pepper and cook uncovered until the garlic is golden brown, about 3 minutes. Drizzle with the lemon juice, season the broccoli with salt and black pepper, and serve.',
    )
    r26 = Recipe(
        user_id=6,
        title='Thanksgiving Leftovers Nachos',
        description='Make next-level nachos with leftovers from your Thanksgiving meal. These leftovers include diced turkey, chopped roasted vegetables, and whole cranberry sauce, but any leftovers you have can be used because gooey Monterey Jack cheese brings them all together.',
        img_url='https://www.foodandwine.com/thmb/fWr9ev8VxVxbPnkaGicfBOySDAE=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/thanksgiving-leftover-nachos-ft-blog1119-1-17ca813a83ee4cc099a9f69a30888161.jpg',
        total_time='30 mins',
        servings='6 to 8 servings',
        ingredients='Extra-virgin olive oil for brushing, 13 ounces thick tortillas chips, 2 pounds shredded Pepper Jack cheese, 3 cups diced roasted vegetables, 12 ounces shredded or diced roasted turkey, 3/4 cup whole cranberry sauce, Cilantro sprigs (thinly sliced), jalapeños and pickled red onion for topping, Sour cream and hot sauce for serving',
        directions='Preheat the oven 400°. Brush a large rimmed baking sheet with olive oil. Spread half of the tortilla chips on the sheet and top with half each of the cheese, vegetables, turkey, and cranberry sauce. Repeat the layering with the remaining chips, cheese, vegetables, turkey, and cranberry sauce. Bake for 12 to 15 minutes, until the cheese is melted. Top the nachos with cilantro, jalapeños, and pickled red onion; serve right away with sour cream and hot sauce.',
    )
    r27 = Recipe(
        user_id=7,
        title='Garlic Confit',
        description='Although garlic is available year-round, fresh summer garlic has large cloves that are especially sweet and juicy. To preserve it, just simmer the cloves with dried red chiles and fresh thyme in olive oil until tender then packs them in the oil. Mash the garlic confit in butter and spread it on bread or slip it under chicken skin before roasting.',
        img_url='https://www.foodandwine.com/thmb/cJYRlmkRz92GQvHCbcqk6lKufwM=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/201110-xl-garlic-confit-36c97e3336bc44e496925b4f78cf2f3d.jpg',
        total_time='1 hour',
        servings='Makes 1 1/2 pints',
        ingredients='6 heads of garlic, cloves peeled (2 cups), 6 thyme sprigs, 3 small bay leaves, 3 dried red chiles such as chiles de arbol, 2 cups pure olive oil',
        directions='Combine all of the ingredients in a medium saucepan and simmer over low heat until the garlic is tender but not browned, about 30 minutes. Let cool. Using a slotted spoon, transfer the garlic, herbs and chiles to three 1/2-pint canning jars. Pour the cooking oil on top, seal and refrigerate for up to 4 months.',
    )
    r28 = Recipe(
        user_id=8,
        title='Apple-Pomegranate Cobbler',
        description='This juicy and bright apple cobbler is just the right amount of sweet, with an irresistibly tender and crunchy crust on top',
        img_url='https://www.foodandwine.com/thmb/BFk1o6eRsWwsH4B2n9MJNwPQOQM=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():gifv():format(webp)/apple-pomegranate-cobbler-XL-RECIPE1017-311bded52afb441d8a506b161eb86df6.jpg',
        total_time='2 hrs',
        servings='8 to 10 servings',
        ingredients='2 cups pomegranate juice, 6 peeled Granny Smith apples (3 pounds) sliced 1/2 inch thick, 1 cup sugar plus more for sprinkling, 2 1/4 cups all-purpose flour, Kosher salt, 2 teaspoons baking powder, 1 stick cold unsalted butter cut into small pieces, 1 cup cold heavy cream plus more for brushing, Pomegranate seeds, Vanilla ice cream for serving',
        directions='Preheat the oven to 375°. Place an 8-by-8-inch glass baking dish on a foil-lined rimmed baking sheet. In a small saucepan, bring the pomegranate juice to a boil over moderately high heat until reduced to 1/3 cup, about 15 minutes. Pour the juice into a large bowl and fold in the apples, 3/4 cup of the sugar, 1/4 cup of the flour and 1/2 teaspoon of salt. Scrape the mixture into the baking dish. In another large bowl, whisk the remaining 2 cups of flour with the remaining 1/4 cup of sugar, the baking powder and 1/2 teaspoon of salt. Add the butter and, using a pastry cutter or 2 knives, cut the butter into the dry ingredients until the mixture resembles very coarse crumbs, with some pieces the size of small peas. Gently stir in the 1 cup of cream just to combine. Gather the topping into small clumps and scatter over the apple filling. Brush the topping with cream and sprinkle generously with sugar. Bake the cobbler for 60 to 70 minutes, or until the filling is bubbling and the topping is golden. Tent with foil if the crust browns too quickly. Let cool for 20 minutes. Serve sprinkled with pomegranate seeds and topped with vanilla ice cream.',
    )
    r29 = Recipe(
        user_id=9,
        title='Carrot Cake Marmalade with Yogurt and Fresh Fruit',
        description='Everyone is raving about this yogurt bowl topped with sunny roasted carrot marmalade. The marmalade gets a big flavor from stewing carrots and apple with cinnamon, cardamom, and star anise for a warmly spiced result.',
        img_url='https://www.foodandwine.com/thmb/gae981F-9W4O3_NCudbSZMSvADM=/2250x0/filters:no_upscale():max_bytes(150000):strip_icc():format(webp)/carrot-cake-marmalade-with-yogurt-and-fresh-fruit-FT-RECIPE0221-1867851526da4613abbf4e863f51e224.jpg',
        total_time='1 hours 40 minutes',
        servings='Makes 2 1/3 Cups',
        ingredients='1 pound carrots, shredded (about 3 1/2 cups or 12 ounces), 2 cups water plus more if needed, 1 medium-size peeled Honeycrisp apple (about 7 ounces),  1 cup shredded Honeycrisp apple, 1 cup granulated sugar, 2 teaspoons grated lemon zest plus 1/4 cup fresh lemon juice, 3 cardamom pods (lightly smashed), 2 whole star anise, 2 cinnamon sticks, 3/4 teaspoon kosher salt, 2 tablespoons honey, yogurt, blueberries, clementine segments, granola for serving',
        directions='Place carrots, 2 cups water, apple, sugar, lemon zest and juice, cardamom pods, star anise, cinnamon sticks, and salt in a large heavy-bottomed saucepan; bring to a boil over medium-high, stirring occasionally. Cover and reduce heat to medium; cook, stirring occasionally, until carrots are crisp-tender, about 15 minutes. Uncover and cook, stirring occasionally, until carrots are tender and liquid has reduced to a thin, syrupy consistency, 20 to 25 minutes. Remove from heat, and discard whole spices. Transfer carrot mixture to a blender; add honey. Blend on low speed 1 minute. Continue blending, gradually increasing speed to medium-high, until smooth, about 1 minute, adding additional water, 1 tablespoon at a time, if necessary to keep puree moving. Transfer mixture to a small bowl; refrigerate 20 minutes.',
    )
    r30 = Recipe(
        user_id=10,
        title='',
        description='',
        img_url='',
        total_time='',
        servings='',
        ingredients='',
        directions='',
    )
    r31 = Recipe(
        user_id=9,
        title='',
        description='',
        total_time='',
        servings='',
        ingredients='',
        directions='',
    )
    r32 = Recipe(
        user_id=8,
        title='',
        description='',
        total_time='',
        servings='',
        ingredients='',
        directions='',
    )



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

    db.session.commit()



def undo_recipes():
    db.session.execute('TRUNCATE products RESTART IDENTITY CASCADE;')
    db.session.commit()

