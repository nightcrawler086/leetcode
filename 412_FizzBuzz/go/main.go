package main

import {
  "fmt"
}

func main() {
      // Set the upper limit
    limit := 100

    // Iterate from 1 to the limit
    for i := 1; i <= limit; i++ {
        if i%3 == 0 && i%5 == 0 {
            fmt.Println("FizzBuzz")
        } else if i%3 == 0 {
            fmt.Println("Fizz")
        } else if i%5 == 0 {
            fmt.Println("Buzz")
        } else {
            fmt.Println(i)
        }
    }
}


