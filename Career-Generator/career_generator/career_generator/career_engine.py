def suggest_careers(data: dict):
    interests = data.get("interests", "").lower()
    skills = data.get("skills", "").lower()
    work_style = data.get("work_style", "").lower()
    environment = data.get("environment", "").lower()
    values = data.get("values", "").lower()

    careers = []

    # Tech Field
    if "technology" in interests or "coding" in skills:
        careers.extend(["Software Developer", "AI Engineer", "Cybersecurity Analyst"])

    # Design Field
    elif "design" in interests or "design" in skills:
        careers.extend(["Graphic Designer", "UX/UI Designer", "Product Designer"])

    # Medical Field
    elif "medical" in interests or "hospital" in environment or "diagnosis" in skills:
        careers.extend(["Doctor", "Nurse", "Physiotherapist"])

    # Social Work
    elif "social" in interests or "helping" in values:
        careers.extend(["Social Worker", "Counselor", "Community Organizer"])

    # Business Field
    elif "business" in interests or "management" in skills:
        careers.extend(["Business Analyst", "Project Manager", "Entrepreneur"])

    # Remote or Flexible Preferences
    elif "remote" in work_style or "flexible" in environment:
        careers.extend(["Freelance Writer", "Virtual Assistant", "Remote Developer"])

    # Growth or Freedom values
    elif "growth" in values or "freedom" in values:
        careers.extend(["Startup Founder", "Consultant", "Digital Nomad"])

    # Fallback
    else:
        careers.extend(["Teacher", "Content Creator", "Operations Specialist"])

    # Ensure exactly 3 results
    return careers[:3]
