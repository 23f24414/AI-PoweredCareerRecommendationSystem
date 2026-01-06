def generate_career_recommendation(user_profile):
    recommendation_generated = False
    retry_count = 0

    while recommendation_generated == False:
        skills = user_profile.get("skills")
        interests = user_profile.get("interests")

        # DEFECT 1: No check if skills or interests are None
        if len(skills) > 0 and len(interests) > 0:
            print("Recommended Career: Software Engineer")
            recommendation_generated = True
        else:
            print("Please update your profile information")

        # DEFECT 2: retry_count not incremented
        if retry_count > 3:
            break
