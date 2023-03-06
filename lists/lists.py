class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        def replace_helper(input_list, max_val):
            if not input_list:
                return []
            new_list = replace_helper(input_list[1:], max_val)

            if input_list[0] > 0:
                input_list[0] = max_val

            return [input_list[0]] + new_list

        if not input_list:
            return []

        max_val = max(input_list)

        return replace_helper(input_list, max_val)

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        def search_helper(input_list, query, start, end):

            if start >= end:
                return -1

            mid = (start + end) // 2

            if input_list[mid] == query:
                return mid

            elif input_list[mid] > query:
                return search_helper(input_list, query, start, mid)

            else:
                return search_helper(input_list, query, mid + 1, end)

        if not input_list:
            return -1

        return search_helper(input_list, query, 0, len(input_list))
