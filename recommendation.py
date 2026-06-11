courses = {
    "Python Basics": ["python", "programming", "coding"],
    "Web Development": ["html", "css", "javascript"],
    "Machine Learning": ["python", "ai", "machine learning"],
    "Cloud Computing": ["cloud", "aws", "azure"],
    "Data Science": ["python", "data", "statistics"]
}

user_interest = input("Enter your interests separated by comma: ")
user_interest = user_interest.lower().split(",")

recommendations = []

for course, skills in courses.items():
    score = 0
    for interest in user_interest:
        interest = interest.strip()
        if interest in skills:
            score += 1
    recommendations.append((course, score))
recommendations.sort(key=lambda x: x[1], reverse=True)

print("\nRecommended Courses:\n")

for course, score in recommendations:
    if score > 0:
        print(course, "- Match Score:", score)