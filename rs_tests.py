#Tests for the reading_speed program
def introduction():
    return "Hello! Please answer the following \
    questions to the best of your ability. (Press enter to continue)"

def test_introduction():
    assert introduction == "Hello! Please answer the following \
    questions to the best of your ability. (Press enter to continue)"
