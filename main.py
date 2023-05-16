# python imports: everthing is exported from a python file automatically
# from where import what
from list import LinkedList

# list testing zone
new_list = LinkedList()
print(new_list.head, new_list.tail)
new_list.insert_front(1)
print(len(new_list), new_list.head, new_list.tail)
new_list.insert_front(2)
print(len(new_list), new_list.head, new_list.tail)
new_list.insert_front(2)
new_list.insert_front(3)
new_list.insert_front(4)
new_list.insert_front("taco")
new_list.insert_front(56)
new_list.insert_front(100)
new_list.insert_front(-1)
new_list.insert_end("🐈‍⬛")
print(new_list)

print(new_list.find("taco"))
print(new_list.find("banana"))

new_list = LinkedList()

print(new_list.find("taco"))