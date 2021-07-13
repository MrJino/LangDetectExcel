import pandas as pd
from textblob import TextBlob

xlsx = pd.read_excel('./sample/sample.xls')

print(TextBlob(xlsx['English_Canada'][0]).detect_language())
print(TextBlob(xlsx['Arabic'][0]).detect_language())
print(TextBlob(xlsx['Assamese'][0]).detect_language())
print(TextBlob(xlsx['Belarusian'][0]).detect_language())
print(TextBlob(xlsx['Farsi'][0]).detect_language())
print(TextBlob(xlsx['French'][0]).detect_language())
print(TextBlob(xlsx['Hindi'][0]).detect_language())

# xlsx.to_excel('./sample/sample_copy.xlsx', index=False)