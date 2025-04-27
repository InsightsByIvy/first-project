#Random Workout Generator
#This project creates a personalised workout routine by randomly selecting exercises based on user's preferences. Each time user runs the program, it generates a different workout.

import random

#List of strenght exercises
strengh_exercises = ["Push-ups", "Pull-ups", "Squats", "Lunges", "Plank", "Bicep Curls", 
                     "Tricep Dips", "Crunches", "Russian Twists", "Glute Bridges", "Side Plank", "Plank Shoulder Taps"]

#List of cardio exercises
cardio_exerciese = ["Jump Rope", "Running", "Burpees", "Jumping Jacks", "Mountain Climber",
                    "High Knees", "Jumping Lunges", "Squat Jumps"]

# Yoga exercises
yoga_exercises = ["Downward Facing Dog", "Child's Pose", "Triangle Pose", "Warrior I", "Warrior II", "Cobra Pose", "Bridge Pose"
                  "Lotus Pose", "Extended Side Angle", "Standing Forward Bend", "Reverse Warrior", "Pyramid Pose", "Low Lunge",
                   "Tree Pose", "Cat-Cow Stretch", "Seated Forward Bend", "Happy Baby Pose", "Supine Spinal Twist"]

def get_user_input():
    print("Choose a workout type: ")
    print("1. Strength Training")
    print("2. Cardio Training")
    print("3. Yoga")

    choice = input("Enter 1, 2 or 3: ")
    return choice


#Generate random workout
def generate_workout(choice):
    if choice == "1":
        workout = random.sample(strengh_exercises, 5)
    elif choice == "2":
        workout = random.sample(cardio_exerciese, 5)
    elif choice == "3":
        workout = random.sample(yoga_exercises, 5)
    else:
        print("Invalid Choice! Please enter 1, 2 or 3.")
        return None
    
    return workout

#Display the workout Plan
def display_workout(workout):
    if workout:
        print("Your workout routine for today:")
        for i, excercise in enumerate(workout, start=1):
            print(f"{i}. {excercise}")
        print("Let's get started!")
    else:
        print("No workout generated. Please try again.")

#Combine Everything
def main():
    print("Welcome to the Random Workout Generator!")

    while True:
        choice = get_user_input()
        workout = generate_workout(choice)

        if workout:
            display_workout(workout)

        again = input("Would you like another workout? (Yes/No): ").strip().lower()
        if again != "yes":
            print("Thank you for using the Workout Generator! Stay fit! ")
            break

main()