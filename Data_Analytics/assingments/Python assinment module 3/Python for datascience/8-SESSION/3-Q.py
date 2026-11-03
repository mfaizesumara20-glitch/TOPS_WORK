# teams = [
    # "Chennai Super Kings",
    # "Mumbai Indians",
    # "Royal Challengers Bengaluru",
    # "Kolkata Knight Riders",
    # "Sunrisers Hyderabad",
    # "Rajasthan Royals",
    # "Delhi Capitals",
    # "Punjab Kings",
    # "Lucknow Super Giants",
    # "Gujarat Titans"
# ]
# for team in teams:
#     if len(team) > 6:
#         print(team)


def print_long_team_names(teams):
    for team in teams:
        if len(team) <= 6:
            continue
        print(team)

teams = [
    "CSK",
    "MI",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders",
    "Sunrisers Hyderabad",
    "Rajasthan Royals",
    "Delhi Capitals",
    "Punjab Kings",
    "Lucknow Super Giants",
    "Gujarat Titans"
]

print_long_team_names(teams)