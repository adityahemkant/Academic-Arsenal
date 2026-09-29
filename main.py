from scientific_calculator import cal
from grade_evaluator import grade
from attendence_evaluator import attendence
while True:
    print("\n" + "=" * 80)
    print("           ---Academic-Aresenal---          ")
    print("=" * 80)
    print("  DEVELOPER : ADITYA PATIL")
    print("  REG NO    : 26BCE10778")
    print("  PROJECT   : Academic-Arsenal [CALCULATOR + ATTENDANCE + GRADES]") 
    print("-" * 80)
    print("  ABOUT:")
    print("  An all-in-one console application built to handle")
    print("  SCIENTIFIC CALCULATOR, GRADE EVALUATOR, and ATTENDANCE EVALUATOR tasks.")
    print("=" * 80)
    print("  [1] Scientific Calculator")
    print("  [2] Grade Evaluator")
    print("  [3] Attendance Evaluator")
    print("  [0] Exit ")
    print("=" * 80)

    choice = input("Enter your choice (0-3) >>> ").strip()

    # 0 Exit
    if choice == "0":
        print("\n" + "*" * 80)
        print("  Logging off: ADITYA PATIL (26BCE10778)")
        print("  Thanks for using the tool in arsenal. Goodbye!")
        print("*" * 80 + "\n")
        break

    # 1 Scientific Calculator
    elif choice == "1":
        print("\nOpening Calculator...")
        cal()  # Calls your calculator function
        input("\nPress Enter to return to main menu...")

    # 2 Grade Evaluator
    elif choice == "2":
        print("\nOpening Grade Evaluator...")
        grade()   # Calls your grade evaluator function
        input("\nPress Enter to return to main menu...")

    # 3 Placeholder for next tool
    elif choice == "3":
        print("\nOpening Attendance Evaluator...")
        attendence()   # Calls your attendance evaluator function
        input("\nPress Enter to return to main menu...")

    # Invalid input
    else:
        print("\nInvalid selection! Please enter 0, 1, 2, or 3.")
