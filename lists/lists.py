class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        max_number = input_list[0] if len(input_list) > 0 else None
        for item in input_list:
            if item > max_number:
                max_number = item
        output_list = []
        for item in input_list:
            if item > 0:
                output_list.append(max_number)
            else:
                output_list.append(item)
        return output_list

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        low = 0
        high = len(input_list) - 1

        while low <= high:
            mid = (low + high) // 2
            if input_list[mid] == query:
                return input_list.index(input_list[mid])
            else:
                if query < input_list[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
        return -1
