package main

import (
	"strconv"
)

// ListNode Definition for singly-linked list.
  type ListNode struct {
      Val int
      Next *ListNode
 }

 func getDecimalValue(head *ListNode) int {
    cur := head
    val := ""
    for cur != nil {
		val += strconv.Itoa(cur.Val)
		cur = cur.Next
	}
	res, _ := strconv.ParseInt(val, 2, 64)
	return int(res)
}

func main() {
	
}