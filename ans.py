while 1:
  try:
    M,N,K = map(int,input().split())
    K -=2
    peanut = []
    for i in range(M):
      peanut.append(input())
    peanut_list = []
    get_peanut = set()
    sum_peanut = 0 #花生的加總
    times = 0 #要走的步數
    for i in peanut:
      peanut_list.append(list(i.split()))
    for i,k in enumerate(peanut_list):
      for j in range(len(k)):
        if k[j] != "0":
          get_peanut.add((int(k[j]),i,j))  #把有花生的位子放入set

    get_peanut1 = (sorted(get_peanut, key=lambda x:x[0])) #排序 把最多花生的放第一個
    get_peanut1.reverse()  #反轉才會是第一個
    for i,j in enumerate(get_peanut1):
      if i != 0:
        times = abs(get_peanut1[i][1] - get_peanut1[i-1][1]) + abs(get_peanut1[i][2]-get_peanut1[i-1][2]) +j[1] #計算去程與回程
      if i == 0 and K - j[1]*2 > 0 :
        K -= j[1]+1
        sum_peanut += j[0]
      elif K - times > 0 and i != 0 :
        K -= (times+1 - j[1])
        sum_peanut += j[0]
      else:
        break
    print(sum_peanut)
    print()
    input()
  except:
    break