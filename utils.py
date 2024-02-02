# utils.py
import time
import random

def generate_mcq(question, options, answer):
    """
    Generate a multiple-choice question (MCQ) with the question, options, and correct answer.
    """
    mcq = {
        'Question': question,
        'Options': options,
        'Answer': answer
    }
    return mcq

def shuffle_options(options):
    """
    Shuffle the options of a multiple-choice question.
    """
    shuffled_options = random.sample(options, len(options))
    return shuffled_options

def calculate_time_remaining(start_time, max_time):
    """
    Calculate the time remaining for a timed MCAT section.
    """
    # Calculate elapsed time
    elapsed_time = time.time() - start_time
    # Calculate time remaining
    time_remaining = max_time - elapsed_time
    return time_remaining

# utils.py

def generate_flashcards(topic, questions_answers):
    """
    Generate flashcards for a given topic based on a list of questions and answers.
    Each flashcard contains a question and its corresponding answer.
    """
    flashcards = []
    for question, answer in questions_answers:
        flashcard = {
            'Topic': topic,
            'Question': question,
            'Answer': answer
        }
        flashcards.append(flashcard)
    return flashcards

def format_date(date):
    return date.strftime("%Y-%m-%d")

def calculate_percentage(score, total):
    """
    Calculate the percentage score based on the number of correct answers and the total number of questions.
    """
    if total == 0:
        return 0
    return (score / total) * 100

def save_progress(user, topic, score, total_questions):
    """
    Save the user's progress in a specific topic, including the score achieved and total questions attempted.
    """
    # Logic to save progress to a database or file
    pass

def load_progress(user, topic):
    """
    Load the user's progress in a specific topic, including the score achieved and total questions attempted.
    """
    # Logic to load progress from a database or file
    pass

# Other utility functions can be added as needed


def record_response(question_id, selected_option, user_responses):
    """
    Record the user's response to a question.
    """
    user_responses[question_id] = selected_option

def evaluate_responses(user_responses, correct_answers):
    """
    Evaluate the user's responses and calculate the score.
    """
    score = 0
    for question_id, selected_option in user_responses.items():
        if selected_option == correct_answers[question_id]:
            score += 1
    return score

def generate_study_plan(subjects, topics):
    """
    Generate a study plan with a list of subjects and topics to cover.
    """
    study_plan = {}
    for subject in subjects:
        study_plan[subject] = topics[subject]
    return study_plan

# Other utility functions can be added as needed
