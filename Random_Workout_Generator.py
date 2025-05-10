#Random Workout Generator
# This project creates a personalised workout routine by randomly selecting exercises based on user's preferences. Each time user runs the program, it generates a different workout.

import random

# List of strenght exercises
strength_exercises = {
    "Beginner": ["Wall Push-ups", "Side Plank", "Bodyweight Squats", "Knee Push-ups", "Glute Bridges", "Bird Dog", "Reverse Lunges", "Elevated Push-ups", "Dead Bug", "Chair Squats"],
    "Intermediate": ["Push-ups", "Lunges", "Squats", "Russian Twists", "Plank", "Bicep Curls", "Tricep Dips", "Superman Hold", "Walking Lunges", "Tricep Dips (on chair)"],
    "Advanced": ["Pull-ups", "Pistol Squats", "Handstand Push-ups", "One-arm Push-ups", "Crunches", "Plank Shoulder Taps", "Dragon Flag", "Bulgarian Split Squats", "Plyometric Push-ups", "L-sit Hold"]}

# List of cardio exercises
cardio_exercises = {
    "Beginner": ["Walking", "Marching in Place", "Step Touches (side to side)", "Low-impact Jumping Jacks", "High Knees", "Butt Kicks", "Seated Marches", "Light Cycling (stationary)", "Arm Circles", "Dancing (low intensity)"],
    "Intermediate": ["Jogging", "Jump Rope", "Mountain Climbers", "Skaters (side-to-side jumps)", "Stair Climbing", "Swimming", "Burpees", "High Knees (fast pace)", "Butt Kicks (fast pace)", "Shadow Boxing"],
    "Advanced": ["Running (fast pace)", "Sprint Intervals", "Jump Rope", "Burpees (full)", "Tuck Jumps", "Box Jumps", "Mountain Climbers (fast pace)", "Squat Jumps", "Jumping Lunges", "HIIT Circuits"]}

# Yoga exercises
yoga_exercises = {
    "Beginner": ["Mountain Pose (Tadasana)", "Child’s Pose (Balasana)", "Cat-Cow Pose (Marjaryasana-Bitilasana)", "Downward Facing Dog (Adho Mukha Svanasana)", "Seated Forward Fold (Paschimottanasana)", "Bridge Pose (Setu Bandhasana)",
                "Corpse Pose (Savasana)", "Standing Forward Fold (Uttanasana)", "Happy Baby (Ananda Balasana)", "Easy Twist (Supta Matsyendrasana)", "Cobra Pose (Bhujangasana)"],
    "Intermediate": ["Warrior I (Virabhadrasana I)", "Warrior II (Virabhadrasana II)", "Triangle Pose (Trikonasana)", "Boat Pose (Navasana)", "Camel Pose (Ustrasana)", "Half Moon Pose (Ardha Chandrasana)", "Extended Side Angle Pose (Utthita Parsvakonasana)"
                     "Plank Pose (Phalakasana)", "Pigeon Pose (Eka Pada Rajakapotasana)", "Reverse Warrior (Viparita Virabhadrasana)"],
    "Advanced": ["Handstand (Adho Mukha Vrksasana)", "Forearm Stand (Pincha Mayurasana)", "Scorpion Pose (Vrschikasana)", "Firefly Pose (Tittibhasana)", "Eight Angle Pose (Astavakrasana)", "Peacock Pose (Mayurasana)",
                 "One-Legged Wheel Pose (Eka Pada Urdhva Dhanurasana)", "Flying Crow Pose (Eka Pada Galavasana)", "Pyramid Pose (Parsvottanasana)", "Wheel Pose (Urdhva Dhanurasana)"]}


# Getting the user input:
def get_user_input():
    print()
    print("Choose a workout type: ")
    print("1. Strength Training")
    print("2. Cardio Training")
    print("3. Yoga")

    workout_choice = input("Enter 1, 2 or 3: ").strip()

    print("\nChoose a difficulty level:")
    print("1. Beginner")
    print("2. Intermediate")
    print("3. Advanced")

    difficulty_choice = input("Enter 1, 2 or 3: ").strip()

    return workout_choice, difficulty_choice

# Mapping user input to difficulty levels:
def map_difficulty(workout_choice):
    mapping = {
        "1": "Beginner",
        "2": "Intermediate",
        "3": "Advanced"
    }

    return mapping.get(workout_choice, None)


# Generate random workout
def generate_workout(workout_choice, difficulty_level):
    if workout_choice == "1":
        exercises = strength_exercises.get(difficulty_level, [])
    elif workout_choice == "2":
        exercises = cardio_exercises.get(difficulty_level, [])
    elif workout_choice == "3":
        exercises = yoga_exercises.get(difficulty_level, [])
    else:
        print("Invalid workout choice.")
        return None

    return random.sample(exercises, 5)

# Display the workout Plan
def display_workout(workout):
    if workout:
        print()
        print("Your workout routine for today:")
        for i, exercise in enumerate(workout, start=1):
            print(f"{i}. {exercise}")
        print("Let's get started!")
        print()
    else:
        print("No workout generated. Please try again.")
        print()

# Combine Everything
def main():
    print("Welcome to the Random Workout Generator!")

    while True:
        workout_choice, difficulty_choice = get_user_input()
        difficulty_level = map_difficulty(difficulty_choice)

        if not difficulty_level:
            print("Invalid difficulty choice. Please enter 1, 2, or 3.")
            print()
            continue

        workout = generate_workout(workout_choice, difficulty_level)

        if workout:
            display_workout(workout)

        again = input("Would you like another workout? (Yes/No): ").strip().lower()
        if again not in ["yes", "y"]:
            print("Thank you for using the Workout Generator! Stay fit!")
            break

main()