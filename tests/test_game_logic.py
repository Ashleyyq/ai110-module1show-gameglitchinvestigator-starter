from logic_utils import check_guess, get_range_for_difficulty

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"


# --- Bug 1: New Game should use difficulty-based range, not hardcoded 1-100 ---
# Before the fix, new_game always used random.randint(1, 100) regardless of difficulty.
# These tests verify get_range_for_difficulty returns the correct bounds per difficulty.
# Added with Claude Code (AI collaboration).

def test_easy_range_is_not_hardcoded_100():
    low, high = get_range_for_difficulty("Easy")
    assert low == 1
    assert high == 20  # was broken when hardcoded to 100

def test_hard_range_is_not_hardcoded_100():
    low, high = get_range_for_difficulty("Hard")
    assert low == 1
    assert high == 50  # was broken when hardcoded to 100

def test_normal_range():
    low, high = get_range_for_difficulty("Normal")
    assert low == 1
    assert high == 100


# --- Bug 2: Non-win outcomes must always return a message for per-guess feedback ---
# Before the fix, show_hint gated ALL feedback including the attempt count message.
# check_guess must always return a non-None message so st.info can display it.
# Added with Claude Code (AI collaboration).

def test_too_high_always_returns_message():
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert message is not None

def test_too_low_always_returns_message():
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert message is not None
