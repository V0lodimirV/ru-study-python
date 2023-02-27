from typing import Any, Callable, List, Tuple


class FilterMapExercise:
    @staticmethod
    def filter_map(func: Callable[[Any], Tuple[bool, Any]], input_array: List[Any]) -> List[Any]:
        my_list = map(func, input_array)
        filter_list = filter(lambda x: x[0] is not False, my_list)
        return [res[1] for res in filter_list]
