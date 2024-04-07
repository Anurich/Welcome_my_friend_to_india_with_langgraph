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
      "response": "['you have been traveling for long please take some rest']",
      "history": [
            "",
            "you have been traveling for long please take some rest"
      ],
      "visiting_city": [
            "new_delhi"
      ]
}{
      "response": "[\"Read about 7 Best Dining Places In Khan Market, Delhi NCR To Unwind The Monsoon Evenings at eazydiner.com. Relax and recharge your soul with the best of Delhi's foodie district & other interesting reads about restaurants and cuisines at eazydiner.com. Share latest food trends with other food lovers. Khan Market's Top 10 Dining Destinations 1. Big Chill. Big Chill, the renowned establishment in Khan Market, beckons all Italian cuisine enthusiasts, or anyone with a hankering for comforting carb-loaded delights. This restaurant has carved a niche for itself with its reputation for generous portions and inviting ambiance. In actuality, the top Indian restaurants normally don't just serve your good food; they set up an exciting experience that puts you in the center of India. 2. Satisfy Your Cravings: Discover the Highly Rated Indian Takeaway Restaurants Near You: The rasping of stewing spices, the vivacious dance in the mouth of flavors - Indian cuisine ... This listicle highlights the top 10 restaurants serving lip-smacking North Indian food in Khan Market. Whether you're craving kebabs, curries or naan bread, these restaurants will satisfy all your North Indian food cravings. So get ready to dig into the best North Indian restaurants in Khan Market has to offer! 1. Town Hall. Established in ... Best Restaurants in Khan Market, Central Delhi: Restaurants serving in Khan Market, Central Delhi. Book a table & enjoy the best deals on restaurants. check &#10004 Deals &#10004 Menus &#10004 Price &#10004 Reviews.\"]",
      "history": [
            "",
            "you have been traveling for long please take some rest",
            "",
            "Read about 7 Best Dining Places In Khan Market, Delhi NCR To Unwind The Monsoon Evenings at eazydiner.com. Relax and recharge your soul with the best of Delhi's foodie district & other interesting reads about restaurants and cuisines at eazydiner.com. Share latest food trends with other food lovers. Khan Market's Top 10 Dining Destinations 1. Big Chill. Big Chill, the renowned establishment in Khan Market, beckons all Italian cuisine enthusiasts, or anyone with a hankering for comforting carb-loaded delights. This restaurant has carved a niche for itself with its reputation for generous portions and inviting ambiance. In actuality, the top Indian restaurants normally don't just serve your good food; they set up an exciting experience that puts you in the center of India. 2. Satisfy Your Cravings: Discover the Highly Rated Indian Takeaway Restaurants Near You: The rasping of stewing spices, the vivacious dance in the mouth of flavors - Indian cuisine ... This listicle highlights the top 10 restaurants serving lip-smacking North Indian food in Khan Market. Whether you're craving kebabs, curries or naan bread, these restaurants will satisfy all your North Indian food cravings. So get ready to dig into the best North Indian restaurants in Khan Market has to offer! 1. Town Hall. Established in ... Best Restaurants in Khan Market, Central Delhi: Restaurants serving in Khan Market, Central Delhi. Book a table & enjoy the best deals on restaurants. check &#10004 Deals &#10004 Menus &#10004 Price &#10004 Reviews."
      ],
      "visiting_city": [
            "new_delhi"
      ]
}{
      "response": "['Welcome to Rishikesh']",
      "history": [
            "",
            "you have been traveling for long please take some rest",
            "",
            "Read about 7 Best Dining Places In Khan Market, Delhi NCR To Unwind The Monsoon Evenings at eazydiner.com. Relax and recharge your soul with the best of Delhi's foodie district & other interesting reads about restaurants and cuisines at eazydiner.com. Share latest food trends with other food lovers. Khan Market's Top 10 Dining Destinations 1. Big Chill. Big Chill, the renowned establishment in Khan Market, beckons all Italian cuisine enthusiasts, or anyone with a hankering for comforting carb-loaded delights. This restaurant has carved a niche for itself with its reputation for generous portions and inviting ambiance. In actuality, the top Indian restaurants normally don't just serve your good food; they set up an exciting experience that puts you in the center of India. 2. Satisfy Your Cravings: Discover the Highly Rated Indian Takeaway Restaurants Near You: The rasping of stewing spices, the vivacious dance in the mouth of flavors - Indian cuisine ... This listicle highlights the top 10 restaurants serving lip-smacking North Indian food in Khan Market. Whether you're craving kebabs, curries or naan bread, these restaurants will satisfy all your North Indian food cravings. So get ready to dig into the best North Indian restaurants in Khan Market has to offer! 1. Town Hall. Established in ... Best Restaurants in Khan Market, Central Delhi: Restaurants serving in Khan Market, Central Delhi. Book a table & enjoy the best deals on restaurants. check &#10004 Deals &#10004 Menus &#10004 Price &#10004 Reviews.",
            "",
            "Welcome to Rishikesh"
      ],
      "visiting_city": [
            "new_delhi",
            "Rishikesh"
      ]
}

```
