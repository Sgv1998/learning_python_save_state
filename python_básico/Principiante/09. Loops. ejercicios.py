

##"Iterate 0 to 10 using for loop, do the same using while loop."

for number_up in range(10):
    print(number_up)        #No hace falta el break , esta leyendo los elementos de una lista
print("reached the limit, 10")    


 
# Iterate 10 to 0 using for loop, do the same using while loop.
for number_down in range(10, -1, -1):
    print(number_down)    
print("reached the limit, 0")    

number_while_down=10
while number_while_down >0:
    print(number_while_down)
    number_while_down=number_while_down-1
print("reached the limit, 0, thanks to the code while")    

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
number_while_down=1
while number_while_down <=7:
    print("#"*number_while_down)
    number_while_down+=1
print("tadaa a triangle")   

number_while_down=0
while number_while_down <=10:
    print(f"{number_while_down} x {number_while_down} = ", number_while_down**2)
    number_while_down+=1
print("tadaa")   

# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
number_while_down=0
total=0
while number_while_down <=100:
    number_while_down+=1
    total=total+number_while_down
    if number_while_down==100: print(total)
print("tadaa")  




# Use for loop to iterate from 0 to 100 and print only odd numbers
for number_down in range(100): 
    if number_down%2!=0 and(number_down<5 or number_down>95):
        print(number_down)
print("tadaa, even numbers by for loop, with a little cut")  


   # Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.

   # This is a fruit list, ['banana', 'orange', 'mango', 'lemon'] reverse the order using loop.
list=['banana', 'orange', 'mango', 'lemon']
for fruits in list[-1::-1]:
    print(fruits)
print("tadaa, fruits inversed")

file_countries=[
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]
suma_lands=0
for countries in file_countries:
    if "land" in countries:
        suma_lands +=1
        print(countries)
print("Nºpaises contienen la palabra \"lands\", es ", suma_lands)
print("tadaa")
  
 
    #Go to the data folder and use the countries_data.py file.
       # What are the total number of languages in the data
       # Find the ten most spoken languages from the data
       # Find the 10 most populated countries in the world
