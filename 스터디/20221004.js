/* 1초 마다 출력하기 */

// print numbers in order every 1 sec
// 0 ~ n-1 까지 숫자를 매 주어진 timeDelay 마다 순서대로 출력하시오. (console.log)

// e.g)
// printNumbers(3, 1000)
// 0
// (1sec)
// 1
// (1sec)
// 2

//1. for loop 이용 (Promise 혹은 async/await 없이)
function printNumbers(n, timeDelayBetween) {
  for (let i = 0; i < n; i++) {
    setTimeout(() => console.log(i), timeDelayBetween * i);
  }
}

// printNumbers(3, 1000);

//2. Promise chaning 이용
function printNumbersWithPromise(n, timeDelayBetween) {
  const getPromise = (i, timeDelayBetween) => {
    return new Promise((resolve, reject) => {
      setTimeout(() => {
        resolve(i);
      }, i * timeDelayBetween);
    });
  };

  for (let i = 0; i < n; i++) {
    getPromise(i, timeDelayBetween).then((result) => {
      console.log(result);
    });
  }
}

// printNumbersWithPromise(5, 500);

//3. async/await 이용
async function printNumbersAsync(n, timeDelayBetween) {
  function delay(i, time) {
    return new Promise((r) => setTimeout(r(i), i * time));
  }

  for (let i = 0; i < n; i++) {
    await delay(i, timeDelayBetween).then((res) => console.log(res));
  }
}

printNumbersAsync(9, 2000);
