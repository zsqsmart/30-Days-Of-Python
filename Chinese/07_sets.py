st = set()

st = {"itm1", "itm2", "itm3", "itm4"}

fruits = {"banana", "orange", "mango", "lemon"}

len(fruits)

print("Does banana in fruits:", "banana" in fruits)

fruits.add("lime")

print(fruits)

fruits.update(["lemon", "apple", "cherry", "lime"])

vegetables = ("tomato", "potato", "cabbage", "onion", "carrot")

fruits.update(vegetables)

print(fruits)

fruits.remove("lemon")

print(fruits)

fruits.clear()
print(fruits)


print(fruits.intersection(st))


# 集合
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add("Twitter")

it_companies.update(["Tencent", "Baidu", "Alibaba"])

print(it_companies)

it_companies.remove("Tencent")

# 移除和丢弃之间有什么区别


print(A.union(B))

print(A.intersection(B))

print("A.issubset(B)", A.issubset(B))
print("A.issuperset(B)", A.issuperset(B))
print("A.isdisjoint(B)", A.isdisjoint(B))

words = "我是一个老师，我喜欢激励和教导人们"
ls = list(words)
print("ls", ls)
print("set", len(set(ls)))
