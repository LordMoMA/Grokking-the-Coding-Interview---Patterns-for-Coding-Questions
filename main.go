package main

func main() {
	// original := "this is a string"
	// var b []byte
	// b = []byte(original)
	// fmt.Printf("byte: %s", string(b))
}

type user struct {
	id       int
	username string
	fullname string
	email    string
}

func setup_test_user() *user {
	sam := user{1001, "sammy", "Sam Winchester", "sam@winchester.org"}
	return &sam
}

func Fib(n int) int {
	if n < 2 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}
