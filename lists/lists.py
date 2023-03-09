class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        max_val = input_list[0] if len(input_list) > 0 else None
        for num in input_list:
            if num > max_val:
                max_val = num
        for i in range(len(input_list)):
            if input_list[i] > 0:
                input_list[i] = max_val
        return input_list

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
