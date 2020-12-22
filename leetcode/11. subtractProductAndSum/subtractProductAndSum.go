package subtractproductandsum

import (
	"fmt"
	"strconv"
)

func subtractProductAndSum(n int) int {
	total, product := 0, 1
	for n != 0 {
		v := n % 10
		total += v
		product *= v
		n /= 10
	}
	return product - total
}

func subtractProductAndSum2(n int) int {
	total, product := 0, 1
	for _, x := range fmt.Sprintf("%d", n) {
		xi, _ = strconv.Atoi(string(x))
		total += xi
		product *= xi
	}
	return product - total
}