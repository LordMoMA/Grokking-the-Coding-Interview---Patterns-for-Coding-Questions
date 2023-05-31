package main

import "fmt"

func main() {
	original := "this is a string"
	var b []byte
	b = []byte(original)
	fmt.Printf("byte: %s", string(b))
}

func Fib(n int) int {
	if n < 2 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}
