/** reduce
 * acc: 콜백 반환 값
 * value: 배열의 값
 * index: 배열의 인덱스
 * src: 현재 배열
 *
 * initValue가 있는지 없는지에 따라 acc, value, index가 하나씩 밀리는 차이가 있다.
 *
 * */

// 하나씩 출력해보기
[1, 2, 3, 4, 5, 6].reduce((accum, value, index, src) => {
  //console.log(accum);
  //console.log(index);
  //console.log(current);
  console.log(src);
  return value;
}, 0);

// 1~10 더하는 예제
const arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];

arr.reduce((acc, value, index, array) => {
  console.log(acc);
  return acc + value;
}, 0);
