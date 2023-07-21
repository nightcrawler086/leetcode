import { fizzBuzz } from '../fizzBuzz'

describe('fizzBuzz tests', () => {
  test('threes should become "Fizz"', () => {
    expect(fizzBuzz(3)).toStrictEqual(['1', '2', 'Fizz']);
  });
  test('fives should become "Buzz"', () => {
    expect(fizzBuzz(5)).toStrictEqual(['1', '2', 'Fizz', '4', 'Buzz']);
  });
  test('fifteens should become "FizzBuzz"', () => {
    expect(fizzBuzz(15)).toStrictEqual(['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']);
  });
});
