package main

import "fmt"

func main(){
	original := "this is a string"
	var b []byte
	b = []byte(original) 
	fmt.Printf("byte: %s",string(b) )
}

