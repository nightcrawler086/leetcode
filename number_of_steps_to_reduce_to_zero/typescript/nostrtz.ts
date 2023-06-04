export function nostrtz(num: number): number {
  let steps: number = 0;
  while (num > 0) {
    let bw: number = num & 1
    if (bw === 0) {
      num = num >> 1
    }
    else {
      num = num - 1
    }
    steps++
  }
  return(steps)
}


export function nostrtz2(num: number): number {
  let steps: number = 0;
  while (num > 0) {
    if (num % 2 === 0) {
      num = num / 2
    }
    else {
      num = num - 1
    }
    steps++
  }
  return(steps)
}
