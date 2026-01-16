from countryinfo import CountryInfo

# user input for Country Name
count = input("Enter Country Name:")
country = CountryInfo(count)

print("Capital:", country.capital())
print("Currencies:", country.currencies())
print("Languages:", country.languages())
print("Borders:", country.borders())
print("Timezones:", country.timezones())