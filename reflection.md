# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
At first it looks fine, but later when I tried to run one more time, I found that the "New Game" button seems to be not working.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The "New Game" button was not working, it did not start a new game
  2. And it's not straightforward for me when the hints said "Go lower" which means I should guess a bigger number.
  3. When I turned off the hints, there's nothing to remind me how many guess I have done. And only when I hit the final guess, there's the message.
  4. The range should be from 1 to 20 for easy mode but it required me to guess a secret number of 90. The setting page was not consistent with the game page.
  5. The developer debug info function somethings also not worked correctly.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Claude Code
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I asked Claude Code to fix the New Game bug, it correctly identified three problems at once: the game status was never reset to "playing", the guess history was never cleared, and the new secret was using a hardcoded range of 1–100 instead of calling get_range_for_difficulty. I verified it by winning a game and then clicking New Game — the game properly restarted with a fresh history and the correct difficulty range in the sidebar.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When I asked Claude Code to refactor functions from app.py into logic_utils.py, it suggested moving extra functions beyond the four required ones. I went along with it at first, but after comparing with the original logic_utils.py stub file I realized only four functions were actually required. I pushed back and Claude Code corrected itself, which taught me to always check AI suggestions against the actual requirements instead of just accepting them.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I think a bug was fixed when the behavior matched what I expected — for example, clicking "New Game" actually restarted the game, and turning off hints still showed the attempt count after every guess. I also looked at the FIXME comments in the code and checked that the specific lines they described were updated. Running pytest at the end gave me a more systematic way to confirm the logic was correct.

- Describe at least one test you ran (manual or using pytest)
  and what it showed you about your code.
When I first ran `PYTHONPATH=. pytest`, I got 3 failures even though I thought everything was working. It turned out the original test cases were asserting `result == "Win"` but `check_guess` actually returns a tuple `("Win", "🎉 Correct!")`. This showed me that the starter tests were already broken before I started, and that tests can give you false confidence if they were written incorrectly to begin with.

- Did AI help you design or understand any tests? How?
Yes, Claude Code helped me write new pytest cases that specifically targeted the two bugs I fixed. It suggested testing `get_range_for_difficulty` for each difficulty to cover Bug 1, and testing that `check_guess` always returns a non-None message for Bug 2. It also pointed out upfront that the original 3 tests had wrong assertions, which helped me understand that fixing tests is sometimes just as important as fixing code.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
