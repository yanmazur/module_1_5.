immutable_var = "home", 2, True
print(immutable_var)
#immutable_var[0]=1 Кортежи являются неизменяемыми структурами данных, поэтому при попытке их изменить будет выдавать ошибку.
mutable_list = ["book","table","pen"]
print(mutable_list)
mutable_list[0:] = [1,2,3]
print(mutable_list)
