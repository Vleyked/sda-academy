package main

import (
	"fmt"
	"math/rand"
)



func main() {
	var numbers []int
	var swapped bool
		
    for x := 1; x <= 10000; x++ {
		numbers = append(numbers, rand.Intn(999999999))
    }
	
	numbers_lenght := len(numbers)

	for z := 0; z < numbers_lenght - 1; z++ {
		for y := 0; y < numbers_lenght - z - 1 ; y++ {
			if numbers[y] > numbers[y + 1] {
				swapped = true
				a := numbers[y + 1]
				b := numbers[y]
				numbers[y] = a
				numbers[y + 1] = b
			}	
		}
		if !(swapped) {
			break;
		}
    }
	

	fmt.Println("Numbers sorted", numbers)
}