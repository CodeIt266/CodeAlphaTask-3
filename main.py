#define a class for excercise 
class Excercise:
    def __init__(self, name, duration_min, intensity):
        self.name = name
        self.duration_min = duration_min
        self.intensity = intensity

#define a class for user
class User:
    def __init__(self, username, age):
        self.name = username
        self.age = age
        self.exercise = []
        self.goals = {}

    def log_exercise(self,exercise):
        self.exercise.append(exercise)


    def calculate_calories_burned(self):
        total_calories = 0
        for excercise in self.exercise:
            calories = excercise.duration_min * excercise.intensity
            total_calories = calories
        return total_calories
    
    def set_goal(self, goal_type, target_value):
        self.goals[goal_type] = target_value


    def track_progress(self):

        total_calories_burned = self.calculate_calories_burned()
        if 'calories' in self.goals:
            goal_calories = self.goals['calories']
            progress_percentage = (total_calories_burned / goal_calories) * 100
            return progress_percentage
        else:
            return None
        

#function to log an excercise
def log_exercise(user):
    name = input("Enter the name of excercise: ")
    duration = int(input("Enter duration (minutes): "))
    intensity = int(input("Enter intensity (1-10): "))
    exercise = Excercise(name, duration, intensity)
    user.log_exercise(exercise)
    print("Excercise logged successfully")

#function to set goal
def set_goal(user):
    goal_type = input("Enter goal type (e.g., calories): ")
    target_value = int(input("Enter target value: "))
    user.set_goal(goal_type, target_value)
    print("Goal set successfully")


#function to track progress
def track_progress(user):
    progress = user.track_progress()
    if progress is not None:
        print(f"Progress towards goal: {progress:.2f}%")
    else:
        print("No goal set yet")

#main function for user interaction
def main():
    username = input("Enter your username: ")
    age = int(input("Enter your age: "))
    user = User(username, age)

    while True:
        print("\n--- Fitness Tracking System ---")
        print("1. Log excercise")
        print("2. Set goal")
        print("3. Track progress")
        print("4. Exit")

        choice = int(input("Enter your choice (1-4): "))
        if choice == 1:
            log_exercise(user)
        elif choice == 2:
            set_goal(user)
        elif choice == 3:
            track_progress(user)
        elif choice == 4:
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()