const DASH_ARRAY = 283;
const WARNING_thresholds = 10;
const ALERT_threshold22 = 5;

const COLOR_CODESs = {
  info: {
    color: "green"
  },
  warning: {
    color: "orange",
    threshold22: WARNING_thresholds
  },
  alert: {
    color: "red",
    threshold22: ALERT_threshold22
  }
};

const TIME_LIMIT22 = 600;
let timePassedd = 0;
let timeLefts = TIME_LIMIT22;
let timerInterval22 = null;
let remainingPathColor2 = COLOR_CODESs.info.color;

document.getElementById("timer").innerHTML = `
<div class="base-timer">
  <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
    <g class="base-timer__circle">
      <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
      <path
        id="base-timer-path-remaining"
        stroke-dasharray="283"
        class="base-timer__path-remaining ${remainingPathColor2}"
        d="
          M 50, 50
          m -45, 0
          a 45,45 0 1,0 90,0
          a 45,45 0 1,0 -90,0
        "
      ></path>
    </g>
  </svg>
  <span id="base-timer-label2" class="base-timer__label">${formatTimes(
    timeLefts
  )}</span>
</div>
`;

startTimer();

function onTimesUps() {
  clearInterval(timerInterval22);
}

function startTimer() {
  timerInterval22 = setInterval(() => {
    timePassedd = timePassedd += 1;
    timeLefts = TIME_LIMIT22 - timePassedd;
    document.getElementById("base-timer-label2").innerHTML = formatTimes(
      timeLefts
    );
    setCircleDasharray2();
    setRemainingPathColors(timeLefts);

    if (timeLefts === 0) {
      onTimesUps();
    }
  }, 1000);
}

function formatTimes(time) {
  const minutes = Math.floor(time / 60);
  let seconds = time % 60;

  if (seconds < 10) {
    seconds = `0${seconds}`;
  }

  return `${minutes}:${seconds}`;
}

function setRemainingPathColors(timeLefts) {
  const { alert, warning, info } = COLOR_CODESs;
  if (timeLefts <= alert.threshold22) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(warning.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(alert.color);
  } else if (timeLefts <= warning.WARNING_thresholds) {
    document
      .getElementById("base-timer-path-remaining")
      .classList.remove(info.color);
    document
      .getElementById("base-timer-path-remaining")
      .classList.add(warning.color);
  }
}

function calculateTimeFraction2() {
  const rawTimeFraction2 = timeLefts / TIME_LIMIT22;
  return rawTimeFraction2 - (1 / TIME_LIMIT22) * (1 - rawTimeFraction2);
}

function setCircleDasharray2() {
  const circleDasharray = `${(
    calculateTimeFraction2() * DASH_ARRAY
  ).toFixed(0)} 283`;
  document
    .getElementById("base-timer-path-remaining")
    .setAttribute("stroke-dasharray", circleDasharray);
}