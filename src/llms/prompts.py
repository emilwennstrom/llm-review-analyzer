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


topics_prompt = '''
Below are examples of app reviews categorized into specific themes. 
Based on these examples, classify the new review into the appropriate category:

1. Category: User Interface
   Review: The navigation buttons are hard to see and donät work well on my tablet. Needs bigger buttons or a different layout.

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