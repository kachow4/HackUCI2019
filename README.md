# HackUCI2019
 Built for HackUCI 2019
 Let's Pack will create a customized packing list based upon your destination, the weather there, and length of stay!

## Inspiration
I love traveling, so I wanted to build something that would help travelers. Let's Pack helps with the one of the most mundane tasks associated with vacation: packing.

## What it does
The program takes in user input destination of trip and length of stay, and formulates a customized packing list, based upon the weather at the destination. 

## How we built it
We started by researching weather APIs, and ended up deciding to use the openweathermaps API. Then we had to figure out how to get and use the data from the API, based upon the user input. The frontend took in and posted the users responses, which we used in the backend to make a request to the API for information. After that, we had to figure out how to get data from a JSON file so that we could search by CityID instead of an ambiguous city name. Then we coded the program that determines how many sets of each type of clothes to pack and formatted it for sending to an HTML template. One of the last things we did was figure out how to use the data from main in the HTML template. Finally, we had our customized packing list. 

## Challenges we ran into
Everything was new for us. Neither of us had worked with front-end before, so we had to figure out a framework to use, we had to learn html and css on the go, and we had to figure out how to link everything together. We didn't know how to use info from a .gz file; I had to download a special unzipping software. Even after we could access the info, I couldn't see what was in the file, because every time I tried to open in it in my text editor, it would crash. When I finally printed the contents of the file, some special unicode characters would make it crash, so I had to error-handle that. I was trying to figure out how to deploy with AppEngine, but one of the necessary imports wouldn't cooperate. The experience was very much a learning process for us!

## Accomplishments that we're proud of
-Using the OpenWeatherMaps API
-Learning HTML and CSS on the go and using that in our project
-Building a functional UI
-Having completed (almost) a project!

## What we learned
We learned so much -- new coding languages, how to deal with merge conflicts, how to use Flask, how to get and use user input, how to use GitHub to share code, how to build a UI -- many things that applicable to real world jobs!

## What's next for Let's Pack!
We want to figure out how to let locals, people from the destination you're traveling to, share input about what they suggest bringing and photos of outfits that people actually wear at that destination. We also want to add a customizing option for reason of travel, and curate a list based on that reason (business trip, fun, wedding, etc.). Another idea is to use the Yelp API to suggest activities/places to eat in the destination. In the future, maybe we could even suggest items to buy for the trip and include a third-party shopping aspect. Also we want to figure out how to deploy the project!
