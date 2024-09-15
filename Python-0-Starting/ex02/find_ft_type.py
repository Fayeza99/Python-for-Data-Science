from typing import Any
def all_thing_is_obj(object: Any) -> int:
	type_map = {
		list: "List",
		tuple: "Tuple",
		set: "Set",
		dict: "Dict",
		str: "{object} is in the kitchen"
	}

	type_name = type_map.get(type(object))
	if type_name :
		print(f"{type_name} : {type(object)}$")
	else:
		print("Type not found")
	return 42