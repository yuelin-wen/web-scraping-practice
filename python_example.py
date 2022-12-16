from random import randint
# from modlue name import sepecific module

# import random as rand
# use aliase name

# import random
# normal import syntax

# from random import *
# import everything

x = randint(-100, 100)

if x > 0 and x < 100:
	print("x between 0 and 100")
# elif x <=0 and x >= -100
# 	print("x between -100 and 0")
elif not x == 2:
	print("x is not 2")
else:
	print("else")



if not 1 == 1:
	print("true")
else:
	print("false")


for y in range(1,-10,-2):
	print("y")

for char in "coffee":
	print(char)

i = 0
while 1:
	print("loop test")
	if 1+1!=2:
		print("1+1=2")
		break
	else:
		print("continue {}".format(i))
		i = i + 1
		if i==10:
			print("you are done")
			break
		continue


people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!
#Change "Hanna" to "Hanna"
people[0] = "Hannah"
#Change "Geoffrey" to "Jeffrey"
people[4] = "Jeffrey"
#Change "aparna" to "Aparna" (capitalize it)
people[-1] = "Aparna"

if "Hannah" in people:
	print("Hannah inside people list")


sounds = ["super", "cali", "fragil", "istic", "expi", "ali", "docious"]
# Define your code below:
result = ''
for s in sounds:
    result += s.upper()
    print(result)




answer = [person[0] for person in ["Elie", "Tim", "Matt"]]
answer2 = [val for val in [1,2,3,4,5,6] if val % 2 == 0]

print(answer)
print(answer2)



answer = [val for val in [1,2,3,4] if val in [3,4,5,6]]
#the slice [::-1] is a quick way to reverse a string
answer2 = [val[::-1].lower() for val in ["Elie", "Tim", "Matt"]]

print(answer)
print(answer2)


cat = {"name":"jerry","age":2}
cat2 = dict(name="jerry",age=23)

cat_name = cat2["name"]
print(cat2)
print(cat_name, cat2["age"])

value = cat.items()
print(value)

test = {"name":"jerry","age":24,"hobby":"gaming","phone":1343}
new_test = test.fromkeys(['phone'],'unknown')
print(test)
print(new_test)



game_properties = [
    "current_score",
    "high_score",
    "number_of_lives",
    "items_in_inventory",
    "power_ups",
    "ammo",
    "enemies_on_screen",
    "enemy_kills",
    "enemy_kill_streaks",
    "minutes_played",
    "notifications",
    "achievements"
]
initial_game_state = dict.fromkeys(game_properties, 20)
print(initial_game_state)

def add(a,b):
	return a+b



def math(a,b,fn=add):
	return fn(a,b)


print(math(3,4))

def exponent(num,power=2):
	return num ** power

print(exponent(2,3))
print(exponent(power = 2,num=3))


def argsfunc(**nums):
	# total=0
	# for k,v in nums.items():
	# 	total+=v

	# return total
	total=0
	for v in nums.values():
		total+=v

	return total


print(argsfunc(one=1,two=2,three=3))



def greet_boss(employee=None, boss=None):
 
      print(f"{employee} greets {boss}")
 
 
names = { "employee": "Colt", "boss": "Bob" }
print(greet_boss(**names))


def count_sevens(*args):
    return args.count(7)

nums = [90,1,35,67,89,20,3,1,2,3,4,5,6,9,34,46,57,68,79,12,23,34,55,1,90,54,34,76,8,23,34,45,56,67,78,12,23,34,45,56,67,768,23,4,5,6,7,8,9,12,34,14,15,16,17,11,7,11,8,4,6,2,5,8,7,10,12,13,14,15,7,8,7,7,345,23,34,45,56,67,1,7,3,6,7,2,3,4,5,6,7,8,9,8,7,6,5,4,2,1,2,3,4,5,6,7,8,9,0,9,8,7,8,7,6,5,4,3,2,1,7]

print(count_sevens(*nums))


lambda_func=lambda a,b: a + b

print(lambda_func("hellow","world"))



cube = lambda arg: arg**3

print(cube(3))

numbers = [1,3,4,5,3,76,1234,32,2]

check = [i*2  for i in numbers if i % 2 == 0]
# check = [i*2  if i % 2 == 0 else i/2 for i in numbers]

lam = [(lambda x:x*3)(x) for x in numbers]

print(check)
print(lam)


try:
	num = int(input("please enter a number: "))
except:
	print("this is not a number")
else:
	print("ELSE")
finally:
	print("runs no matter what")


def divide(a,b):
	try:
		return a/b
	except ZeroDivisionError:
		print("dont ivide by zero please")
	except TypeError as err:
		print(err)
		print("must be number")

print(divide(1,0))
print(divide(1,'a'))



class Counter:
	def __init__(self,low,high):
		self.current = low
		self.high = high

	def __iter__(self):
		return self

	def __next__(self):
		if self.current < self.high:
			num = self.current
			self.current += 1
			return num
		raise StopIteration


x = Counter(10,50)
print(x)
