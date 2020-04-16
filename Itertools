#For every meal combination print out only that <= 30
import itertools

main_courses = ['beef stew', 'fried fish']
price_main_courses = [28, 23]
 
desserts = ['ice-cream', 'cake']
price_desserts = [2, 4]
 
drinks = ['cola', 'wine']
price_drinks = [3, 10]

##1st version without itertools
for x, a in enumerate(main_courses):
    for y, b in enumerate(desserts):
        for z, c in enumerate(drinks):
            if price_main_courses[x] + price_desserts[y] + price_drinks[z] <= 30:
                print(a, b, c, price_main_courses[x] + price_desserts[y] + price_drinks[z])

##2nd version with itertools
for dishes, prices in zip(itertools.product(main_courses, desserts, drinks),
                          itertools.product(price_main_courses, price_desserts, price_drinks)):
    if sum(prices) <= 30:
        print(" ".join(dishes), sum(prices))
        
#combinations of 2 elements from list
import itertools

teams = ['Best-ever', 'Not-so-good', 'Amateurs']

for i in itertools.combinations(teams, 2):
    print(i)

#all combinations of length <=3 from list
import itertools

flower_names = ['rose', 'tulip', 'sunflower']

for n in range(3):
    for i in itertools.combinations(flower_names, n + 1):
        print(i)
