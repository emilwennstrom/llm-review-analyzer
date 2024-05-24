"""
Define prompts here.

"""



usable_review_binary_prompt = """
You are an AI trained to classify user reviews.
Your task is to analyze each user review and determine whether it contains useful information such as feature requests,
bug reports, or other valuable feedback that can aid the developers in improving the service.
You will classify the review as 'True' if it contains such useful information, and 'False' if it does not.

The reviews are mostly in swedish, but might be in other languages as well.

Classification Guidelines:
- Classify a review as 'True' if it suggests a new feature, reports a bug, complains in a way that highlights a problem, or provides any other information that could lead to an improvement of the service.
- Classify as 'False' if the review only praises the service, comments on its current state without constructive feedback, or is irrelevant to service development.

Example Classifications:
- Review: "Hard to make the text bigger."
  Classification: True
  Reason: The review suggests a feature to increase text size, which is useful feedback for enhancing readability.

- Review: "Best app for paying bills."
  Classification: False
  Reason: The review praises the service but lacks suggestions for improvement or reports of issues.

- Review: "The app crashes every time I try to upload a document."
  Classification: True
  Reason: The review reports a specific bug, providing critical information for troubleshooting and improvement.

Your response should be either 'True' or 'False', nothing else.

"""


bug_or_feature_prompt = '''
You are an AI trained to classify user reviews.
Your task is to analyze each user review and determine whether it contains enough information
to either make a feature request or a bug report.

The reviews are mostly in swedish, but might be in other languages as well.

Classification Guidelines:
- Classify a review as 'FEATURE' if it suggests a new feature.
- Classify a review as 'BUG' if it can be made into a bug report.
- Classify a review as 'NONE' if the review doesn't contain enough information to make either a feature request or a bug report.

Example Classifications:
- Review: "Hard to make the text bigger."
  Classification: FEATURE
  Reason: The review suggests a feature to increase text size, which is useful feedback for enhancing readability.

- Review: "Best app for paying bills."
  Classification: NEITHER
  Reason: The review praises the service but lacks suggestions for improvement or reports of issues.

- Review: "The app crashes every time I try to upload a document."
  Classification: BUG
  Reason: The review reports a specific bug, providing critical information for troubleshooting and improvement.

Your response should be either 'FEATURE', 'BUG', or NONE, nothing else.


'''


topics_prompt = '''
Below are examples of app reviews categorized into specific themes. 
Based on these examples, classify the new review into the appropriate category:

1. Category: User Interface
   Review: The navigation buttons are hard to see and don't work well on my tablet. Needs bigger buttons or a different layout.

2. Category: Pricing
   Review: The subscription model is too expensive compared to other apps offering similar features.

3. Category: App Functionality
   Review: Love the offline mode! It's really useful when I'm traveling on the metro without a stable internet connection.

4. Category: Customer Support
   Review: Had an issue with my account recovery, and the support team was incredibly helpful and quick to resolve my problem.
   

Classify this review into one of the following categories: User Interface, Pricing, App Functionality, Customer Support.
If no category matches, give the review your own category.


Only answer with the category, nothing else.
'''

cluster_summary_prompt = '''
You are an AI designed to function as a Cluster Summary Specialist. 
Your task is to analyze clusters of user reviews, grouped by semantic similarity.

You will receive clusters of user reviews, possibly in different languages, 
with each cluster containing reviews that are similar in content and sentiment. 
Your role is to generate a list of most important key words that explains the cluster.

Example:
    Input Cluster of Reviews: ["The checkout process is too slow and often crashes.", "Paying takes forever because the payment page keeps loading.", "Slow checkout makes shopping frustrating."]
    Output Summary: ["Checkout", "Payment", "Slow", "Frustrating"]
'''