function fizzBuzz(n: number): string[] {
	let answer : string[] = []	
	for (let i = 1; i <= n; i++) {
		let mystr = ''
		if (i % 3 != 0 && i % 5 != 0) {
			mystr += i.toString()
		}
		if (i % 3 === 0) {
			mystr += "Fizz"
		}
		if (i % 5 === 0) {
			mystr += "Buzz"
		}
	}
	answer.push(mystr)
	return answer
}
