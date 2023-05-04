package main

import "log"

type Animal interface {
	// The method set of an interface type is its interface
	Walk()
}

type Cat struct {
	name string
}

// A method of type T
func (c Cat) Walk() {
	log.Println("Animal name:", c.name)
}

// A method of type *T
func (c *Cat) changeName(newName string) {
	c.name = newName
}

func main() {
	c1 := &Cat{name: "Tom"} // Pointer type
	c2 := Cat{name: "Katie"}

	// c1 with pointer receiver : Has all methods attached to both *Car(pointer) and Cat(Non-pointer)
	c1.changeName("Tommy")
	// C1 has access to Walk() method although Walk() method expect a pointer receiver
	c1.Walk()
	// c2 non-pointer receiver: // c2 with value receiver : Has all methods attached to Cat(Non-pointer)
	c2.changeName("Kate")
	c2.Walk()
}
