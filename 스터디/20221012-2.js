/*
<!-- 질문1. 이벤트 버블랑과 이벤트 캡쳐링이란? -->
<!-- 질문2. 이벤트 버블링 막는 방법은? -->


<!-- 1. 이벤트 버블링 문제 -->
<body id="body" onclick="alert(`상위요소`)">
  <button id="button" onclick="alert('클릭')">클릭해 주세요.</button>
</body> 



<!-- 2. 이벤트 위임 -->
<body id="body">
  <button id="button">클릭해 주세요.</button>

  <script>
    document.addEventListener("click",(e) => {
      if (e.target.id === 'button') alert('클릭');
      else if(e.target.id === 'body') alert('상위요소');
    })
  </script>
</body>


<!-- 3. stopPropagation -->
<body id="body" onclick="alert(`상위요소`)">
  <button id="button" onclick="alert('클릭')">클릭해 주세요.</button>

  <script>
    document.querySelector('#button').addEventListener("click",(e) => {
      e.stopPropagation();
    })
  </script>
</body>


//참고자료1: https://ko.javascript.info/bubbling-and-capturing
//참고자료2: https://joshua1988.github.io/web-development/javascript/event-propagation-delegation/




*/
