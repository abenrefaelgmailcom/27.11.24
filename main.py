#
#
# SENTINEL = (-999,)
#
# num: int = 0

# while num != SENTINEL[0]:
#     num: int = int(input('enter number [-999 to exit]:'))

# while True:
#     num: int = int(input('enter number [-999 to exit]:'))
#     if num != SENTINEL[0]:
#         break

john = {"name": "Johnny", "age": 21, "major": "Computer science"}


for i in range(10):
    print(i, end=" ")
print()
#           0      1       2
# keys = ["name", "age", "major"]
for key in john.keys():
    print(key, end = " ")

print()
# enumerator
for index, key in enumerate(john.keys()):
    print(index, key, end = " ")
# unpack
print(john.items())
for item in john.items():
    key = item[0]
    value = item[1]
    print(key,':', value , end = ",  ")

for key, value in john.items():
    value = str(value) + "!"
    print(key,':', value , end = ",  ")
print()
print(john)

john["name"] = "Johnny!"

# input 3 numbers
# exit if number2 > avg and number3 not in 0-100
# while True:
#     #
#     break

def foo():
    pass

if __name__ == "__main__":
    try:
        {1,2}.remove(3)
    except KeyError as e:
        print('KeyError: cannot find item with value', e)
    except Exception as e:
        print('Something unexpected happened', e)
    finally:
        print('done')

# _ _ _ A
# _ _ B _
# 0, 3
# 1, 2
# _ _ _ A
# A _ _ _

# _ _ _
# _ X _
# O _ _
# x: 1, 1
# O: 2, 0