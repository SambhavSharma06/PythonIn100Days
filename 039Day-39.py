# --------------------------------------------
#   KAUN BANEGA CROREPATI (KBC) GAME
#   With checkpoints + easy-to-understand notes
# --------------------------------------------

print("Kaun Banega Crorepati")

# These are all the questions the player will answer in order.
Questions = [
    "What is the capital of India?",
    "How many days do we have in a week?",
    "How many months do we have in a year?",
    "What is the capital of Ireland?",
    "What is the best phone in the world?",
    "What is the full form of VIP?",
    "What is the best wonder in the world?",
    "What datatype do we use for words and letters?",
    "What datatype do we use for digits?",
    "What datatype do we use for key-value pairs?",
    "What is the best organ of our body?",
    "What is the full form of Pihu?",
    "What is the full form of Sam?"
]

# Money you win after every question.
# The 1st question gives ₹5,000, 2nd gives ₹10,000, and so on.
Money_Prize = [
    "₹5,000", "₹10,000", "₹20,000", "₹40,000", "₹80,000", "₹160,000",
    "₹320,000", "₹640,000", "₹1,250,000", "₹2,500,000", "₹5,000,000",
    "₹1 Crore", "₹5 Crore"
]

# Options for each question (A, B, C, D)
Options = [
    "A. Chennai B. Delhi C. Mumbai D. Bombay",
    "A. 8 B. 7 C. 10 D. 11",
    "A. 11 B. 12 C. 13 D. 14",
    "A. Dublin B. Kerry C. Cork D. Limerick",
    "A. iPhone B. Poco C. Samsung D. Moto",
    "A. Very Important Person B. Very Impressive Person C. Very Ice Person D. Very Inch Person",
    "A. Me B. Taj Mahal C. You D. GOD",
    "A. String B. Char C. Int D. Array",
    "A. Int B. Array C. Float D. Char",
    "A. Dictionary B. Array C. Float D. String",
    "A. Brain B. Lips C. Legs D. GOD",
    "A. Priyanshi B. Sambhav C. Asala D. Kamasal",
    "A. Sambhav B. Priyanshi C. Kushal D. Sam"
]

# Correct answers to each question.
# For example, the answer to Q1 is "B".
Answers = ["B", "B", "B", "A", "B", "A", "B", "A", "A", "A", "A", "A", "A"]

# These are the SAFE LEVELS.
# If you cross a checkpoint, that amount is guaranteed even if you later lose.
checkpoints = {
    1: "₹10,000",  # After question 2
    5: "₹1,00,000",  # After question 6
    9: "₹10,00,000"  # After question 10
}

# Before reaching any safe level, your guaranteed money is 0.
safe_amount = "₹0"

# ---- MAIN GAME LOOP ----
# We ask questions one by one using the number "i" as an index.
for i in range(len(Questions)):

    # Just printing the question number and question text.
    print("\n--------------------------------------")
    print(f"Question {i + 1}: {Questions[i]}")
    print(Options[i])
    print("--------------------------------------")

    # Player types their answer.
    userinput = input("Your answer (A/B/C/D): ").upper()

    # If the player gives the right answer:
    if userinput == Answers[i]:
        print("✔ Correct Answer!")
        print(f"You won {Money_Prize[i]}")

        # Now check if this question is a "checkpoint".
        # If yes, the safe amount should be updated.
        if i in checkpoints:
            safe_amount = checkpoints[i]
            print(f"🎉 CHECKPOINT REACHED! Safe Money = {safe_amount}")

    else:
        # If the answer is wrong:
        print("❌ Wrong Answer")
        print(f"💰 You fall back to your safe amount: {safe_amount}")
        print("💀 GAME OVER 💀")
        break  # This stops the entire game.

# If the loop finishes without break, it means the player won all 13 questions.
else:
    print("\n🎉🎉 YOU DID IT!! 🎉🎉")
    print("You won the FULL prize of ₹5 CRORE!")
