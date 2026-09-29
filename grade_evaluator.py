def grade():
    print("\n" + "=" * 58)
    print("                 GRADE EVALUATOR")
    print("=" * 58)
    
    try:
        num_courses = int(input("ENTER NUMBER OF COURSES REGISTERED  ->>> "))
    except ValueError:
        print("Error: Please enter a valid integer for the number of courses.")
        return

    all_courses = []
    mis = []         
    ais = []         
    grade = []       

    # Ask for input for each course
    for i in range(num_courses):
        course = input(f"Enter course '{i+1}' name => ")
        all_courses.append(course)
        
        try:
            get_m = int(input(f"Enter your mark in '{course}' => "))
            get_a = float(input(f"Enter your class avg. in '{course}' => "))
        except ValueError:
            print("Error: Invalid numeric input. Grading aborted for safety.")
            return
            
        mis.append(get_m)
        ais.append(get_a)

    # Evaluate grades
    for i in range(num_courses):
        if mis[i] >= ais[i] + 10:
            grade.append("S")
        elif mis[i] >= ais[i] + 5:
            grade.append("A")
        elif mis[i] >= ais[i] - 5:
            grade.append("B")
        elif mis[i] >= ais[i] - 10:
            grade.append("C")
        elif mis[i] >= ais[i] - 15:
            grade.append("D")
        else:
            grade.append("F")

    # Print Report Card
    print("\n" + "=" * 58)
    print("\t----REPORT CARD----")
    print("=" * 58)

    for i in range(num_courses):
        print("Course        :  ", all_courses[i])
        print("Scored mark   ->  ", mis[i])
        print("Class avg.    ->  ", ais[i])
        print("Grade         ->  ", grade[i])
        print("_" * 58)
        