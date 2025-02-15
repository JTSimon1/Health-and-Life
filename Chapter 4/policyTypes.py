import random

# Define the quiz questions and answers
word_definitions = {
"Accidental Death and Dismemberment Insurance (AD&D)" : "This is a form of insurance that provides benefits in the event of accidental death; the accidental loss of sight, speech, or hearing; loss of use of limbs (i.e., paralysis); or loss of a member(s), such as the loss of an arm or a leg.",
"Accidental Death Benefit (ADB)" : "The ADB provides a lump-sum payment for loss of life due to an accident that was the direct cause of death. The cause of the death must be accidental for a benefit to be payable under the policy.",
"Additional Premium" : "This provision is used in Universal Life Policies. Additional premiums can be paid into the policy account in an amount above the target premium. Current tax laws limit the amount of excess cash value that can be accumulated in a life insurance policy. The insurance company may not accept the additional premium if it nears this limit without increasing the limit of life insurance (subject to underwriting).",
"Attained Age" : "This is the age that a person or an insured has attained as of a given date. For life insurance purposes, the age is based on either the nearest birthday or the last birthday, depending on the practices of the insurance company involved. Attained age is also referred to as “current age.”",
"Adjustable Life Insurance" : "This is a type of policy that combines permanent, whole life, and temporary term life into a single plan that provides the policy owner with the flexibility to adjust premiums throughout the life of the policy.",
"Cash Surrender (non-forfeiture) Value" : "This is the amount that’s available in cash upon the surrender of a policy by the owner before or after the policy matures (as a death claim or otherwise). This value is also simply referred to as surrender value.",
"Cash Value" : "This is the equity portion of a whole life policy that increases with each subsequent premium payment. The insurer pays interest on the cash value, which is tax-deferred. In a whole life policy, the cash value is designed to equal the policy’s death benefit at age 100. Traditional whole life insurance policies are considered to mature when the insured attains the age of 100.",
"Credit Insurance" : "This is insurance that’s designed to pay the balance of a loan if the insured dies or becomes permanently disabled before the loan has been repaid in full. Generally, credit insurance is sold by a lender or finance company.",
"Convertible Term Life Insurance" : "This is temporary life insurance that provides the policy owner with the right to exchange an existing policy for other policies that are offered by the insurance company. This conversion may be the conversion of individual term insurance to an individual permanent plan that a company sells or the conversion of group disability, life, or health to an individual plan.",
"Decreasing Term Insurance" : "This is a type of temporary or pure protection that’s characterized by a reducing face amount each year and the cost of this coverage remains constant. Decreasing term insurance may be referred to as mortgage redemption or mortgage protection insurance since it’s primarily used in conjunction with a debt or loan.",
"Endowment Contract" : "This contract pays a face amount after a fixed time period, at a specific age, or upon the death of the insured if it occurs before the end of the period.",
"Evidence of Insurability" : "This involves an insurance applicant establishing the fact that they meet the insurance company’s health requirements. Statements of good health, attending physician statements, health history, and an applicant’s current health can all be used as evidence of insurability.",
"Extended Term Insurance" : "This is a non-forfeiture option that’s available when a policy is surrendered and the same face amount of the policy is continued in force for a specified additional period; however, the coverage has changed from permanent to level term protection. Extended term insurance is the non-forfeiture option that provides the policy owner with the highest face amount of coverage.",
"Face Amount" : "This is another name for the death benefit of a life insurance policy.",
"Family Income Policy" : "This is a policy that combines a whole life policy with a decreasing term rider to provide a death benefit together with monthly income payments to the beneficiary. Monthly income payments are made only from the date of death until the maturity date of the contract. Thereafter, the lump sum part of the whole life coverage is paid.",
"Family Maintenance Policy" : "This is a type of policy that combines whole life insurance and a level term rider. It provides for the payment of a monthly income during a stated period of years once the insured dies. The monthly income is payable from the date of death to the end of the pre-selected period. The payment of the face amount of the policy is payable at the end of the pre-selected period.",
"Family Policy" : "This is a policy that covers an entire family. Whole life insurance covers the primary insured (i.e., breadwinner) with varying amounts of level term insurance on the remainder of the family.",
"Guideline Premium" : "This represents the maximum premium that can be paid into universal life policies and still have the benefit qualify as life insurance under federal tax laws. If a guideline premium is paid regularly, there may be little margin for any additional premium payments into a universal life insurance policy account.",
"Indexed Contracts" : "These are contracts in which the policy holder can share in a percentage of the growth of an indexed investment (e.g., a mutual fund tied to the Standard & Poor’s Index). The principle (benefit) is guaranteed, and in many cases, a minimum interest is guaranteed. These products are not considered securities.",
"Increasing Term Life Insurance" : "This is term life insurance that provides an increasing face amount over time based on specific amounts or a percentage of the original face amount.",
"Industrial Life Insurance" : "This is insurance under which premiums are paid monthly or more often (i.e., weekly). Additionally, the face amount of the policy doesn’t exceed a stated amount, and the words “industrial policy” are printed in prominent type on the face of the policy. Industrial life insurance is also referred to as “debit insurance.”",
"Joint Life Insurance (First to Die Insurance)" : "This is a life insurance policy that covers the lives of two or more persons. The policy pays a death benefit and ends when the first insured dies. This type of policy is also referred to as “first to die” insurance.",
"Joint Life Survivor (Last to Die Insurance)" : "This is a life insurance policy that covers the lives of two or more persons. The policy pays a death benefit and ends when the last insured dies. This type of policy is also referred to as “last to die” insurance.",
"Juvenile Life Insurance" : "This is a life insurance policy that’s owned by an adult and written on the lives of children.",
"Level Premium" : "This describes a premium that remains constant, fixed, or predetermined throughout the life of a policy.",
"Life Insurance" : "This represents insurance on the lives of human beings that creates an immediate and guaranteed estate upon the death of an insured or at the end of a predetermined period (in whole life insurance, this is age 100).",
"Limited Pay Life Insurance" : "This is a life insurance plan under which the premiums are payable for a specified number of years, after which the policy remains in effect for life without any additional payments. However, the policy still doesn’t mature until age 100.",
"Maturity Date" : "This is the date on which a life insurance policy becomes payable due to the death of the insured or as a result of an insured’s living to the end of a specified period (i.e., age 100). In whole life insurance, the cash value is designed to equal the face amount at maturity.",
"Maturity Value" : "This is the amount that’s paid under a whole life insurance contract if the insured reaches the age of the mortality table on which the contract was based. If it’s an endowment contract, it represents the cash value amount at the end of the endowment period.",
"Modified Endowment Contract (MEC)" : "This is a whole life insurance policy under which the amount a policy owner pays in premium during the early years exceeds the sum of premiums required for the first seven years of insurance. The IRS views MECs as the policy owner’s attempt to use the policy as a short-term investment vehicle, and as such, the policy will be designated for tax purposes as an MEC.",
"Modified Life Policy" : "This is a whole life plan that’s characterized by a lower premium during the initial years of the contract to make it more affordable for the policy owner. The premium then increases after this introductory period and remains level for the life of the contract.",
"Mortgage Redemption Plan" : "This is another name for a decreasing term life insurance policy. This type of plan is used to provide funds for a survivor to pay off a debt. This type of plan is also referred to as mortgage protection coverage or reducing term insurance.",
"Mutual Insurance Company" : "This is an insurance company that’s owned and controlled by its policy holders. Mutual insurance companies issue participating policies that may pay dividends to policy holders.",
"Non-Forfeiture Values" : "These are benefits that are required by law to be made available to the policy owner if she surrenders the policy by discontinuing premium payments. These values state that the owner will not forfeit or lose all that she has invested in the policy. Also referred to as non-forfeiture options, they include surrender for cash, extended term insurance, and reduced paid-up insurance.",
"Non-Medical Life Insurance" : "This is issued without requiring the applicant to submit to a medical examination. The insurer relies on the applicant’s answers to the questions regarding his physical condition, personal references, and inspection reports. However, the insurance company retains the right to require a medical examination if an investigation indicates a need for one.",
"Non-Participating Insurance" : "This is a type of insurance policy that’s issued by a stock insurer. This form of insurance contract doesn’t pay dividends to the policy holders.",
"Ordinary Life Insurance" : "This is most often described as an insurance policy that’s issued by commercial insurers with face values of $1,000, or multiples thereof.",
"Paid-Up Insurance" : "This is life insurance on which future premium payments are not required. Frequently, the term is used to identify a 10, 20, or 30 payment life insurance policy on which 10, 20, or 30 annual premium payments have been paid. Although the policy is “paid-up” at the end of the payment period, the contract doesn’t mature until the age of 100.",
"Participating Insurance" : "This is a type of insurance policy that entitles the policy holder to share in the divisible surplus of the insurer through dividends.",
"Permanent Life Insurance" : "This is any plan of life insurance that’s designed to last throughout the life of the insured. Level premium, cash value, and non-forfeiture options characterize permanent life insurance.",
"Policy Proceeds" : "This refers to the amount that’s paid as a death, surrender, or maturity benefit. In the case of a death benefit, it includes the face value, plus any earned dividends, minus any outstanding loans and interest. If paid as a surrender benefit, the amount includes any cash value, minus surrender charges, outstanding loans, and interest. If the benefit is paid at maturity, the benefit includes the cash value, minus any outstanding loans and interest.",
"Policy Term" : "Typically expressed in years, this is the time for which a policy remains in existence.",
"Renewable Term Life Insurance" : "This is temporary life insurance that may be renewed at the end of the policy term without evidence of insurability. The premium is based on the attained age of the insured and, as such, increases at each renewal.",
"Single-Premium Insurance" : "This form of insurance involves the payment of one premium that’s large enough to cover the cost of a life or annuity contract for life. This is also referred to as a lump-sum premium.",
"Straight Life Insurance" : "This is a type of whole life insurance that provides coverage for the entire life of the insured and for which the premiums are payable until death. This is also referred to as continuous premium life.",
"Stock Insurance Company" : "This is an insurance company that’s owned and controlled by its stockholders who share in its divisible surplus. Generally, stock insurance companies issue non-participating life insurance; however, some also issue participating life insurance policies.",
"Target Premium" : "This represents the suggested premium that’s used in universal life insurance policies; however, there’s no guarantee that there will be adequate funds to maintain the policy. Instead, it may indicate what will be needed (under conservative estimates) to maintain the policy. The validity of a target premium is based on an individual insurance company’s marketing stance, investment performance, and cost control.",
"Term Life Insurance" : "This is temporary life insurance that’s generally designed to afford coverage for a limited number of years. The policy includes no cash value and can be described as pure protection.",
"Universal Life Insurance" : "This is adjustable life insurance under which premiums and coverage are adjustable. For a universal policy, company expenses are not explicitly disclosed to the insured, but a financial report is provided to policy holders annually.",
"Variable Life Insurance" : "This is life insurance whose face value or duration varies depending on the value of underlying securities.",
"Variable Universal Life Insurance" : "This form of insurance combines the flexible premium features of universal life with the component of variable life in which excess credited to the cash value of the account depends on investment results of separate accounts. The policy holder selects the accounts into which the premium payments are to be made.",
"Whole Life Insurance" : "This is the form of life insurance that may be kept in force for a person’s entire life, and that pays a benefit upon the person’s death.",
"Level Term Life Insurance" : "provides a constant or fixed amount of coverage for as long as the policy remains in force. This form is characterized by a level face amount (death benefit) for a specified period. A level term policy expires at the end of the policy period.",
"Interim Term Life Insurance" : "s a type of convertible term insurance that’s written on a person who wants protection immediately, but who’s not able to afford permanent protection immediately. It provides interim coverage between now with the eventual conversion to permanent protection.",
"Step-Up Premium" : "The premiums for each renewal period will be higher than the initial period, reflecting the insured’s increased age and increased risk.",
"Annually Renewable Term (ART) or Yearly Renewable Term (YRT)" : "life insurance provides coverage for one year and allows the policy owner to renew coverage each year, without evidence of insurability.  This renewal is typically automatic and renews with an increased premium cost each renewal period. This type of term life insurance policy provides an insured with two sets of premium rates—a current or scheduled premium (based on the insurer’s current cost of insurance) and a guaranteed maximum premium (based on the maximum the insurer agrees to increase the cost of insurance).",
"Re-Entry (Revertible) Term Insurance" : " which states that the premium can change at renewal based on insurability. The insured has the option of taking the standard renewal rate without proving insurability. However, to maintain the lowest premium rate (or a discount from standard), the insured may be required to prove insurability again upon renewal. If there’s an insurability problem (i.e., the insured fails the medical exam), coverage may be maintained but at a higher premium rate.",
"Advantages of Term Life Insurance" : "Term life insurance is less expensive than permanent insurance.\n Term life insurance may protect the insured’s insurability if the policy is renewable and/or convertible.\n Term life insurance may be used in conjunction with debts, mortgages, or as a supplement to whole life insurance.\n Term life insurance provides the most substantial amount of protection for the lowest cost.",
"Disadvantages of Term Life Insurance" : " The protection provided by term life insurance policies terminates with the policy terminates. No protection is in effect once the term protection ends.\n If the term life insurance policy is renewable or convertible, premium rates rise as the insured ages. This premium increase often leads to policy cancellation prior to the policy terminating.\n Due to the temporary nature of term insurance, few death claims are actually paid under term life insurance policies.\n Term life insurance policies don’t contain any cash savings or equity elements (i.e., cash value). Since it has no cash value, it doesn’t mature like a whole life policy.",
"Bundled Premiums" : "the insurer is not required to explain to the policy owner how the premium paid is ultimately distributed (i.e., for death protection, commissions, and other expenses). Premium rates are based on a dollar amount per $1,000 of coverage and are typically expressed annually.",
"Single pRemium Whole Life Insurance Policy" : "the extreme form of a limited payment policy and is characterized by a lump-sum or single premium payment. Therefore, the policy is fully paid-up upon the payment of a lump-sum premium. Some single premium plans are in existence, which consists of two premium payments, such as a “dual premium” policy. Single premium plans may possess tax advantages and the ability to borrow against the cash value at below-market interest rates. However, when compared to a straight life policy over the life of the contract, the single premium life is the least expensive.",
"Non-traditional Whole Life Insurance" : "The premium charged for these plans is less than that for a straight life insurance policy in the first few years of the policy. Cash values also accumulate with each premium payment. Insureds who need permanent protection but cannot afford the higher traditional whole life premiums required, will buy this type of policy.",
"Graded Premium Whole Life Insurance" : "is a contract that’s characterized, like modified life, by a lower premium than whole life in the early years of the contract. However, premiums increase annually or every year for the initial period. Thereafter, it jumps to an amount that’s higher than the whole life premium and remains fixed for life. The premiums for these policies are predetermined, but are not level in the traditional sense, as they would be in the traditional straight whole life or limited pay whole life plans.",
"Enhanced Whole Life Insurance (Economatic / Extraordinary Life)" : " is a low premium based participating permanent insurance policy. The contract’s face amount is reduced each year. Any dividends that are paid are set aside and used to purchase either paid-up additions or one-year term insurance which is equal to the reduction of death coverage. This policy provides a guaranteed death benefit in the early years of the policy, even if dividends are insufficient to maintain level coverage.",
"Indeterminate Premium Whole Life Insurance" : " is a type of whole life policy that provides low initial premium costs for a specified period. After that period, the insurer may then increase premiums. The characteristics of and benefits provided by this policy are similar to other contracts. However, an indeterminate premium whole life policy allows for a change of premium due to a change in the investment income of the insurer. Therefore, future premium adjustments are based on the insurer’s investment performance, mortality experience, and expenses. Premiums may be raised or lowered by the company, but they can never exceed the guaranteed maximum.",
"Current Assumption Whole Life (CAWL) / Interest Sensitive Whole Life" : "Is characterized by premiums that vary to reflect the insurer’s changing assumptions concerning its death, investment, and expense factors. However, interest-sensitive products also provide that the cash values may be higher than the guaranteed levels. If the company’s underlying death, investment, and expense assumptions are more favorable than expected, policy owners will have two options—lower premiums or higher cash values. Underlying assumptions could also turn out to be less favorable than anticipated, which would call for a higher premium than that at policy issue.",
"Partial Surrender" : "The policy owner may then either pay the higher premium or choose to reduce the policy’s face amount and continue to pay the same premium. An interest-sensitive life insurance policy owner may be able to withdraw the policy’s cash value interest-free. ",
"Low Premium Type" : " includes an indeterminate premium that’s initially low. It also contains a redetermination provision, which states that after a specified period, the insurance company can refigure the premium.",
"High Premium Type" : "the initial premium is relatively high. It possesses an optional pay-up provision which states that the policy owner may cease paying premiums once the policy’s values are sufficient to pay-up the contract.",
"Equity Index Whole Life Insurance" : " This type of policy combines most of the features, benefits, and security of traditional life insurance with the potential of earned interest based on the upward movement of an equity index. Rather than the policy including a specific interest rate (as in a traditional whole life plan), interest earnings are credited based on increases in the specific equity index (e.g., the S&P 500 Index) to which the policy is linked. Therefore, credited interest is linked to an index without the downside risk connected with directly investing in the stock market. These policies are characterized by a guaranteed minimum interest rate, tax deferral of interest accumulations, and policy loan access.",
"Adjustable Life Insurance" : "This type of permanent insurance product combines elements of traditional fixed premium whole life insurance with the potential to adjust the coverage or face amount based on the policy owner’s changing needs. ",
"Unbundled Premium" : " This means that the contract owner is provided with information describing where the policy costs are allocated. In other words, the contract owner receives a breakdown of premiums, death benefits, mortality charges, expenses, and cash values. This breakdown shows the contract owner the disposition of the policy funds.",
"Death Benefit" : "Under Option A (also referred to as Option One), a level death benefit is provided. The net amount at risk (NAR) is adjusted after each month. As such, a mortality charge is deducted from the policy’s cash savings plan monthly. Therefore, the cash value and NAR (benefit) together provide a fixed death benefit. Option B (also referred to as Option Two) provides an increasing death benefit as the cash value increases. As such, the death benefit equals the face amount plus the cash value at the time of death.",
"Waiver of Monthly Deduction Rider (Waiver of the Cost of Insurance)" : "This rider waives the monthly portion of the premium that pays for the expenses of the policy (e.g., contract expenses and mortality charge), but not the portion that’s allocated to the cash value.",
"No Lapse Guarantee Rider" : "guarantees that the policy will not terminate before a determined date if specified amounts of premium are paid, and any policy loan plus accrued loan interest don’t exceed the cash surrender value. The length of the policy’s guarantee period generally ranges from five to 40 years, depending on the age of the insured when the policy was issued. Some (but not all) insurers charge an extra premium for this rider.",
"Special Use" : "Many of these are a combination or packaging of different types of policies that are designed to serve a variety of needs.",
"Decreasing Term Insurance" : "Julie has a $100,000 30-year mortgage on her new home. What type of life insurance could she purchase that is designed to pay off the loan balance if she dies within the 30-year period?",
"The Face Amount" : "What does the word 'level' in Level Term describe?",
"Level Premiums (Exam Answer)" : "When a decreasing term policy is purchased, it contains a decreasing death benefit and?",
"Can Be converted to permanent coverage without evidence of insurability" : "Donald is the primary insured of a life insurance policy and adds a children's term rider. What is the advantage of adding this rider?",
"Hedge against Inflation" : "Index whole life insurance contains a securities component that acts as a(n)",
"Family Term Insurance Rider" : "Which of these riders will pay a death benefit if the insured's spouse dies?",
"Universal Life Policy" : "Joe has a life insurance policy that has a face amount of $300,000. After a number of years, the policy's cash value accumulates to $50,000 and the face amount becomes $350,000. What kind of policy is this?",
"Equity Index Whole Life" : "Peter has a policy where 80% to 90% of the premium is invested in traditional fixed income securities and the remainder of the premium is invested in contracts tied to a stipulated stock index. What kind of policy is this?",
"Variable Universal Policy" : "Which type of life insurance offers flexible premiums, a flexible death benefit, and the choice of how the cash value will be invested?",
"$500,000" : "Rob purchased a standard whole life policy with a $500,000 death benefit when he was age 30. His insurance agent told him the policy would be paid up if he reached age 100. The present cash value of the policy equals $250,000. Rob recently died at age 60. The death benefit would be",
"Policyowner has the right to select the investment which will provide the greatest return" : "Variable life insurance and Universal life insurance are very similar. Which of these features are held exclusively by variable universal life insurance?",
"Renewal" : "What is the automatic continuance of insurance coverage referred to as?",
"Term" : "Which of the following policies does NOT build cash value?",
"Separate Account Investments" : "Which of the following are the premium payments for a Universal life policy NOT used for?",
"lifetime protection" : "A limited payment whole life policy provides",
"Limited Pay Policy" : "A permanent life insurance policy where the policyowner pays premiums for a specified number of years is called a(n)",
"the MEC tends to be an investment vehicle" : "Pre-death distributions from a modified endowment contract (MEC) receive different tax treatment than other life insurance policies because",
"seeks temporary protection and lower premiums" : "Term insurance is appropriate for someone who",
"The shorter the payment period, the higher the premium" : "The statement which best describes the relationship between the premiums of a whole life policy and the premium payment period is",
"Endowment Policy (Exam Answer)" : "Which type of life insurance policy pays the face amount at the end of the specified period if the insured is still alive?",


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
