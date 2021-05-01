N = int(input())
status = [tuple(map(int,input().split())) for _ in range(N)]
team = tuple(range(3))
power = min(max(status[j][i] for j in team) for i in range(5))
for i in range(3,N):
	newteams = [(i, team[1], team[2]), (team[0], i, team[2]), (team[0], team[1], i)]
	for newteam in newteams:
		newpower = min(max(status[j][i] for j in newteam) for i in range(5))
		if newpower > power:
			team = newteam
			power = newpower
print(power)
