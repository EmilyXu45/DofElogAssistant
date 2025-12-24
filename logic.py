def generate_reflection(activity, skills, challenges, style):

    if style == "Structured (What / So what / Now what)":
        return (
            f"This week, I took part in {activity}. "
            f"This helped me develop {skills}. "
            f"I faced challenges such as {challenges}, "
            f"which taught me how to manage difficulties and improve. "
            f"Next time, I will apply what I have learnt to continue developing."
        )

    elif style == "Short & simple":
        return (
            f"I completed {activity}. "
            f"I developed {skills}. "
            f"The main challenge I faced was {challenges}."
        )

    elif style == "Reflective & personal":
        return (
            f"Taking part in {activity} was a valuable experience. "
            f"I improved my {skills}, which increased my confidence. "
            f"Although {challenges} was challenging, it helped me grow "
            f"and better understand my strengths and areas for improvement."
        )

    elif style == "Assessor-focused summary":
        return (
            f"The participant completed {activity}, demonstrating development in {skills}. "
            f"They encountered {challenges} and responded positively, "
            f"showing commitment and progress towards their DofE goals."
        )

    else:
        return "Please select a reflection style."
