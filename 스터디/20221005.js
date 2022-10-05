// 클로저

function fn1() {
  let count = 0;

  return function fn2() {
    return count++; //클로저 // (외부 함수의 실행없이도) 내부함수에서 외부 변수를 기억해놓고 접근할 수 있다.
  };
}

let counter = fn1(); //이 부분 필수, counter는 fn1()의 공간을 가리킨다(객체의 참조느낌), 그래서 해당 공간에 저장되어 있는 변수를 기억해놓고 있다.

console.log(counter());
console.log(counter());
console.log(counter());

//렉시컬 환경 3개
