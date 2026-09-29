import math

def attendence():
    print("\n" + "=" * 60)
    print("               ATTENDANCE EVALUATOR")
    print("=" * 60)
    
    try:
        tl_cl_ad = int(input("ENTER TOTAL NUMBER OF CLASSES ATTENDED => "))
        tl_cl = int(input("ENTER TOTAL NUMBER OF CLASSES SCHEDULED => "))
        tl_cl_p = int(input("ENTER NUMBER OF UPCOMING CLASSES => "))
    except ValueError:
        print("Error: Please enter valid integer numbers.")
        return

    if tl_cl == 0:
        print("Error: Total scheduled classes cannot be zero.")
        return
        
    if tl_cl_ad > tl_cl:
        print("Error: You cannot attend more classes than are scheduled.")
        return

    # FORMULA FOR CURRENT ATTENDANCE CALCULATION
    a = (tl_cl_ad / tl_cl) * 100 
    
    # TOTAL CLASSES NEEDED FOR 75% BY SEMESTER END (Rounded up)
    ase = math.ceil(0.75 * (tl_cl + tl_cl_p))
    
    # CLASSES LEFT TO ATTEND TO COMPLETE 75% ATTENDANCE
    c = ase - tl_cl_ad 
    
    # CLASSES THAT CAN BE BUNKED
    b = tl_cl_p - c 
    
    print("\n" + "-" * 60)
    
    # CHECKS ATTENDANCE CRITERIA
    if a < 75 and b >= 0:
        print(f"YOU ARE CURRENTLY BELOW THE CRITERIA WITH: {a:.2f}%")
        print(f"YOU HAVE TO ATTEND {c} MORE CLASS(ES) TO MAINTAIN 75%")
        
    elif a >= 75 and b >= 0:
        print(f"YOU ARE CURRENTLY ABOVE THE CRITERIA WITH: {a:.2f}%")
        if c > 0:
            print(f"YOU MUST ATTEND {c} MORE CLASS(ES) TO MAINTAIN 75%")
        else:
            print("YOU HAVE ALREADY SECURED 75% FOR THE ENTIRE SEMESTER!")
        print(f"YOU CAN AFFORD TO BUNK {b} CLASS(ES)")
        
    else:
        print(f"CURRENT ATTENDANCE: {a:.2f}%")
        print("R.I.P. - YOU CANNOT REACH 75% EVEN IF YOU ATTEND EVERY REMAINING CLASS.")
        
    print("-" * 60 + "\n")