package main
 
import "fmt"
 
func main() {
   // Defining variables to store values of type string, int, boo, and float64
   var username string = "Go developer"
   var age int = 12
   var isAwesome = true
   var height = 5.5
 
   // Declaring pointers of types :string, int, bool and float64 using * operator
   // Pointer to a string
   var usernamePointer *string = &username
   // Pointer to an integer
   var agePointer *int = &age
   // Pointer to a boolean
   var isAwesomePointer *bool = &isAwesome
   // Pointer to a floating number
   var heightPointer *float64 = &height
 
 
   fmt.Printf("usernamePointer : %v ===> username value: %v \n", usernamePointer, *usernamePointer)
   fmt.Printf("agePointer: %v  ===> age value: %v \n", agePointer, *agePointer)
   fmt.Printf("isAwesomePointer: %v  ===> isAwesome value: %v \n", isAwesomePointer, *isAwesomePointer)
   fmt.Printf("heightPointer : %v  ===> height value: %v \n", heightPointer, *heightPointer)
}
