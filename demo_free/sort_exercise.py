numbers = [5, 2, 9, 1]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 9]

sorted(numbers, reverse=True)
# [9, 5, 2, 1]

sorted("banana")
# ['a', 'a', 'a', 'b', 'n', 'n']

words = ['apple', 'banana', 'kiwi', 'grape']
sorted(words, key=len)
# ['kiwi', 'apple', 'grape', 'banana']

students = [
    {'name': 'Tom', 'score': 90},
    {'name': 'Jerry', 'score': 85},
    {'name': 'Spike', 'score': 92}
]
sorted(students, key=lambda x: x['score'])
# [{'name': 'Jerry', 'score': 85}, {'name': 'Tom', 'score': 90}, {'name': 'Spike', 'score': 92}]


# Sort in-place
numbers.sort()