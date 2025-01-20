import random

# Define the quiz questions and answers
word_definitions = {
    "Adhesion" : "A contract of adhesion is one that has been prepared by one party (the insurance company) with no negotiation between the applicant and insurer. The applicant adheres to the contract terms on a “take it or leave it” basis when accepted. (See Rule Regarding Ambiguities)",
    "Ambiguities in a Contract of Adhesion" : "Ambiguities or confusing language in a contract can result in differing legal interpretations and conflicts. In any contract of adhesion, the party that dictates the contract terms has the responsibility to ensure that all of the contract terms are clear and free of ambiguities. The insurance company has this responsibility when it comes to its insurance policies. \nIf a legal question arises regarding an insurance policy, it often involves an ambiguous definition, description, or policy provision. In such cases, courts will rule in favor of the insured because the insurance company is responsible for making the policy terms clear. After all, the insurer has total control of the contract language.",
    "Agent Authority" : "There are three types of agent authority—express, implied, and apparent. The significance of this authority (whether express, implied, or apparent) is that it ties the company to the acts and deeds of its agents. The law will view the agent and company as identical when the agent acts within the scope of his authority. Additionally, an insurer may be liable to an insured for unauthorized acts of its agent when the agency contract is unclear about the authority granted.",
    "Agent" : "This is the person who represents the insurer during an insurance transaction and has been authorized to act on the insurance company’s behalf. Agents have a fiduciary responsibility to both parties—the insurer and the policy owner.",
    "Aleatory" : "This is a legal arrangement in which there’s the potential for an unequal exchange of value or consideration between both parties. The insured may never file a claim in an insurance contract, or a claim may be filed after only one or two premiums.",
    "Ambiguities" : "This refers to terms or conditions that are not clearly defined in an insurance contract. (See Adhesion)",
    "Apparent Authority" : "This is the appearance of the insurer providing the agent authority to perform unspecified tasks based on the agent-insurer relationship. This perception of authority must stem from the insurer’s actions, even if the perception is unintended and the perception is in error.",
    "Broker" : "This is a licensed producer who represents himself and the insured (i.e., the client or customer) during an insurance transaction. However, a broker is different from an agent. A broker doesn’t hold an appointment with the insurer in question, and a broker cannot bind coverage on behalf of the insurer.",
    "Cancellation" : "The voluntary act of terminating an insurance contract is referred to as cancellation. The policy owner may voluntarily cancel an insurance contract for any reason at any time.",
    "Counter Offer" : "the original offer that was made by the applicant has been rejected by the insurer and that initial offer is void. No contract will exist unless the applicant accepts the insurer’s counteroffer, usually by paying an additional premium or agreeing to benefit limitations.",
    "Competent Party" : "This is a person who’s able to understand the contract to which two parties are agreeing. All parties must be of legal competence, which means that they must be of legal age, mentally capable of understanding the contract terms, and not under the influence of drugs or alcohol.",
    "Concealment" : "This is the failure of an applicant to disclose a known material fact when applying for insurance.",
    "Conditional" : "This is an agreement that remains in force if certain conditions are met. The insurer’s promise to pay benefits is dependent on the occurrence of an event that’s covered by the contract.",
    "Consideration" : "This is the legal description of the items of value that each party to the contract provides to the other. In the case of an insurance policy, the applicant provides material information and the premium. In return, the insurance company agrees to pay the cost of claims that are covered by the policy.",
    "Consideration Clause" : "This clause is part of an insurance contract and sets forth the initial and renewal premiums and frequency of future payments.",
    "Doctrine of Reasonable Expectations" : "This doctrine states that an insurance contract will be interpreted to mean what a reasonable individual would think it means, even if the insurer must pay additional benefits that are not intended by the contract.",
    "Estoppel" : "This is the legal impediment to one party’s ability to deny the consequences of its own actions or deeds if such actions or deeds result in another party acting in a specific manner or if certain conclusions are drawn.",
    "Express Authority" : "This is the explicit authority that’s granted to the agent by the insurer, as written in the agency contract.",
    "Fiduciary" : "A fiduciary is a person to whom property or power is entrusted for the benefit of another person. A producer is a fiduciary that’s in a position of trust regarding the funds of its clients and the insurer. It’s the responsibility of an insurance producer to account for all of the premiums collected and to provide sound financial advice to clients.",
    "Gross Negligence" : "results from a reckless disregard for the need to act in a reasonable manner, regardless of the potential for harm.",
    "Fraud" : "An individual commits fraud when he engages in intentional deceit to gain a benefit. Fraud includes having deliberate knowledge of false statements that are made or intended as well as the act of a person making such statements herself.",
    "Implied Authority" : "This is an authority that’s not explicitly granted to the agent in the contract of agency, but which common sense dictates the agent has. This authority enables the agent to carry out routine responsibilities.",
    "Indemnity Contract" : "This type of contract attempts to return the insured to his original financial position.",
    "Insurable Interest" : "This is the financial, economic, and emotional impact that’s experienced by a person who suffers a covered loss. A person has an insurable interest if she has more to gain by not experiencing the loss.",
    "The Law of Agency" : "When acting within the scope of the authority granted, an agent is considered to be the insurance company. The relationship between an agent and the company being represented is governed by agency law. An agent’s role involves the following duties: \n Describing the company’s insurance policies to prospective buyers \n Soliciting applications for insurance \n Collecting premiums from policy owners \n Rendering service to prospects and currently insured consumers",
    "Insurance Policy (Contract)" : "This is a written contract in which one party promises to indemnify another against a loss that arises from an unknown event.",
    "Legal Purpose" : "This means that an insurance contract must be legal in nature and not in opposition to public policy.",
    "Material Misrepresentation" : "This is a false statement being made by an applicant that influences either an insurer’s decision to accept the risk, or the classification and pricing of a risk that’s accepted by the insurer.",
    "Misrepresentation" : "This is a statement being made as a legal representation that’s factually incorrect, either totally or in part.",
    "Principles of Agency Law" : "By legal definition, an agent is a person or entity that acts on behalf of another person (i.e., the principal). For insurance purposes, the insurer. The agent represents the principal in dealings with third parties that concern contractual arrangements. Authorized agents have the power to bind the principal to contracts (and to the rights and responsibilities of those contracts). From this description, the four essential principles of agency law can be identified: \n 1.    The acts of an agent (within the scope of his authority) are the acts of the principal.\n 2.    A contract that’s completed by an agent on behalf of the principal is a contract of the principal.\n 3.    Payments received by an agent on behalf of the principal are payments made to the principal.\n 4.    An agent’s knowledge regarding a business matter of concern to the principal is presumed to be known by the principal.",
    "Personal Contract" : "By referring to an insurance policy as a ______ contract, it’s understood that a policy insures the owner (person) of the property, and not the property itself. As such, most types of insurance cannot be transferred to another person.",
    "Parole Evidence Rule" : "This rule states that, when the parties agree in writing, all previous verbal statements come together. A written contract cannot be changed or modified by parole (oral) evidence.",
    "Policy Rider or Endorsement" : "This is an amendment which is added to an insurance contract that overrides terms in the original policy. Riders may add or remove coverages, change deductibles, or revise any other policy feature. In general, a policy owner must pay an additional premium to add a policy rider that enhances policy benefits.",
    "Reasonable Expectations" : "This indicates that the insured is entitled to coverage under a policy that any sensible and prudent person would expect it to provide.",
    "Representations" : "These are statements made by the applicant that he considers true and accurate to the best of his belief.",
    "Rule Regarding Ambiguities" : "This rule applies to contracts of adhesion. Courts will interpret the terms of an insurance contract in favor of the insured if there’s a legal dispute and the court holds the terms of the contract to be ambiguous. The insurer is responsible for ensuring that the contract is clear since it creates the policy terms as a contract of adhesion.",
    "Simple Negligence" : "is a failure to act (or not act) in a reasonable or prudent manner.",
    "Tort Law" : "involves private wrongs that are independent of contracts. By definition, a tort is a private wrong that occurs when one individual wrongs another by failing to act in a reasonable or prudent manner. The concept of tort law is to provide compensation for proven harms, or put another way, to right a wrong that’s been done to a person and provide relief from the wrongful acts of others by awarding monetary damages as compensation. There are several types of negligence, including:\n Simple negligence is a failure to act (or not act) in a reasonable or prudent manner.\n Gross negligence results from a reckless disregard for the need to act in a reasonable manner, regardless of the potential for harm.\n Willful and wanton negligence occurs when a person recklessly disregards reasonable care standards and is aware that bodily injury or property damage will probably occur. This borders on being an intentional act, which liability insurance doesn’t cover.",
    "Subrogation" : "This is the right for an insurer to pursue a third party that caused an insurance loss to the insured.",
    "Unilateral" : "This is a type of contract in which only one party—the insurer—makes any kind of enforceable promise. The promises remain in force for as long as the insured pays the required premium.",
    "Utmost Good Faith" : "This statement is based on the belief that both the policy owner and the insurer must know all of the material facts and relevant information. As such, they will provide each other with all material facts and relevant information.",
    "Valued Contract" : "This type of contract pays a stated sum regardless of the actual loss incurred. Life insurance contracts are valued contracts.",
    "Void Contract" : "This contract is an agreement that has never really been in force because it lacks one of the essential elements of a contract. For example, if a third party (rather than the applicant for insurance) provides a urine sample for analysis, this act of impersonation deprives the insurer of the information it needs. In effect, the applicant is withholding necessary consideration; therefore, any policy is void from the day it’s issued. In other words, it never really goes into effect. (See Voidable Contract for contrast.)",
    "Voidable Contract" : "This type of contract is an agreement that may be set aside by one of the parties in the contract for a reason that’s satisfactory to the court. (See Void Contract for contrast.)",
    "Waiver" : "This is the voluntary giving up of a legal, given right.",
    "willful and Wanton Negligence" : "occurs when a person recklessly disregards reasonable care standards and is aware that bodily injury or property damage will probably occur. This borders on being an intentional act, which liability insurance doesn’t cover.",
    "Warranty" : "This is a statement made by the applicant that’s guaranteed to be true in every respect and also becomes a part of the contract. The discovery that a warranty is untrue can be grounds for revoking the agreement. In general, all statements that are made by an applicant are representations, rather than warrantie.",
    "Legally Valid and Binding" : "Competent Parties\n Legal purpose \n Offer and acceptance (agreement) \n Consideration",
    "Law of Agency (question answer)" : "The authority granted to a licensed producer is provided via the",
    "Implied" : "The power given to an individual producer that is not specifically addressed in his/her contract is considered what type of authority?",
    "The terms must be accepted or rejected in full": "Under a contract of adhesion,",
    "Representation" : "What are an applicant's statements concerning occupation, hobbies, and personal health history regarded as?",
    "Tom" : "Bob and Tom start a business. Since each partner contributes an important element to the success of the business, they decide to take life insurance policies out on each other, and name each other as beneficiaries. Eventually, they retire and dissolve the business. Bob dies 12 months later. The policies continue in force with no change. Both partners are still married at the time of Bob's death. In this situation, who will receive Bob's policy proceeds?",
    "Errors and Omissions" : "A professional liability for which producers can be sued for mistakes of putting a policy into effect is called",
    "Concealment" : "Intentional withholding of material facts that would affect an insurance policy's validity is called a(n)",
    "Apparent" : "The deeds and actions of a producer indicate what kind of authority?",
    "A paid Premium" : "Which of the following is an example of the insured's consideration?",
    "Promises Made" : "According to the principle of Utmost Good Faith, the insured will answer questions on the application to the best of their knowledge and pay the required premium, while the insurer will deal fairly with the insured and it's",

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
