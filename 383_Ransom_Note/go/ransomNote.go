package main

import (
  "fmt"
  "strings"
)

func canConstruct(ransomNote string, magazine string) bool {
  for _, v := range ransomNote {
    if strings.Count(ransomNote, string(v)) > strings.Count(magazine, string(v)) {
      return false
    }
  }
  return true
}

func main() {
  fmt.Println(canConstruct("a", "b"))
  fmt.Println(canConstruct("aa", "ab"))
  fmt.Println(canConstruct("aa", "aab"))
  fmt.Println(canConstruct("aa", "aba"))
}

