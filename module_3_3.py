def print_params(a=1, b="строка", c=True):
    print(a,b,c,"\n")

print_params()
print_params(2, "grt")
print_params("jfj")

print_params(b = 25)
print_params(c = [1,2,3])

values_list=["link", 4.78, False]
values_dict={"a": 43, "b": "low", "c": 2.93}
print_params(*values_list)
print_params(**values_dict)

values_list_2=["work", 52]
print_params(*values_list_2, 42)
