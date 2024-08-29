

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}


for i in range(len(ft_list)):
	if ft_list[i] == "tata!":
		ft_list[i] = "world!"


tmp_tuple_list = list(ft_tuple)
tmp_tuple_list[1] = "France!"
ft_tuple = tuple(tmp_tuple_list)


ft_set.remove("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"


#your code here
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)