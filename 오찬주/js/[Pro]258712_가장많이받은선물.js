// 두 사람 중 많은 선물을 준 사람이 다음 달에 선물을 하나 받는다
// if 선물 주고 받은 기록 없거나 주고 받은 수 같다면, 선물지수가 더 큰 사람이 작은 사람에게 선물 받음
// 선물지수(score): 자신이 친구들에게 준 선물의 수 - 받은 선물의 수
// 선물 지수 같다면 선물 주고 받지 않음
// return 선물 가장 많이 받는 사람의 선물 수
// friends, gifts
// gifts는 split으로 나눈 후 변수에 담기, 변수[0] = 준 사람, 변수[1] = 받은 사람

// 이름 저장 객체 (map으로)
// 이번 달 선물 개수 저장할 배열(giftNum) - 2차원 : gift[i][j] : i가 j에게 선물 줌
// 선물 지수 저장할 배열(score)
// 다음 달 받을 선물 저장할 배열

const friends = ["muzi", "ryan", "frodo", "neo"];
const gifts = [
  "muzi frodo",
  "muzi frodo",
  "ryan muzi",
  "ryan muzi",
  "ryan muzi",
  "frodo muzi",
  "frodo ryan",
  "neo muzi",
];

function solution(friends, gifts) {
  //친구들의 수 저장 for 동적 저장
  const len = friends.length;
  //이름 저장
  const nameMap = new Map();
  //이번달 선물 개수 선언
  const giftNum = new Array(len).fill(0).map((_) => new Array(len).fill(0));

  //선물 지수 선언
  const score = new Array(len).fill(0);
  //다음달 받을 선물 선언
  const nextGift = new Array(len).fill(0);

  //친구 이름과 인덱스 매핑
  friends.forEach((name, index) => {
    nameMap.set(name, index);
  });

  //선물 주고 받은 내역
  gifts.forEach((count) => {
    const [giver, receiver] = count.split(" ");
    giftNum[nameMap.get(giver)][nameMap.get(receiver)]++;
  });

  //선물지수 선언 (자신이 친구들에게 준 선물의 수 - 받은 선물의 수)
  //각 친구가 다른 친구에게 준 횟수 계산

  for (let i = 0; i < len; i++) {
    score[i] = giftNum[i].reduce((acc, cur) => (acc += cur), 0);
  }

  //각 친구가 선물 받은 횟수 빼주기
  for (let i = 0; i < len; i++) {
    for (let j = 0; j < len; j++) {
      score[i] -= giftNum[j][i];
    }
  }

  //다음달 받을 선물 (i와 j 비교하기)
  for (let i = 0; i < len; i++) {
    for (let j = i + 1; j < len; j++) {
      if (giftNum[i][j] > giftNum[j][i]) nextGift[i]++;
      if (giftNum[i][j] < giftNum[j][i]) nextGift[j]++;
      if (giftNum[i][j] == giftNum[j][i]) {
        if (score[i] > score[j]) nextGift[i]++;
        if (score[i] < score[j]) nextGift[j]++;
      }
    }
  }
  return Math.max(...nextGift);
}

console.log(solution(friends, gifts));

//아휴 이게 머야 이게 먼데!!! 디질뻔했네!!!

//다른 사람 풀이

function solution(friends, gifts) {
  const length = friends.length;
  const giftPoints = new Array(length).fill(0);
  //index?? friends 매핑한 느낌 (인덱스로)
  const index = {};
  const record = [];
  const points = new Array(length).fill(0);
  for (let i = 0; i < length; i++) {
    record[i] = new Array(length).fill(0);
    index[friends[i]] = i;
  }
  for (const gift of gifts) {
    const [giver, taker] = gift.split(" ");
    record[index[giver]][index[taker]] += 1;
    giftPoints[index[giver]] += 1;
    giftPoints[index[taker]] -= 1;
  }
  for (let i = 0; i < length; i++) {
    for (let j = 0; j < length; j++) {
      if (record[i][j] > record[j][i]) {
        points[i] += 1;
      } else if (record[i][j] === record[j][i]) {
        if (giftPoints[i] > giftPoints[j]) {
          points[i] += 1;
        }
      }
    }
  }
  return Math.max(...points);
}
