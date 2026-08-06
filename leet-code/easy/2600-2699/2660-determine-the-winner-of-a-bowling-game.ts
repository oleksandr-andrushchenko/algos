// You are given two 0-indexed integer arrays player1 and player2, representing the number of pins that player 1 and
// player 2 hit in a bowling game, respectively.
//
// The bowling game consists of n turns, and the number of pins in each turn is exactly 10.
//
// Assume a player hits xi pins in the ith turn. The value of the ith turn for the player is:
//
// 2xi if the player hits 10 pins in either (i - 1)th or (i - 2)th turn.
// Otherwise, it is xi.
// The score of the player is the sum of the values of their n turns.
//
// Return
//
// 1 if the score of player 1 is more than the score of player 2,
// 2 if the score of player 2 is more than the score of player 1, and
// 0 in case of a draw.

function isWinner(player1: number[], player2: number[]): number {
  function score(player: number[]): number {
    let total = 0;

    for (let i = 0; i < player.length; i++) {
      if (
        (i > 0 && player[i - 1] === 10) ||
        (i > 1 && player[i - 2] === 10)
      ) {
        total += player[i] * 2;
      } else {
        total += player[i];
      }
    }

    return total;
  }

  const score1 = score(player1);
  const score2 = score(player2);

  if (score1 > score2) {
    return 1;
  }

  if (score2 > score1) {
    return 2;
  }

  return 0;
}