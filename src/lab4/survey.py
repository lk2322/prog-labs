from collections import defaultdict

age_groups = [int(arg) for arg in input().split()]

age_group_dict = defaultdict(list)

while True:
    line = input()
    if line == "END":
        break
    name, age = line.split(',')
    age = int(age)

    group_found = False
    for i, upper_bound in enumerate(age_groups):
        if age <= upper_bound:
            age_group = f"{age_groups[i - 1] + 1}-{upper_bound}" if i > 0 else f"0-{upper_bound}"
            age_group_dict[age_group].append((name, age))
            group_found = True
            break

    if not group_found:
        age_group = f"{age_groups[-1] + 1}+"
        age_group_dict[age_group].append((name, age))

for age_group, respondents in sorted(age_group_dict.items(), reverse=True):
    if respondents:
        sorted_respondents = sorted(respondents, key=lambda x: (-x[1], x[0]))
        formatted_respondents = [f"{name} ({age})" for name, age in sorted_respondents]
        print(f"{age_group}: {', '.join(formatted_respondents)}")
