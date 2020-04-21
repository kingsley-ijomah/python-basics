from collections import Counter

group_cost = [800, 1520, 2160, 2560, 3000]

def total(basket):
    books = Counter(basket)
    groups = []
    price = 0

    while group_count := len(books):
        price += group_cost[group_count - 1]
        groups.append(group_count)
        for book in books:
            books[book] -= 1
        # remove books with zero count
        books = +books

    # 2 * 4 books are cheaper than 5 + 3 books (5120 = 5160 - 40)
    while 3 in groups and 5 in groups:
        price -= 40
        groups.remove(3)
        groups.remove(5)

    return price
