from agents.skill_agent import analyze_skills


def test_skill_agent():

    result = analyze_skills(
        ["Java"],
        "Data Engineer"
    )

    assert "Python" in result["missing_skills"]