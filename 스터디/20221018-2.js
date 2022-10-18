/** fill
 *  (채우는값, 시작인덱스, 끝인덱스+1)
 */

const array1 = [1, 2, 3, 4];

console.log(array1.fill(0, 2, 4));
// 인덱스 2부터 3까지 0으로 채우기  [1, 2, 0, 0]

// fill with 5 from position 1
console.log(array1.fill(5, 1));
// 인덱스 1부터 끝까지 5로 채우기   [1, 5, 5, 5]

console.log(array1.fill(6));
// 모두 6으로 채우기  [6, 6, 6, 6]
