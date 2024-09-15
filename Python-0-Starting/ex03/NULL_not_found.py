from typing import Any

def NULL_not_found(object: Any) -> int:
	null_types = {
		type(None): "Nothing",
		float: "Garlic",
		int: "Zero",
		str: "Empty",
		bool: "Fake",
	}

	if type(object) in null_types:
		obj_name = null_types[type(object)]
		print(f"{obj_name}: {object} < {type(object).__name__}>$")
		return 0
	else:
		print("Type not Found$")
		return 1
