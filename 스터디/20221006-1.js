//생성자 함수
function User(name) {
  this.name = name;
  this.boo = false;

  this.sayHi = function () {
    console.log(this);
  };
}

let user = new User("geunwoo");

//클래스
class User2 {
  value = 1;

  constructor(name) {
    this.name = name;
    this.speed = 0;
  }

  sayHi() {
    console.log(this.name);
    console.log(this.speed);
    console.log(this.value);
  }
}

let user2 = new User2("geunwoo");

console.log(user2);
