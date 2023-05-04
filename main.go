package main

import "fmt"
 
func main() {
   // Pointer to a string
   username := "Go developer"
   // Trying to change username by passing it a memory address using the & operator
   changeNameByReference(&username)
   // Print the new username value
   fmt.Println(username)
 
}
 
func changeNameByReference(name *string) {
   // name : Pointer to variable
   // dereference name variable using the * operator
   *name = "Go and cloud developer"
}
