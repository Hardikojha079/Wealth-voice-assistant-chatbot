import pandas as pd
import random

# Original 10 Q&A pairs
original_qa = [
    ["What is the difference between stocks and bonds?", "Stocks represent ownership in a company, offering potential for higher returns but with higher risk. Bonds are debt instruments where you lend money to an entity for fixed interest payments, offering more stability but typically lower returns."],
    ["How should I diversify my investment portfolio?", "Effective diversification involves spreading investments across different asset classes (stocks, bonds, real estate), industries, geographic regions, and risk levels. Aim for a mix that aligns with your financial goals, time horizon, and risk tolerance."],
    ["What is dollar-cost averaging?", "Dollar-cost averaging is an investment strategy where you invest a fixed amount regularly regardless of market conditions. This reduces the impact of market volatility as you buy more shares when prices are low and fewer when prices are high."],
    ["How much should I save for retirement?", "A general guideline is to save 15-20% of your annual income for retirement. However, the ideal amount depends on your desired retirement lifestyle, expected retirement age, current age, and existing savings. Consider using the 4% rule for estimating your retirement nest egg."],
    ["What is the difference between a traditional IRA and a Roth IRA?", "Traditional IRAs offer tax-deductible contributions with taxes paid on withdrawals during retirement. Roth IRAs use after-tax contributions with tax-free qualified withdrawals. Traditional IRAs have required minimum distributions (RMDs) starting at age 72, while Roth IRAs don't have RMDs."],
    ["How do capital gains taxes work?", "Capital gains tax applies to profits from selling investments. Short-term gains (assets held less than a year) are taxed as ordinary income. Long-term gains (assets held over a year) are taxed at preferential rates: 0%, 15%, or 20% depending on your income bracket, plus potentially a 3.8% net investment income tax."],
    ["What is estate planning and why is it important?", "Estate planning involves arranging for the management and distribution of your assets after death. It includes creating wills, trusts, designating beneficiaries, and establishing power of attorney. It's important to ensure your wishes are fulfilled, minimize taxes, and prevent family disputes."],
    ["How do I choose between a financial advisor and robo-advisor?", "Financial advisors offer personalized guidance and comprehensive planning but charge higher fees (typically 1-2% of assets). Robo-advisors provide automated, algorithm-based portfolio management with lower fees (0.25-0.50%) but less personalization. Consider your needs for personalization, complexity of finances, and cost sensitivity."],
    ["What is the 4% rule in retirement planning?", "The 4% rule suggests withdrawing 4% of your retirement savings in the first year, then adjusting that amount for inflation each subsequent year. This approach is designed to provide income throughout retirement (typically 30 years) without depleting your principal too quickly."],
    ["How should I prioritize between paying off debt and investing?", "Generally, prioritize high-interest debt (>7%) before investing beyond employer matches. Pay off credit cards first, then consider student loans and mortgages based on interest rates versus potential investment returns. Maintain emergency savings regardless of debt situation. Balance emotional benefits of debt freedom with mathematical optimization."]
]

# Additional domain-specific Q&A pairs
additional_qa = [
    ["What is a mutual fund?", "A mutual fund is an investment vehicle that pools money from many investors to purchase a diversified portfolio of stocks, bonds, or other securities. Professional fund managers make investment decisions aligned with the fund's goals, providing diversification and professional management for individual investors."],
    ["How do ETFs differ from mutual funds?", "ETFs (Exchange-Traded Funds) trade on exchanges like stocks with prices fluctuating throughout the day, while mutual funds trade once daily at the closing NAV price. ETFs typically have lower expense ratios, greater tax efficiency, lower investment minimums, and more trading flexibility than mutual funds."],
    ["What's the difference between active and passive investing?", "Active investing involves attempting to outperform market indexes through strategic security selection and market timing. Passive investing aims to match market performance by tracking indexes with minimal trading. Active strategies have higher fees and potential for outperformance but most underperform passive approaches over time."],
    ["What is tax-loss harvesting?", "Tax-loss harvesting involves selling investments at a loss to offset capital gains tax liability. The strategy allows you to maintain market exposure by immediately reinvesting in similar (but not identical) securities. This can reduce your tax burden while maintaining your overall investment strategy."],
    ["How much should I have in an emergency fund?", "An emergency fund should typically cover 3-6 months of essential expenses, though some advisors recommend 6-12 months. Those with variable income or specialized careers might need larger reserves. Keep these funds in liquid, accessible accounts like high-yield savings accounts or money market funds."],
    ["What is asset allocation?", "Asset allocation is the process of dividing investments among different asset categories like stocks, bonds, real estate, and cash based on goals, risk tolerance, and time horizon. It's considered one of the most important factors in determining long-term investment performance and portfolio volatility."],
    ["How does a 401(k) work?", "A 401(k) is an employer-sponsored retirement plan where employees contribute pre-tax income, reducing their taxable income. Employers often match contributions up to a certain percentage. Investments grow tax-deferred until withdrawal in retirement, when they're taxed as ordinary income. Early withdrawals before age 59½ typically incur penalties."],
    ["What is a fiduciary financial advisor?", "A fiduciary financial advisor is legally obligated to put clients' best interests first, avoiding conflicts of interest and disclosing all fees and commissions. Unlike advisors following the suitability standard, fiduciaries must recommend the best options for clients rather than merely suitable ones. They typically charge transparent fees rather than commissions."],
    ["How do I create a financial plan?", "Creating a financial plan involves assessing your current situation, defining goals, identifying gaps, developing strategies, implementing changes, and regularly reviewing progress. Key components include budgeting, debt management, emergency savings, insurance coverage, retirement planning, investment strategy, tax planning, and estate planning."],
    ["What's the difference between term and whole life insurance?", "Term life insurance provides coverage for a specific period (10-30 years) with lower premiums and no cash value component. Whole life insurance covers your entire lifetime with higher premiums but includes a cash value component that grows tax-advantaged over time and can be borrowed against or withdrawn."],
    ["What is the Rule of 72?", "The Rule of 72 is a simple formula to estimate how long it takes for an investment to double. Divide 72 by the annual rate of return to get the approximate years required. For example, an 8% return would double your money in about 9 years (72÷8=9). It's a quick mental calculation to understand growth potential."],
    ["How do target-date retirement funds work?", "Target-date funds automatically adjust asset allocation based on your expected retirement year. They start more aggressive with higher stock allocations when retirement is distant, gradually becoming more conservative by increasing bond allocations as retirement approaches. They offer simple, professional management with automatic rebalancing in a single diversified fund."],
    ["What is a bond ladder?", "A bond ladder is a strategy of buying bonds with staggered maturity dates to manage interest rate risk and maintain liquidity. As each bond matures, you reinvest at current rates. This provides regular access to principal, captures higher rates when available, and reduces overall portfolio risk through diversification across different maturities."],
    ["What are alternative investments?", "Alternative investments are assets beyond traditional stocks, bonds, and cash, including real estate, private equity, hedge funds, commodities, cryptocurrency, collectibles, and structured products. They typically have lower correlation with traditional markets, potentially enhancing diversification but often with higher fees, less liquidity, and more complexity."],
    ["How does inflation affect my retirement savings?", "Inflation erodes purchasing power over time, meaning your retirement savings need to grow faster than inflation to maintain lifestyle. A 3% annual inflation rate would cut purchasing power in half in about 24 years. Investment strategies should target returns exceeding inflation, and retirement planning should account for increasing costs throughout retirement."]
]

# Create variations of questions - FIXED VERSION
def create_variations(qa_pair):
    question, answer = qa_pair
    variations = []
    
    # Different phrasings for each question type - with error checking
    if "difference between" in question.lower():
        try:
            topic = question.lower().split("difference between")[1].strip()
            variations.append([f"Can you explain how {topic} compare?", answer])
            variations.append([f"What makes {topic} different from each other?", answer])
        except IndexError:
            pass
        
    if "how" in question.lower():
        try:
            topic = question.lower().split("how")[1].strip()
            variations.append([f"What's the best way to {topic}", answer])
            variations.append([f"Could you tell me about {topic}", answer])
        except IndexError:
            pass
        
    if "what is" in question.lower():
        try:
            topic = question.lower().split("what is")[1].strip()
            variations.append([f"Can you explain {topic}?", answer])
            variations.append([f"Tell me about {topic}", answer])
        except IndexError:
            pass
    
    # Extract main topic regardless of question format
    main_topic = question.lower().replace("?", "")
    for prefix in ["what is ", "how do ", "how does ", "what's ", "what are "]:
        if main_topic.startswith(prefix):
            main_topic = main_topic[len(prefix):].strip()
            break
    
    # If it starts with "difference between", extract the key comparison
    if "difference between" in main_topic:
        try:
            main_topic = main_topic.split("difference between")[1].strip()
        except IndexError:
            pass
    
    # Add casual/verbal versions for all questions
    informal_prefixes = [
        "Hey, I was wondering about ",
        "I need some help understanding ",
        "So, ",
        "I've heard about ",
        "Quick question about ",
        "Could you explain ",
        "I'm confused about ",
        "Can you help me understand ",
        "I'm not sure about ",
        "I'd like to know more about "
    ]
    
    informal_suffixes = [
        ", can you explain that?",
        ", how does that work?",
        ", what's that all about?",
        ", can you tell me more?",
        "?",
        ", I'm trying to learn.",
        ", I'm really confused.",
        ", I need to understand this.",
        ", could you break it down for me?",
        ", what does that mean exactly?"
    ]
    
    # Create verbal variations
    for _ in range(2):  # Create 2 verbal variations per question
        prefix = random.choice(informal_prefixes)
        suffix = random.choice(informal_suffixes)
        verbal_q = f"{prefix}{main_topic}{suffix}"
        variations.append([verbal_q, answer])
    
    return variations

# Create dataset with variations and additional Q&A
all_qa = []

# Add original Q&A with variations
for qa_pair in original_qa:
    all_qa.append(qa_pair)  # Original question
    variations = create_variations(qa_pair)
    all_qa.extend(variations)  # Add variations

# Add additional domain-specific Q&A with variations
for qa_pair in additional_qa:
    all_qa.append(qa_pair)  # Original question
    variations = create_variations(qa_pair)
    all_qa.extend(variations)  # Add variations

# Create and save the dataset
df = pd.DataFrame(all_qa, columns=["question", "answer"])
df.to_csv("augmented_wealth_management_qa.csv", index=False)

print(f"Created dataset with {len(df)} question-answer pairs")

# Display sample of the dataset
print("\nSample of augmented dataset:")
print(df.sample(10)[["question"]].to_string(index=False))

# Generate dataset statistics
original_count = len(original_qa)
additional_count = len(additional_qa)
variations_count = len(df) - original_count - additional_count

print(f"\nDataset Statistics:")
print(f"Original Questions: {original_count}")
print(f"Additional Domain Questions: {additional_count}")
print(f"Question Variations: {variations_count}")
print(f"Total Dataset Size: {len(df)}")
