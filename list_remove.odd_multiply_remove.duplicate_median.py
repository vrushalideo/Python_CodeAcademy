def count(sequence, item):
    count =0
    for i in sequence:
        if i == item:
            count +=1
    return(count)

def purify(numbers):
    even = []
    for i in numbers:
        if i % 2 == 0:
            even.append(i)
    return (even)

def product(numbers):
    total = 1
    for i in numbers:
        total *=i
    return (total)

def remove_duplicates(elements):
    new_elements = []
    for i in elements:
        for j in elements:
            if i == j and j not in new_elements:
                new_elements.append(j)
    return (new_elements)

def median(numbers):
    new_numbers = []
    new_numbers = sorted(numbers)
    print new_numbers
    y = len(numbers)
    print y
    addition = 0.0
    med = 0.0
    if y == 1:
        med = new_numbers[0]
    elif y % 2 == 0:
        addition = float(new_numbers[(y-1)/2] + new_numbers[y/2])
        med = float(addition/2)
    else:
        addition = new_numbers[(y-1)/2]
        med = addition
    return(med)
    
median([6, 8, 12,2, 23])
