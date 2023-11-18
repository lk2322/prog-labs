from collections import defaultdict


class AgeGroupClassifier:
    def __init__(self, age_groups):
        self.age_groups = age_groups
        self.age_group_dict = defaultdict(list)

    def classify_age_group(self, age):
        for i, upper_bound in enumerate(self.age_groups):
            if age <= upper_bound:
                return f"{self.age_groups[i - 1] + 1}-{upper_bound}" if i > 0 else f"0-{upper_bound}"

        return f"{self.age_groups[-1] + 1}+"

    def process_input(self, name, age):
        age_group = self.classify_age_group(age)
        self.age_group_dict[age_group].append((name, age))

    def display_results(self):
        for age_group, respondents in sorted(self.age_group_dict.items(), reverse=True):
            if respondents:
                sorted_respondents = sorted(respondents, key=lambda x: (-x[1], x[0]))
                formatted_respondents = [f"{name} ({age})" for name, age in sorted_respondents]
                print(f"{age_group}: {', '.join(formatted_respondents)}")


def main():
    age_groups = [int(arg) for arg in input("Enter age groups: ").split()]
    age_group_classifier = AgeGroupClassifier(age_groups)

    while True:
        line = input()
        if line == "END":
            break
        name, age = line.split(',')
        age_group_classifier.process_input(name, int(age))

    age_group_classifier.display_results()


if __name__ == "__main__":
    main()
