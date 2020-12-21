package shufflestring

import (
	"strings"
)

func restoreString(s string, indices []int) string {
	length := len(s)
	slist := make([]string, length)
	for i := 0; i < length; i++ {
		slist[indices[i]] = string(s[i])
	}
	return strings.Join(slist, "")
}