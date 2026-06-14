score = int(input("Enter your score: "))
if score >= 90:
    grade = "A"
    message = "Excellent work!"
elif score >= 80:
    grade = "B"
    message = "Good job!"
elif score >= 70:
    grade = "C"
    message = "You passed." 
elif score >= 60:
    grade = "D"
    message = "You barely passed."
else:
    grade = "F"
    message = "You failed. Better luck next time."  
print(f"Your grade is: {grade}. {message}")
