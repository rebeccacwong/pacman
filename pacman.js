// CREATING GHOSTS
class Ghost {
  constructor(color, num, row, col) {
    this.color = color;
    this.num = num;
    this.row = row;
    this.col = col;
    this.eatable = false;
    this.direction = "up";
    this.coin = false;
  }

  generateCoords() {
    /* 
		returns the coordinates that the ghost should go to next 
		mutates the ghost's direction
		*/

    function randomizeDirection(ghost) {
      /* randomly picks. a direction for the ghost to go in if the next spot is valid */
      var moves = [];
      const directions = ["right", "left", "down", "up"];
      const spots = [
        MAP[ghost.row][ghost.col + 1],
        MAP[ghost.row][ghost.col - 1],
        MAP[ghost.row + 1][ghost.col],
        MAP[ghost.row - 1][ghost.col],
      ];
      for (var i = 0; i < spots.length; i++) {
        if (spots[i] !== 2 && spots[i] <= 4) {
          console.log("spot is " + spots[i]);
          moves.push(directions[i]);
        }
      }

      if (moves.length === 0) {
        // if there are no moves, stay in the current spot
        return [ghost.row, ghost.col];
      } else {
        ghost.direction = moves[Math.floor(Math.random() * moves.length)]; // picks a random whole num between 0 and the length of moves
        console.log("new direction: " + ghost.direction);
        return ghost.generateCoords();
      }
    }

    if (
      this.row === 7 &&
      this.col === 9 &&
      MAP[this.row - 1][this.col] !== 2 &&
      MAP[this.row - 1][this.col] <= 4
    ) {
      this.direction = "up";
      return [this.row - 1, this.col];
    }

    switch (this.direction) {
      case "right":
        if (
          MAP[this.row][this.col + 1] !== 2 &&
          MAP[this.row][this.col + 1] <= 4
        ) {
          return [this.row, this.col + 1];
        } else {
          return randomizeDirection(this);
        }
        break;
      case "left":
        if (
          MAP[this.row][this.col - 1] !== 2 &&
          MAP[this.row][this.col - 1] <= 4
        ) {
          return [this.row, this.col - 1];
        } else {
          return randomizeDirection(this);
        }
        break;
      case "up":
        if (
          MAP[this.row - 1][this.col] !== 2 &&
          MAP[this.row - 1][this.col] <= 4
        ) {
          return [this.row - 1, this.col];
        } else {
          return randomizeDirection(this);
        }
        break;
      case "down":
        if (
          MAP[this.row + 1][this.col] !== 2 &&
          MAP[this.row + 1][this.col] <= 4
        ) {
          return [this.row + 1, this.col];
        } else {
          return randomizeDirection(this);
        }
        break;
      default:
        return randomizeDirection(this);
    }
  }

  move() {
    /* mutates the board and internal attributes og the ghost to move it */
    const next = this.generateCoords(); // a two item list
    const row = next[0];
    const col = next[1];
    if (row === this.row && col === this.col) {
      return;
    }
    if (MAP[row][col] <= 4 && MAP[row][col] !== 2) {
      // you can move there
      if (this.coin) {
        MAP[this.row][this.col] = 4; // leave a coin in the map where the ghost was
      } else {
        MAP[this.row][this.col] = 3;
      }
      if (MAP[row][col] === 4) {
        this.coin = true;
      } else {
        this.coin = false;
      }
      MAP[row][col] = this.num; // add the ghost number in that location on the map
      this.row = row; // reset internal attributes to store new location
      this.col = col;
      console.log("moved");
    }
  }
}

var HIGHSCORE = 0;
var CURRENTSCORE = 0;
const red = new Ghost("red", 5, 7, 8); // 5
const pink = new Ghost("pink", 6, 7, 9); // 6
const blue = new Ghost("blue", 7, 7, 10); // 7
const orange = new Ghost("orange", 8, 6, 9); // 8
var GHOSTS = [red, pink, blue, orange];

// STORING THE DATA

// 1 is pacman
// 2 is wall
// 3 is blank
// 4 is coin
// 5-8 is ghost

const DEFAULT = [
  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], // 0
  [2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2], // 1
  [2, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 4, 2], // 2
  [2, 4, 2, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 4, 2], // 3
  [2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 4, 2], // 4
  [2, 4, 2, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 2, 4, 2], // 5
  [2, 4, 2, 4, 2, 4, 4, 2, 2, 8, 2, 2, 4, 4, 2, 4, 2, 4, 2], // 6
  [2, 4, 4, 4, 4, 4, 4, 2, 5, 6, 7, 2, 4, 4, 4, 4, 4, 4, 2], // 7
  [2, 4, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 4, 2], // 8
  [2, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2], // 9
  [2, 4, 4, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 4, 4, 2], // 10
  [2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2], // 11
  [2, 4, 2, 2, 4, 2, 2, 2, 4, 2, 4, 2, 2, 2, 4, 2, 2, 4, 2], // 12
  [2, 4, 2, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 2, 4, 2], // 13
  [2, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 4, 2], // 14
  [2, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 2], // 15
  [2, 4, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 4, 2], // 16
  [2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2], // 17
  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], // 18
];

var MAP = [
  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], // 0
  [2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2], // 1
  [2, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 4, 2], // 2
  [2, 4, 2, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 2, 4, 2], // 3
  [2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 4, 2, 4, 2], // 4
  [2, 4, 2, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 2, 4, 2], // 5
  [2, 4, 2, 4, 2, 4, 4, 2, 2, 8, 2, 2, 4, 4, 2, 4, 2, 4, 2], // 6
  [2, 4, 4, 4, 4, 4, 4, 2, 5, 6, 7, 2, 4, 4, 4, 4, 4, 4, 2], // 7
  [2, 4, 2, 2, 2, 4, 4, 2, 2, 2, 2, 2, 4, 4, 2, 2, 2, 4, 2], // 8
  [2, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 2], // 9
  [2, 4, 4, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 4, 4, 2], // 10
  [2, 4, 4, 4, 4, 4, 4, 4, 4, 2, 4, 4, 4, 4, 4, 4, 4, 4, 2], // 11
  [2, 4, 2, 2, 4, 2, 2, 2, 4, 2, 4, 2, 2, 2, 4, 2, 2, 4, 2], // 12
  [2, 4, 2, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 2, 4, 2], // 13
  [2, 4, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 4, 2], // 14
  [2, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 4, 2, 4, 4, 4, 2], // 15
  [2, 4, 2, 2, 2, 2, 2, 2, 4, 2, 4, 2, 2, 2, 2, 2, 2, 4, 2], // 16
  [2, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 2], // 17
  [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], // 18
];

function generateMaze(pacmanRotation) {
  var maze = document.getElementById("maze-container");
  // var temp_ghosts = [red.id, pink.id, blue.id, orange.id]
  maze.innerHTML = "";
  for (var row = 0; row < MAP.length; row++) {
    for (var col = 0; col < MAP[row].length; col++) {
      check = MAP[row][col];
      if (check === 1) {
        maze.innerHTML += "<div class = 'pacman'></div>";
      } else if (check === 2) {
        maze.innerHTML += "<div class = 'wall'></div>";
      } else if (check === 3) {
        maze.innerHTML += "<div class = 'blank'></div>";
      } else if (check === 4) {
        maze.innerHTML += "<div class = 'coin'></div>";
      } else if (check === 5) {
        // red
        maze.innerHTML += "<div class = 'ghost' id ='red'></div>";
      } else if (check === 6) {
        maze.innerHTML += "<div class = 'ghost' id ='pink'></div>";
      } else if (check === 7) {
        maze.innerHTML += "<div class = 'ghost' id ='blue'></div>";
      } else if (check === 8) {
        maze.innerHTML += "<div class = 'ghost' id ='orange'></div>";
      }
    }
    maze.innerHTML += "<br />";
  }
  document.getElementsByClassName("pacman")[0].id = pacman.direction;
}

var pacman = {
  row: 13,
  col: 9,
  direction: "right",

  move: function () {
    var new_spot = false;
    if (pacman.direction === "right" && MAP[pacman.row][pacman.col + 1] !== 2) {
      MAP[pacman.row][pacman.col] = 3; // set where pacman was to empty in the MAP
      pacman.col++; // change internal attriutes
      new_spot = true;
    } else if (
      pacman.direction === "left" &&
      MAP[pacman.row][pacman.col - 1] !== 2
    ) {
      MAP[pacman.row][pacman.col] = 3;
      pacman.col--;
      new_spot = true;
    } else if (
      pacman.direction === "up" &&
      MAP[pacman.row - 1][pacman.col] !== 2
    ) {
      MAP[pacman.row][pacman.col] = 3;
      pacman.row--;
      new_spot = true;
    } else if (
      pacman.direction === "down" &&
      MAP[pacman.row + 1][pacman.col] !== 2
    ) {
      MAP[pacman.row][pacman.col] = 3;
      pacman.row++;
      new_spot = true;
    }
    if (new_spot) {
      if (MAP[pacman.row][pacman.col] === 4) {
        // if the spot pacman is in is a coin, add points
        CURRENTSCORE += 10;
      }
      MAP[pacman.row][pacman.col] = 1; // update pacman on the MAP
      // generateMaze()
    }
  },

  // rotate() {
  // 	// do something
  // }
};

// changing directions

function gameOver() {
  if (CURRENTSCORE === 1800) {
    return true;
  }
  for (var i = 0; i < GHOSTS.length; i++) {
    if (
      pacman.row === GHOSTS[i].row &&
      pacman.col === GHOSTS[i].col &&
      !GHOSTS[i].eatable
    ) {
      console.log("true");
      return true;
    }
  }
  console.log("false");
  return false;
}

function KeyIsDown(event) {
  var rotation = false;
  var move = true;
  if (event.keyCode === 37 && MAP[pacman.row][pacman.col - 1] !== 2) {
    if (pacman.direction === "left") {
      move = false;
    } else {
      pacman.direction = "left";
    }
  } else if (event.keyCode === 38 && MAP[pacman.row - 1][pacman.col] !== 2) {
    if (pacman.direction === "up") {
      move = false;
    } else {
      pacman.direction = "up";
    }
  } else if (event.keyCode === 39 && MAP[pacman.row][pacman.col + 1] !== 2) {
    if (pacman.direction === "right") {
      move = false;
    } else {
      pacman.direction = "right";
    }
  } else if (event.keyCode === 40 && MAP[pacman.row + 1][pacman.col] !== 2) {
    if (pacman.direction === "down") {
      move = false;
    } else {
      pacman.direction = "down";
    }
  }
  document.getElementsByClassName("pacman")[0].id = pacman.direction;
}

function start() {
  var countdown = 3;
  setInterval(function () {
    if (countdown > 0) {
      document.getElementById("start").innerHTML = countdown;
      countdown--;
    }
  }, 1000);
  setTimeout(function () {
    $("#start-screen").hide();
    game();
  }, 4000);
}

// GAME CODE BELOW
$(document).ready(generateMaze);

function game() {
  setInterval(function () {
    if (gameOver()) {
      clearInterval();
      $("#maze-container").css("opacity", "0.4");
      $("#game-over-screen").css("display", "block");
      $(".more").css("display", "none");
      document.getElementById("score").innerHTML =
        "Score: " + CURRENTSCORE.toString();
      setTimeout(function () {
        $("#game-over-screen").css("display", "block");
        $(".more").css("display", "block");
        $("#game-over-screen").removeClass("blink");
        $("#game-over-text").removeClass("blink");
        // $('#restart').show()
      }, 4000);
    } else {
      document.getElementById("curr-score").innerHTML = CURRENTSCORE;
      document.onkeydown = KeyIsDown;
      pacman.move();
      for (var i = 0; i < GHOSTS.length; i++) {
        if (!gameOver()) {
          GHOSTS[i].move();
        }
      }
      generateMaze();
    }
  }, 400);
}
