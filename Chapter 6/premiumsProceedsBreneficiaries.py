import random

# Define the quiz questions and answers
word_definitions = {
"Accelerated Benefit (Option) Rider" : "This rider allows the insured to receive a portion of the death benefit prior to death if the insured has a terminal illness that’s certified by a physician and is expected to die within one to two years.",
"Beneficiary" : "This is the person (or entity) who’s designated in a life insurance policy to receive the death proceeds.",
"Cash Value" : "This is the equity or savings element of whole life insurance policies.",
"Class Designation" : "This is a beneficiary group designation (e.g., all of a person’s children), opposed to specifying one or more beneficiaries by name.",
"Common Disaster Provision" : "This is a provision of the Uniform Simultaneous Death Act, which ensures a policy owner that death benefits will be paid to the contingent beneficiary if both the insured and the primary beneficiary die within a short period of time of one another. It also states that the primary beneficiary must outlive the insured by a specified period in order to receive the proceeds.",
"Contingent (Secondary) Beneficiary" : "This is the beneficiary who’s second in line to receive death benefit proceeds if the primary beneficiary dies before the insured.",
"Earned Premium" : "This is the amount of premium that’s paid by the policy owner for policy coverage or insurance protection up to a specific point.",
"Expense Factor" : "Also referred to as the loading charge, this is a measure of what it costs an insurance company to continue to operate.",
"Excess Interest" : "In life insurance, this provision means that the cash value will increase faster than the guaranteed rate if the insurer earns a greater return than the guaranteed rate.",
"Fixed Amount Installment Option" : "This option pays a fixed death benefit in specified installment amounts until the principal and interest are exhausted.",
"Fixed/Level Premium" : "This is a concept which averages what the total single premium would be for a policy over periodic payments. More periodic payments = higher total premium.",
"Fixed Period or Period Certain Option" : "This payment option pays the death benefit proceeds in equal installments over a set number of years. The dollar amount of each installment is dependent on the total number of installments.",
"Graded Premium" : "This premium funding option is characterized by a lower premium in the early years of the contract, with premiums increasing annually for an introductory period. After the introductory period, the premium increases to an amount that’s higher than what the initial level premium would have been. Thereafter, it remains fixed or constant for the life of the policy.",
"Gross (Annual) Premium" : "An insurer’s gross premium consists of the net premium for insurance PLUS commissions, operating and miscellaneous expenses, and dividends.",
"Interest Factor" : "This is the calculation for determining the amount of interest an insurance company can expect to earn from investing insurance premiums.",
"Interest Only Option" : "This is a death settlement option in which the insurance company holds the death benefit for a period and pays only the interest that’s earned to the named beneficiary. A minimum rate of interest is guaranteed, and the interest must be paid at least annually.",
"Irrevocable Beneficiary" : "This is a beneficiary that cannot be changed by the policy owner without the written consent of the beneficiary.",
"Joint and Survivor Option" : "This is a settlement option which guarantees that benefits will be paid on a life-long basis to two or more people. This option may include a period certain, and the amount payable is based on the ages of the beneficiaries.",
"Life Income Option" : "This is a death benefit settlement option which provides the beneficiary with an income that she cannot outlive. Installment payments are guaranteed for as long as the recipient is alive. The amount of each installment is based on the recipient’s life expectancy and the amount of principal.",
"Life Settlement" : "This is an agreement in which a policy owner sells or transfers ownership in all or part of a life insurance policy to a third party for compensation that’s less than the expected death benefit of the policy.",
"Lump-Sum Option" : "This is a death settlement option in which the death benefit is paid in a single payment, minus any outstanding policy loan balances and overdue premiums. The lump-sum option is considered the automatic (or “default”) option for most life insurance contracts.",
"Modified Premium" : "This is a premium funding option which is characterized by an initial premium that’s lower than it should be during an introductory period (typically the first three to five years). After this period, the premium will increase to an amount that’s greater than what the initial level premium would have been and then remain level or constant for the life of the policy.",
"Morbidity Rate" : "This rate demonstrates the incidence and extent of disability that may be expected from a given group of people.",
"Mortality Rate" : "This rate is the measure of the number of deaths (in general or due to a specific cause) in some population, scaled to the size of that population, per unit time.",
"Net Payment Cost Index" : "This is a formula that’s used to determine the actual cost of a policy for a policy owner. It helps the consumer compare costs of death protection between policies that will be held for 10 to 20 years.",
"Net (Single) Premium" : "This is a premium calculation that’s used to calculate an insurer’s policy reserves factoring in interest and mortality.",
"Per Capita (By the Head)" : "This form evenly distributes benefits among all named living beneficiaries (i.e., all living children).",
"Per Stirpes (By the Bloodline)" : "This form evenly distributes benefits among an insured’s beneficiaries according to the family line, branch, or root (i.e., children and grandchildren).",
"Premium Mode" : "This is the frequency in which a policy owner elects to pay premiums.",
"Primary Beneficiary" : "This is the first beneficiary in line to receive benefit proceeds upon the death of an insured.",
"Policy Proceeds" : "This is the amount actually paid as a death, surrender, or maturity benefit. In the case of a death benefit, it includes the face value, plus any earned dividends, less any outstanding loans and interest. In the case of a surrender benefit, the amount includes any cash value, minus surrender charges, outstanding loans, and interest. In the case of maturity, the benefit amount includes the cash value, less any outstanding loans and interest.",
"Reserves" : "This is the money an insurer sets aside (as required by the state’s insurance laws) to pay future claims.",
"Revocable Beneficiary" : "This is a beneficiary that the policy owner may change at any time without notifying or getting permission from the beneficiary.",
"Settlement Options" : "These are optional modes of settlement that are provided by most life insurance policies. Options include lump-sum cash, interest only, fixed-period, fixed-amount, and life income.",
"Single Premium Funding" : "This is a policy funding option in which the policy owner pays a single premium that provides protection for life as a paid-up policy.",
"Spendthrift Clause" : "This clause prevents creditors from obtaining any portion of policy proceeds upon an insured’s death. Additionally, the clause can be selected by the policy owner to prevent a beneficiary from recklessly spending benefits by requiring the benefits to be paid in fixed amounts or installments over a certain period.",
"Surrender Cost Index" : "This is a cost comparison calculation formula which is used to determine the average cost-per-thousand for a policy that’s surrendered for its cash value. It aids in cost comparisons if the policy owner plans to surrender the policy for its cash value in 10 or 20 years.",
"Tertiary Beneficiary" : "This is the third beneficiary in line to receive death benefit proceeds. The tertiary beneficiary will only receive the death benefit if both the primary and contingent beneficiaries die before the insured.",
"Underwriting Department" : "This is the department within an insurance company that’s responsible for reviewing applications, approving or declining applications, and assigning risk classifications.",
"Unearned Premium" : "This includes the premium that has been paid by a policy owner for insurance coverage which has not yet been provided.",
"Uniform Simultaneous Death Act" : "This act states that if the insured and the primary beneficiary die in a common accident at approximately the same time, with no clear evidence as to who died first, the law will assume that the primary died first. Therefore, the death benefit proceeds are paid to the contingent beneficiaries.",
"Viatical Settlement" : "This settlement involves a person with a terminal illness selling his existing life insurance policy to a third party for a percentage of the death benefit.",
"Viatical (Viatee)" : "This is the new third-party owner in a viatical settlement.",
"Viator" : "This is the original policy owner in a viatical settlement.",
"Age of the Proposed Insured" : "The older the person, the higher probability of death and disability",
"Sex/Gender" : "Women tend to live longer than men; therefore, their premiums are typically lower.",
"Health History of Proposed Insured" : "Poor health increases the probability of death and disability.",
"occupation" : "Having a hazardous job can increase the risk of loss.",
"Personal Activities and Hobbies" : "High-risk activities or hobbies (e.g., parachuting) also increase the risk of loss.",
"Personal Habits" : "Tobacco use, DWI, or DUI presents a higher risk.",
"Travel Outside the United States" : "This travel can expose a proposed insured to additional risks and/or illnesses.",
"PAYING PREMIUMS FROM POLICY VALUES" : "Depending on the type of policy, a policy owner may be able to use the policy’s cash value and dividends to pay the premium. With dividends, a policy owner could choose to pay down premiums on the existing policy or buy additional coverage in the form of paid-up whole life additions or one-year term. While using the policy (cash) value to pay premiums is an option, this funding method also decreases the value of the policy. The policy will lapse if the policy’s value becomes insufficient, and the policy owner fails to pay the required premium.",
"MINIMUM DEPOSIT (FINANCED) INSURANCE" : "a method of financing life insurance that’s best suited for individuals who are in high marginal tax brackets. It allows the policy owner to use policy loans to pay premiums that are due each year. The policy owner only pays the difference between the premium due and the amount borrowed (plus interest on the policy loan). For this payment method to work, the policy owner must make two to three initial premium payments to build up the cash value. Additionally, under IRS rules, at least four of the initial seven annual premiums must be paid from funds other than policy loans to avoid classification as an MEC.",
"Legal Researve" : "is the amount of funds an insurance commissioner (or director/superintendent) requires an insurer to maintain based on the CSO mortality table and the assumed rate that’s designated by the state’s commissioner or state insurance law.",
"NAIC Model Life Insurance Solicitation Regulation" : "requires two interest-adjusted cost indexes for policy illustrations—a surrender cost index and a net payment cost index. These indexes show average annual costs and payments per $1,000 of insurance, while also recognizing that $1.00 payable today is worth more than $1.00 payable in the future (i.e., the time value of money).",
"Comparative Interest Rate" : "the rate of return required on the investment account, so that the value of the investment is equal to the surrender value of the higher premium policy at a specific point (i.e., 30 years or death). The higher the comparative interest rate (CIR), the less expensive the higher-premium permanent policy is compared to the alternative plan.",
"Chronically ill" : " This is a person who needs considerable supervision due to cognitive impairment or is unable to perform at least two activities of daily living (eating, toileting, transferring, bathing, dressing, or continence).",
"Terminally ill" : "This is a person who’s not expected to survive a medical condition for more than 24 months.",
"Beneficiary Qualifications" : "Individuals – a person who’s identified by name and relationship (e.g., spouse, daughter)\n Class designations – a group of individuals (e.g., children of the insured, all siblings)\nBusinesses – businesses often hold life insurance policies on the owner or key personnel to help mitigate the expense involved in finding a replacement\n Charities – as a lump-sum donation or to create continued funding (e.g., a scholarship fund)\nTrust – provides management of the proceeds\n Estate – although a policy owner may choose to list an estate as a beneficiary, it’s typically not advisable",
"Filing (recording) Method" : "is the predominant method used and requires the policyholder to notify the insurer in writing of the desired change. The effective date of the change is the date of the request. Some insurers require a witness to sign the request.",
"Endorsement Method" : "the policy is returned to the insurer so that the new beneficiary designation can be added to the policy. The effective date of the change is the date that the new policy is printed.",
"DISTRIBUTION TO A MINOR" : "A life insurance company typically will NOT pay policy proceeds directly to a minor beneficiary. Although any entity can be named as a beneficiary, many states don’t permit proceeds to be paid to a minor since she lacks “legal capacity.” ",
"DISTRIBUTION TO A TRUST" : "Trusts may be named as the beneficiary of a life insurance policy and manage the proceeds upon the insured’s death. Naming a trust as beneficiary is the most advantageous designation to use if a policy owner wants to leave policy proceeds to a “minor” child.",
"Testamentary Trust" : "is created at the time of the insured’s death according to a will.",
"Inter vivos (living) Trust" : "is created during the life of the insured.",
"Facility of Payment" : "permits an insurer to pay a portion (or all) of the policy proceeds to ANY individual who appears to be equitably entitled. Such payment may be provided to a party who paid for the medical or final expenses of the insured who has died. Typically, the facility of payment provision arises when a death claim is not filed within two months following the death of the insured. Additionally, this provision may be triggered to assist a guardian when a minor is listed as the beneficiary.",


# Chapter Exam Questions Start Here
"Mortality costs" : "What would be an expense factor in an insurance program?",
"from insurer to insurer and no cash is received by the policyowner" : "A tax-free Section 1035 Exchange of a life insurance policy to a different policy is permitted if it occurs",
"Extended Term" : "All of these are settlement options for life insurance policies EXCEPT",
"Irrevocable Beneficiary" : "A policyowner is prohibited from making any changes to the policy without the beneficiary's written consent under which beneficiary designation?",
"Liquidity" : "Insurance premium is determined by each of the following factors EXCEPT",
"have premiums that are averaged over the policy period" : "Level premium term life insurance policies",
"Estate Conservation" : "Purchasing a life insurance policy in order to avoid the forced sale of assets upon death is called",
"Irrevocable" : "Sharon is the policyowner of a $50,000 life insurance policy. Her son, Mike, is the beneficiary. If Sharon MUST obtain Mike's signature in order to change the beneficiary, what kind of beneficiary designation is this?",
"1035 Exchange" : "Tonya has replaced her whole life policy with an annuity without incurring a tax penalty. This transaction is called a(n)",
"the insured outlived the beneficiary" : "If the beneficiary dies from the same accident as the insured individual, the insurer will proceed as if",
"Monthly" : "Over the course of a year, which premium payment mode is most expensive?",
"Bi-Weekly" : "Which of these premium payment frequencies is not typically available to a policyowner?",
"Individual" : "Which type of beneficiary should be named if the insured wants to give explicit directions on how the policy proceeds should be paid?",
"People and Time" : "Mortality is calculated by using a large risk pool of",
"Common Disaster Clause" : "Pat is insured with a life insurance policy and Karen is his primary beneficiary. They are both involved in an automobile accident where Pat dies instantly and Karen dies 5 days later. Which policy provision will protect the rights of the contingent beneficiary to receive the policy benefits?",



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
