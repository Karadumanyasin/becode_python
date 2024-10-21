
""" 2 bottles of milk at €0.45 each
    3 bottles of raw cider at €3.85 each
    1 bag of flour at 0.9 €
    1 packet of butter at €0.77
    1 jar of nutella at €1.87 """

bottles_of_milk = 0.45
bottles_of_raw_cider = 3.85
bag_of_flour = 0.9
packet_of_butter = 0.77
jar_of_nutella = 1.87
allowanceMoney = 20

print( "la brique de lait cout €0.45")
nbr_milk = input("combien de brique de lait vous voulez ? ")
nbr_milk = int(nbr_milk)
total_milk = nbr_milk * bottles_of_milk
print("vous avez choisie " + str(nbr_milk) + " brique de lait" )
print("le lait vous coutera : " + str(total_milk) + "€")

print( "la bouteille de cidre brut cout €3.85")
nbr_cidre = input("combien de bouteille de cidre brut vous voulez ? ")
nbr_cidre = int(nbr_cidre)
total_cidre = nbr_cidre * bottles_of_raw_cider
print("vous avez choisie " + str(nbr_cidre) + " bouteille de cidre brut" )
print("le cidre brut vous coutera : " + str(total_cidre) + "€")

print( "le sac de farine cout €0.9")
nbr_flour = input("combien de sac de farine vous voulez ? ")
nbr_flour = int(nbr_flour)
total_flour = nbr_flour * bag_of_flour
print("vous avez choisie " + str(nbr_flour) + " sac de farine" )
print("la farine vous coutera : " + str(total_flour) + "€")

print( "le packet de beurre cout €0.77")
nbr_butter = input("combien de packet de beurre vous voulez ? ")
nbr_butter = int(nbr_butter)
total_butter = nbr_butter * packet_of_butter
print("vous avez choisie " + str(nbr_butter) + " bouteille de cidre brut" )
print("le beurre vous coutera : " + str(total_butter) + "€")

print( "le pot de nutella cout €1.87")
nbr_nutella = input("combien de pot de nutella vous voulez ? ")
nbr_nutella = int(nbr_nutella)
total_nutella = nbr_nutella * jar_of_nutella
print("vous avez choisie " + str(nbr_nutella) + " pot de nutella" )
print("le nutella vous coutera : " + str(total_nutella) + "€")

orderPrice = total_milk + total_cidre + total_flour + total_butter + total_nutella
orderPrice=float(orderPrice)

argent_restant = allowanceMoney - orderPrice
message = ""

if argent_restant > 0:
    message = "Vous avez dépensé " + str(orderPrice) + "€, il vous reste " + str(argent_restant) + "€"
elif argent_restant < 0:
    montant_manquant = abs(argent_restant)
    message = "Désolé, il vous manque " + str(montant_manquant) + " euros"
else:
    message = "Vous êtes fauché !"
print(message)


import math
count_alpha = len("Hello world!")
count_float = float(count_alpha)
round_pi = round(math.pi, 2)
text = "Hello world!"
reversed_text = list(text[::-1])
print(reversed_text)
age = input("quel est votre age ? :")
print("votre age est " + age + "ans")
print(type(age))
num = [ 2, 8, 1, 4, 6, 3, 7]
sorted_num = sorted(num)
sum_of_list = sum(num)
min_value = min(num)
max_value = max(num)
calc = "1 + 2"
string_interpret = eval(calc)
print(string_interpret)
import unittest


class TestNotebook(unittest.TestCase):
    def test_count_alpha(self):
        self.assertEqual(count_alpha, 12)

    def test_count_float(self):
        self.assertEqual(type(count_float), float)

    def test_pi(self):
        self.assertEqual(3.14, round_pi)

    def test_reversed(self):
        self.assertEqual(
            reversed_text, ["!", "d", "l", "r", "o", "w", " ", "o", "l", "l", "e", "H"]
        )

    def test_age(self):
        self.assertEqual(type(age), str)

    def test_sorted(self):
        self.assertEqual(sorted_num, [1, 2, 3, 4, 6, 7, 8])

    def test_sum(self):
        self.assertEqual(sum_of_list, 31)

    def test_min(self):
        self.assertEqual(min_value, 1)

    def test_max(self):
        self.assertEqual(max_value, 8)

    def test_interpret(self):
        self.assertEqual(string_interpret, 3)


unittest.main(argv=[""], verbosity=2, exit=False)

translate ={}
translate ["here"] = "ici"
translate ["work"] = "work"
translate ["programming"] = "programmation"
translate ["pleasure"] = "plaisir"
translate ["learn"] = "apprendre"
translate ["career"] = "carriere"
sentence = ["I",  "am", "the", "master", "of", "the", "world"]
universal_number = "The universal number is 42"
heroes = {"Superman": "Clark Kent", "Batman": "Bruce Wayne", "Spiderman": "Tony Parker"}
definition = heroes.values()
print(list(definition))
keys = heroes.keys()
print(list(keys))
heroes ["Spiderman"] = "Peter Parker"
print(heroes)
products = {"Laser sword": 229.0,"Mitendo DX": 127.30,"Linux cushion": 74.50,"Goldorak briefs": 29.90,"Nextpresso station": 184.60}
print(products)
sum_products = sum(products.values())
print(sum_products)

products.pop("Laser sword")
print(products)

print("voila la liste")
students = [
    "Merouane",
    "Baptiste",
    "Caroline",
    "Joe",
    "Sophie",
    "Nathan",
    "Raphaël",
    "Axel",
    "Mathieu",
    "Adrien",
]
students_trie = sorted(students)
for x in students_trie:
    print(x)

print("voila les 2 nom qui commance par M")
for x in students:
    if x.startswith("M"):
        print(x)

print("voila la liste de 0 a 15 non inclus")
for i in range(15):
    print(i)

print("voila la bouble for qui affiche de 1 a 10 inclus mais qui s'arret a 5")
for i in range(1,11):
    if i == 5:
        break
    print(i)

print("voila la bouvle for qui affiche de 1 a 10 inclus mais qui continue apres 5 avec une modification")
for i in range(1, 11):
    if i <= 5:
        print(i)
    else:
        print(f"{i} on continue")

list_nbr = [17, 38, 10, 25, 72]

list_nbr.sort()
print(list_nbr)

list_nbr = [17, 38, 10, 25, 72]
list_nbr.append(12)
print(list_nbr)

list_nbr.reverse()
print(list_nbr)

index_dernier = len(list_nbr) - 1
print(index_dernier)

for i in range(len(list_nbr)):
    if list_nbr[i] == 38:
        list_nbr.remove(38)
        break
print(list_nbr)

sous_list =list_nbr[1:3]
print(sous_list)

sous_list_2 = list_nbr[:2]
print(sous_list_2)

sous_list_3 = list_nbr[2:]
print(sous_list_3)

sous_list_complet = list_nbr[:]
print(sous_list_complet)

last_element = list_nbr[-1]
print(last_element)






