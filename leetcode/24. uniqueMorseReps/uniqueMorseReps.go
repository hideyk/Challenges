package main

import "fmt"

func uniqueMorseRepresentations(words []string) int {
	morselist := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
	morseset := make(map[string]bool, 0)
	for _, word := range words {
		morse := ""
		for _, rune := range word {
			morse += morselist[int(rune) - 97]
		}
		morseset[morse] = true
	}
	return len(morseset)
}

func main() {
	words := []string{"gin", "zen", "gig", "msg"}
	uniquecount := uniqueMorseRepresentations(words)
	fmt.Println(uniquecount)
}
