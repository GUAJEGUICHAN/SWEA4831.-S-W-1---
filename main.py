def find_station(K,N,M):#충전소 찾고 충전횟수 출력 (변수 이동가능 거리, 정류장 개수, 충전소 개수)
  temp_position = 0#현재위치
  charge_count = 0#충전 횟수
  while(temp_position!=N):#종점까지 갈때까지 반복한다.
    if(temp_position+K>=N):#종점이 현재에서 이동가능 거리안에 있을 때
      temp_position=N#종점으로 간다.
      break
    for i in range(len(M)-1,-1,-1):
      if(temp_position+K>=M[i]):#역순으로 충전소가 거리에 포함 되어있다면 /최대거리 값을 찾기 위함.
        temp_position = M[i] #현재위치를 그 충전소로 옮긴다
        charge_count+=1#충전횟수를 하나 늘린다.
        M = M[i+1:]#지나간 정류장은 없앤다.
        break#다시 반복하기위해 나간다.
      if(i==0):#만약 가장 가까운 충전소가 이동가능거리에 없다면
        return 0;#끝낸다.


  return charge_count


T = int(input())#노선 수
A = []
for test_case in range(1, T + 1): #노선 수만큼 반복
  K,N,M = map(int, input().split())  #이동가능 거리, 정류장 개수, 충전소 개수
  M = list(map(int, input().split()))[:M] #충전소 위치(변수 재사용)
  A.append(find_station(K,N,M))#노선별 출력할 최소 충전횟수를 A배열에 모아둠

for test_case in range(1, T + 1): #노선별 최소 충전횟수 출력
  print("#"+str(test_case), A[test_case-1])

