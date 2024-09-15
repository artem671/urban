def calculate_structure_sum(data_structure):
    stri=""
    counter_structure=0
    for i, j in enumerate(data_structure):
        stri+=str(j)
        if data_structure[i]!=data_structure[-1]:
            counter_structure+=1
        
    return (len(stri))+counter_structure

print(calculate_structure_sum(data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]))