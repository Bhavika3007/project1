def calculate_positive_feedback_percentage(ratings):
    if not ratings:  # Handle case where there are no ratings
        return 0.0

    positive_ratings = [rating for rating in ratings if rating == 4 or rating == 5]
    positive_percentage = (len(positive_ratings) / len(ratings)) * 100
    return positive_percentage

ratings = [5, 4, 3, 5, 2, 4, 1, 5]

positive_feedback_percentage = calculate_positive_feedback_percentage(ratings)

print(f"Positive Feedback: {positive_feedback_percentage}%")
