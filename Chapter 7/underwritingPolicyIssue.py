import random

# Define the quiz questions and answers
word_definitions = {

"Adverse Selection" : "This represents the tendency of a disproportionate number of poor risks to seek or buy insurance or to maintain existing insurance in force (i.e., the selection against the insurance company). Sound underwriting reduces adverse selection.",
"Age Change" : "This is the date halfway between birthdays when the applicant’s age changes to the next higher age. For some insurers, the age is based on the applicant’s age at his nearest birthday, while for others, it’s based on the applicant’s age as of his last birthday.",
"Applicant" : "The applicant is the person who’s completing an application with an insurance company for the insurance policy. In most cases, the applicant is also the proposed insured, but this is not always the case.",
"Application" : "The application is the statement of information that’s given when a person applies for life, health, or disability insurance. The insurance company’s underwriter uses this information as a basis in determining whether the applicant qualifies for acceptance under the company’s guidelines. Applications are attached to, and made a part of, all individual contracts.",
"Attending Physician Statement (APS)" : "An APS is used when the application or medical examiner’s report reveals conditions or situations, past or present, about which more information is desired. Due to physician/patient confidentiality guidelines, the applicant must sign an authorization for a physician is allowed to release information to the insurance company underwriter.",
"Backdating" : "This is the practice of making the effective date of a policy earlier than the application date. Backdating is used to make the issue age lower than an applicant’s real age in order to obtain a lower premium. State laws typically limit the time to which policies can be backdated to six months. Due to the nature of the investment, backdating is not allowed in variable contracts.",
"Binding Receipt (Unconditional Receipt)" : "This is one of the types of receipts that’s given by an insurance company upon the completion of an insurance application if the initial premium is collected with the application. Insurance becomes effective on the receipt date and continues for a specified period or until the insurer declines the application.",
"Buyer's Guide" : "This is a pamphlet which describes and compares various forms of life or health insurance. This guide must be provided to a consumer by the producer when the producer is attempting to solicit insurance. This guide provides the consumer with information so that she can make an informed decision when purchasing insurance coverage. ",
"Conditional Receipt" : "This is a form that’s customarily required to be signed by the agent and given to the prospective owner at the time a new application is completed. The issuing of a receipt is subject to rules of the individual company. Most companies require the agent to collect an initial premium and, in turn, grant some level of limited coverage under special conditions before issuing the policy. Without a valid conditional receipt, no coverage is in force until the policy is issued, delivered, and accepted with the initial premium paid.",
"Consumer Report (Investigative Consumer Report)" : "This report is a detailed background investigation that may include an interview with co-workers, friends, and neighbors about an applicant’s character, reputation, lifestyle, etc. Insurers are allowed to conduct a consumer report to obtain additional information as long there’s no invasion of privacy. A common type of consumer report is a credit report.",
"Credit Report" : "This is a summary of an insurance applicant’s credit history (i.e., credit score, debt levels, repayment history, assumed creditworthiness, etc.) that’s completed by an independent organization which has investigated the applicant’s credit standing. Credit reports are typically obtained from one of the three major credit bureaus (Experian, Equifax, and TransUnion).",
"Declined Risk" : "This describes an individual whose application for coverage was rejected by an insurance company.",
"Disclosure Form" : "As required by various state regulatory agencies, this is a comparison form that must be given to every policy owner who chooses to replace an existing policy with another.",
"Evidence of Insurability" : "This describes a statement or proof of a person’s health history and current health status which qualifies that person for coverage.",
"Fair Credit Reporting Act" : "Passed in 1970, this is a federal law that provides an insurer with the right to receive additional information regarding applicants for insurance coverage. This law permits an insurer to conduct a consumer report on both applicants and proposed insureds. An applicant for insurance must be informed of the purpose of the report. If coverage is declined due to the information in the report, the insurer must provide the name and address of the reporting agency so that the applicant can secure a copy of the information in the report.",
"Field Underwriter" : "This is the agent or producer who completes the applicant’s application for insurance.",
"Free-Look Period" : "All life insurance policies must include at least a 10-day free-look period. This period begins when the producer delivers the insurance policy. During this period, if the policy owner decides to return the contract to the insurer, he will receive a full premium refund. Mail order or direct response insurers must include a free-look period of at least 30 days.",
"Inspection Report" : "This is a report that contains general information regarding the health, habits, finances, and reputation of an applicant. This report is developed by a firm that specializes in rendering this type of service.",
"Insurable Interest" : "This describes the financial or emotional relationship between two or more parties which justifies one owning a life insurance policy on the other. A person is considered to have an unlimited insurable interest in her own life. Insurable interest may exist in another person’s life if there’s a chance of a financial or emotional loss due to that person’s death. The insurable interest must exist at the time of policy issue.",
"Medical Information Bureau" : "This is a service organization that collects medical data on life and health insurance applicants for member insurance companies.",
"Policy Summary" : "This summarizes the basic terms of an insurance policy, including the conditions, coverage limitations, and premiums. Policy summaries are often used with life insurance, long-term care insurance, and annuities.",
"Preferred Risk" : "This describes an applicant who represents the likelihood of risk that’s lower than that of the standard applicant. This is typically due to better than average physical condition, occupation, mode of living, and other characteristics as compared to other applicants of the same age.",
"Proposed Insured" : "This is the person who’s requesting that her life be insured. This is also typically the applicant (but not always).",
"Rated Policy (Rating Up)" : "A rated policy is the basis for an additional charge to the standard premium because the person insured is classified as a higher-than-average risk. The higher risk level is typically the result of impaired health or a hazardous occupation.",
"Replacement" : "This is a permitted activity in which a producer convinces a prospective client to lapse or surrender a life or health policy and purchase a new one. If this activity occurs, producers must provide a “Notice Regarding Replacement” to the consumer. The producer must also notify the insurer that a replacement is occurring.",
"Representations" : "Most state laws specify that an applicant’s statements on an application are considered representations and not warranties. A representation is only required to be substantially accurate to the best of the applicant’s knowledge. Generally, a representation is considered to be fraudulent if it relates to a situation that would be material to the risk and that the applicant made with fraudulent intent.",
"Risk Classification" : "This describes the underwriting category into which risk is placed depending on the applicant’s susceptibility to injury, illness, or death.",
"Special Class" : "This describes an applicant who cannot qualify for a standard policy but may secure one with a rider that waives the payment for a loss involving certain existing health impairments. The applicant may be required to pay a higher premium or to accept a type of policy that’s different from the one for which he applied.",
"Standard Risk" : "This describes a person who, according to a company’s underwriting standards, is considered an average risk and insurable at standard rates. High-risk or low-risk candidates may qualify for increased or discounted rates based on their deviation from the standard.",
"Substandard Risk (Impaired Risk)" : "This describes an applicant whose physical condition doesn’t meet the usual minimum standards. If the substandard classification is due to adverse health, the application may be declined or written with a “rated-up” premium. An applicant may be in excellent health, but considered substandard due to her activities, hobbies, or avocations (e.g., scuba diving, skydiving, etc.).",
"Underwriter (risk selection)" : "This is a person who identifies, examines, and classifies the degree of risk represented by a proposed insured in order to determine whether coverage should be provided and, if so, at what rate.",
"Underwriting" : "This involves the analysis of information that’s obtained from various sources pertaining to an applicant for insurance and the determination of whether the insurance should be issued as requested, offered at a higher premium, or declined.",
"Warranties" : "Most state laws specify that an applicant’s statements on the application are considered representations and not warranties. A warranty must be absolutely and literally true. A breach of warranty may be sufficient to void the policy regardless of whether the warranty is material and whether such breach of warranty had contributed to the loss.",
"Tort" : "A producer who has made an unintentional error or honest mistake has committed a _____ which is referred to as an error and omission. Therefore, it is recomended that insurers purchase Errors and Omissions (E&O) insurance to cover the malpractice or negligence of producers.",
"Approval Language in a Conditional Receipt" : "This type of receipt indicates that coverage is effective only after the application has been approved by the insurer. Therefore, if the producer collects the premium and application on June 15, and the application is approved by underwriting on June 29, coverage is effective as of June 29.",
"USA Patriot Act" : "This act increased the ability of the law enforcement agencies to search telephone and e-mail communications, as well as medical, financial, and other records in order to thwart and prevent terrorist activities. The act also expanded the Secretary of the Treasury’s authority to regulate financial transactions, particularly those involving foreign and individual entities, in order to protect the United States and its interests. Insurance companies are required to implement written AML programs which include designating a compliance officer for updating the program, ensuring that the appropriate persons are educated and trained on the use of the program, and conducting on-going AML training.",
"Unfair Discrimination" : "An insurer is not permitted to engage in any unfair discrimination regarding applicants for life insurance. Sexual orientation, religious preference, or geographical location are prohibited life insurance underwriting factors because they’re unfairly discriminatory.",
"Policy Effective Date" : "not only does it identify when the coverage is effective, but it also establishes the date by which future annual premiums must be paid. Let’s assume that a receipt (either conditional or binding) is issued in exchange for the initial premium payment. In this case, the receipt’s date will generally be noted as the policy effective date in the contract. If a premium deposit is not given with the application, the policy effective date is typically left to the insurer’s discretion. Often, it will be the date that the insurance company issues the policy. However, the policy will not be truly effective until it’s delivered to the applicant, the first premium is paid, and a Statement of Continued Good Health is obtained.",
"Constructive Delivery" : "Mailing the policy to the agent for unconditional delivery to the policy owner also constitutes constructive delivery, even if the agent never personally delivers the policy. On the other hand, if the company instructs the agent to not deliver the policy unless the applicant is in good health, there’s no constructive delivery.",

# Chapter Exam Questions Start Here
"providing commission information to the applicant" : "An insurance producer is often responsible for field underwriting during the application process. All of these are possible field underwriting roles EXCEPT",
"better than average mortality or morbidity experience" : "Preferred risk policies with reduced premiums are issued by insurance companies because the insured has",
"Warranty" : "What guarantees that the statements supplied by an insurance applicant are true?",
"The insured does not meet established underwriting requirements" : "Which of the following would be a valid reason why a policy premium would be higher than the standard premium?",
"Investigative consumer report" : "An applicant's character and personal habits can be obtained for underwriting purposes from which source?",
"Number of Children" : "Which of these is NOT considered to be a risk factor in life insurance underwriting?",
"Adverse Selection" : "An underwriter's primary responsibility to an insurer is to protect against",
"A Statement of Good Health" : "Upon policy delivery, which of the following must a producer have an applicant sign if no initial premium was collected with the life insurance application?",
"To help underwriters evaluate risk" : "What is the purpose of the Medical Information Bureau (MIB)?",
"At the request of the insurer to assist in the underwriting decision" : "An attending physician's statement would be appropriate for which life insurance purpose?",


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
