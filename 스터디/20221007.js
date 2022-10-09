/* 타이머 - 리액트 */

//setTimeout, setInterval 브라우저 단에서 돌 수 있음 -> useEffect로 마운트 이후에 실행되어야 함
import { useEffect, useState } from "react";

const Timer = () => {
import React, { useState, useEffect } from "react";

function useTimer() {
  const [isStart, setIsStart] = useState(false);
  const [timer, setTimer] = useState(0);

  useEffect(() => {
    if (!isStart) {
      return;
    }

    const interval = setInterval(() => {
      setTimer((prev) => prev + 1);
    }, 1000);

    return () => clearInterval(interval);
  }, [isStart]);

  return { timer, setIsStart };
}

function formatTime(totalSeconds) {
  const minute = Math.floor(totalSeconds / 60);
  const second = totalSeconds % 60;

  return {
    minutes: minute > 9 ? minute : `0${minute}`,
    seconds: second > 9 ? second : `0${second}`
  };
}

export default function App() {
  const [min, setMin] = useState(0);
  const [sec, setSec] = useState(0);

  const { timer, setIsStart } = useTimer();

  // const [minTimer, setMinTimer] = useState(0);
  // const [secTimer, setSecTimer] = useState(0);

  const remainingSeconds = min * 60 + sec - timer;
  const { minutes, seconds } = formatTime(remainingSeconds);

  return (
    <div>
      <div>
        <label>
          <input type="number" onChange={(e) => setMin(Number(e.target.value))} />
          Minutes
        </label>
        <label>
          <input type="number" onChange={(e) => setSec(Number(e.target.value))} />
          Seconds
        </label>

        <button onClick={() => setIsStart(true)}>START</button>
        <button>PAUSE / RESUME</button>
        <button>RESET</button>
      </div>

      <h2>
        {minutes} : {seconds}
      </h2>
    </div>
  );
}

