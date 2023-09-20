// this is not currently used, since the array model provides a better indication of progress
const initialScores = {
  "MAX": 1500,
  "GRACEY": 1500,
  "BOGDAN": 1500,
  "CHRISTIAN": 1500,
  "JESSIE": 1500,
  "HAYWAD": 1500,
  "GRACEZ": 1500,
  "JUSTIN": 1500,
  "PAUL": 1500,
  "SAMSON": 1500,
  "PHILLIP": 1500,
  "PREM": 1500,
  "SHUOTONG": 1500,
  "ANNA": 1500,
  "CARMEN": 1500
}

// each player starts with 1500 score. Subsequent wins/losses will be pushed to the end of this array
const initialScoresArray = {
  "MAX": [1500],
  "GRACEY": [1500],
  "BOGDAN": [1500],
  "CHRISTIAN": [1500],
  "JESSIE": [1500],
  "HAYWAD": [1500],
  "GRACEZ": [1500],
  "JUSTIN": [1500],
  "PAUL": [1500],
  "SAMSON": [1500],
  "PHILLIP": [1500],
  "PREM": [1500],
  "SHUOTONG": [1500],
  "ANNA": [1500],
  "CARMEN": [1500]
}
/*
  During a tournament, players will not be punished for losing. 
  A player who advances to the next round will always have a higher score than one who did not advance.
  Furthermore, the farther one advances in the tournament, the less points they will gain for the win, as the grap would grow too large
*/
const calculateTournamentRanking = (playerA, playerB, scoreA, scoreB, round) => {
  // look up the rating of each player for the current match
  const ratingA = initialScores[playerA];
  const ratingB = initialScores[playerB];

  // In round 1, the tournamentMultiplier is 1. in round 2, it's 2/3. In round 3, it's 2/4, etc.
  const tournamentMultiplier = round !== null ? 2 / (round + 1) : 1;

  // winners can have a little bit more points, as a treat
  const winMultiplier = 1.15;

  const kConstant = 32;

  const marginOfVictoryMultiplier = Math.sqrt(Math.abs(scoreA - scoreB) / 2);

  // expected win rate of each player, based on their current points. Players with equal rating will both have 0.5
  const expectedA = 1 / (1 + Math.pow(10, ((ratingB - ratingA) / 400)));
  const expectedB = 1 - expectedA;

  // player A wins vs player B, player A gains points, playerB does not lose points
  if (scoreA > scoreB) {
    const newA = ratingA + (kConstant * winMultiplier * marginOfVictoryMultiplier * tournamentMultiplier * (1 - expectedA));
    initialScores[playerA] = newA;
  } else {
    const newB = ratingB + (kConstant * winMultiplier * marginOfVictoryMultiplier * tournamentMultiplier * (1 - expectedB));
    initialScores[playerB] = newB;
  }
}

/*
  A regular match will lower the rating of the loser.
  The increase/decrease in score is based on the expected win rate of each player.
  Therefore, an upset wqill have the winner gain more points, and the loser will lose more points than usual. 

  TODO: Create a calculateMatchRankingArray, or simply just adapt this to work with score arrays instead of scores
*/
const calculateMatchRanking = (playerA, playerB, scoreA, scoreB) => {
  const expectedA = 1 / (1 + Math.pow(10, (initialScores[playerB] - initialScores[playerA]) / 400));
  const expectedB = 1 - expectedA;

  // lower kConstant for regular match games in order to offset the amount of points one can gain/lose
  const kConstant = 24;

  const marginOfVictoryMultiplier = Math.sqrt(Math.abs(scoreA - scoreB) / 2);

  if (scoreA > scoreB) {
    const newA = initialScores[playerA] + (kConstant * marginOfVictoryMultiplier * (1 - expectedA));
    const newB = initialScores[playerB] + (kConstant * marginOfVictoryMultiplier * (0 - expectedB));
    console.log(`MATCH: ${playerA}(${initialScores[playerA].toFixed(2)}) vs ${playerB}(${initialScores[playerB].toFixed(2)}): ${playerA} WINS. +${(kConstant * marginOfVictoryMultiplier * (1 - expectedA)).toFixed(2)}    /    ${(kConstant * marginOfVictoryMultiplier * (0 - expectedB)).toFixed(2)}`)
    initialScores[playerA] = newA;
    initialScores[playerB] = newB;
  } else {
    const newA = initialScores[playerA] + (kConstant * marginOfVictoryMultiplier * (0 - expectedA));
    const newB = initialScores[playerB] + (kConstant * marginOfVictoryMultiplier * (1 - expectedB));
    console.log(`MATCH: ${playerA}(${initialScores[playerA].toFixed(2)}) vs ${playerB}(${initialScores[playerB].toFixed(2)}): ${playerB} WINS. +${(kConstant * marginOfVictoryMultiplier * (1 - expectedB)).toFixed(2)}    /    ${(kConstant * marginOfVictoryMultiplier * (0 - expectedA)).toFixed(2)}`)
    initialScores[playerA] = newA;
    initialScores[playerB] = newB;
  }
}

/*
  Instead of reading from the player's score, this function reads from the last value in the player's score array. 
  Therefore, we can see a sort-of timeline of a player's score. Player's scores at the end of a match are placed at the end of their array

  TODO: There is a glaring issue with the algorithm: Samson ends up with more points than Haywad, despite the fact that Haywad advanced farther in the tournament. 
  The margin of victory should matter less to the winner, or the tournamentMultiplier should be slightly larger to compensate.
*/
const calculateTournamentRankingArray = (playerA, playerB, scoreA, scoreB, round) => {
  // look up the rating of each player for the current match
  const ratingA = initialScoresArray[playerA][initialScoresArray[playerA].length - 1];
  const ratingB = initialScoresArray[playerB][initialScoresArray[playerB].length - 1];

  // In round 1, the tournamentMultiplier is 1. in round 2, it's 2/3. In round 3, it's 2/4, etc.
  const tournamentMultiplier = round !== null ? 2 / (round + 1) : 1;

  const winMultiplier = 1.15;

  const kConstant = 32;

  const marginOfVictoryMultiplier = Math.sqrt(Math.abs(scoreA - scoreB) / 2);

  const expectedA = 1 / (1 + Math.pow(10, ((ratingB - ratingA) / 400)));
  const expectedB = 1 - expectedA;

  if (scoreA > scoreB) {
    const newA = ratingA + (kConstant * winMultiplier * marginOfVictoryMultiplier * tournamentMultiplier * (1 - expectedA));
    initialScoresArray[playerA].push(newA);
    initialScoresArray[playerB].push(initialScoresArray[playerB][initialScoresArray[playerB].length - 1])
  } else {
    const newB = ratingB + (kConstant * winMultiplier * marginOfVictoryMultiplier * tournamentMultiplier * (1 - expectedB));
    initialScoresArray[playerA].push(initialScoresArray[playerA][initialScoresArray[playerA].length - 1])
    initialScoresArray[playerB].push(newB);
  }
}

const matchArray = [
  ["MAX", "GRACEY", 15, 13, 1], // round of 16
  ["BOGDAN", "CHRISTIAN", 15, 1, 1],
  ["JESSIE", "HAYWAD", 13, 15, 1],
  ["GRACEZ", "JUSTIN", 15, 10, 1],
  ["PAUL", "SAMSON", 5, 15, 1],
  ["PHILLIP", "PREM", 8, 15, 1],
  ["SHUOTONG", "ANNA", 5, 15, 1],
  ["MAX", "BOGDAN", 6, 15, 2], // quarterfinals
  ["HAYWAD", "GRACEZ", 15, 9, 2],
  ["SAMSON", "PREM", 9, 15, 2],
  ["ANNA", "CARMEN", 15, 3, 2],
  ["BOGDAN", "HAYWAD", 15, 4, 3], // semifinals
  ["BOGDAN", "HAYWAD", 15, 1, 4],
  ["PREM", "ANNA", 15, 8, 3],
  ["PREM", "ANNA", 15, 6, 4],
  ["BOGDAN", "PREM", 15, 10, 4], // finals
  ["BOGDAN", "PREM", 15, 7, 5],

  // after the tournament
  // ["PREM", "HAYWAD", 13, 15, null],
  // ["PREM", "SAMSON", 6, 11, null],
  // ["PREM", "SAMSON", 11, 7, null],
  // ["PREM", "SAMSON", 11, 5, null],
  // ["SAMSON", "PREM", 6, 11, null],
  // ["PAUL", "PHILLIP", 12, 15, null],
  // ["PREM", "PHILLIP", 12, 3, null],
  // ["JUSTIN", "ANNA", 7, 11, null],
  // ["ANNA", "GRACEY", 15, 7, null],
  // ["SAMSON", "PREM", 11, 13, null],
  // ["PHILLIP", "SAMSON", 12, 15, null],
  // ["PREM", "SAMSON", 11, 5, null],
  // ["PREM", "SAMSON", 12, 10, null],
  // ["HAYWAD", "SAMSON", 11, 15, null],
  // ["PAUL", "SAMSON", 11, 15, null],
  // ["ANNA", "SAMSON", , 15, null],
  // ["PHILLIP", "PAUL", 8, 15, null],
  // ["PHILLIP", "PAUL", 10, 15, null],
  // ["PAUL", "SAMSON", 12, 15, null],


  // ["BOGDAN", "PREM", 14, 12, null],
  // ["JUSTIN", "GRACEZ", 15, 10, null],
  // ["JUSTIN", "ANNA", 8, 15, null],
  // ["PHILLIP", "PAUL", 14, 16, null],
  // ["PREM", "HAYWAD", , , null],
  // ["PAUL", "PHILLIP", 11, 15, null],
  // ["ANNA", "PHILLIP", 10, 15, null],
  // ["GRACEZ", "SAMSON", 8, 11, null],

];

for (const match of matchArray) {
  const playerA = match[0];
  const playerB = match[1];
  const scoreA = match[2];
  const scoreB = match[3];
  const round = match[4];
  if (round === null) {
    calculateMatchRanking(playerA, playerB, scoreA, scoreB);
  } else {
    // calculateTournamentRanking(playerA, playerB, scoreA, scoreB, round)
    calculateTournamentRankingArray(playerA, playerB, scoreA, scoreB, round)
  }
}

// the amount of games one has played during the tournment is 1 + number of elements in the array
console.log("After Tournament: ", initialScoresArray);

let sortableScores = []
for (const ranking in initialScoresArray) {
  sortableScores.push([ranking, initialScoresArray[ranking][initialScoresArray[ranking].length - 1]])
}

sortableScores.sort((a, b) => {return b[1] - a[1]});

console.log("Final Result: ", sortableScores);

// OLD FORMULA GRAVEYARD
// (A: win, B: loss)
// newA = ratingA + roundMultiplier*32*(1.5 * Math.sqrt(0.5*(scoreA-scoreB))*expectedA)
// newB = ratingB + roundMultiplier*32*(-0.5 * Math.sqrt(Math.abs(scoreB-scoreA))*expectedB)

// (A: loss, B: win)
// newA = ratingA + roundMultiplier*32*(-0.5 * Math.sqrt(Math.abs(scoreA-scoreB))*expectedA)
// newB = ratingB + roundMultiplier*32*(1.5 * Math.sqrt(0.5*(scoreB-scoreA))*expectedB)