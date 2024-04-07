# Langgraph To Welcome My Friends In Style.
My friends are visiting from Europe to India. Since we all studied together in the same university and took the same courses, I would say we're a bit techy. While being a good host is one way to welcome them, I also want to introduce them to all that India has to offer. Additionally, I'm keen on experimenting with the power of AI and showcasing how it can be used for human development. 
I believe this example will demonstrate how AI can be utilized for good. Hence, I plan to create a state-machine that encapsulates the essence of the entire trip for my friends. Although there's room for improvement, I believe the start isn't too shabby either.

## State Machine
![State Machine of Travel](https://github.com/Anurich/Welcome_my_friend_to_india_with_langgraph/blob/main/Screenshot%202024-04-07%20at%207.38.39%E2%80%AFPM.png)

## Agent State
```
  # agent state 
class AgentState(TypedDict):
    messages: List[str]
    history: List[str]
    last_visited_city: List[str]
    created_message: str
    print: bool = True

```
## Agent output
```
{
      "inputs": [
            "I am in love city i wanna enjoy the food "
      ],
      "response": "['Mercato Centrale Roma. Mercato Centrale is a real blockbuster: 18 artisanal food stands line the perimeter of the Cappa Mazzoniana, in Termini Train Station, a monumental hall with 100-foot ... A short walk from the Spanish Steps and Trevi Fountain, the restaurant treats diners to bubbling cauldrons of broth (served as garlic and chile-laden as you\\'d like) for cooking vegetables ... Top 10 Places To Eat in or Near Piazza Navona. Piazza Navona is one of Rome\\'s most iconic piazzas. It\\'s wise to avoid being ripped off in a tourist trap, but you can expect to pay a little more here. There are some decent restaurants in and near Piazza Navona and there are also some amazing ones! Check out Bernini and Terrazza Borromini ... Taverna Trilussa is the place to go for an Italian meal just like your grandparents, great grandparents, and generations before them made. According to Amorico, this is where you\\'ll find the \"best ... La Pergola is considered to be an institution of Italian dining. This 3-star Michelin restaurant has continuously earned its crown year after year. Let\\'s put it this way, there are just 142 Michelin restaurants with 3 stars in the world. Nine of those are in Italy, and La Pergola is the only one in Rome.']",
      "history": [
            "",
            "Mercato Centrale Roma. Mercato Centrale is a real blockbuster: 18 artisanal food stands line the perimeter of the Cappa Mazzoniana, in Termini Train Station, a monumental hall with 100-foot ... A short walk from the Spanish Steps and Trevi Fountain, the restaurant treats diners to bubbling cauldrons of broth (served as garlic and chile-laden as you'd like) for cooking vegetables ... Top 10 Places To Eat in or Near Piazza Navona. Piazza Navona is one of Rome's most iconic piazzas. It's wise to avoid being ripped off in a tourist trap, but you can expect to pay a little more here. There are some decent restaurants in and near Piazza Navona and there are also some amazing ones! Check out Bernini and Terrazza Borromini ... Taverna Trilussa is the place to go for an Italian meal just like your grandparents, great grandparents, and generations before them made. According to Amorico, this is where you'll find the \"best ... La Pergola is considered to be an institution of Italian dining. This 3-star Michelin restaurant has continuously earned its crown year after year. Let's put it this way, there are just 142 Michelin restaurants with 3 stars in the world. Nine of those are in Italy, and La Pergola is the only one in Rome."
      ],
      "visiting_city": [
            "Rome"
      ]
}{
      "inputs": [
            "I am in love city i wanna enjoy the food ",
            "Tell me touristic place to visit in Rome",
            "I want to explore the city"
      ],
      "response": "[\"Naples Tickets & Tours. 9. Take a Train Ride to Lake Bracciano. Lake Bracciano is a volcanic lake located near Rome, Italy. It is one of the largest lakes in Italy and is known for its pristine waters and scenic surroundings. Moreover, Lake Bracciano is a popular destination for boating, swimming, and hiking. 4. Veio Park. Horses at Veio Park. If you want to spend a day immersed in beautiful nature near Rome, but not far from the city, then consider visiting the Veio Regional Park. The park features about 15000 hectares of woods and pastures and has a great wealth of plant and animal biodiversity. 17 - Capalbio. A beautiful gorgeous village in Southern Maremma that is an easy day trip from Rome. This charming city is best to visit in the summer season for its sandy beaches, its top places to visit is the Fortress of Aldobrandeschi and the Church of San Nicola. Capalbio is rich in history, natural vistas and long sandy beaches. Tivoli. Tivoli is the perfect town near Rome to escape for the day. This small, historic town is a hidden gem nestled by the Sabine Hills just 30 kilometers (19 miles) from Rome. It's perfect for a quick day trip! Quickly access the town with about an hour-long bus or train ride from Rome for less than \u20ac5 each way. Take a direct bus to Sulmona from Rome-Tiburtina Station and then another bus to Villetta Barrea. 25. Cervara di Roma. Cervara di Roma is a small village located about an hour's drive from Rome. This charming little village is at the top of the list of the highest towns in the province of Rome and the Lazio region.\"]",
      "history": [
            "",
            "Mercato Centrale Roma. Mercato Centrale is a real blockbuster: 18 artisanal food stands line the perimeter of the Cappa Mazzoniana, in Termini Train Station, a monumental hall with 100-foot ... A short walk from the Spanish Steps and Trevi Fountain, the restaurant treats diners to bubbling cauldrons of broth (served as garlic and chile-laden as you'd like) for cooking vegetables ... Top 10 Places To Eat in or Near Piazza Navona. Piazza Navona is one of Rome's most iconic piazzas. It's wise to avoid being ripped off in a tourist trap, but you can expect to pay a little more here. There are some decent restaurants in and near Piazza Navona and there are also some amazing ones! Check out Bernini and Terrazza Borromini ... Taverna Trilussa is the place to go for an Italian meal just like your grandparents, great grandparents, and generations before them made. According to Amorico, this is where you'll find the \"best ... La Pergola is considered to be an institution of Italian dining. This 3-star Michelin restaurant has continuously earned its crown year after year. Let's put it this way, there are just 142 Michelin restaurants with 3 stars in the world. Nine of those are in Italy, and La Pergola is the only one in Rome.",
            "Sure! Here are some popular tourist attractions to visit in Rome:\n\n1. Colosseum: An iconic symbol of Rome, the Colosseum is an ancient amphitheater where gladiators once fought.\n\n2. Vatican City: Visit St. Peter's Basilica, the Sistine Chapel, and the Vatican Museums in this independent city-state within Rome.\n\n3. Trevi Fountain: Make a wish and toss a coin into the Trevi Fountain, one of the most famous fountains in the world.\n\n4. Pantheon: Explore this well-preserved ancient Roman temple, known for its impressive dome and oculus.\n\n5. Roman Forum: Walk through the ruins of the Roman Forum, once the center of ancient Rome's political and social life.\n\n6. Spanish Steps: Climb the Spanish Steps for a great view of the city and visit the nearby Piazza di Spagna.\n\n7. Piazza Navona: Enjoy the lively atmosphere of this beautiful square, known for its fountains, street performers, and outdoor cafes.\n\nThese are just a few of the many amazing attractions Rome has to offer!",
            "",
            "Naples Tickets & Tours. 9. Take a Train Ride to Lake Bracciano. Lake Bracciano is a volcanic lake located near Rome, Italy. It is one of the largest lakes in Italy and is known for its pristine waters and scenic surroundings. Moreover, Lake Bracciano is a popular destination for boating, swimming, and hiking. 4. Veio Park. Horses at Veio Park. If you want to spend a day immersed in beautiful nature near Rome, but not far from the city, then consider visiting the Veio Regional Park. The park features about 15000 hectares of woods and pastures and has a great wealth of plant and animal biodiversity. 17 - Capalbio. A beautiful gorgeous village in Southern Maremma that is an easy day trip from Rome. This charming city is best to visit in the summer season for its sandy beaches, its top places to visit is the Fortress of Aldobrandeschi and the Church of San Nicola. Capalbio is rich in history, natural vistas and long sandy beaches. Tivoli. Tivoli is the perfect town near Rome to escape for the day. This small, historic town is a hidden gem nestled by the Sabine Hills just 30 kilometers (19 miles) from Rome. It's perfect for a quick day trip! Quickly access the town with about an hour-long bus or train ride from Rome for less than \u20ac5 each way. Take a direct bus to Sulmona from Rome-Tiburtina Station and then another bus to Villetta Barrea. 25. Cervara di Roma. Cervara di Roma is a small village located about an hour's drive from Rome. This charming little village is at the top of the list of the highest towns in the province of Rome and the Lazio region."
      ],
      "visiting_city": [
            "Rome"
      ]
}{
      "inputs": [
            "I am in love city i wanna enjoy the food ",
            "Tell me touristic place to visit in Rome",
            "I want to explore the city",
            "I want to leave this city"
      ],
      "response": "['Welcome to Portugal']",
      "history": [
            "",
            "Mercato Centrale Roma. Mercato Centrale is a real blockbuster: 18 artisanal food stands line the perimeter of the Cappa Mazzoniana, in Termini Train Station, a monumental hall with 100-foot ... A short walk from the Spanish Steps and Trevi Fountain, the restaurant treats diners to bubbling cauldrons of broth (served as garlic and chile-laden as you'd like) for cooking vegetables ... Top 10 Places To Eat in or Near Piazza Navona. Piazza Navona is one of Rome's most iconic piazzas. It's wise to avoid being ripped off in a tourist trap, but you can expect to pay a little more here. There are some decent restaurants in and near Piazza Navona and there are also some amazing ones! Check out Bernini and Terrazza Borromini ... Taverna Trilussa is the place to go for an Italian meal just like your grandparents, great grandparents, and generations before them made. According to Amorico, this is where you'll find the \"best ... La Pergola is considered to be an institution of Italian dining. This 3-star Michelin restaurant has continuously earned its crown year after year. Let's put it this way, there are just 142 Michelin restaurants with 3 stars in the world. Nine of those are in Italy, and La Pergola is the only one in Rome.",
            "Sure! Here are some popular tourist attractions to visit in Rome:\n\n1. Colosseum: An iconic symbol of Rome, the Colosseum is an ancient amphitheater where gladiators once fought.\n\n2. Vatican City: Visit St. Peter's Basilica, the Sistine Chapel, and the Vatican Museums in this independent city-state within Rome.\n\n3. Trevi Fountain: Make a wish and toss a coin into the Trevi Fountain, one of the most famous fountains in the world.\n\n4. Pantheon: Explore this well-preserved ancient Roman temple, known for its impressive dome and oculus.\n\n5. Roman Forum: Walk through the ruins of the Roman Forum, once the center of ancient Rome's political and social life.\n\n6. Spanish Steps: Climb the Spanish Steps for a great view of the city and visit the nearby Piazza di Spagna.\n\n7. Piazza Navona: Enjoy the lively atmosphere of this beautiful square, known for its fountains, street performers, and outdoor cafes.\n\nThese are just a few of the many amazing attractions Rome has to offer!",
            "",
            "Naples Tickets & Tours. 9. Take a Train Ride to Lake Bracciano. Lake Bracciano is a volcanic lake located near Rome, Italy. It is one of the largest lakes in Italy and is known for its pristine waters and scenic surroundings. Moreover, Lake Bracciano is a popular destination for boating, swimming, and hiking. 4. Veio Park. Horses at Veio Park. If you want to spend a day immersed in beautiful nature near Rome, but not far from the city, then consider visiting the Veio Regional Park. The park features about 15000 hectares of woods and pastures and has a great wealth of plant and animal biodiversity. 17 - Capalbio. A beautiful gorgeous village in Southern Maremma that is an easy day trip from Rome. This charming city is best to visit in the summer season for its sandy beaches, its top places to visit is the Fortress of Aldobrandeschi and the Church of San Nicola. Capalbio is rich in history, natural vistas and long sandy beaches. Tivoli. Tivoli is the perfect town near Rome to escape for the day. This small, historic town is a hidden gem nestled by the Sabine Hills just 30 kilometers (19 miles) from Rome. It's perfect for a quick day trip! Quickly access the town with about an hour-long bus or train ride from Rome for less than \u20ac5 each way. Take a direct bus to Sulmona from Rome-Tiburtina Station and then another bus to Villetta Barrea. 25. Cervara di Roma. Cervara di Roma is a small village located about an hour's drive from Rome. This charming little village is at the top of the list of the highest towns in the province of Rome and the Lazio region.",
            "",
            "Welcome to Portugal"
      ],
      "visiting_city": [
            "Rome",
            "Portugal"
      ]
}{
      "inputs": [
            "I am in love city i wanna enjoy the food ",
            "Tell me touristic place to visit in Rome",
            "I want to explore the city",
            "I want to leave this city",
            "Tell me best food to eat "
      ],
      "response": "[\"Chef Miguel Azevedo Peres and his team follow a nose-to-tail philosophy when working with the hog, incorporating pig into pork fat-infused butter, a pork-filled take on the classic bifana sandwich ... There's no denying that some of the best restaurants in Lisbon are the most talked-about in Europe right now. Before the pandemic hit in 2020, the city was on a roll with new openings\u2014Prado ... 13. A Taberna da Rua das Flores. Best Lisbon restaurant for: traditional Portuguese dishes. Often considered to be one of the best Portuguese restaurants in Lisbon, A Taberna da Rua das Flores is a must-try. The atmosphere is friendly, relaxed and local while the menu is a twist on traditional; order the tuna tataki, sardines on toast and fried ... Sem Palavras. The Mercado de Alvalade is one of the best food markets in Lisbon, and up on one end there's a small, busy restaurant called Sem Palavras. It's a traditional beer house, with fast and efficient service, paper placements, and tables that are practically on top of each other. More Seafood Restaurants In Lisbon. A Cevicheria, Cervejaria Liberdade, Cervejaria Pin\u00f3quio, Marisqueira Nunes and Sea Me. 2. Belcanto - Lisbon's Most Lauded Michelin Starred Restaurant. Not only is Belcanto one of the best restaurants in Lisbon, it's also one of the best restaurants in the world.\"]",
      "history": [
            "",
            "Mercato Centrale Roma. Mercato Centrale is a real blockbuster: 18 artisanal food stands line the perimeter of the Cappa Mazzoniana, in Termini Train Station, a monumental hall with 100-foot ... A short walk from the Spanish Steps and Trevi Fountain, the restaurant treats diners to bubbling cauldrons of broth (served as garlic and chile-laden as you'd like) for cooking vegetables ... Top 10 Places To Eat in or Near Piazza Navona. Piazza Navona is one of Rome's most iconic piazzas. It's wise to avoid being ripped off in a tourist trap, but you can expect to pay a little more here. There are some decent restaurants in and near Piazza Navona and there are also some amazing ones! Check out Bernini and Terrazza Borromini ... Taverna Trilussa is the place to go for an Italian meal just like your grandparents, great grandparents, and generations before them made. According to Amorico, this is where you'll find the \"best ... La Pergola is considered to be an institution of Italian dining. This 3-star Michelin restaurant has continuously earned its crown year after year. Let's put it this way, there are just 142 Michelin restaurants with 3 stars in the world. Nine of those are in Italy, and La Pergola is the only one in Rome.",
            "Sure! Here are some popular tourist attractions to visit in Rome:\n\n1. Colosseum: An iconic symbol of Rome, the Colosseum is an ancient amphitheater where gladiators once fought.\n\n2. Vatican City: Visit St. Peter's Basilica, the Sistine Chapel, and the Vatican Museums in this independent city-state within Rome.\n\n3. Trevi Fountain: Make a wish and toss a coin into the Trevi Fountain, one of the most famous fountains in the world.\n\n4. Pantheon: Explore this well-preserved ancient Roman temple, known for its impressive dome and oculus.\n\n5. Roman Forum: Walk through the ruins of the Roman Forum, once the center of ancient Rome's political and social life.\n\n6. Spanish Steps: Climb the Spanish Steps for a great view of the city and visit the nearby Piazza di Spagna.\n\n7. Piazza Navona: Enjoy the lively atmosphere of this beautiful square, known for its fountains, street performers, and outdoor cafes.\n\nThese are just a few of the many amazing attractions Rome has to offer!",
            "",
            "Naples Tickets & Tours. 9. Take a Train Ride to Lake Bracciano. Lake Bracciano is a volcanic lake located near Rome, Italy. It is one of the largest lakes in Italy and is known for its pristine waters and scenic surroundings. Moreover, Lake Bracciano is a popular destination for boating, swimming, and hiking. 4. Veio Park. Horses at Veio Park. If you want to spend a day immersed in beautiful nature near Rome, but not far from the city, then consider visiting the Veio Regional Park. The park features about 15000 hectares of woods and pastures and has a great wealth of plant and animal biodiversity. 17 - Capalbio. A beautiful gorgeous village in Southern Maremma that is an easy day trip from Rome. This charming city is best to visit in the summer season for its sandy beaches, its top places to visit is the Fortress of Aldobrandeschi and the Church of San Nicola. Capalbio is rich in history, natural vistas and long sandy beaches. Tivoli. Tivoli is the perfect town near Rome to escape for the day. This small, historic town is a hidden gem nestled by the Sabine Hills just 30 kilometers (19 miles) from Rome. It's perfect for a quick day trip! Quickly access the town with about an hour-long bus or train ride from Rome for less than \u20ac5 each way. Take a direct bus to Sulmona from Rome-Tiburtina Station and then another bus to Villetta Barrea. 25. Cervara di Roma. Cervara di Roma is a small village located about an hour's drive from Rome. This charming little village is at the top of the list of the highest towns in the province of Rome and the Lazio region.",
            "",
            "Welcome to Portugal",
            "",
            "Chef Miguel Azevedo Peres and his team follow a nose-to-tail philosophy when working with the hog, incorporating pig into pork fat-infused butter, a pork-filled take on the classic bifana sandwich ... There's no denying that some of the best restaurants in Lisbon are the most talked-about in Europe right now. Before the pandemic hit in 2020, the city was on a roll with new openings\u2014Prado ... 13. A Taberna da Rua das Flores. Best Lisbon restaurant for: traditional Portuguese dishes. Often considered to be one of the best Portuguese restaurants in Lisbon, A Taberna da Rua das Flores is a must-try. The atmosphere is friendly, relaxed and local while the menu is a twist on traditional; order the tuna tataki, sardines on toast and fried ... Sem Palavras. The Mercado de Alvalade is one of the best food markets in Lisbon, and up on one end there's a small, busy restaurant called Sem Palavras. It's a traditional beer house, with fast and efficient service, paper placements, and tables that are practically on top of each other. More Seafood Restaurants In Lisbon. A Cevicheria, Cervejaria Liberdade, Cervejaria Pin\u00f3quio, Marisqueira Nunes and Sea Me. 2. Belcanto - Lisbon's Most Lauded Michelin Starred Restaurant. Not only is Belcanto one of the best restaurants in Lisbon, it's also one of the best restaurants in the world."
      ],
      "visiting_city": [
            "Rome",
            "Portugal"
      ]
}

```
