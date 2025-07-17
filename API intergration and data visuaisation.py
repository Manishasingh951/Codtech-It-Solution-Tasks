import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://disease.sh/v3/covid-19/countries"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
else:
    print("API Error:", response.status_code)
    exit()
df = pd.DataFrame(data)
df = df[['country', 'cases', 'deaths', 'recovered', 'active', 'population']]
top10 = df.sort_values('cases', ascending=False).head(10)
plt.figure(figsize=(12, 6))
sns.barplot(x='cases', y='country', data=top10, palette='coolwarm')
plt.title("Top 10 Countries by COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()
