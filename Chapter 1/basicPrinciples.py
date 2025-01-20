import random

# Define the quiz questions and answers
word_definitions = {
    "Actuarial Department": "Calculates policy rates, reserves, and dividends. They also make other applicable statistical studies and repoorts. Concerned with thte cost of insurance as a whole or the cost for a specific class of risk.",
    "Adjuster" : "This is a person who investigates claims and arranges for them to be settled or denied.",
    "Alien Insurer": "An insurer whose principal office and domiciled location is outside the country.",
    "Admitted Insurer": "An insurer who has received a certificate of authority from a state's department of insurance authorizing them to conduct insurance business in that state.",
    "Agent" : "This is an individual or organization that's authorized to solicit, sell, and transact (bind) coverage for specific insurance providers under the terms of one or more agent contracts.",
    "Authorized Insurer" : "This is an admitted insurer",
    "Broker": "Represents themselves and the insurered (i.e., the client or customer)",
    "Captive Insurer": "An issuer established and owned by a parent firm for the purpose of insuring the parent firm's losss exposure.",
    "Certificate of Authority": "A license issued to an insurer by a departmetn of insurance (or equivalent state agency), which authorizes that company to conduct insurance business in that particular state.",
    "Claims Department": "Is responsible for processing, investigating, and paying claims.",
    "Divisible Surplus": "The amount of earnings paid to policyowners as dividends after the insurance company sets aside funds required to cover reserves, operating expenses, and general business purposes.",
    "Domestic Insurer": "An insurer with its principal or home office in a state where it is authorized.",
    "Foreign Insurer": "An insurer with its principal office or domicile location in a state different from the state it is transacting insurance business.",
    "Fraternal Benefit Society" : "This is a non-profit benevolent organization that provides insurance to its members. MUST : 1) be a non-profit, 2) have a lodge system that includes ritualistic work and must maintain a representative government form with elected officers, 3) Exist for reasons other than obtain insurance.",
    "Independent Insurance Agency" : "This is an agency that any number of insurance compnaies through contractual agreements.",
    "Industrial Insurer": "A specialized brnach of the industry, primarily provideing policies with small face amounts with weekly premiums (i.e., home service/debt insurers)",
    "Insurance": "The transfer of risk through the pooling or accumulation of funds.",
    "Insured": "The customer recieving insruance protection under an insurance policy.",
    "Insurer": "The insurance comapny",
    "Lloyds of London": "NOT an insurer, but a group of individuals and companies that underwrite unusual insurance.",
    "Marketing Division" : "This is the division responsible for acquiring prospective applicants through various advertising media.",
    "Monoline Insurer" : "This is an insurance carrier that only sells one line of insurance.",
    "Multi-Line Insurer": "An insurance company or independent agent hat provides a one-stop-shop for businesses orindividuals seeking coverage for all their insurance needs.",
    "Mutual Insurance Company": "Insurance companies characterized by ahving no capital stock, being owned by its policy owners, and usually issue participating insurance.",
    "Non-admitted Insurer": "An insurer who has not received a certificate of authority from a state's departmetn of insurace authorizing them to conduct insurance business in that state.",
    "Non participating policy": "An insurance policy, typically issued by stock companies, do not allow policyowners to participate in dividends or electing the board of directors.",
    "Participating Plan": "An insurance policy under which the policy owners share in the company's earnings through receipt of devidends and also elect the company's board of directors.",
    "Personal Producing General Agency (PPGA)" : "This is an agency that represents one or more specific insurers. A PPGA is a similar agency system, but don't recruit, train, or supervise career agents.",
    "Policy Owner" : "This is the person who's responsible for the payment of premiums and who possesses all ownership rights of the contract. Typically, the policy owner is also the insured.",
    "Private (Commercial) Insurer": "Companies owned by private citizens or groups that offer one or more insurance lines. NOT GOVERNMENT OWNED",
    "Producer" : "This is an individual who's licensed by one or more states to sell, solicit, or transact insurance in a given state.",
    "Proposed Insured" : "This is the person whose life will be covered by an insurance policy.",
    "Public Adjuster" : "This person acts on behalf of a consumer who's settling an insurance claim.",
    "Reciprocal Insurer": "An unincorporated organization in which all mebers insure one another.",
    "Reinsurance" : "The acceptance by one or more insurers, of a portion of the risk underwritten by another insurer who has contacted for the entire coverage.",
    "Risk Retention Group": "A group-owned liability insurer which assumes and spread product liability and other forms of commercial liability risks among its members.",
    "Sales Department" : "This department acquires clients through one-on-one meetings in which consumers complete applications.",
    "Self-Insurers": "Establishes a self-funded plan to cover potential losses instead of transferring the risk to an insurnce company.",
    "Service Representatives" : "These are customer service employees. Service representatives are not required to obtain a license because they neither sell nor solicit coverage, and they don't bind coverage.",
    "Solicitors" : "These are the individuals who solicit and schedule sales meetings between consumers and the producers for whom they work. Some states separately license these individuals.",
    "Stock Insurance Company": "An insurance company owned and controlled by a group of stockholders whose investmetn in the company provides the safety margin necessary in the issuance of guaranteed, fixed premium, nonparticipating policies.",
    "Surplus Lines Insurance": "A nontraditional insurance only available froma surplus lines insurer. They offer coverage for substandard or unusual risks not available throgh pribate or commercial carriers.",
    "Unauthorized Insurer" : "This is a non-admitted insurer.",
    "Underwriting Department": "The department within an insurance company responsible for reviewing applications, approving or declining applications, and assigning risk classifications.",
    "Indemnify Policyholders" : "The policies restore insureds to the financial position they experienced before the insured loss.",
    "Principle of Indemnity" : "The goal of an action isto 'restore' an insured to the same financial position they were in prior to when the loss in question occurred.",
    "Social Insurance" : "Insurers that are operated bya federal or state entity, either: 1) Write insurance to cover catastrophic perils or losses that are not insurable by commercial insurers (war, flood, etc.). 2) Write insurance on insurable risks in competition with commercial insurance or possibly instead of them.",
    "Attorney-in-fact" : "Handles transactions for the reciprocal insurer and is authorized to conduct the day-to-day affairs of the insurer on behalf of the subscribers.",
    "Risk Purchasing Group" : "Operate under the Federal Liability Risk Retention Act (LRRA) of 1986. The organization provides liability insurance for individuals and entities with a common bond. Membership allows for increased bargaining power and streamlined administration for individuals and businesses participating in the group.",
    "Conference of Insurance Legislators (NCOIL)" : "A legislative organization that focuses on the insurance industry. Works to preserve state regulation of the industry and to educate public policymakers on related issues.",
    "Agent Marketing and Sales Practices" : "Selling to needs: An ethical agent learns the client's needs and determines the best way to address those needs. \n Suitability of recommended products:  The ethical agent assesses the correlation between a recommended product and the client’s needs and capabilities. \n Full and accurate disclosure.  The ethical agent makes it a practice to inform clients about all aspects of the products being recommended, including benefits and limitations. \n Documentation.  The ethical agent documents each client’s meeting and transactions. He also uses fact-finding forms and obtains the client’s written agreement for the needs determined, the products recommended, and the decisions made. \n Client service.  The ethical agent knows that a sale doesn’t mark the end of a relationship with a client but rather the beginning.",
    "Producer Responsiblies" : "Providing customers with the best service possible. \n Soliciting new business for his company by helping clients acquire products from application to policy delivery. \n Guiding customers to the right products that meet their needs and maintaining a relationship with them. \n Building a business by keeping current customers satisfied and also actively seeking referrals.",
    "reserves" : "Are the accounting measurement of an insurer's future obligations to its policyholders.",
    "Liquidity" : "Indicates a compnay's ability to make unpredictable payouts to policy owners.",
    # Federal Court Cases and LEgislation Affecting the Regulation of the Insurance Industry
    "1868 – Paul v. Virginia" : "As decided by the U.S. Supreme Court, this case involved one state’s attempt to regulate an insurance company that was domiciled in another state. The Supreme Court sided against the insurance company, ruling that the sale and issuance of insurance is not interstate commerce, thereby upholding a state’s right to regulate insurance.",
    "1944 – United States v. Southeastern Underwriters Association (SEUA)." : "The Supreme Court revisited the issue of state versus federal regulation of the insurance industry. In the SEUA case, the Supreme Court ruled that the insurance industry is a form of interstate commerce that’s regulated by the federal government and subject to a series of federal laws which often conflict with existing state laws. Although this decision did not affect states’ power to regulate insurance, it did nullify state laws that conflicted with federal legislation.",
    "1945 – The McCarran-Ferguson Act" : "The turmoil created by the SEUA case prompted Congress to enact Public Law 15, The McCarran-Ferguson Act. This law made it clear that the states’ continued participation in the regulation of insurance was in the public’s best interest. However, it also made possible the application of federal antitrust laws to the extent that the insurance business is not regulated by state law. This Act led each state to revise its insurance laws to conform to federal statutes. Today, the insurance industry is considered to be state-regulated. Any person who violates the McCarran-Ferguson Act faces a fine of $10,000 or up to one year in jail.",
    "1958 – Intervention by the FTC" : "In the mid-1950s, the Federal Trade Commission (FTC) sought to control the health insurance industry’s advertising and sales literature. In 1958, the Supreme Court held that the McCarran-Ferguson Act disallowed such supervision by the FTC—a federal agency. Additional attempts have been made by the FTC to force further federal control, but none have been successful.",
    "1959 – Intervention by the Securities and Exchange Commission (SEC)" : "In this instance, the issue was whether variable annuities are an insurance product that should be regulated by the states or a securities product that should be regulated federally by the SEC. The Supreme Court ruled that federal securities laws applied to insurers that issued variable annuities and, therefore, required these insurers to conform to both SEC and state regulations. The SEC also regulates variable life insurance.",
    "1970 – Passage of the Fair Credit Reporting Act" : "This Act attempts to protect an individual’s right to privacy. This law requires fair and accurate reporting of information about consumers, including insurance applications. Insurers must inform applicants about any investigations that are being conducted following the completion of the application. If any consumer report is used to deny coverage or charge higher rates, the insurer must provide the applicant with the name of the reporting agency that’s conducting the investigation.",
    "1994 – United States Code (USC) Sections 1033 and 1034 Regarding Fraud and False Statements" : "According to these sections of the USC, it’s a criminal offense for an individual who’s convicted of a felony involving dishonesty or a breach of trust to participate in the insurance business without first obtaining a “Letter of Written Consent to Engage in the Business of Insurance” from the appropriate state regulator.",
    "1999 – Financial Services Modernization Act (also referred to as the Gramm-Leach-Bliley Act or GLBA)" : "This Act allowed commercial banks, investment banks, retail brokerages, and insurance companies to engage in each other’s lines of business. The Financial Services Modernization Act repealed The Glass-Steagall Act of 1933, which barred common ownership of banks, insurance companies, and securities firms and erected a regulatory wall between banks and non-financial companies. MUST: 1) Notify consumers about their privacy policies, 2) Provide consumers with the opportunity to prohibit the sharing of their protected financial information with non-affiliated third parties, 3) Obtain affirmative consent from consumers before sharing protected health information with any other parties, affiliates, and non-affiliates.",
    "2001 – Uniting and Strengthening America by Providing Appropriate Tools Required to Intercept and Obstruct Terrorism Act (USA PATRIOT Act)" : "The USA PATRIOT Act was adopted in response to the terrorist attacks on September 11, 2001. The law aims to detect, deter, and disrupt terrorist efforts and funding while prosecuting international money laundering. These anti-money laundering (AML) measures impact the financial services community.",
    "2003 – Do Not Call Implementation Act" : "The Do Not Call Registry allows consumers to list their phones in a registry of numbers to whom telemarketers (including insurers) cannot legally make solicitation calls. Calls made on behalf of charities, political organizations, and surveys are exempt.",
    "2003-CAN-SPAM Act" : "This Act creates rules for commercial emails and messages. Specifically, the regulation outlines the right for a consumer to request a business to stop sending emails, the requirements for businesses to honor such requests, and the penalties incurred for those who violate the Act. The Act covers all electronic mail messages with the primary purpose of advertisement or promotion of a product, service, or commercial website. The Act does not apply to transactional and relationship messages. According to the Federal Trade Commission, the main requirements of the CAN-SPAM Act include the following: \n Don't use false or misleading header information \n don't use deceptive subject lines \n Indentify the message as an advertisement. \n Include the company's valid physical postal address in every email. \n Tell recipients how to opt out of receiving future emails. \n Honor opt-out requests promptly \n Dont charge a fee, require the recipient to give personally identifying information beyond an email address or make overcomplicate the process.",


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

