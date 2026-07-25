def analyze_skills(current_skills, target_role):

    missing_skills = []

    if "Python" not in current_skills:
        missing_skills.append("Python")

    if "SQL" not in current_skills:
        missing_skills.append("SQL")

    return {
        "target_role": target_role,
        "missing_skills": missing_skills
    }