# Backend code for managing user data

# Global dictionary to store user scores
user_scores = {
    'user1': 0,
    'user2': 0
}

# Function to initialize user data
def initialize_data():
    """Initializes the user data by setting scores to zero."""
    global user_scores
    user_scores = {'user1': 0, 'user2': 0}

# Function to get the score for a specific user
def get_score(user):
    """Returns the score for the specified user."""
    return user_scores.get(user, 0)

# Function to update the score for a specific user
def update_score(user, score_change):
    """Updates the user's score by adding the specified score_change."""
    global user_scores
    if user in user_scores:
        user_scores[user] += score_change
    else:
        user_scores[user] = score_change

# Function to reset scores for all users
def reset_scores():
    """Resets the scores for all users to zero."""
    global user_scores
    user_scores = {'user1': 0, 'user2': 0}
