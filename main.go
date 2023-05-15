package main

import (
	"fmt"
	"strings"
)

func main(){
	// This works fine
str := "abc"
str = str + "def"

// This is more efficient if you are combining lots of strings
var sb strings.Builder
sb.WriteString("abc")
sb.WriteString("def")

fmt.Printf("str: %s", str)
fmt.Printf("sb: %s", sb.String())
}