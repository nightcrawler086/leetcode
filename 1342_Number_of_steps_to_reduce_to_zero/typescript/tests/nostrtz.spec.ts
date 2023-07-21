import { nostrtz } from '../nostrtz'
import { nostrtz2 } from '../nostrtz'

describe('nostrtz tests', () => {
  test('Solution1 - Test 1', () => {
    expect(nostrtz(14)).toEqual(6);
  });
  test('Solution1 - Test 2', () => {
    expect(nostrtz(8)).toEqual(4);
  });
  test('Solution1 - Test 3', () => {
    expect(nostrtz(123)).toEqual(12);
  });
  test('Solution1 - Test 4', () => {
    expect(nostrtz(9000)).toEqual(18);
  });
  test('Solution2 - Test 1', () => {
    expect(nostrtz2(14)).toEqual(6);
  });
  test('Solution2 - Test 2', () => {
    expect(nostrtz2(8)).toEqual(4);
  });
  test('Solution2 - Test 3', () => {
    expect(nostrtz2(123)).toEqual(12);
  });
  test('test case 4', () => {
    expect(nostrtz2(9000)).toEqual(18);
  });
});
