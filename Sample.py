import random
hands = ['ぐー' , 'ちょき' , 'ぱー']
print('0 = ぐー 1 =ちょき 2 = ぱー')

while True:
  input_str = input ('ここに数字を入力')
  hand_num = int(input_str)
  player_hand = hands[hand_num]
  computer_hand_num = random.randrange(3)
  computer_hand = hands[computer_hand_num]
  print('あなたは' +player_hand+ 'を出しました')
  print('相手は' +computer_hand+'を出しました')

  calcresult = hand_num - computer_hand_num
  if calcresult == 0:
    print('あいこ！')
  elif calcresult == -1 or calcresult == 2:
    print('勝利！')
    break
  else:
    print('負け！')
    break