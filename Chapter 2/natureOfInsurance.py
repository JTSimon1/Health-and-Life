import random

# Define the quiz questions and answers
word_definitions = {
    "Adverse Selection" :  "This is broadly defined as selection against the company or the tendency of people with higher risks to seek/continue insurance to a greater extent than those with little or less risk. In other words, adverse selection occurs when the percentage of poor risks among those covered by issued policies exceeds the ratio predicted by the actuaries when they designed the policies. This also consists of the tendency of policy owners to take advantage of favorable options in insurance contracts. \nProperty insurance covers losses caused by such perils as fire, lightning, windstorm hail, earthquake, and vandalism.\nLiability insurance covers an insured’s legal responsibility to indemnify a third-party that’s harmed due to the insured’s negligence.\nAccident and health insurance covers losses caused by illnesses and accidents.\nFor life insurance and annuities, the covered peril is mortality. Life insurance protects against premature death; however, annuities provide a measure of protection when death is delayed, and the insured would otherwise outlive his assets. ",
    "Accident" : "is an unforeseen, unexpected, unintended, and sudden event that occurs at a specific time and specific place.",
    "Hazard" : "This is any factor, condition, or situation that creates an increased possibility that a peril (a cause of a loss) will actually occur.",
    "Homogeneous Exposure Units" : "These are similar “objects of insurance” that are exposed to the same group of perils. An “object of insurance” can be a person, a business, or a piece of property. Each “unit” represents one of many similar risks that are undertaken to be insured by an insurance company.",
    "Indemnify" : "This is the act of restoring insureds to the financial condition that existed prior to a loss.",
    "Indemnity" : "This is the amount needed to restore an individual to the financial condition he was in before he suffered a loss.  An indemnity can be a reimbursement or a fixed dollar amount.",
    "Indemnity Contract" : "This is a contract that attempts to return the insured to her original financial position.",
    "Law of Large Numbers" : "This is a fundamental principle of insurance. The larger the number of individual risks that are combined into a group, the more certainty there is in predicting the degree or amount of loss that will be incurred in any given period.",
    "Loss" : "The insurance industry defines the word “loss” as the unintentional decrease in the monetary value of an asset due to a peril.",
    "Loss Exposure" : "This is the risk of a possible loss.",
    "Loss Exposure Unit" : "This refers to each individual, organization, or asset that’s exposed to the potential of financial loss due to a defined peril. When loss exposure units are aggregated together, the maximum potential loss expresses the overall loss exposure.",
    "Direct Loss" : "occur when a person or property is damaged, destroyed, or killed by a peril without any intervening cause.",
    "Occurrence" : "can be any event that causes a loss. Occurrences include accidents, injuries, illnesses, as well as losses that are caused by repeated or continuous exposure to conditions over time.",
    "Indirect (Consequential) Loss" : "the loss is a consequence of, or results from, a direct loss. This distinction is most relevant for property and casualty insurance.",
    "Moral Hazard" :  "This is the type of hazard that exists because of the effect of an insured’s personal reputation, character, associates, personal living habits, or degree of financial responsibility. This also includes criminal activity.",
    "Morale Hazard" : "This is a hazard that arises from an insured’s indifference to loss because of the existence of insurance. Morale hazards are often associated with having a careless attitude.",
    "Peril" : "A peril is the immediate, specific event that causes loss and gives rise to risk.",
    "Principle of Indemnification" : " states that the goal of an action is to “restore” an insured to the same financial position that he was in prior to when the loss in question occurred. Insurance contracts indemnify insureds. Indemnification also holds to the principle that an insured shall not profit or gain from their loss. In other words, they will not receive more than they lost.",
    "Physical Hazard" : "This is a physical or tangible condition that exists in a manner which makes a loss more likely to occur.",
    "Primary Insurance Company" : "This phrase has the following meanings: \nWhen more than one policy covers the same claim, the term “primary insurance company” refers to the first policy to pay.\nAs it relates to reinsurance, the primary insurance company writes a policy to cover a risk in the marketplace. This primary insurer then surrenders a portion of the risk to a reinsurer and the reinsurer assumes the excess risk for a reinsurance premium.",
    "Pure Risk" : "This is a type of risk that involves the chance of loss only; there’s no opportunity for gain. Pure risks are the only form of insurable risks.",
    "Reinsurance" : "This is the acceptance by one or more insurers—referred to as reinsurers—of a portion of the risk underwritten by another insurer that has contracted with an insured to provide coverage for the total value of a loss exposure.",
    "Reinsurer" : "This is an insurance company that assumes a portion of the risk underwritten by a primary insurance company.",
    "Risk" : "This is the uncertainty regarding loss. Risk is the probability of a loss occurring for an insured or prospect.",
    "Risk Avoidance" : "This occurs when individuals evade risk entirely. It’s the act of NOT participating in an activity that could possibly cause a loss.",
    "Risk Management" : "This is the process of analyzing exposures that create risk and then designing programs to address them.",
    "Risk Reduction" : "This is the risk management strategy that focuses on taking actions which decrease the chances of a loss occurring. It also refers to action taken to lessen the severity of a loss if one occurs.",
    "Risk Retention" : "This is the act of analyzing the loss exposure presented by a risk and determining that the potential loss is acceptable. Risk retention is often associated with self-insurance.",
    "Risk Selection" : "This is not a risk management technique that’s used by consumers. Instead, “risk selection” describes the insurance company’s process for determining whether to cover a new loss exposure. If done correctly, the ratio of losses to premium should reflect what actuaries predicted when they created the product, established the price, and set the underwriting criteria.",
    "Risk Sharing (Risk Pooling or Loss Sharing)" : "This is the risk management technique that manages an individual’s risk by sharing the possibility of loss with others and spreading the cost over a large number of individuals. This technique transfers risk from an individual to a group.",
    "Risk Transfer" : "This is the act of exchanging the responsibility for a significant potential loss (risk) to another party in exchange for a smaller, preset cost or premium.",
    "Self-Insurance" : "This is a risk retention process. A self-insuring individual or organization maintains monetary reserves to cover potential costs in the event of a financial loss occurring.",
    "Speculative Risk" : "This is a type of risk that involves the chance of both loss and gain; it’s not insurable.",
    "Specified (Named) Perils" : "list those specific perils that they cover. If a loss is caused by a peril that’s not listed within the insurance policy, then the loss is not covered.",
    "Special (Open Perils)" : "insurance policies don’t name the perils that they cover. Instead, these policies begin by stating that they cover all direct causes of loss and then list all of the perils that they exclude from coverage.",
    "Insurable Loss (Accidental)" : "'Chance' means that it’s outside an insured’s control. In this sense, the individual insured (loss exposure unit) that suffers the loss is randomly selected. This characteristic helps insurers avoid adverse selection.",
    "Insurable Loss (Measurable/Definite)" : "means that the time, place, amount, and whether the claim is payable can be documented.",
    "Insurable Loss (Predictable)" : "means that the (estimated) average frequency and severity of future losses can be calculated. There must be a sufficient number of homogeneous loss exposure units to effectively allow insurers to apply law of large numbers.",
    "Insurable Loss (Catastrophic)" : "is from the perspective of the insurer. This is meant to indicate that it’s too big and uncertain to be insured. The loss exposure must be reasonable.",
    "Standard Risks" : "are considered to have an average potential for loss. Standard risks are typically insured in return for a predetermined standard premium.",
    "Substandard Risks" : " judged to be a poor risk for an insurance company and have a higher-than-average potential for loss. Substandard risks may be insured for an increased premium, covered with a lower benefit, or declined altogether.",
    "Preferred Risks" : "judged to be a better than average risk for an insurance company. Preferred risks have a lower potential for loss. Insurers offer coverage to preferred risks for a lower-than-average premium.",
    "Loss Prevention" : "involves taking actions to eliminate damage or loss. In fact, it’s a method used to identify and analyze risk and to control losses.",
    "All of the following are examples of PURE risk EXCEPT" : "Losing Money at a Casino",
    "How do insurers predict the increase of individual risks?" : "Law of Large Numbers",
    "Peril" : "What is known as the immediate specific event causing loss and giving rise to risk?",
    "Hazard" : "Which of the following is considered to be an event or condition that increases the probability of an insured's loss?",
    "Doctors pooling their money to cover malpractice exposures" : "An example of risk sharing would be",
    "Risk Avoidance" : "An individual who removes the risk of losing money in the stock market by never purchasing stocks is said to be engaging in",
    "Law of Large Numbers and Risk Pooling" : "Insurance companies determine risk exposure by which of the following?",
    "transference" : "Insurance represents the process of risk...",
    "peril" : "The cause of a loss is referred to as a(n)",
    "adverse selection" : "People with higher loss exposure have the tendency to purchase insurance more often than those at average risk. This is called",

}

def quiz():
    score = 0
    num_questions = len(word_definitions)  # Limit to the number of unique definitions

    # Get a list of all words and shuffle them
    words = list(word_definitions.keys())
    random.shuffle(words)

    for i in range(num_questions):
        correct_word = words[i]
        correct_definition = word_definitions[correct_word]

        # Create a list of wrong choices
        wrong_words = random.sample([word for word in words if word != correct_word], 3)
        choices = [correct_word] + wrong_words
        random.shuffle(choices)

        # Display the definition and choices
        print(f"Definition: {correct_definition}")
        print("Choices:")
        for j, word in enumerate(choices, 1):
            print(f"{j}. {word}")

        # Get user's answer
        answer = input("Choose the correct word (1-4): ")

        # Check if the answer is correct
        try:
            if choices[int(answer) - 1] == correct_word:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect: The right answer was '{correct_word}'.")
        except (ValueError, IndexError):
            print("Invalid input. Please choose a number between 1 and 4.")

        print()  # Print a new line for better readability

    # Print the final score
    print(f"Your final score is: {score}/{num_questions}")

# Run the quiz
quiz()
