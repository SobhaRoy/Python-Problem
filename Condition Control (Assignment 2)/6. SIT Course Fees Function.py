def CalculateSITcourseFees(course_code, TIGans, entrance_test, Male):
    # Course fee data: [Admission + 1st sem fee, Remaining semester fee per sem, Total semesters]
    courses = {
        1: [100000, 75000, 8],  # BTech
        2: [70000, 50000, 8],   # BCA
        3: [70000, 50000, 8],   # BBA
        4: [60000, 45000, 6],   # BHHA
        5: [50000, 30000, 6],   # BSc
        6: [140000, 100000, 4], # MBA
        7: [120000, 80000, 4]   # MCA
    }

    admission_fee, sem_fee, total_sem = courses[course_code]

    # Scholarships
    if TIGans == 1:  # Techno India Group scholarship
        if course_code <= 5:
            admission_fee -= 10000
            sem_fee -= 10000
        else:
            admission_fee -= 15000
            sem_fee -= 15000
    elif entrance_test == 1:  # Entrance test scholarship
        admission_fee -= 15000

    if Male == 0:  # Female scholarship
        admission_fee -= 10000

    # Total fees calculation
    remaining_semesters = total_sem - 1
    total_fee = admission_fee + remaining_semesters * sem_fee
    return round(total_fee, 2)

# Example usage
total = CalculateSITcourseFees(1, 1, 0, 1)
print("Total course fee:", total)
