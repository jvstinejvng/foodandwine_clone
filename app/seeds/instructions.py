from app.models import db, Instruction

def seed_instructions():
    in1 = Instruction(
        recipe_id = 1,
        specification  = 'In a blender, puree the silken tofu with the olive oil, lemon juice, the 1 1/2 tablespoons of Parmigiano, the anchovy, garlic, Worcestershire and mustard; season the dressing with salt and pepper.',
        )
    in2 = Instruction(        
        recipe_id = 1,
        specification  = 'Wrap the firm tofu in paper towels and press out some of the water. In a large skillet, heat 1/4 inch of vegetable oil until shimmering. In a bowl, toss the tofu with the cornstarch until coated. Add the cubes to the oil and fry over moderately high heat, turning once, until crisp, about 8 minutes. Using a slotted spoon, transfer the croutons to a paper towel–lined plate; season with salt.',
        )
    in3 = Instruction(
        recipe_id = 1,
        specification  = 'In a large bowl, toss the romaine with the dressing and two-thirds of the croutons. Transfer the salad to plates and top with the remaining croutons. Sprinkle with Parmigiano and serve.',
        )
    in4 = Instruction(
        recipe_id = 2,
        specification  = 'In a large saucepan, cover the eggs with water and bring to a vigorous boil. Cover the saucepan, remove from the heat and let stand for 10 minutes.',
        )
    in5 = Instruction(
        recipe_id = 2,
        specification  = 'Drain off the water and shake the pan gently to crack the eggs. Cool the eggs slightly under cold running water, then peel them under running water. Pat dry.',
        )
    in6 = Instruction(
        recipe_id = 2,
        specification  = 'Cut the eggs in half lengthwise and carefully remove the yolks. Transfer the yolks to a bowl and mash well with a fork. Stir in the salmon, mayonnaise, cornichons, cornichon liquid and Dijon mustard. Season with salt. Mound the filling in the egg-white halves and sprinkle with Old Bay. Serve lightly chilled.',
        )
    in7 = Instruction(
        recipe_id = 3,
        specification  = 'In a large saucepan, melt the butter. Add the celery, carrots, onion, garlic, thyme and a generous pinch each of salt and pepper and cook over moderate heat, stirring occasionally, until the vegetables just start to soften, about 10 minutes. Sprinkle the flour over the vegetables and cook, stirring, until evenly coated and lightly browned, about 3 minutes.',
        )
    in8 = Instruction(
        recipe_id = 3,
        specification  = 'Add the wild rice to the saucepan and gradually stir in the stock and water. Bring to a boil, then simmer over moderately low heat, stirring occasionally, until the vegetables are tender, about 30 minutes. Add the chicken and simmer, stirring occasionally, until the wild rice is tender, 10 to 15 minutes longer. Stir in the cream and season with salt and pepper. Ladle the soup into bowls and serve.',
        )
    in9 = Instruction(
        recipe_id = 4,
        specification  = 'Light a grill or preheat a grill pan. Brush the apricots with oil and season with salt and pepper. Grill over high heat, cut sides down, just until lightly charred, 5 minutes. Let cool.',
        )
    in10 = Instruction(
        recipe_id = 4,
        specification  = 'In a bowl, whisk the lemon juice with the 1/4 cup of oil and season with salt and pepper. Gently toss in the apricots, radicchio and arugula. Transfer to a platter and top with the burrata, ham and vinegar. Serve.',
        )
    in11 = Instruction(
        recipe_id = 5,
        specification  = 'Heat a saucepan over medium heat. Melt the butter, and then stir in the garlic. Cook for 1 to 2 minutes, or until the garlic is lightly browned.',
        )
    in12 = Instruction(
        recipe_id = 5,
        specification  = 'Whisk in the mustard and honey. Stir in the Worcestershire sauce, apple cider vinegar, and season with salt and pepper. Reduce heat to low and simmer the sauce for about 3 to 5 minutes or until thickened. Set aside.',
        )
    in13 = Instruction(
        recipe_id = 5,
        specification  = 'Rinse the chicken wings and pat them dry. Generously season the chicken with salt and black pepper. Dredge the wings in flour, shaking off any excess flour, and set aside.',
        )
    in14 = Instruction(
        recipe_id = 5,
        specification  = 'In a large saucepan or deep fryer, heat the oil to about 375°. Fry the chicken wings in small batches until golden brown, 8 to 10 minutes. Shake off any excess oil and place on paper towels to drain. Continue frying the chicken in batches until all of the wings are cooked.',
        )
    in15 = Instruction(
        recipe_id = 5,
        specification  = 'Toss the wings with the honey mustard sauce and serve warm with leftover sauce for dipping.',
        )
    in16 = Instruction(
        recipe_id = 6,
        specification  = 'Preheat oven to 350°F. Line a roasting pan with heavy-duty aluminum foil. Stir together brown sugar, honey, mustard, salt, pepper, and 1/2 cup of the cider in a medium bowl.',
        )
    in17 = Instruction(
        recipe_id = 6,
        specification  = 'Place ham in prepared pan so that individual ham slices are perpendicular to pan bottom. Brush ham with 3/4 cup glaze, gently pushing glaze in between slices. Turn ham over so that bottoms of slices are now facing up; brush an additional 3/4 cup glaze in between slices. Turn ham so that the large, flat, cut side is facing down in pan.',
        )
    in18 = Instruction(
        recipe_id = 6,
        specification  = 'Pour remaining 1/2 cup cider into bottom of pan. Cover tightly with foil. Bake in preheated oven 1 1/2 hours. Remove from oven; remove and discard foil. Brush ham evenly with 1/3 cup glaze; return to oven, and bake 15 minutes. Remove from oven. Brush with 1/3 cup glaze; return to oven, and bake until a thermometer inserted in thickest portion of ham registers 140°F, about 15 minutes. Remove from oven; brush with remaining 1/3 cup glaze and pan drippings. Let stand 15 minutes. Serve warm or at room temperature.',
        )
    in19 = Instruction(
        recipe_id = 7,
        specification  = 'In a glass baking dish, season the steak with salt and pepper and rub with the olive oil. Spread the garlic, scallions and bay leaves all over the steak. Cover both sides of the steak with lemon slices. Cover and refrigerate for 24 hours. Light a grill and brush with vegetable oil. Scrape off the seasonings and bring the steak to room temperature. Season with salt and pepper and grill over moderately high heat until medium-rare within, 3 1/2 minutes per side. Transfer to a carving board and let rest for 5 minutes. Thinly slice across the grain and serve.',
        )
    in20 = Instruction(
        recipe_id = 8,
        specification  = 'In a small bowl, whisk the 1/4 cup of olive oil with the lemon juice, mustard and rosemary. Season the vinaigrette with salt and pepper.',
        )
    in21 = Instruction(
        recipe_id = 8,
        specification  = 'Light a grill or heat a grill pan. Thread the salmon and cherry tomatoes onto the skewers, brush with olive oil and season all over with salt and pepper. Grill over moderately high heat, turning once, until the salmon is just cooked through, about 6 minutes. Transfer the skewers to a platter and drizzle with some of the vinaigrette. Serve right away, passing additional vinaigrette at the table.',
        )
    in22 = Instruction(
        recipe_id = 9,
        specification  = 'Preheat oven to 350°F. Beat cream cheese, lemon curd, and 1/8 teaspoon salt with an electric mixer on medium speed until smooth, about 3 minutes.',
        )
    in23 = Instruction(
        recipe_id = 9,
        specification  = 'Grease a 13- x 9-inch baking dish with butter. Arrange 1 crêpe on a work surface. Using a small offset spatula, spread 1 1/2 tablespoons cream cheese mixture evenly over crêpe, leaving a 1-inch border. Fold crêpe in half, and then fold in half again. Place folded crêpe in prepared baking dish. Repeat with remaining crêpes and remaining cream cheese mixture, overlapping folded crêpes in baking dish. Bake in preheated oven until crêpes are heated through and edges are golden brown, 15 to 20 minutes.',
        )
    in24 = Instruction(
        recipe_id = 9,
        specification  = 'Meanwhile, melt butter in a large nonstick skillet over medium-low. Add lemon slices, sprinkle with remaining 1/8 teaspoon salt, and cook, stirring occasionally, until lemon peel is softened, about 7 minutes. Stir in maple syrup, and remove from heat. Spoon lemon sauce over casserole. Dust with powdered sugar, and serve.',
        )
    in25 = Instruction(
        recipe_id = 10,
        specification  = "Preheat the oven to 375°. Using the flat side of a chef’s knife, crush the garlic and 1/2 teaspoon of salt to a paste. Scrape the garlic paste into a medium bowl and add the cream cheese, scallions, egg yolk, cumin, mustard and 1/3 cup of cilantro. Stir with a rubber spatula until well combined. Season with a generous pinch each of salt and pepper, then fold the cheddar into the filling.",
        )
    in26 = Instruction(
        recipe_id = 10,
        specification  = 'On a rimmed baking sheet, toss the jalapeños with the olive oil and a pinch each of salt and pepper until well coated. Arrange them cut side up and spoon 1 1/2 to 2 tablespoons of filling into each one. Bake for about 20 minutes, rotating the sheet from front to back halfway through, until the filling is puffed and bubbling and the jalapeños are tender. Garnish with minced cilantro and serve with lime wedges.',
        )
    in27 = Instruction(
        recipe_id = 11,
        specification  = 'In a mini food processor, combine garlic, rosemary and olive oil and process until garlic is finely chopped. Season lamb racks with salt and pepper and rub garlic-rosemary oil all over them. Set racks fat-side up on a large rimmed baking sheet and let stand for 1 hour.',
        )
    in28 = Instruction(
        recipe_id = 11,
        specification  = 'Preheat oven to 450°F. Roast lamb in upper third of oven for 15 minutes. Turn racks and roast for 10 minutes longer for medium-rare meat. Transfer racks to a carving board, stand them upright and let rest for 10 minutes.',
        )
    in29 = Instruction(
        recipe_id = 11,
        specification  = 'Carve racks in between rib bones and transfer to plates. Serve immediately.',
        )
    in30 = Instruction(
        recipe_id = 12,
        specification  = 'Heat a large griddle. Spread 10 of the brioche slices with the jam. Top with the ham and Gruyère and close the sandwiches. Lightly butter the outside of the sandwiches and cook over moderate heat until toasted and the cheese is melted, 2 minutes per side. Cut in half and serve right away.',
        )
    in31 = Instruction(
        recipe_id = 13,
        specification  = 'Using a sharp knife, cut the skin and all of the bitter white pith off of the grapefruits. Working over a bowl, cut in between the membranes to release the sections. Squeeze the juice from the membranes into the bowl.',
        )
    in32 = Instruction(
        recipe_id = 13,
        specification  = 'Transfer 2 tablespoons of the juice to another bowl. Add the zest, shallot and vinegar; let the dressing stand for 10 minutes.',
        )
    in33 = Instruction(
        recipe_id = 13,
        specification  = 'Season the avocado with salt and arrange on plates with the grapefruit sections. Stir the oil into the dressing; season with salt and pepper. Drizzle onto the grapefruit and avocado, garnish with the chervil and serve.',
        )
    in34 = Instruction(
        recipe_id = 14,
        specification  = 'In a food processor, puree the ricotta, lemon zest, lemon juice, garlic and the 1/4 cup of olive oil until smooth. Scrape into a medium bowl, stir in the herbs and season generously with salt and pepper.',
        )
    in35 = Instruction(
        recipe_id = 14,
        specification  = 'Light a grill. Brush the baguettes with olive oil. Grill over moderately high heat, turning once, until lightly charred, 3 minutes. Drizzle the herbed ricotta with olive oil and garnish with herbs and cracked pepper. Serve with the bread.',
        )
    in36 = Instruction(
        recipe_id = 15,
        specification  = 'Preheat the oven to 400°F. Line 2 rimmed baking sheets with foil. In a small bowl, whisk the brown sugar with the chile powder.',
        )
    in37 = Instruction(
        recipe_id = 15,
        specification  = 'Arrange the bacon strips on the foil and coat the tops with the chile sugar. Bake for 20 to 25 minutes, until caramelized and almost crisp.',
        )
    in38 = Instruction(
        recipe_id = 15,
        specification  = 'Transfer the bacon to a rack set over a sheet of foil to cool completely; serve.',
        )
    in39 = Instruction(
        recipe_id = 16,
        specification  = 'In a food processor, combine the 11/2 cups of mint with the pistachios and lemon juice and pulse until finely chopped. With the machine on, gradually add the olive oil until incorporated and the pesto is nearly smooth. Scrape into a large bowl and season generously with salt and pepper.',
        )
    in40 = Instruction(
        recipe_id = 16,
        specification  = 'Meanwhile, in a large saucepan of salted boiling water, cook the pasta until al dente. Drain well, reserving 1 cup of the cooking water. Add the pasta, chicken, zucchini, yellow squash, tomatoes and reserved cooking water to the pesto and toss well. Season generously with salt and pepper and toss again. Garnish with mint leaves and serve right away.',
        )
    in41 = Instruction(
        recipe_id = 17,
        specification  = 'Spread pineapple in an even layer on a baking sheet lined with parchment paper. Freeze at least 8 hours or up to overnight.',
        )
    in42 = Instruction(
        recipe_id = 17,
        specification  = 'Place frozen pineapple, coconut cream, agave, and salt in a food processor; pulse until finely chopped, about 40 times. Process until smooth and airy, 3 to 4 minutes, stopping to scrape down sides of bowl as needed. Serve soft, or transfer to an airtight container, and freeze until just firm, about 1 hour. Garnish with flaked coconut.',
        )
    in43 = Instruction(
        recipe_id = 18,
        specification  = 'In a medium bowl, whisk the flour with the salt. In a large bowl, using a hand mixer, beat the butter with both sugars at medium speed until blended, about 2 minutes. At low speed, beat in the milk and vanilla until just combined. Add the dry ingredients and mix until just combined. Using a rubber spatula, fold in the chocolate chips. Eat the cookie dough straight out of the bowl or refrigerate in an airtight container for up to 2 weeks.',
        )
    in44 = Instruction(
        recipe_id = 19,
        specification  = 'Preheat the oven to 350°. Butter a deep, 9-inch round cake pan. In a bowl, whisk the cake flour, baking powder and salt. In another bowl, beat the ricotta, 1 1/2 sticks of butter and 1 1/2 cups of the sugar at medium-high speed until smooth. Beat in the eggs one at a time until just incorporated, then beat in the amaretto, vanilla and orange zest. Beat in the dry ingredients in 3 batches just until incorporated.',
        )
    in45 = Instruction(
        recipe_id = 19,
        specification  = 'Scrape the batter into the prepared pan and bake for 50 minutes, until a toothpick inserted in the center comes out with a few crumbs. Transfer to a rack to cool for 20 minutes; unmold and let cool completely.',
        )
    in46 = Instruction(
        recipe_id = 19,
        specification  = 'In a bowl, toss the strawberries with the Prosecco and remaining 2 tablespoons of sugar and let stand at room temperature until juicy, about 30 minutes.',
        )
    in47 = Instruction(
        recipe_id = 19,
        specification  = "Dust the pound cake with confectioners' sugar. Cut into wedges and serve with the strawberries and whipped cream.",
        )
    in48 = Instruction(
        recipe_id = 20,
        specification  = 'In a blender, combine the avocado and lemon juice with 1/3 cup of hot water. Puree until smooth and light in texture, about 2 minutes, scraping down the side of the bowl occasionally. With the machine on, drizzle in the olive oil and puree until combined. Season with salt and pepper. Serve the hollandaise over poached eggs.',
        )
    in49 = Instruction(
        recipe_id = 21,
        specification  = 'If needed, carefully widen holes in bagel halves to 1 3/4 inches in diameter using a paring knife. Spread bagel halves evenly on both sides with butter. Heat a 12-inch skillet over medium. Place bagel halves, cut sides up, in skillet. Cook until golden brown, 2 to 3 minutes.',
        )
    in50 = Instruction(
        recipe_id = 21,
        specification  = 'Flip bagel halves cut sides down. Reduce heat to low; crack eggs into bagel holes. Pour 1 tablespoon water around edge of skillet, and immediately cover skillet. Cook until egg whites are set and yolks are cooked to desired degree of doneness, 5 to 8 minutes. Transfer bagel halves to a plate; season with salt and pepper. Serve with smoked salmon and caviar or sliced avocado.',
        )
    in51 = Instruction(
        recipe_id = 22,
        specification  = 'In a large cast-iron skillet, heat 1 teaspoon of the grapeseed oil. Add half of the peppers and cook over moderately high heat, turning occasionally, until charred and tender, about 4 minutes. Transfer to a large bowl. Repeat with the remaining oil and peppers.',
        )
    in52 = Instruction(
        recipe_id = 22,
        specification  = 'Add the 1 tablespoon of furikake, the lime juice and shoyu to the shishitos and toss to combine; season with flaky sea salt. Transfer to a platter; garnish with more furikake. Serve immediately with lime wedges.',
        )
    in53 = Instruction(
        recipe_id = 23,
        specification  = 'In a large, nonreactive saucepan, toss the fig pieces with the sugar and let stand, stirring occasionally, for about 15 minutes, until the sugar is mostly dissolved and the figs are juicy.',
        )
    in54 = Instruction(
        recipe_id = 23,
        specification  = 'Add the lemon juice and water and bring to a boil, stirring until the sugar is completely dissolved. Simmer the fig jam over moderate heat, stirring occasionally, until the fruit is soft and the liquid runs off the side of a spoon in thick, heavy drops, about 20 minutes.',
        )
    in55 = Instruction(
        recipe_id = 23,
        specification  = 'Spoon the jam into three 1/2-pint jars, leaving 1/4 inch of space at the top. Close the jars and let cool to room temperature. Store the jam in the refrigerator for up to 3 months.',
        )
    in56 = Instruction(
        recipe_id = 24,
        specification  = 'Line a large, rimmed baking sheet with parchment paper and lightly oil the paper. In a medium saucepan, combine the sugar, water and corn syrup and bring to a boil. Boil over moderate heat until the caramel is golden and registers 320° on a candy thermometer, about 10 minutes. Remove from the heat and stir in the butter, salt and baking soda. Stir in the sunflower seeds and quickly spread the mixture on the prepared baking sheet in a thin layer. Let the brittle stand until completely cool, then break into pieces.',
        )
    in57 = Instruction(
        recipe_id = 25,
        specification  = 'In a large, deep skillet, heat 2 tablespoons of the olive oil. Add the broccoli, cut side down, cover, and cook over moderate heat until richly browned on the bottom, about 8 minutes.',
        )
    in58 = Instruction(
        recipe_id = 25,
        specification  = 'Add the water, cover, and cook until the broccoli is just tender and the water has evaporated, about 7 minutes.',
        )
    in59 = Instruction(
        recipe_id = 25,
        specification  = 'Add the remaining 1 tablespoon of olive oil along with the garlic and the crushed red pepper and cook uncovered until the garlic is golden brown, about 3 minutes. Drizzle with the lemon juice, season the broccoli with salt and black pepper, and serve.',
        )
    in60 = Instruction(
        recipe_id = 26,
        specification  = 'Preheat the oven 400°. Brush a large rimmed baking sheet with olive oil. Spread half of the tortilla chips on the sheet and top with half each of the cheese, vegetables, turkey, and cranberry sauce. Repeat the layering with the remaining chips, cheese, vegetables, turkey, and cranberry sauce. Bake for 12 to 15 minutes, until the cheese is melted.',
        )
    in61 = Instruction(
        recipe_id = 26,
        specification  = 'Top the nachos with cilantro, jalapeños, and pickled red onion; serve right away with sour cream and hot sauce.',
        )
    in62 = Instruction(
        recipe_id = 27,
        specification  = 'Combine all of the ingredients in a medium saucepan and simmer over low heat until the garlic is tender but not browned, about 30 minutes. Let cool.',
        )
    in63 = Instruction(
        recipe_id = 27,
        specification  = 'Using a slotted spoon, transfer the garlic, herbs and chiles to three 1/2-pint canning jars. Pour the cooking oil on top, seal and refrigerate for up to 4 months.',
        )
    in64 = Instruction(
        recipe_id = 28,
        specification  = 'Preheat the oven to 375°. Place an 8-by-8-inch glass baking dish on a foil-lined rimmed baking sheet. In a small saucepan, bring the pomegranate juice to a boil over moderately high heat until reduced to 1/3 cup, about 15 minutes. Pour the juice into a large bowl and fold in the apples, 3/4 cup of the sugar, 1/4 cup of the flour and 1/2 teaspoon of salt. Scrape the mixture into the baking dish.',
        )
    in65 = Instruction(
        recipe_id = 28,
        specification  = 'In another large bowl, whisk the remaining 2 cups of flour with the remaining 1/4 cup of sugar, the baking powder and 1/2 teaspoon of salt. Add the butter and, using a pastry cutter or 2 knives, cut the butter into the dry ingredients until the mixture resembles very coarse crumbs, with some pieces the size of small peas. Gently stir in the 1 cup of cream just to combine.',
        )
    in66 = Instruction(
        recipe_id = 29, 
        specification  = 'Gather the topping into small clumps and scatter over the apple filling. Brush the topping with cream and sprinkle generously with sugar. Bake the cobbler for 60 to 70 minutes, or until the filling is bubbling and the topping is golden. Tent with foil if the crust browns too quickly. Let cool for 20 minutes. Serve sprinkled with pomegranate seeds and topped with vanilla ice cream.',
        )
    in67 = Instruction(
        recipe_id = 29,
        specification  = 'Place carrots, 2 cups water, apple, sugar, lemon zest and juice, cardamom pods, star anise, cinnamon sticks, and salt in a large heavy-bottomed saucepan; bring to a boil over medium-high, stirring occasionally. Cover and reduce heat to medium; cook, stirring occasionally, until carrots are crisp-tender, about 15 minutes. Uncover and cook, stirring occasionally, until carrots are tender and liquid has reduced to a thin, syrupy consistency, 20 to 25 minutes. Remove from heat, and discard whole spices.',
        )
    in68 = Instruction(
        recipe_id = 29,
        specification  = 'Transfer carrot mixture to a blender; add honey. Blend on low speed 1 minute. Continue blending, gradually increasing speed to medium-high, until smooth, about 1 minute, adding additional water, 1 tablespoon at a time, if necessary to keep puree moving. Transfer mixture to a small bowl; refrigerate 20 minutes.',
        )
    in69 = Instruction(
        recipe_id = 29,
        specification  = 'Spoon yogurt into bowls, and dollop desired amount of marmalade on top; swirl together with a spoon. Top with blueberries, clementine segments, and granola.',
        )
    in70 = Instruction(
        recipe_id = 30,
        specification  = 'Preheat oven to 400 F.',
        )
    in71 = Instruction(
        recipe_id = 30,
        specification  = 'In a large bowl, sift together flour, sugar, baking powder, salt, and cinnamon. Add butter and using your hands or a pastry cutter, cut the butter into the flour until the size of peas, working quickly so the butter stays cold. Carefully fold in blueberries so they don’t burst.',
        )
    in72 = Instruction(
        recipe_id = 30,
        specification  = 'In a small bowl, combine buttermilk and ½ cup heavy cream.',
        )
    in73 = Instruction(
        recipe_id = 30,
        specification  = 'Make a well in the center of the flour mixture, then pour in the liquid mixture. Use a rubber spatula to carefully fold the ingredients until the liquid is just incorporated.',
        )
    in74 = Instruction(
        recipe_id = 30,
        specification  = 'Roll the dough out onto a lightly floured surface, adding more flour as needed if too sticky to work with. Press down into a small rectangle, about 6-inches by 8-inches. Cut the dough in half once horizontally and twice vertically to create 6 equal rectangles. Slice each rectangle in half diagonally to form 12 triangle-shaped scones. Carefully transfer scones to a large half sheet baking pan lined with a silpat baking mat or parchment paper.',
        )
    in75 = Instruction(
        recipe_id = 30,
        specification  = 'In a small bowl, whisk together egg and 1 tablespoon heavy cream. Brush the tops of the scones with egg wash, then bake for 16-18 minutes, or until scones are lightly golden brown. Let cool 5 minutes in pan, then transfer to a wire rack to cool completely.',
        )
    in76 = Instruction(
        recipe_id = 30,
        specification  = 'While scones are cooling, combine confectioner’s sugar and half the lemon juice in in a small bowl. Whisk until combined, adding more lemon juice as needed to reach desired glaze consistency. When scones are cool, drizzle lemon glaze on top.',
        )
    in77 = Instruction(
        recipe_id = 31,
        specification  = 'Cut 2 lemons in half and squeeze juice into a measuring glass or small bowl; you should have ¼ cup juice. Set aside. Using a paring knife, cut ends off remaining lemon to expose flesh. Upend lemon on a cut end and remove peel and white pith from lemons; discard. Cut between membranes to release segments into bowl with juice; squeeze membranes to get any last drops of juice. Fish out any seeds; set aside. Thinly slice chives and place in a small bowl; set aside.',
        )
    in78 = Instruction(
        recipe_id = 31,
        specification  = 'Pull side muscle off scallops, if needed; pat dry. Season lightly on both sides with salt and pepper. Heat a large skillet, preferably stainless steel, over medium-high. Pour in oil to lightly coat surface (2–3 Tbsp.); heat until it shimmers and you see first wisps of smoke. Swiftly place scallops into skillet, flat side down, and cook without touching, tossing, or fussing until underside is deep golden brown, 3–4 minutes. Use a thin spatula or tongs to gently turn over; if they resist, cook another 30 seconds and try again. Cook on second side until flesh at top and bottom looks opaque but there is still a faintly translucent strip in the middle, 1–2 minutes, depending on size. Transfer scallops to a plate.',
        )
    in79 = Instruction(
        recipe_id = 31,
        specification  = 'our off any oil in skillet and set over medium heat. Add butter and cook, swirling, until butter foams, then browns, about 2 minutes. Add reserved lemon juice and segments; energetically stir and swirl pan to emulsify sauce. Mix in capers and reserved chives and spoon pan sauce around and over scallops.',
        )
    in80 = Instruction(
        recipe_id = 32,
        specification  = 'Cook kale leaves in a large pot of boiling salted water until bright green and wilted, about 30 seconds. Transfer to a rimmed baking sheet with tongs; keep water boiling. Let kale cool slightly; wring out excess water with your hands.',
        )
    in81 = Instruction(
        recipe_id = 32,
        specification  = 'Cook pasta in pot of boiling water, stirring occasionally, until al dente.',
        )
    in82 = Instruction(
        recipe_id = 32,
        specification  = 'Blend nuts, oil, garlic, and ⅓ cup water in a blender or food processor until very smooth. Add kale and 1 oz. Parmesan. Purée, adding water 1 Tbsp. at a time as needed, until smooth. Transfer pesto to a large bowl.',
        )
    in83 = Instruction(
        recipe_id = 32,
        specification  = 'Using tongs, transfer pasta to bowl with pesto; add butter and ⅓ cup pasta cooking liquid. Toss, adding more pasta cooking liquid by the tablespoonful if needed, until sauce coats pasta. Divide among bowls; top with more Parmesan and a few grinds of pepper.',
        )
    in84 = Instruction(
        recipe_id = 33,
        specification  = 'Preheat oven to 350°F. Line a 9 inch cake pan pan with parchment paper so that it covers the bottom and goes up the sides of the pan. Fold parchment paper so that it hugs the sides of the pan, like an upside down hat. Spray with non-stick spray.',
        )
    in85 = Instruction(
        recipe_id = 33,
        specification  = 'With the skin still on, slice citrus 1/2 inch thick. Use a paring knife to carefully remove the skin from the citrus slices (like cutting off the outer ring). Doing it this way will ensure your oranges citrus stays intact and does not break apart when you slice it.',
        )
    in86 = Instruction(
        recipe_id = 33,
        specification  = 'Microwave the sugar and water together until the sugar dissolves completely, about 45 seconds. Pour half of the sugar-water into the bottom of the prepared cake pan, then line the bottom with prepared citrus fruits. Once arranged, pour the remaining sugar-water over the citrus. Set aside.',
        )
    in87 = Instruction(
        recipe_id = 33,
        specification  = 'In a large bowl, beat the butter and sugars together until light and fluffy. Add in the eggs, orange juice, orange zest, and vanilla extract.',
        )
    in88 = Instruction(
        recipe_id = 33,
        specification  = 'In a separate bowl, combine the flour, baking powder, baking soda, and salt, whisking to combine. Slowly alternate folding in the flour mixture and the yogurt into the wet ingredients until everything is combined. Mixture will be thick.',
        )
    in89 = Instruction(
        recipe_id = 33,
        specification  = 'Pour the batter over the prepared citrus slices, spreading it evenly to the edges.',
        )
    in90 = Instruction(
        recipe_id = 33,
        specification  = 'Bake for 35 minutes, then allow to cool completely before inverting onto a serving tray.',
        )
    in91 = Instruction(
        recipe_id = 34,
        specification  = 'Heat coconut oil in a Dutch oven on medium-low heat. Add garlic, lemongrass and chile and cook until softened, about 2 minutes. Add ginger and cook for 1 minute more, then stir in coconut milk, broth, fish sauce and coconut sugar.',
        )
    in92 = Instruction(
        recipe_id = 34,
        specification  = 'Bring mixture to a simmer, then add mussels. Cover and simmer, stirring occasionally, until the shells open, 5 to 6 minutes (discard any mussels that failed to open).',
        )
    in93 = Instruction(
        recipe_id = 34,
        specification  = 'Remove from heat and stir in lime juice. Divide mussels and broth evenly into four bowls. Garnish with lime zest, cilantro and chile.',
        )
    in94 = Instruction(
        recipe_id = 35,
        specification  = 'In a large wok, heat up with a drizzle of oil. Let it get hot and add in the curry paste.',
        )
    in95 = Instruction(
        recipe_id = 35,
        specification  = 'If cooking with chicken, add the chicken cut into small pieces, and stir fry for 4-5 minutes until cooked through.If using shrimp, cook for a minute until pink and remove / set aside. If cooking shrimp and chicken, then leave in and add the pineapples, bell pepper, garlic, and green onion.',
        )
    in96 = Instruction(
        recipe_id = 35,
        specification  = 'Nestle the shrimp on top of the veggies to slow down the cooking process. Once the pineapple starts to caramelize for (about 3 minutes), add the cold rice and break it up a bit.',
        )
    in97 = Instruction(
        recipe_id = 35,
        specification  = 'Add the fish sauce and soy sauce, the cashews, mix well and serve.',
        )
    in98 = Instruction(
        recipe_id = 36,
        specification  = 'Stir together Kewpie mayonnaise, ketchup, and yuzu juice in a bowl. Refrigerate until ready to serve. Process canned tomatoes in a food processor until smooth, about 1 minute. Set processed tomatoes aside.',
        )
    in99 = Instruction(
        recipe_id = 36,
        specification  = 'Heat oil in a small saucepan over medium-high. Add 1 pound ground beef, onion, and 2 teaspoons salt; cook, stirring occasionally, until meat is no longer pink and onion is lightly browned, about 7 minutes. Add processed tomatoes, tonkatsu, gochugaru, sugar, coriander, and cumin; stir in sake. Bring to a simmer. Stir together 1/4 cup cold water and flour in small bowl; add to ground beef mixture, and stir to combine. Stir in smoked paprika and 1/2 teaspoon black pepper. Reduce heat to medium-low, and return to a simmer. Cook, stirring often, 10 minutes. Remove from heat.',
        )
    in100 = Instruction(
        recipe_id = 36,
        specification  = 'Preheat grill or griddle to medium (350°F to 450°F). Gently stir together remaining 3 pounds ground beef, remaining 2 teaspoons salt, and remaining 1 teaspoon black pepper in a large bowl until just combined. Shape mixture into 8 (6-ounce) patties, pressing to 1/2-inch thickness. Place on oiled grates, and grill, covered, to desired degree of doneness, about 5 minutes per side for medium.',
        )
    in101 = Instruction(
        recipe_id = 36,
        specification  = 'Place patties on buns. Top each with 1/3 cup chili, 1 tomato slice, 1/4 cup lettuce, and 1 tablespoon mayonnaise mixture. Chili can be made up to 3 days ahead and stored in an airtight container in refrigerator.',
        )
    in102 = Instruction(
        recipe_id = 37,
        specification  = 'Preheat your oven to 350° F. Grease an 9x9" pan (if you want less thick brownies, use a 9x13" pan).',
        )
    in103 = Instruction(
        recipe_id = 37,
        specification  = 'Make the brownies: In a medium bowl, beat the eggs with the cocoa powder, salt, baking powder, espresso powder (if using), and vanilla. Beat for a few minutes until well combined.',
        )
    in104 = Instruction(
        recipe_id = 37,
        specification  = 'In the microwave or in a saucepan over medium heat, melt the butter with the sugar and stir until the sugar dissolves. Add the hot sugar and butter mixture to the bowl with the cocoa mixture. Stir to combine well. Add the flour and chocolate chips and mix well until shiny.',
        )
    in105 = Instruction(
        recipe_id = 37,
        specification  = "Pour the brownie batter into the prepared pan and bake for 20 to 25 minutes—the crust should be just set, but the brownies shouldn't be cooked through.",
        )
    in106 = Instruction(
        recipe_id = 37,
        specification  = "While the brownies bake, make the cheesecake layer. In a large bowl or stand mixer, beat together the cream cheese, softened butter, and cornstarch. Slowly add the condensed milk, egg, and vanilla and mix until very well combined.",
        )
    in107 = Instruction(
        recipe_id = 37,
        specification  = 'When the brownies have finished their first bake, remove them from the oven and pour the cheesecake batter over the top. Return the pan to the oven and bake for 25 to 30 minutes, or until the top is just beginning to brown. Let cool, then slice.',
        )
    in108 = Instruction(
        recipe_id = 38,
        specification  = 'Preheat the oven to 400°F. Grease four 6-ounce ramekins and place them on a sheet pan.',
        )
    in109 = Instruction(
        recipe_id = 38,
        specification  = "Melt the chocolate in the microwave and set aside to cool slightly. In a separate bowl, whisk together the eggs, sugar, salt, vanilla, clementine zest, and olive oil until light and fluffy (you don't have to go overboard here; just incorporate all of the ingredients—though, if you have the wherewithal in you, a little air in the eggs now will result in a deliciously chewy-edged lava cake later). Fold in the chocolate.",
        )
    in110 = Instruction(
        recipe_id = 38,
        specification  = 'Pour batter into the ramekins and bake for 10 to 15 minutes, or until just cooked. (The tops should be slightly cracked, the insides hot and gooey.) Dust with powdered sugar before serving, or top with vanilla ice cream',
        )
    in111 = Instruction(
        recipe_id = 39,
        specification  = 'For the Bourbon Peach Sauce: Melt butter in a small saucepan over medium heat. Add shallot and cook until softened, about 3 minutes. Stir in brown sugar, bourbon, vinegar, mustard, 1/2 teaspoon kosher salt and chopped peaches.Bring to a gentle simmer and cook, stirring occasionally, until peaches are soft and the sauce has thickened, 15-20 minutes. Keep warm.',
        )
    in112 = Instruction(
        recipe_id = 39,
        specification  = 'Turn all burners on gas grill to high, cover, and heat until hot, about 15 minutes. Leave primary burner on high and turn other burners to medium.',
        )
    in113 = Instruction(
        recipe_id = 39,
        specification  = 'Combine brown sugar, ginger, salt and pepper in a small bowl. Pat pork chops dry and coat all over with sugar mixture. Oil grates and place chops on hot side of grill. Cook 8-10 minutes, flipping halfway, until browned on both sides.',
        )
    in114 = Instruction(
        recipe_id = 39,
        specification  = 'Move to cooler side of grill and brush with melted butter. Continue to cook, turning once and brushing with more butter, until an instant read thermometer registers 145°F when inserted into the center of the chop, about 5 more minutes. Transfer to a platter and spoon warm bourbon peach sauce over the meat.',
        )
    in115 = Instruction(
        recipe_id = 40,
        specification  = 'Preheat oven to 350° F. Grease a 9-inch round cake pan with butter and line the bottom with parchment paper.',
        )
    in116 = Instruction(
        recipe_id = 40,
        specification  = 'Combine turbinado sugar and chopped rosemary in a small bowl. Using your fingers, gently massage the rosemary into the sugar. Set aside.',
        )
    in117 = Instruction(
        recipe_id = 40,
        specification  = 'Sift flour, 1 cup of granulated sugar, baking powder, and salt into a large bowl. In a separate bowl, whisk together eggs, ricotta, vanilla extract, lemon zest, and melted butter. Add cheese mixture to flour mixture and stir until smooth. (Batter will be very thick.)',
        )
    in118 = Instruction(
        recipe_id = 40,
        specification  = 'Transfer batter into prepared pan, smooth out the top with a spatula. Sprinkle with half of the prepared rosemary sugar and scatter half of the figs over top. Bake until a toothpick comes out clean, about 45 minutes. Let cool completely.',
        )
    in119 = Instruction(
        recipe_id = 40,
        specification  = 'As the cake is cooling, combine remaining 2 teaspoons granulated sugar and heavy cream in the bowl of a stand mixer fitted with a whisk attachment. Whip on medium speed until cream is light and airy, about 45 seconds.',
        )
    in120 = Instruction(
        recipe_id = 40,
        specification  = 'Dollop whipped cream in the center of the cake and top with remaining figs and rosemary sugar.',
        )
    in121 = Instruction(
        recipe_id = 41,
        specification  = 'In a 2-cup liquid measuring cup (or other small, shatter-proof mixing bowl with tall sides), combine the softened butter, honey, cinnamon and salt.',
        )
    in122 = Instruction(
        recipe_id = 41,
        specification  = 'Using a hand mixer, whip the ingredients together until the butter is light and fluffy.',
        )
    in123 = Instruction(
        recipe_id = 41,
        specification  = 'Transfer the mixture to a small serving bowl. Lightly drizzle honey on top, followed by a little sprinkle of flaky salt or kosher salt.',
        )
    in124 = Instruction(
        recipe_id = 41,
        specification  = 'Serve promptly, or refrigerate for later (let the mixture come back to room temperature before serving). Leftovers keep well in the refrigerator, covered, for up to 5 days.',
        )
    in125 = Instruction(
        recipe_id = 42,
        specification  = 'Combine onion, celery, and 2 1/2 cups dashi in a small Dutch oven. Bring to a boil over medium-high. Reduce heat to medium-low, and simmer, uncovered, stirring occasionally, until vegetables are tender, 35 to 40 minutes.',
        )
    in126 = Instruction(
        recipe_id = 42,
        specification  = 'Add leftover mashed potatoes to dashi mixture, and whisk until well combined. Stir in milk, if desired, for a creamier texture. Stir in remaining 1 cup dashi, 1/4 cup at a time, to thin soup to desired consistency. Cook over medium-low, stirring occasionally, until warm, 4 to 6 minutes. Season with salt and pepper.',
        )
    in127 = Instruction(
        recipe_id = 42,
        specification  = 'Top servings with butter and drizzle with soy sauce. Garnish with mitsuba or celery leaves.Soup can be prepared up to 3 days in advance and stored in an airtight container in refrigerator. Reheat over low, stirring often to prevent simmering.',
        )
    in128 = Instruction(
        recipe_id = 43,
        specification  = 'Start by thinly slicing your silken tofu into small squares. Also cut your avocado in half. Thinly slice it crosswise so you get pieces similarly sized to the tofu slices. Arrange alternating slices of silken tofu and avocado on a serving platter.',
        )
    in129 = Instruction(
        recipe_id = 43,
        specification  = 'In a small bowl, combine the minced garlic and ginger, soy sauce, sesame oil, sugar, vinegar, white pepper, water, and salt to taste. Mix well to combine, and drizzle over the tofu and avocado.',
        )
    in130 = Instruction(
        recipe_id = 43,
        specification  = 'Garnish with chopped scallions and serve.',
        )
    in131 = Instruction(
        recipe_id = 44,
        specification  = 'Preheat oven to 400°F with 1 rack in middle position and 1 rack positioned 4 inches from broiler. Whisk together chopped herbs, 1/4 cup oil, 2 tablespoons capers, lemon zest and juice, black pepper, and 1/8 teaspoon crushed red pepper in a medium bowl until combined. Season with salt to taste; set aside.',
        )
    in132 = Instruction(
        recipe_id = 44,
        specification  = 'Process garlic, anchovies, remaining 2 tablespoons capers, and remaining 1/8 teaspoon crushed red pepper in a mini food processor until a coarse paste forms, about 10 seconds. Add remaining 2 tablespoons oil, and process until creamy and mostly smooth, about 40 seconds. (Alternatively, pound and mash garlic, anchovies, capers, and crushed red pepper using a mortar and pestle until a coarse paste forms, about 1 minute and 30 seconds. Add remaining 2 tablespoons oil, and continue to pound and mash until creamy and mostly smooth, about 2 minutes.',
        )
    in133 = Instruction(
        recipe_id = 44,
        specification  = 'Arrange lamb on a large baking sheet lined with parchment paper. Rub lamb evenly with garlic-caper paste. Roast in preheated oven on middle rack until a thermometer inserted in thickest portion of chops registers 110°F, 12 to 16 minutes. Remove lamb from oven; let rest until temperature stops rising and begins to fall, 5 to 10 minutes. Increase oven temperature to high broil; preheat 5 minutes. Return lamb to oven on top rack. Broil until lamb is golden and sizzling and a thermometer inserted in thickest portion of chops registers 120°F, 2 to 3 minutes. Remove from oven; transfer lamb to a cutting board, and let rest 5 minutes. Cut each lamb chop in half between ribs; serve with herb mixture and lemon wedges. Garnish with additional fresh herbs.',
        )
    in134 = Instruction(
        recipe_id = 45,
        specification  = 'Rinse the ribs and thoroughly pat them dry with paper towels. Mix the rest of the ingredients in a bowl to make the marinade.',
        )
    in135 = Instruction(
        recipe_id = 45,
        specification  = 'Reserve about ⅓ of the marinade, and rub the ribs with the rest of it. Allow the ribs to marinate for at least 2 hours. For best results, allow to marinate overnight.',
        )
    in136 = Instruction(
        recipe_id = 45,
        specification  = 'Preheat your oven to 400 degrees, and put the ribs on a rack resting on a baking sheet. Pour 1 cup water into the pan, and transfer to the oven. Roast for 30 minutes.',
        )
    in137 = Instruction(
        recipe_id = 45,
        specification  = 'Remove the ribs from the oven and baste with the marinade. Return to the oven and roast for another 30 minutes.',
        )
    in138 = Instruction(
        recipe_id = 45,
        specification  = 'Allow the ribs to rest for 5 minutes. Slice and serve!',
        )
    in139 = Instruction(
        recipe_id = 49,
        specification  = 'Start by making the crust. In a large mixing bowl, combine the flour, sugar, and salt. Cut in the butter with a pastry cutter or two knives until the mixture resembles coarse crumbs. Whisk together the egg yolk and water, and add it to the flour mixture. Mix everything together with a fork until the dough comes together. Flatten into a disk, cover tightly with plastic wrap, and place in the refrigerator to chill for at least an hour. Take out of the refrigerator about a few minutes before you’re ready to roll it out.',
        )
    in140 = Instruction(
        recipe_id = 49,
        specification  = 'Roll out the dough and fit it to your tart pan. You may have to patch it up a bit, but don’t worry, it’ll turn out great. Pierce the dough all over with a fork and place the tart shell in the freezer for 30 minutes.',
        )
    in141 = Instruction(
        recipe_id = 49,
        specification  = 'Meanwhile, melt 2 tablespoons of butter in a large skillet over medium heat. Add the chopped leeks and cook for about 10 minutes. Add the kale, crushed red pepper flakes, and a couple drizzles of olive oil. Season with salt and pepper to taste. Cook for another couple minutes, just until the kale is wilted. Remove from the heat.',
        )
    in142 = Instruction(
        recipe_id = 49,
        specification  = 'Preheat the oven to 375 degrees F (210 degrees C). Blind bake the tart shell for 10 minutes, and remove from the oven. If you see it starting to puff up at all, poke the dough with a fork again!',
        )
    in143 = Instruction(
        recipe_id = 49,
        specification  = 'Prep your potato by peeling it and slicing it paper-thin. A mandolin helps, but a sharp knife will do the job. Add the thyme and ricotta (or cream cheese) to the kale mixture. Place a layer of sweet potato slices in the bottom of the tart shell. Spread the kale and cheese mixture evenly over that, and top with another layer of sweet potato slices. Brush the top thoroughly with olive oil and sprinkle the cheese over the tart. Bake for about 20 minutes, until golden brown.',
        )
    in144 = Instruction(
        recipe_id = 46,
        specification  = 'Position a rack in the center of the oven and preheat to 375°F.',
        )
    in145 = Instruction(
        recipe_id = 46,
        specification  = 'Meanwhile, spread 1 tablespoon of the butter on both sides of each slice of bread.',
        )
    in146 = Instruction(
        recipe_id = 46,
        specification  = 'Heat a medium cast-iron skillet over medium-high heat until hot, then add the bread and cook, turning once, until evenly toasted and browned, 1–2 minutes per side. Transfer to a plate to cool slightly, then rub each slice all over with the cut side of the garlic clove. Discard any leftover garlic.',
        )
    in147 = Instruction(
        recipe_id = 46,
        specification  = 'To the empty skillet, add the cream and remaining butter and bring to a simmer over medium-low heat. Season to taste with salt and black pepper. Pour the liquid into a small bowl. To the empty skillet, add the bread slices 1 inch apart. Pour 2 tablespoons of the hot cream mixture over each slice.',
        )
    in148 = Instruction(
        recipe_id = 46,
        specification  = 'Gently crack 1 egg into a small bowl, making sure not to break the yolk. Tilt it onto one of the toast slices so that the yolk rests atop the bread. Repeat with the remaining eggs, topping each slice with 2 eggs. (It’s fine if the whites spill over the sides.) Pour the rest of the hot cream over the eggs and transfer the skillet to the oven. Bake until the whites are set and the yolks are cooked to your desired doneness, about 13 minutes for runny. Top with the chives and more black pepper, then serve immediately.',
        )
    in149 = Instruction(
        recipe_id = 47,
        specification  = "Crack 3 eggs in a liquid measuring cup and note the volume. Pour the eggs into a large bowl, add salt, and beat for at least 1 minute. Now measure out water at the same volume as the eggs, and add it to the bowl. Do the same with the broth. Whisk in the sesame oil, and make sure everything's well combined.",
        )
    in150 = Instruction(
        recipe_id = 47,
        specification  = 'Place 4 empty ramekins in a steamer over high heat. Be sure the water will not bubble and touch the ramekins during steaming. Once the water boils, turn the heat down to a slow simmer. Then, divide the egg mixture into the ramekins, pouring it through a fine mesh strainer.',
        )
    in151 = Instruction(
        recipe_id = 47,
        specification  = 'Cover the steamer, turn up the heat to high, and steam for 3 minutes. After 3 minutes have elapsed, shut off the heat but keep the steamer covered. Let stand for 14 minutes with the lid firmly covered. Remove from the steamer, sprinkle with scallions, and serve.',
        )
    in152 = Instruction(
        recipe_id = 48,
        specification  = 'Position a rack in the center of the oven and preheat to 500°F. Line a large rimmed baking sheet with parchment paper.',
        )
    in153 = Instruction(
        recipe_id = 48,
        specification  = 'In a small bowl, combine the oregano, thyme, salt, and black pepper. In a large bowl, toss the tomatoes, fennel, and garlic with ½ cup olive oil. Transfer the tomato mixture to the prepared baking sheet.',
        )
    in154 = Instruction(
        recipe_id = 48,
        specification  = 'Rinse the fish inside and out and pat dry with paper towels. Rub the remaining 2 tablespoons of olive oil over the exterior of the fish, then place a generous pinch of the herb seasoning into each cavity. Arrange the fish atop the tomato mixture, and sprinkle with the remaining seasoning. Cook until the vegetables are soft, 18–20 minutes. Pour the vermouth over the fish, then cook for 10 additional minutes. Garnish with parsley, and serve with crusty bread for ­sopping up the juices.',
        )
    in155 = Instruction(
        recipe_id = 50,
        specification  = 'In a bowl, whisk together the flour, instant yeast, sugar, parmesan, and salt. Add the warm milk, honey, 3 eggs, and yolk. Using a dough hook on a stand mixer, mix together at a low to medium speed until a shaggy dough forms. Mix the dough together for another minute or so until the dough is combined.',
        )
    in156 = Instruction(
        recipe_id = 50,
        specification  = "Split the butter into four portions. Add the first portion into the dough, and knead for about two minutes until fully incorporated. Scrape down the sides of the bowl, and add in the second portion. Continue this for the next few portions. The batter will resemble cake batter at this point. Increase the mixer speed to medium and knead for an additional 8-10 minutes, or until the dough is completely smooth and velvety. It'll come off the sides of the bowl cleanly when done.",
        )
    in157 = Instruction(
        recipe_id = 50,
        specification  = "Turn the dough out on to a lightly floured surface. Fold each side into the center and repeat 3 times. Flip the dough over and you'll have a smooth surface. Transfer the dough to a bowl for the first proofing. Cover the bowl and allow it to proof for about an hour, or until it doubles in size.",
        )
    in158 = Instruction(
        recipe_id = 50,
        specification  = "While the dough rests, toss together all the ingredients for Mom's Green Chutney into the blender, removing the water from the recipe, until a thick chutney forms.",
        )
    in159 = Instruction(
        recipe_id = 50,
        specification  = "Layer parchment paper in a 10-inch cast iron or spring form pan and butter it. Once the dough has risen, punch it down and turn out the dough onto a lightly floured surface. Roll the dough out into a 12 x 18 inches rectangle. Spread the chutney all over the dough, being sure to go all the way up to the edges. Top with shredded cheese.",
        )
    in160 = Instruction(
        recipe_id = 50,
        specification  = "Roll the edge of the dough into itself and continue rolling to form a log. Pinch the seals together. Cut the log into 8 rolls. Carefully transfer the rolls into the cast iron. Cover and let rise for another 1-2 hours. Check if the dough is done proofing by poking it. If it leaves an indentation, it's done. Preheat the oven to 450°F.",
        )
    in161 = Instruction(
        recipe_id = 50,
        specification  = "Brush the top of the rolls with a beaten egg. Bake for 25 minutes until the top begins to brown. Then, reduce the oven temperature to 350°F and bake for another 30-35 minutes until the internal temperature reaches 180°F. Sprinkle additional cheese on warm rolls and serve with additional chutney.",
        )
    in162 = Instruction(
        recipe_id = 51,
        specification  = 'Preheat the oven to 350°. Butter and flour a 10-by-5-inch metal loaf pan. In a bowl, using a fork, mash 4 of the bananas until chunky. In another bowl, whisk the flour, baking soda, baking powder and salt.',
        )
    in163 = Instruction(
        recipe_id = 51,
        specification  = "Using a stand mixer fitted with the paddle, cream the butter, sugar and miso at medium speed until fluffy, about 5 minutes. At low speed, slowly add the buttermilk, then beat in the eggs 1 at a time until incorporated. Beat in the mashed bananas; the batter will look curdled. Add the dry ingredients and mix until just blended. Scrape into the prepared pan.",
        )
    in164 = Instruction(
        recipe_id = 51,
        specification  = 'Slice the remaining banana lengthwise and arrange the halves on top of the batter side by side, cut side up. Bake for 90 minutes, or until a toothpick inserted in the center comes out clean. Let the bread cool on a rack for 30 minutes before turning out to cool completely. The banana bread can be wrapped in plastic and kept at room temperature for up to 3 days.',
        )
    in165 = Instruction(
        recipe_id = 52,
        specification  = 'Preheat the oven to 250°F. Line 2 large rimmed baking sheets with parchment paper and set aside.',
        )
    in166 = Instruction(
        recipe_id = 52,
        specification  = 'In the bowl of a stand-mixer fitted with a whip attachment, beat the egg whites on high speed just to medium-stiff peaks, about 2 minutes. With the mixer still running, gradually add ⅓ cup plus 1 tablespoon superfine sugar, and continue beating on high speed until the meringue is smooth and glossy, about 1 minute more. Turn the mixer off and remove the whip attachment. Sift the confectioners’ sugar and potato starch over the meringue and use a silicone spatula to gently fold together. Fill a piping bag or a large, zip-top freezer bag with the meringue, cut off the tip, then pipe 2-inch circles onto the lined baking sheet, leaving at least 2 inches between each circle.Transfer to the oven and bake until puffed and slightly golden, about 35 minutes. Set aside to cool to room temperature.',
        )
    in167 = Instruction(
        recipe_id = 52,
        specification  = 'Meanwhile, in a medium bowl, whisk together the cream and the remaining ⅔ cup superfine sugar to soft peaks. Add the yogurt and whisk just to combine.',
        )
    in168 = Instruction(
        recipe_id = 52,
        specification  = 'Immediately before serving, break or slice 8 meringues in half, reserving the rest in an airtight container for another use. Divide the pieces among 8 dessert plates; add a generous dollop of yogurt cream in the center of each plate, top with some of the kiwi and a few sprigs of fresh dill, drizzle with olive oil, and serve.',
        )
    in169 = Instruction(
        recipe_id = 53,
        specification  = 'Preheat the oven to 300°. Line a large rimmed baking sheet with parchment paper. In a large bowl, toss the tomatoes with the olive oil, honey, thyme leaves, salt and pepper. Scrape the tomatoes onto the prepared baking sheet and turn them cut side up. Bake the tomatoes for about 1 hour and 25 minutes, until they begin to shrivel and brown. Let cool.',
        )
    in170 = Instruction(
        recipe_id = 53,
        specification  = 'Preheat the broiler. Spread out the baguette slices on a baking sheet. Broil for about 30 seconds on each side, until the edges are golden brown.',
        )
    in171 = Instruction(
        recipe_id = 53,
        specification  = 'Spread the ricotta over the baguette slices and top with the slow-roasted tomatoes. Lightly drizzle the tomatoes with the buckwheat honey, sprinkle with the sliced basil and serve with additional buckwheat honey on the side.The roasted tomatoes can be refrigerated for up to 2 days. Bring to room temperature before serving.',
        )
    in172 = Instruction(
        recipe_id = 54,
        specification  = 'In a medium skillet over medium heat, warm the oil. Cook the shallots, stirring occasionally, for 4 to 5 minutes, until softened and translucent. Add the salt and pepper and reduce the heat to low. Continue to cook, stirring occasionally, for 20 to 25 minutes, until the shallots have begun to brown. Stir in the vinegar and let cool completely.',
        )
    in173 = Instruction(
        recipe_id = 54,
        specification  = 'On a lightly floured surface, roll out the dough to a rectangle about 20x20 inches/50x50 centimeters, slightly thicker than ¼ inch/6 millimeters. If the dough feels soft at this point, use the rolling pin to unfurl onto a parchment-lined baking sheet and chill before proceeding.',
        )
    in174 = Instruction(
        recipe_id = 54,
        specification  = 'Using a pastry wheel, bench scraper, or sharp knife, divide the dough into 8 pieces and form into squares (each about 5x5 inches/13x13 centimeters). Divide the shallots evenly among the dough, spreading in an even layer in the center.',
        )
    in175 = Instruction(
        recipe_id = 54,
        specification  = 'Divide the asparagus into 8 even portions. Divide the Brie into 8 even portions, each about 1½ ounces (43 grams). Line a baking sheet with parchment paper.',
        )
    in176 = Instruction(
        recipe_id = 54,
        specification  = 'Working with one piece of dough at a time, place on the prepared baking sheet. Arrange one portion of asparagus in a bundle in the center, then place one portion of Brie on top. Fold one of the points inward toward the center of the square. Brush the exposed dough with the egg wash, then fold the opposite corner in, pressing on the dough to seal. Brush any remaining exposed dough with the egg wash. Sprinkle the dough generously with the sesame seeds. Repeat with the remaining pieces of dough, asparagus, and Brie. Refrigerate for at least 15 minutes or up to 1 hour.',
        )
    in177 = Instruction(
        recipe_id = 54,
        specification  = "Toward the end of the chill time, arrange a rack in the lower third of the oven, preferably with a baking steel or stone on it; heat the oven to 425°F/218°C.",
        )
    in178 = Instruction(
        recipe_id = 54,
        specification  = 'Bake the pies (on the steel/stone, if using) for 30 to 35 minutes, until the crust is deeply golden brown and the asparagus is tender. Let cool for at least 5 minutes before serving warm (they are also delicious at room temperature).',
        )
    in179 = Instruction(
        recipe_id = 55,
        specification  = 'Heat the oven to 425°F. Line a half-sheet pan with aluminum foil and set an oven-safe wire rack on top. In a large nonstick pan over medium-high heat, toast the panko breadcrumbs with 2 tablespoons of olive oil until the crumbs turn golden brown, about 10 minutes. Pour the panko into a large shallow bowl and set aside to cool for a few minutes.',
        )
    in180 = Instruction(
        recipe_id = 55,
        specification  = 'In a large bowl, toss the sweet potato wedges with the olive oil, salt, and pepper. Spread the sweet potatoes on the wire rack making sure to lay the wedges flat, then place the sheet pan in the oven and cook for 20 minutes.',
        )
    in181 = Instruction(
        recipe_id = 55,
        specification  = 'While the sweet potatoes are baking, prepare the fish. Add the chopped herbs, ¼ teaspoon salt, and several cranks of freshly ground black pepper to the bowl of browned panko and mix to combine. Pour the cornmeal into a second shallow dish. Crack the eggs into a third shallow dish and whisk with a fork until well combined.',
        )
    in182 = Instruction(
        recipe_id = 55,
        specification  = 'Lay the fillets on a large plate lined with parchment (if they’re wet, pat the fillets dry with a paper towel). Generously season both sides with salt and pepper. Working with one fillet at a time, lightly coat the fish in the cornmeal, followed by the egg mixture, then thoroughly dredge in the herbed panko breadcrumbs, making sure each fillet is fully coated',
        )
    in183 = Instruction(
        recipe_id = 55,
        specification  = 'Once the sweet potatoes have cooked for 20 minutes, remove from the oven and give them a toss with a wooden spoon or spatula, then push them to one side of the pan to make room for the fish. Carefully transfer the breaded fillets to the rack on the pan and return to the oven. Cook for 10 to 12 minutes.',
        )
    in184 = Instruction(
        recipe_id = 55,
        specification  = 'While the fish and sweet potatoes cook, make the dipping sauce. In a small bowl, add the mayo, paprika, honey, soy sauce, Sriracha, vinegar, a few pinches of salt, and several cranks of black pepper and mix to combine. Taste and adjust the seasoning, if needed.',
        )
    in185 = Instruction(
        recipe_id = 55,
        specification  = 'After 10 to 12 minutes have passed, remove the baking sheet from the oven and check for doneness: the sweet potatoes should be soft enough to pierce and the Alaska cod should flake when poked with a fork. To finish, return the pan to the oven and broil on high for 1 to 2 minutes, until the sweet potatoes are lightly charred and the tops of the fish are golden brown. Sprinkle the fish with fresh parsley and/or dill and serve with the creamy paprika dip on the side.',
        )
    in186 = Instruction(
        recipe_id = 56,
        specification  = 'Add the strawberries to a bowl and sprinkle with a pinch each of salt and pepper. Toss, then let hang out while you work on the rest of the sandwich',
        )
    in187 = Instruction(
        recipe_id = 56,
        specification  = 'Add the bacon to a cast-iron skillet and set over medium heat. Cook, shuffling around and flipping until crisp, 6 to 8 minutes.',
        )
    in188 = Instruction(
        recipe_id = 56,
        specification  = 'Use tongs to transfer the bacon to a plate, then immediately add the bread to the pan. Cook for 1 to 2 minutes per side, lowering the heat if needed, until the bread is toasty and golden-brown. Transfer the bread to a plate and let cool for a couple minutes.',
        )
    in189 = Instruction(
        recipe_id = 56,
        specification  = 'Spread each slice of bread with mayo, then build the sandwich in this order: strawberries, bacon, lettuce. Slice in half and eat immediately.',
        )
    in190 = Instruction(
        recipe_id = 57,
        specification  = 'Preheat the oven to 200° F (100° C). Line a baking sheet with lightly greased parchment paper or a Silicone baking mat.',
        )
    in191 = Instruction(
        recipe_id = 57,
        specification  = 'In a blender or food processor, combine raspberries, honey, and lemon juice. Purée until smooth.',
        )
    in192 = Instruction(
        recipe_id = 57,
        specification  = 'You could pour this purée straight onto your baking sheet and pop it into the oven, but the cooking time would take about 8 hours. For a quicker cook time, it helps to reduce the purée on the stovetop.',
        )
    in193 = Instruction(
        recipe_id = 57,
        specification  = 'Pour purée through a sieve and into a medium-sized saucepan. Use a ladle to push the purée through the sieve if necessary. Bring the mixture to a boil over medium-high heat. Reduce heat to low and simmer, stirring often, until the mixture has thickened, about 20 to 30 minutes.',
        )
    in194 = Instruction(
        recipe_id = 57,
        specification  = 'Spread the mixture onto the prepared baking sheet. Use an off-set spatula to spread the mixture into a thin even layer. It is important to have an even layer as thicker spots will take longer to cook.',
        )
    in195 = Instruction(
        recipe_id = 57,
        specification  = 'Place in the oven and bake until the Fruit Roll-Up is no longer sticky to the touch—this will take anywhere between 2 1/2 to 3 hours. The mixture will still be slightly tacky to the touch but no longer wet. Turn the oven off and leave the sheet in the oven to cool completely.',
        )
    in196 = Instruction(
        recipe_id = 57,
        specification  = 'Remove the baking sheet from the oven and invert the roll-up onto a piece of parchment paper. Peel the fruit layer from the baking mat and cut it into long strips. Roll up using parchment paper.',
        )
    in197 = Instruction(
        recipe_id = 58,        specification  = 'Heat the broiler on high. Combine butter, uni, lemon zest and juice, oregano, red-pepper flakes, smoked paprika, garlic, and salt in a medium bowl. Using an electric mixer, beat the butter mixture until well combined. Set aside.',
        )
    in198 = Instruction(
        recipe_id = 58,
        specification  = "Spread rock salt on a rimmed baking sheet. Carefully nestle opened oysters in salt so they remain upright. Top each oyster with 1 tablespoon uni butter; broil until butter melts and browns on edges, 3 to 5 minutes. Serve immediately with lemon wedges.",
        )
    in199 = Instruction(
        recipe_id = 59,
        specification  = 'In a medium skillet over medium-low heat, warm the oil. Cook the onion, stir­ring often, for about 45 minutes, until light brown. Meanwhile, slice the pota­toes as thinly as pos­si­ble (use a man­do­line if avail­able).',
        )
    in200 = Instruction(
        recipe_id = 59,
        specification  = 'Heat the oven to 300°F. In medium saucepan over medium heat, bring the cream, gar­lic, pep­per­corns, thyme, and salt to just under a boil. Reduce the heat to low, cover, and sim­mer for 15 min­utes. Remove from the heat; set aside.',
        )
    in201 = Instruction(
        recipe_id = 59,
        specification  = 'Layer one-quarter of the pota­toes in greased 12x8-inch glass bak­ing or casse­role dish; top with one-third of the onion and one-quarter of the cheese. Repeat twice. Top with the remain­ing pota­toes. Strain the reserved cream mix­ture over the pota­toes, shak­ing the pan to dis­trib­ute evenly. Sprin­kle with the remain­ing cheese.',
        )
    in202 = Instruction(
        recipe_id = 59,
        specification  = 'Place the pan on a baking sheet (to catch drips) and bake for 1½ to 2 hours, until ten­der and a knife inserted into the dish pierces the pota­toes eas­ily. The casserole can be made 2 days ahead. Cover and refrigerate. Reheat, tented with foil, in a 375°F oven for 30 minutes.  For a lighter ver­sion, steep the gar­lic, pep­per­corns, thyme, and salt in 2 cups (500 milliliters) milk. Then make the béchamel sauce: Melt 2 tablespoons but­ter over medium-low heat. Add 2 tablespoons all-purpose flour. Cook, stir­ring, for 1 minute. Whisk in the strained milk mix­ture and sim­mer for 5 min­utes, until slightly thickened. Pour over the pota­toes.',
        )
    in203 = Instruction(
        recipe_id = 60,
        specification  = 'Preheat oven to 375℉. Line a rimmed baking sheet with parchment paper, and lightly spray with cooking spray. Set aside.',
        )
    in204 = Instruction(
        recipe_id = 60,
        specification  = 'Place egg white, salt, 1/4 cup of the brown sugar, 1 teaspoon of the orange zest, and 1/4 teaspoon of the cinnamon in a medium bowl; whisk to combine well. Add pecan halves, stirring to evenly coat pecans in egg white mixture. Scoop pecans from bowl, allowing excess egg white mixture to drip off; spread in an even layer on parchment-lined baking sheet. Bake in preheated oven until pecans are lightly browned, 12 to 14 minutes, stirring halfway through baking time. Set aside, and let cool, about 20 minutes. (Pecans will not be completely crisp but will continue to crisp as they cool.)',
        )
    in205 = Instruction(
        recipe_id = 60,
        specification  = 'While pecans cool, place butter, vanilla bean paste, and remaining 1/4 cup brown sugar, 2 teaspoons orange zest, and 1/2 teaspoon cinnamon in a 10-inch cast-iron skillet over medium-high; whisk constantly until butter is melted and fully incorporated into sugar and mixture is smooth. Cook, whisking constantly, until thickened slightly, 1 to 2 minutes. Remove skillet from heat; add rum, and whisk until alcohol evaporates, about 1 minute. Place skillet over medium-high heat; add bananas, cut sides down, and cook until slightly softened and lightly browned, about 1 minute. Gently turn bananas, and cook 30 seconds; remove skillet from heat.',
        )
    in206 = Instruction(
        recipe_id = 60,
        specification  = 'Place scoops of ice cream directly into skillet; top with 1/2 cup crispy pecans and flaky sea salt. Garnish with additional orange zest (if using); serve immediately.',
        )
    # in = Instruction(
    #     recipe_id = ,
    #     #     specification  = '',
    #     )

    db.session.add(in1)
    db.session.add(in2)
    db.session.add(in3)
    db.session.add(in4)
    db.session.add(in5)
    db.session.add(in6)
    db.session.add(in7)
    db.session.add(in8)
    db.session.add(in9)
    db.session.add(in10)
    db.session.add(in11)
    db.session.add(in12)
    db.session.add(in13)
    db.session.add(in14)
    db.session.add(in15)
    db.session.add(in16)
    db.session.add(in17)
    db.session.add(in18)
    db.session.add(in19)
    db.session.add(in20)
    db.session.add(in21)
    db.session.add(in22)
    db.session.add(in23)
    db.session.add(in24)
    db.session.add(in25)
    db.session.add(in26)
    db.session.add(in27)
    db.session.add(in28)
    db.session.add(in29)
    db.session.add(in30)
    db.session.add(in31)
    db.session.add(in32)
    db.session.add(in33)
    db.session.add(in34)
    db.session.add(in35)
    db.session.add(in36)
    db.session.add(in37)
    db.session.add(in38)
    db.session.add(in39)
    db.session.add(in40)
    db.session.add(in41)
    db.session.add(in42)
    db.session.add(in43)
    db.session.add(in44)
    db.session.add(in45)
    db.session.add(in46)
    db.session.add(in47)
    db.session.add(in48)
    db.session.add(in49)
    db.session.add(in50)
    db.session.add(in51)
    db.session.add(in52)
    db.session.add(in53)
    db.session.add(in54)
    db.session.add(in55)
    db.session.add(in56)
    db.session.add(in57)
    db.session.add(in58)
    db.session.add(in59)
    db.session.add(in60)
    db.session.add(in61)
    db.session.add(in62)
    db.session.add(in63)
    db.session.add(in64)
    db.session.add(in65)
    db.session.add(in66)
    db.session.add(in67)
    db.session.add(in68)
    db.session.add(in69)
    db.session.add(in70)
    db.session.add(in71)
    db.session.add(in72)
    db.session.add(in73)
    db.session.add(in74)
    db.session.add(in75)
    db.session.add(in76)
    db.session.add(in77)
    db.session.add(in78)
    db.session.add(in79)
    db.session.add(in80)
    db.session.add(in81)
    db.session.add(in82)
    db.session.add(in83)
    db.session.add(in84)
    db.session.add(in85)
    db.session.add(in86)
    db.session.add(in87)
    db.session.add(in88)
    db.session.add(in89)
    db.session.add(in90)
    db.session.add(in91)
    db.session.add(in92)
    db.session.add(in93)
    db.session.add(in94)
    db.session.add(in95)
    db.session.add(in96)
    db.session.add(in97)
    db.session.add(in98)
    db.session.add(in99)
    db.session.add(in100)
    db.session.add(in101)
    db.session.add(in102)
    db.session.add(in103)
    db.session.add(in104)
    db.session.add(in105)
    db.session.add(in106)
    db.session.add(in107)
    db.session.add(in108)
    db.session.add(in109)
    db.session.add(in110)
    db.session.add(in111)
    db.session.add(in112)
    db.session.add(in113)
    db.session.add(in114)
    db.session.add(in115)
    db.session.add(in116)
    db.session.add(in117)
    db.session.add(in118)
    db.session.add(in119)
    db.session.add(in120)
    db.session.add(in121)
    db.session.add(in122)
    db.session.add(in123)
    db.session.add(in124)
    db.session.add(in125)
    db.session.add(in126)
    db.session.add(in127)
    db.session.add(in128)
    db.session.add(in129)
    db.session.add(in130)
    db.session.add(in131)
    db.session.add(in132)
    db.session.add(in133)
    db.session.add(in134)
    db.session.add(in135)
    db.session.add(in136)
    db.session.add(in137)
    db.session.add(in138)
    db.session.add(in139)
    db.session.add(in140)
    db.session.add(in141)
    db.session.add(in142)
    db.session.add(in143)
    db.session.add(in144)
    db.session.add(in145)
    db.session.add(in146)
    db.session.add(in147)
    db.session.add(in148)
    db.session.add(in149)
    db.session.add(in150)
    db.session.add(in151)
    db.session.add(in152)
    db.session.add(in153)
    db.session.add(in154)
    db.session.add(in155)
    db.session.add(in156)
    db.session.add(in157)
    db.session.add(in158)
    db.session.add(in159)
    db.session.add(in160)
    db.session.add(in161)
    db.session.add(in162)
    db.session.add(in163)
    db.session.add(in164)
    db.session.add(in165)
    db.session.add(in166)
    db.session.add(in167)
    db.session.add(in168)
    db.session.add(in169)
    db.session.add(in170)
    db.session.add(in171)
    db.session.add(in172)
    db.session.add(in173)
    db.session.add(in174)
    db.session.add(in175)
    db.session.add(in176)
    db.session.add(in177)
    db.session.add(in178)
    db.session.add(in179)
    db.session.add(in180)
    db.session.add(in181)
    db.session.add(in182)
    db.session.add(in183)
    db.session.add(in184)
    db.session.add(in185)
    db.session.add(in186)
    db.session.add(in187)
    db.session.add(in188)
    db.session.add(in189)
    db.session.add(in190)
    db.session.add(in191)
    db.session.add(in192)
    db.session.add(in193)
    db.session.add(in194)
    db.session.add(in195)
    db.session.add(in196)
    db.session.add(in197)
    db.session.add(in198)
    db.session.add(in199)
    db.session.add(in200)
    db.session.add(in201)
    db.session.add(in202)
    db.session.add(in203)
    db.session.add(in204)
    db.session.add(in205)
    db.session.add(in206)

    db.session.commit()

# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_instructions():
    db.session.execute('TRUNCATE instructions RESTART IDENTITY CASCADE;')
    db.session.commit()
