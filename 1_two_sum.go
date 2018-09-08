package leetcode

func twoSum(nums []int, target int) []int {
	m := make(map[int]int)

	for i, v := range nums {
		if leftIndex, ok := m[target-v]; ok {
			return []int{leftIndex, i}
		} else {
			m[v] = i
		}
	}

	return []int{}
}
