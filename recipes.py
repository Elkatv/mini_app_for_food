import pandas as pd
from random import randint

import joblib

class Main_class:
    def open_df(self):
        df = pd.read_csv("data/epi_r.csv", usecols=['title', 'almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot', 'artichoke', 'arugula', 'asian pear', 'asparagus', 'avocado', 'bacon', 'banana', 'barley', 'basil', 'bass', 'bean', 'beef', 'beef rib', 'beef shank', 'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry', 'biscuit', 'blackberry', 'blue cheese', 'blueberry', 'bok choy', 'bourbon', 'bran', 'brandy', 'bread', 'breadcrumbs', 'breakfast', 'brie', 'brine', 'brisket', 'broccoli', 'broccoli rabe', 'brown rice', 'brussel sprout', 'buffalo', 'bulgur', 'butter', 'buttermilk', 'butternut squash', 'butterscotch/caramel', 'cabbage', 'calvados', 'campari', 'candy', 'cantaloupe', 'capers', 'caraway', 'cardamom', 'carrot', 'cashew', 'cauliflower', 'caviar', 'celery', 'chambord', 'champagne', 'chard', 'chartreuse', 'cheddar', 'cherry', 'chestnut', 'chicken', 'chickpea', 'chile', 'chile pepper', 'chive', 'chocolate', 'cilantro', 'cinnamon', 'citrus', 'clam', 'clove', 'coconut', 'cod', 'coffee', 'cognac/armagnac', 'collard greens', 'coriander', 'corn', 'cornmeal', 'cottage cheese', 'couscous', 'crab', 'cranberry', 'cream cheese', 'créme de cacao', 'crêpe', 'cr��me de cacao', 'cuba', 'cucumber', 'cumin', 'currant', 'curry', 'custard', 'date', 'dill', 'dried fruit', 'duck', 'eau de vie', 'egg', 'egg nog', 'eggplant', 'endive', 'escarole', 'fennel', 'feta', 'fig', 'fish', 'fontina', 'fortified wine', 'frangelico', 'fruit', 'fruit juice', 'garlic', 'gin', 'ginger', 'goat cheese', 'goose', 'gouda', 'grand marnier', 'granola', 'grape', 'grapefruit', 'grappa', 'green bean', 'green onion/scallion', 'ground beef', 'ground lamb', 'guam', 'guava', 'haiti', 'halibut', 'ham', 'hazelnut', 'herb', 'hominy/cornmeal/masa', 'honey', 'honeydew', 'horseradish', 'hot drink', 'hot pepper', 'hummus', 'iced coffee', 'iced tea', 'jalapeño', 'jerusalem artichoke', 'jícama', 'kahlúa', 'kale', 'kirsch', 'kiwi', 'kumquat', 'lamb', 'lamb chop', 'lamb shank', 'leafy green', 'leek', 'legume', 'lemon', 'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lime', 'lime juice', 'lingonberry', 'liqueur', 'lobster', 'lychee', 'macadamia nut', 'mango', 'maple syrup', 'margarita', 'marsala', 'marscarpone', 'marshmallow', 'martini', 'mayonnaise', 'melon', 'mezcal', 'midori', 'milk/cream', 'mint', 'molasses', 'monterey jack', 'mortar and pestle', 'mozzarella', 'mushroom', 'mussel', 'mustard', 'mustard greens', 'nectarine', 'noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus', 'okra', 'olive', 'onion', 'orange', 'oregano', 'orzo', 'oyster', 'papaya', 'paprika', 'parmesan', 'parsley', 'parsnip', 'passion fruit', 'pea', 'peach', 'peanut', 'peanut butter', 'pear', 'pecan', 'pepper', 'pernod', 'persimmon', 'phyllo/puff pastry dough', 'pine nut', 'pineapple', 'pistachio', 'plantain', 'plum', 'poach', 'poblano', 'pomegranate', 'pomegranate juice', 'poppy', 'pork', 'pork chop', 'pork rib', 'pork tenderloin', 'port', 'potato', 'prosciutto', 'prune', 'pumpkin', 'quail', 'quince', 'quinoa', 'rabbit', 'rack of lamb', 'radicchio', 'radish', 'raisin', 'raspberry', 'red wine', 'rhubarb', 'rice', 'ricotta', 'root vegetable', 'rosemary', 'rosé', 'rum', 'rutabaga', 'rye', 'saffron', 'sage', 'sake', 'salmon', 'sangria', 'sardine', 'scallop', 'seed', 'semolina', 'sesame', 'sesame oil', 'shallot', 'sherry', 'shrimp', 'snapper', 'sour cream', 'sourdough', 'soy', 'soy sauce', 'sparkling wine', 'spice', 'spinach', 'squash', 'squid', 'strawberry', 'sugar snap pea', 'sweet potato/yam', 'swiss cheese', 'swordfish', 'tamarind', 'tangerine', 'tapioca', 'tarragon', 'tea', 'tequila', 'thyme', 'tilapia', 'tomatillo', 'tomato', 'tortillas', 'tree nut', 'tree nut free', 'triple sec', 'tropical fruit', 'trout', 'tuna', 'turnip', 'vanilla', 'veal', 'venison', 'vermouth', 'vinegar', 'vodka', 'walnut', 'wasabi', 'watercress', 'watermelon', 'white wine', 'wild rice', 'windsor', 'yellow squash', 'yogurt', 'yuca', 'zucchini'])
        df.drop(columns='title', inplace=True)

        return df
    
    def name_in_name(self, name1, name2):
        name1 = name1.lower()
        name2 = name2.lower()

        if name1 == name2:
            return True
        elif f"{name1}/" in name2 or f"/{name1}" in name2:
            return True
        else:
            return False

    def preproc_data(self, product_list):
        all_product = ['almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot', 'artichoke', 'arugula', 'asian pear', 'asparagus', 'avocado', 'bacon', 'banana', 'barley', 'basil', 'bass', 'bean', 'beef', 'beef rib', 'beef shank', 'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry', 'biscuit', 'blackberry', 'blue cheese', 'blueberry', 'bok choy', 'bourbon', 'bran', 'brandy', 'bread', 'breadcrumbs', 'breakfast', 'brie', 'brine', 'brisket', 'broccoli', 'broccoli rabe', 'brown rice', 'brussel sprout', 'buffalo', 'bulgur', 'butter', 'buttermilk', 'butternut squash', 'butterscotch/caramel', 'cabbage', 'calvados', 'campari', 'candy', 'cantaloupe', 'capers', 'caraway', 'cardamom', 'carrot', 'cashew', 'cauliflower', 'caviar', 'celery', 'chambord', 'champagne', 'chard', 'chartreuse', 'cheddar', 'cherry', 'chestnut', 'chicken', 'chickpea', 'chile', 'chile pepper', 'chive', 'chocolate', 'cilantro', 'cinnamon', 'citrus', 'clam', 'clove', 'coconut', 'cod', 'coffee', 'cognac/armagnac', 'collard greens', 'coriander', 'corn', 'cornmeal', 'cottage cheese', 'couscous', 'crab', 'cranberry', 'cream cheese', 'créme de cacao', 'crêpe', 'cr��me de cacao', 'cuba', 'cucumber', 'cumin', 'currant', 'curry', 'custard', 'date', 'dill', 'dried fruit', 'duck', 'eau de vie', 'egg', 'egg nog', 'eggplant', 'endive', 'escarole', 'fennel', 'feta', 'fig', 'fish', 'fontina', 'fortified wine', 'frangelico', 'fruit', 'fruit juice', 'garlic', 'gin', 'ginger', 'goat cheese', 'goose', 'gouda', 'grand marnier', 'granola', 'grape', 'grapefruit', 'grappa', 'green bean', 'green onion/scallion', 'ground beef', 'ground lamb', 'guam', 'guava', 'haiti', 'halibut', 'ham', 'hazelnut', 'herb', 'hominy/cornmeal/masa', 'honey', 'honeydew', 'horseradish', 'hot drink', 'hot pepper', 'hummus', 'iced coffee', 'iced tea', 'jalapeño', 'jerusalem artichoke', 'jícama', 'kahlúa', 'kale', 'kirsch', 'kiwi', 'kumquat', 'lamb', 'lamb chop', 'lamb shank', 'leafy green', 'leek', 'legume', 'lemon', 'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lime', 'lime juice', 'lingonberry', 'liqueur', 'lobster', 'lychee', 'macadamia nut', 'mango', 'maple syrup', 'margarita', 'marsala', 'marscarpone', 'marshmallow', 'martini', 'mayonnaise', 'melon', 'mezcal', 'midori', 'milk/cream', 'mint', 'molasses', 'monterey jack', 'mortar and pestle', 'mozzarella', 'mushroom', 'mussel', 'mustard', 'mustard greens', 'nectarine', 'noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus', 'okra', 'olive', 'onion', 'orange', 'oregano', 'orzo', 'oyster', 'papaya', 'paprika', 'parmesan', 'parsley', 'parsnip', 'passion fruit', 'pea', 'peach', 'peanut', 'peanut butter', 'pear', 'pecan', 'pepper', 'pernod', 'persimmon', 'phyllo/puff pastry dough', 'pine nut', 'pineapple', 'pistachio', 'plantain', 'plum', 'poach', 'poblano', 'pomegranate', 'pomegranate juice', 'poppy', 'pork', 'pork chop', 'pork rib', 'pork tenderloin', 'port', 'potato', 'prosciutto', 'prune', 'pumpkin', 'quail', 'quince', 'quinoa', 'rabbit', 'rack of lamb', 'radicchio', 'radish', 'raisin', 'raspberry', 'red wine', 'rhubarb', 'rice', 'ricotta', 'root vegetable', 'rosemary', 'rosé', 'rum', 'rutabaga', 'rye', 'saffron', 'sage', 'sake', 'salmon', 'sangria', 'sardine', 'scallop', 'seed', 'semolina', 'sesame', 'sesame oil', 'shallot', 'sherry', 'shrimp', 'snapper', 'sour cream', 'sourdough', 'soy', 'soy sauce', 'sparkling wine', 'spice', 'spinach', 'squash', 'squid', 'strawberry', 'sugar snap pea', 'sweet potato/yam', 'swiss cheese', 'swordfish', 'tamarind', 'tangerine', 'tapioca', 'tarragon', 'tea', 'tequila', 'thyme', 'tilapia', 'tomatillo', 'tomato', 'tortillas', 'tree nut', 'tree nut free', 'triple sec', 'tropical fruit', 'trout', 'tuna', 'turnip', 'vanilla', 'veal', 'venison', 'vermouth', 'vinegar', 'vodka', 'walnut', 'wasabi', 'watercress', 'watermelon', 'white wine', 'wild rice', 'windsor', 'yellow squash', 'yogurt', 'yuca', 'zucchini']

        product_list = list(set(product_list))

        product_dict = dict()

        for i in all_product:
            flag = False
            for j in product_list:
                if self.name_in_name(j, i):
                    flag = True

            if flag:
                product_dict[i] = [1]
            else:
                product_dict[i] = [0]

        data = pd.DataFrame(product_dict)


        return data

    def rating(self, product_list):
        df = self.preproc_data(product_list)

        model = joblib.load('model.joblib')

        y_pred = model.predict(df)[0]

        if y_pred == 0:
            print("Bad idea")
        elif y_pred == 1:
            print("So-so")
        elif y_pred == 2:
            print("!!!GREAT!!!")

    def similar_reciept(self, product_list):
        # recipt = self.preproc_data(product_list).iloc[0]
        # print(recipt.sum())
        # recipt = set(recipt[recipt == 1].index.to_list())
        # print(product_list)
        recipt = set(product_list)
        # print(recipt)

        df = self.open_df()

        id_list = [0, 0, 0]
        k_list = [0, 0, 0]
        min_k = 0

        for i in range(len(df)):
            row = df.iloc[i]
            row = set(row[row == 1].index.to_list())
            l = len(row | recipt)
            k = len(row & recipt) / l if l != 0 else 0

            if k > min_k:
                idx = k_list.index(min(k_list))
                k_list[idx] = k
                id_list[idx] = i
                min_k = min(k_list)

        df = pd.read_csv("data/epi_r.csv", usecols=['title', 'rating', 'url'])

        for i in id_list:
            dihes = df.iloc[i]
            print(f'- {dihes['title'].strip()}, rating: {dihes['rating']}, URL: {dihes['url']}' )

        # print(id_list)
        # print(k_list)

    def beatiful_output(self, name, product):
        print(name)
        for i in ["fat","carbohydrat","protein","Fe","Mg","Na","K","Ca","Zn","Se","Cu","C","D","B12","E","A"]:
            print(f"{i.capitalize()} - {product[i]}% of Daily Value")

    def nutrientions_fact(self, product_list):
        df = pd.read_csv("data/nutrition_with_percents.csv")
        df.set_index('name', inplace=True)

        for i in list(df.index.to_list()):
            if i in product_list:
                # print(type(df.loc[i]))
                self.beatiful_output(i, df.loc[i])

                product_list.remove(i)

        if len(product_list) != 0:
            for i in product_list:
                print(f"{i} not in our database")

class Dayly_menu():
    def open_df(self):
        df = pd.read_csv("data/epi_r.csv", usecols=['rating', 'url', 'breakfast', 'dinner', 'lunch', 'title', 'almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot', 'artichoke', 'arugula', 'asian pear', 'asparagus', 'avocado', 'bacon', 'banana', 'barley', 'basil', 'bass', 'bean', 'beef', 'beef rib', 'beef shank', 'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry', 'biscuit', 'blackberry', 'blue cheese', 'blueberry', 'bok choy', 'bourbon', 'bran', 'brandy', 'bread', 'breadcrumbs', 'breakfast', 'brie', 'brine', 'brisket', 'broccoli', 'broccoli rabe', 'brown rice', 'brussel sprout', 'buffalo', 'bulgur', 'butter', 'buttermilk', 'butternut squash', 'butterscotch/caramel', 'cabbage', 'calvados', 'campari', 'candy', 'cantaloupe', 'capers', 'caraway', 'cardamom', 'carrot', 'cashew', 'cauliflower', 'caviar', 'celery', 'chambord', 'champagne', 'chard', 'chartreuse', 'cheddar', 'cherry', 'chestnut', 'chicken', 'chickpea', 'chile', 'chile pepper', 'chive', 'chocolate', 'cilantro', 'cinnamon', 'citrus', 'clam', 'clove', 'coconut', 'cod', 'coffee', 'cognac/armagnac', 'collard greens', 'coriander', 'corn', 'cornmeal', 'cottage cheese', 'couscous', 'crab', 'cranberry', 'cream cheese', 'créme de cacao', 'crêpe', 'cr��me de cacao', 'cuba', 'cucumber', 'cumin', 'currant', 'curry', 'custard', 'date', 'dill', 'dried fruit', 'duck', 'eau de vie', 'egg', 'egg nog', 'eggplant', 'endive', 'escarole', 'fennel', 'feta', 'fig', 'fish', 'fontina', 'fortified wine', 'frangelico', 'fruit', 'fruit juice', 'garlic', 'gin', 'ginger', 'goat cheese', 'goose', 'gouda', 'grand marnier', 'granola', 'grape', 'grapefruit', 'grappa', 'green bean', 'green onion/scallion', 'ground beef', 'ground lamb', 'guam', 'guava', 'haiti', 'halibut', 'ham', 'hazelnut', 'herb', 'hominy/cornmeal/masa', 'honey', 'honeydew', 'horseradish', 'hot drink', 'hot pepper', 'hummus', 'iced coffee', 'iced tea', 'jalapeño', 'jerusalem artichoke', 'jícama', 'kahlúa', 'kale', 'kirsch', 'kiwi', 'kumquat', 'lamb', 'lamb chop', 'lamb shank', 'leafy green', 'leek', 'legume', 'lemon', 'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lime', 'lime juice', 'lingonberry', 'liqueur', 'lobster', 'lychee', 'macadamia nut', 'mango', 'maple syrup', 'margarita', 'marsala', 'marscarpone', 'marshmallow', 'martini', 'mayonnaise', 'melon', 'mezcal', 'midori', 'milk/cream', 'mint', 'molasses', 'monterey jack', 'mortar and pestle', 'mozzarella', 'mushroom', 'mussel', 'mustard', 'mustard greens', 'nectarine', 'noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus', 'okra', 'olive', 'onion', 'orange', 'oregano', 'orzo', 'oyster', 'papaya', 'paprika', 'parmesan', 'parsley', 'parsnip', 'passion fruit', 'pea', 'peach', 'peanut', 'peanut butter', 'pear', 'pecan', 'pepper', 'pernod', 'persimmon', 'phyllo/puff pastry dough', 'pine nut', 'pineapple', 'pistachio', 'plantain', 'plum', 'poach', 'poblano', 'pomegranate', 'pomegranate juice', 'poppy', 'pork', 'pork chop', 'pork rib', 'pork tenderloin', 'port', 'potato', 'prosciutto', 'prune', 'pumpkin', 'quail', 'quince', 'quinoa', 'rabbit', 'rack of lamb', 'radicchio', 'radish', 'raisin', 'raspberry', 'red wine', 'rhubarb', 'rice', 'ricotta', 'root vegetable', 'rosemary', 'rosé', 'rum', 'rutabaga', 'rye', 'saffron', 'sage', 'sake', 'salmon', 'sangria', 'sardine', 'scallop', 'seed', 'semolina', 'sesame', 'sesame oil', 'shallot', 'sherry', 'shrimp', 'snapper', 'sour cream', 'sourdough', 'soy', 'soy sauce', 'sparkling wine', 'spice', 'spinach', 'squash', 'squid', 'strawberry', 'sugar snap pea', 'sweet potato/yam', 'swiss cheese', 'swordfish', 'tamarind', 'tangerine', 'tapioca', 'tarragon', 'tea', 'tequila', 'thyme', 'tilapia', 'tomatillo', 'tomato', 'tortillas', 'tree nut', 'tree nut free', 'triple sec', 'tropical fruit', 'trout', 'tuna', 'turnip', 'vanilla', 'veal', 'venison', 'vermouth', 'vinegar', 'vodka', 'walnut', 'wasabi', 'watercress', 'watermelon', 'white wine', 'wild rice', 'windsor', 'yellow squash', 'yogurt', 'yuca', 'zucchini'])

        return df
    
    def nutrient_norm(self, df_ing):
        df = pd.read_csv("data/nutrition_with_percents_copy.csv").set_index("name",)
        substances = {
            'fat': 0,
            'carbohydrat': 0,
            'protein': 0,
            'Fe': 0,               
            'Mg': 0, 
            'Na': 0,             
            'K': 0,              
            'Ca': 0,             
            'Zn': 0,               
            'Se': 0,              
            'Cu': 0,                         
            'C': 0,              
            'D': 0,     
            'B12': 0,             
            'E': 0,      
            'A': 0,              
            'K': 0,
        }



        for i in [*df_ing]:
            if df.index.isin([i]).any():
                subs = df.loc[i]
                for j in subs.index:
                    # print(j)
                    substances[j] += subs.loc[j] * 0.5
                # print(df.loc[i])
                # break

        return substances
    
    def beautiful_output(self, df, df_ing):
        print(f"{df['title']} (rating: {df['rating']})")

        print("Ingredients:")
        for i in df_ing:
            print("-", i)
        
        print("Nutrients:")
        nutrient = self.nutrient_norm(df_ing)
        for i in nutrient.keys():
            print(f"- {i}: {nutrient[i]:.2f}%")

        print("URL:", df['url'])


    def dayly_menu(self):
        df = self.open_df()

        b_df = df[df['breakfast'] == 1].sample(frac=1, random_state=randint(1, 100)).reset_index().drop(columns=['index', 'breakfast', 'dinner', 'lunch']).iloc[0]
        l_df = df[df['lunch'] == 1].sample(frac=1, random_state=randint(1, 100)).reset_index().drop(columns=['index', 'breakfast', 'dinner', 'lunch']).iloc[0]
        d_df = df[df['dinner'] == 1].sample(frac=1, random_state=randint(1, 100)).reset_index().drop(columns=['index', 'breakfast', 'dinner', 'lunch']).iloc[0]

        b_df_info = b_df[['title', 'url', 'rating']]
        l_df_info = l_df[['title', 'url', 'rating']]
        d_df_info = d_df[['title', 'url', 'rating']]

        b_df.drop(columns=['title', 'url', 'rating'])
        l_df.drop(columns=['title', 'url', 'rating'])
        d_df.drop(columns=['title', 'url', 'rating'])

        b_df_ing = b_df[b_df == 1].index.to_list()
        l_df_ing = l_df[l_df == 1].index.to_list()
        d_df_ing = d_df[d_df == 1].index.to_list()

        print("BREAKFAST")
        print("---------------------")
        self.beautiful_output(b_df_info, b_df_ing)

        print("LUNCH")
        print("---------------------")
        self.beautiful_output(l_df_info, l_df_ing)

        print("DINNER")
        print("---------------------")
        self.beautiful_output(d_df_info, d_df_ing)



# a = Dayly_menu()

# a.dayly_menu()

# # df = set(['title', 'almond', 'amaretto', 'anchovy', 'anise', 'apple', 'apple juice', 'apricot', 'artichoke', 'arugula', 'asian pear', 'asparagus', 'avocado', 'bacon', 'banana', 'barley', 'basil', 'bass', 'bean', 'beef', 'beef rib', 'beef shank', 'beef tenderloin', 'beer', 'beet', 'bell pepper', 'berry', 'biscuit', 'blackberry', 'blue cheese', 'blueberry', 'bok choy', 'bourbon', 'bran', 'brandy', 'bread', 'breadcrumbs', 'breakfast', 'brie', 'brine', 'brisket', 'broccoli', 'broccoli rabe', 'brown rice', 'brussel sprout', 'buffalo', 'bulgur', 'butter', 'buttermilk', 'butternut squash', 'butterscotch/caramel', 'cabbage', 'calvados', 'campari', 'candy', 'cantaloupe', 'capers', 'caraway', 'cardamom', 'carrot', 'cashew', 'cauliflower', 'caviar', 'celery', 'chambord', 'champagne', 'chard', 'chartreuse', 'cheddar', 'cherry', 'chestnut', 'chicken', 'chickpea', 'chile', 'chile pepper', 'chive', 'chocolate', 'cilantro', 'cinnamon', 'citrus', 'clam', 'clove', 'coconut', 'cod', 'coffee', 'cognac/armagnac', 'collard greens', 'coriander', 'corn', 'cornmeal', 'cottage cheese', 'couscous', 'crab', 'cranberry', 'cream cheese', 'créme de cacao', 'crêpe', 'cr��me de cacao', 'cuba', 'cucumber', 'cumin', 'currant', 'curry', 'custard', 'date', 'dill', 'dried fruit', 'duck', 'eau de vie', 'egg', 'egg nog', 'eggplant', 'endive', 'escarole', 'fennel', 'feta', 'fig', 'fish', 'fontina', 'fortified wine', 'frangelico', 'fruit', 'fruit juice', 'garlic', 'gin', 'ginger', 'goat cheese', 'goose', 'gouda', 'grand marnier', 'granola', 'grape', 'grapefruit', 'grappa', 'green bean', 'green onion/scallion', 'ground beef', 'ground lamb', 'guam', 'guava', 'haiti', 'halibut', 'ham', 'hazelnut', 'herb', 'hominy/cornmeal/masa', 'honey', 'honeydew', 'horseradish', 'hot drink', 'hot pepper', 'hummus', 'iced coffee', 'iced tea', 'jalapeño', 'jerusalem artichoke', 'jícama', 'kahlúa', 'kale', 'kirsch', 'kiwi', 'kumquat', 'lamb', 'lamb chop', 'lamb shank', 'leafy green', 'leek', 'legume', 'lemon', 'lemon juice', 'lemongrass', 'lentil', 'lettuce', 'lima bean', 'lime', 'lime juice', 'lingonberry', 'liqueur', 'lobster', 'lychee', 'macadamia nut', 'mango', 'maple syrup', 'margarita', 'marsala', 'marscarpone', 'marshmallow', 'martini', 'mayonnaise', 'melon', 'mezcal', 'midori', 'milk/cream', 'mint', 'molasses', 'monterey jack', 'mortar and pestle', 'mozzarella', 'mushroom', 'mussel', 'mustard', 'mustard greens', 'nectarine', 'noodle', 'nut', 'nutmeg', 'oat', 'oatmeal', 'octopus', 'okra', 'olive', 'onion', 'orange', 'oregano', 'orzo', 'oyster', 'papaya', 'paprika', 'parmesan', 'parsley', 'parsnip', 'passion fruit', 'pea', 'peach', 'peanut', 'peanut butter', 'pear', 'pecan', 'pepper', 'pernod', 'persimmon', 'phyllo/puff pastry dough', 'pine nut', 'pineapple', 'pistachio', 'plantain', 'plum', 'poach', 'poblano', 'pomegranate', 'pomegranate juice', 'poppy', 'pork', 'pork chop', 'pork rib', 'pork tenderloin', 'port', 'potato', 'prosciutto', 'prune', 'pumpkin', 'quail', 'quince', 'quinoa', 'rabbit', 'rack of lamb', 'radicchio', 'radish', 'raisin', 'raspberry', 'red wine', 'rhubarb', 'rice', 'ricotta', 'root vegetable', 'rosemary', 'rosé', 'rum', 'rutabaga', 'rye', 'saffron', 'sage', 'sake', 'salmon', 'sangria', 'sardine', 'scallop', 'seed', 'semolina', 'sesame', 'sesame oil', 'shallot', 'sherry', 'shrimp', 'snapper', 'sour cream', 'sourdough', 'soy', 'soy sauce', 'sparkling wine', 'spice', 'spinach', 'squash', 'squid', 'strawberry', 'sugar snap pea', 'sweet potato/yam', 'swiss cheese', 'swordfish', 'tamarind', 'tangerine', 'tapioca', 'tarragon', 'tea', 'tequila', 'thyme', 'tilapia', 'tomatillo', 'tomato', 'tortillas', 'tree nut', 'tree nut free', 'triple sec', 'tropical fruit', 'trout', 'tuna', 'turnip', 'vanilla', 'veal', 'venison', 'vermouth', 'vinegar', 'vodka', 'walnut', 'wasabi', 'watercress', 'watermelon', 'white wine', 'wild rice', 'windsor', 'yellow squash', 'yogurt', 'yuca', 'zucchini']) - set(pd.read_csv("data/nutrition_with_percents.csv", usecols=['name'])['name'].to_list())
# # print(df)

# # a = Main_class()

# # print(a.similar_reciept(['honey', 'jam', 'milk']))