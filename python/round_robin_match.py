competitions = [
['Panthers', 'Lionesses'],
['Lionesses', 'Dolphins'],
['Dolphins', 'Panthers'],
]
results = [0, 0, 1]

# competitions = [
#      ['A', 'B'],
#      ['B', 'C'],
#      ['C', 'A'],
#      ['D', 'C'],
#      ['E', 'D'],
#      ['D', 'A'],
#  ]
# 
# results = [0, 1, 1, 1, 0, 1]

# competitions = [
#     ['Panthers', 'Lionesses'],
#     ['Panthers', 'Dolphins'],
#     ['Dolphins', 'Lionesses'],
# ]
# 
# results = [0, 0, 0]



points = {}

for ele  in range (len(competitions)):
    home_team , away_team = competitions[ele]
    result = results[ele]

        
    if home_team not in points:
        points[home_team] = 0
    if away_team not in points:
        points[away_team] = 0
        
    if result == 0:
        points[away_team] += 3
    else:
        points[home_team] += 3
        
winner = max (points, key=points.get)
print(f"The winner is : {winner}")
        

