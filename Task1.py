#Task 1 -  Dictionary
def manage_courses():
    courses = {
        "CSE101": {"Course name": "Introduction to Programming", "Credits": 3, "Instructor": "Dr. Alice"},
        "CSE102": {"Course name": "Data Structures", "Credits": 4, "Instructor": "Dr. Bob"},
        "CSE103": {"Course name": "Database Systems", "Credits": 3, "Instructor": "Dr. Carol"},
    }
    courses["CSE102"]["Instructor"] = "Dr. Bob Jr."

    courses["CSE104"] = {"Course name":"Algorithms","Credits":4,"Instructor":"Dr. Dave"}

    del courses["CSE101"]
    
    for course_code in courses:
        print(f"Course Code:{course_code},Details:{courses[course_code]}")

man