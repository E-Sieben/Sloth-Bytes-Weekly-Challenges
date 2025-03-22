def bridge_shuffle_array(arr1: list[any], arr2: list[any]) -> list[any]:
    sol: list[any] = []
    for ita in range(len(arr1 if len(arr1) >= len(arr2) else arr2)):
        try:
            sol.append(arr1[ita])
        except IndexError:
            pass
        try:
            sol.append(arr2[ita])
        except IndexError:
            pass
    return sol

print(bridge_shuffle_array(["A", "B", "C"], [1, 2, 3, 4]))
#! Examples
print(bridge_shuffle_array(["A", "A", "A"], ["B", "B", "B"]))
print(bridge_shuffle_array(["C", "C", "C", "C"], ["D"]))
print(bridge_shuffle_array([1, 3, 5, 7], [2, 4, 6]))