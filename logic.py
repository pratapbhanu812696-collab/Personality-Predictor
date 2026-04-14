def calculate_results(answers):
    # Simple Logic for Demonstration:
    # Extraversion = Q1 + Q6
    # Conscientiousness = Q2 + Q7
    # Agreeableness = Q3 + Q8
    ext = (answers[0] + answers[5]) / 2
    con = (answers[1] + answers[6]) / 2
    agr = (answers[2] + answers[7]) / 2
    
    result_text = f"""
    Aapka Personality Result:
    -------------------------
    Extraversion (Social): {ext}/5
    Conscientiousness (Organized): {con}/5
    Agreeableness (Kind): {agr}/5
    
    Note: Yeh ek basic simulation hai.
    """
    return result_text
