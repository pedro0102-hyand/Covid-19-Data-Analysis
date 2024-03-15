url = "https://covid-193.p.rapidapi.com/statistics"
headers = {
 'x-rapidapi-host': "covid-193.p.rapidapi.com",
 'x-rapidapi-key': "a499da44a9mshaf133d89799c5dfp108066jsnb1100424366a" }


response=requests.request("GET",url,headers=headers)
print(response.text)