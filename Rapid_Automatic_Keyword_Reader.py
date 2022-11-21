from rake_ntlk import Rake
rake_ntlk_var = Rake()

text = """ I am a programmer from India, and I am here to guide you 
with Data Science, Machine Learning, Python, and C++ for free. 
I hope you will learn a lot in your journey towards Coding, 
Machine Learning and Artificial Intelligence with me."""

rake_ntlk_var.extract_keywords_from_text(text)
keyword_extracted = rake_ntlk_var.get_ranked_phrases()
print(keyword_extracted)