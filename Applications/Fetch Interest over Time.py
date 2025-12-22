from pytrends.request import TrendReq

pytrends = TrendReq()
keywords = ["Python", "Java", "C++"]
pytrends.build_payload(keywords, timeframe= "today 12-m")
data = pytrends.interest_over_time()

print(data)