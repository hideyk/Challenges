package main

import (
	"fmt"
)

func insertN(numbers []int, index int, value int) []int {
	numbers = append(numbers, 0)
	copy(numbers[index+1:], numbers[index:])
	numbers[index] = value
	return numbers
}

func createTargetArray(nums []int, index []int) []int {
	size := len(nums)
	result := make([]int, 0)
	for i := 0; i < size; i++ {
		if index[i] == len(result) {
			result = append(result, nums[i])
			continue
		}
		result = insertN(result, index[i], nums[i])
	}
	return result
}

func main() {
	nums := []int{0, 1, 2, 3, 4}
	index := []int{0, 1, 2, 2, 1}
	result := createTargetArray(nums, index)
	fmt.Println(result)
}
