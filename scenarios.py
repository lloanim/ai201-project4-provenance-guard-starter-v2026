"""
What your test runs. ← UNIT 8, MILESTONE 3

Each of your five criteria needs something run against it. A criterion about
false positives needs your own writing. One about label coverage needs inputs
across the score range. One about the appeal path needs a real content_id.

Working that out is Milestone 3's first step, and this file is where you write
it down. `run_eval.py` runs everything here three times.

Two are filled in as examples. Replace them with what your criteria actually
need — these are a shape, not a set.

A scenario carries **either** of these:

    "texts"   a list of strings. Each is sent as {"text": ..., "creator_id": ...}
              with a creator_id made up for you. Use this for most criteria.

    "bodies"  a list of whole request bodies, sent exactly as written. Use this
              when the malformed request IS the point — empty text, no `text`
              field at all, something enormous. A bad-input criterion needs it,
              because you cannot express "the field is missing" as a string.
"""

SCENARIOS = [
    {
        "name": "my own writing",
        "criterion": 1,
        "texts": [
            "Last year 2019 in Washington state 35 people contracted measles and most of them were children. There is considerable debate between people who believe all children should be required to be vaccinated and those who believe not all children should be required to be vaccinated. Although one may argue that children should not be required to be vaccinated, however, the truth of the matter is children should be required to be vaccinated because vaccines can eliminate common diseases, help children with other illnesses, and prevent outbreaks of diseases.  For these reasons, all children should be required to be vaccinated.",
            "Overall, despite the fact that some believe that not all children should be required to be vaccinated because of their religion and their fear of risk, the fact of the matter is all children should be required to be vaccinated because vaccines can eliminate common diseases, help children with other illnesses, and prevent outbreaks of diseases. As stated previously stated, vaccines eliminate common disease because with many people vaccinated it causes the disease to die out. Additionally, vaccines help children with other illnesses because some children are not able to fight both diseases and need herd immunity in order to not get the disease. Furthermore, vaccines can prevent outbreaks because it can eliminate the disease and can not come back, unless people stop taking the vaccines. The counterclaim that not all children should be required to be vaccinated is less convincing because vaccines reduce the number of deaths from diseases.",
            "Before the printing press, it would take a long time to produce one book especially the bible. But after the invention of the printing press, it changed the lives of people. The impact of innovation is seen because the printing press is the method to addressing the problem of not being able to spread ideas quickly. With the printing press, more people were able to spread ideas and more learned how to read.",
            "In document five, shows Martin Luther nailing his 95 theses to the doors of a church. He does this because he found that the church was corrupted. In the 95 theses, he says why the church is corrupted. Indulgence was one of the reasons he saw corruption in the church. The church took the money of people in order to take away their sins which was not true.",
            "Martin Luther uses the method of the printing press to try to solve the problem of letting people know about the churchs corruption. The printing press helped Martin Luther to spread his idea that the church is corrupted. People seeing the truth about the church changed the way they believed. Most of peoples lives changed from religion to science.",
            "In conclusion, the enduring issue impact of innovation impacted the lives of many people throughout history. It was a significant impact because it was able to change peoples lives. This enduring issue still continues to impact today. Today we have more advanced technology and the internet. This relates to the enduring issue because we use technology as a method to solve our problem.",
            "In the age of exploration, Europeans sailed around the world to find new routes to Asia. What caused the start of this was the limit the Europeans had on Aian goods during the middle ages. They only heard stories of the riches of China and India. The only way to get those goods was through the Byzantine Empire which controlled Constantinople.",
            "Christine counters the works of literature of males by telling the story of how the three ladies named Reason, Rectitude, and Justice approached her to ask to help build a city of ladies. Where women can live in solidarity in a city that praises their contributions to society and their values. Gournay suggests a solidarity that allows women to have more opportunities for education to help give more representation of the contributions of women to societal advancements. Both authors views demonstrate a more inclusive solidarity that brings women up to equal terms to men.",
            "However, More recalls the story of a land called Utopia because of its communal governance and society. In Utopia, residents choose a governor through a series of elections. They set laws that foresee any situations of power disparity that may arise. They eliminated the need for private property by giving everyone the responsibility of learning the trade of agriculture and one other trade. Everyone contributes to producing food and goods for themselves, creating a surplus of resources to share with others.",
            "In our modern society, we have grown to change many aspects that the previous works of literature show their society lacked. However, we still face multiple problems that affect peoples daily lives. One example is our political situation in America, where the major division has separated the countrys solidarity. We are dealing with a society that has split between the two narratives of our major political houses.",
        ],
    },
    {
        "name": "formal human pieces",
        "criterion": 2,
        "texts": [
            "In conclusion, we experimented to find the most efficient method to cook popcorn. The hypotheses was that popcorn machine method would be the most efficient method. But as a result Jiffy Pop was the most efficient method. Five of the seven groups showed Jiffy Pop as most efficient. The null hypothesis was correct that if the popcorn is made in different methods, then there will be no significant difference in the popcorn machine method to the efficiency of the popcorn. Instead it would be if the popcorn is made in different methods, and then there will be a significant difference in the Jiffy Pop method to the efficiency of the popcorn.",
            "Global warming is damaging the Earth in various ways. Global warming is the increase in temperatures worldwide. Two authors hypothesize what the cause of global warming. In the article \"How much will Earth warm if carbon dioxide doubles pre-industrial levels?\"  the author Rebecca Lindsey claims the doubling of pre-industrial carbon dioxide will cause the Earth's temperature to rise. On the other hand, the author Fred Pearce of the article \"Global warming is down to the Sun, not humans\" claims solar changes is the causing of warming temperatures. However, an alternative author claims differently on the cause of global warming. Yet the claims of each author compare to each other to some extent.",
            "Sterne’s amazement to the environment of New York City caused her art to begin to shift from surrealism to abstract expressionism. In Sterne’s 1950’s artwork she would use spray paint in combination with oil to paint her experience living in the city. However, for the art piece, New York #2, she had only used oil to create this piece. Looking at the artwork, we can see her use of lines shifts from a more wave form to a more structured area. On the top portion of the painting the lines are more flowy and bunched up together showing a more free and fast movement. There is a circular shape behind these lines that from the audio from THE MET mentioned how the cream color white in the back is like the moon that is rising behind the city.",
            "However, the truth of the matter is that the practical benefits of space travel far outweigh the costs. For example, many medicines and drugs have been created and tested in the zerogravity of space. One such test done aboard the International Space Station was conducted to try a new form of cancer treatment delivery, an experiment that provided, \"better drug delivery and new medical treatments for solid tumors and resistant infections\" (\"Cancer Treatment Delivery\"). Developments such as this can provide direct help for doctors on Earth. NASA’s space program provides new possibilities for experimentation. Another benefit from space travel lies in the excess of natural resources to be found in space",
            "It is safe, however, to state that animals have yet to exhibit a quality or sustainment of conscious abstraction, insight, synthesis, or any pursuit thereof. Non-hominid animals do not appear to grasp inner, ethereal concepts such as spirituality, the mysteries of existence, or scientific truths, nor can they apply any of these to a practice or to the development of complex technology—machines. While primates do have opposable thumbs, they still have not evolved the sustained mental focus to use their grasp for anything more complex than simple tools.",
            "This case study surrounding the Risque Internet Service Company violates multiple principles of the ACM code of ethics and professional responsibilities. The first principle that was violated was 1.1 where it states that “computing professionals should contribute to society and to human well-being, acknowledging that all people are stakeholders in computing.” The RISC promoted their servers to be cheap, and guaranteed uptime, no matter what, which should be great for most users. But the company should have considered the possibilities in which this can be used in harmful ways to the public. Allowing this technology to be released to the public without regulations to prevent misuse, shows that the company did not acknowledge all people as stakeholders for this service.",
            "Responsibility falls on the government to act towards overcoming the consequences that come from societal shifts and to be able to provide a livable society for the American citizens. When it comes to elections, running candidates say that they can take the responsibility of providing a better government and increasing the stability of the American Dream under their presidential administration. Additionally, the 114th Congress mentioned the American Dream over 500 times, including in the names of four bills (Wolak, 2020). The definition of the American Dream remains as the thought of success in life, and politicians use it to help state what they will contribute to American society if they are elected.",
            "The origins of immigrant’s impact on the upbringing of American society, started around the Industrial Revolution as stated in the research of Hirschman (2009). America was shifting from rural living to an urban lifestyle with an increase in manufacturing of goods. This gave not just Americans but also incoming immigrants new job opportunities in the factories. However, working in the factories was not as safe and high paying as the other rising jobs that required education. Privileged Americans had the advantage of getting an education and obtaining good paying jobs but for immigrants who lacked education, they had to begin their American Dream in the factories.",
            "A peek at the future through the artwork “Hello America” by Alice Tye (see Figure 5), a series of art pieces depicting a dystopian future. In this painting, however, it shows a future of the city that never sleeps, filled with dunes of sand. The city is still standing tall, but no life seems to be seen other than the cactus and plants that thrive in this desert. A nature that is currently happening around the world from natural disasters and human disasters. The increase in natural disasters is the result of human activity and poses a future threat to people who are so distant from the natural environment.",
            "The theme of social criticism is visible through the works of Christine de Pizan, The Book of the City of Ladies, and the work of Marie de Gournay, The Equality of Men and Women. However, Christine uses the approach of criticism towards the society she is living in by discussing the misogyny depicted in works of literature. As she states in the text, \"... an extraordinary thought became planted in my mind which made me wonder why on earth it was that so many men, both clerks and others, have said and continue to say and write such awful, damming things about women and their ways.\" (Christine, \"City of Ladies\", p. 6). When Christine picked a book by Matheolus to read for fun, her thoughts began to take sides with the words in the book. She realizes that she has not read any literature written by men that has said great things about women. She concluded that women are the things that men have written about in the books and questions why she was not born male.",
        ],
    },
    {
        "name": "casual human pieces",
        "criterion": 3,
        "texts": [
            "I had a test yesterday and it was brutal. Two days ago I was none stop studying for the test and now I feel at ease! I had to study a lot for it because it is worth 40 percent on our final grade. I just hope I did well...",
            "You know I heard there is a new coffee shop that opened down the street. I heard that it has the best matcha drinks in town. We should go try them and see for ourself! I am kinda of craving a crossant dipped in chocalate with piece of almond on top. Yummm.",
            "I am sooo excited! The next best movie is just a month away! I have been counting down the days and I can't hold in my excitement. I know its going to be the best day ever this year. I even got my tickets during the pre-sale event!",
            "Today's commute to work was rough. Let me tell you why. When I arrived at my car, two other cars parked really close to mines! So I had to do multiple maneuvers just to take my car out of the tight spot. Once I got on the highway, two lanes were blocked due to construction. Once I was close by an object in the middle of the road so it slowed traffic down. Everything was trying to make me come in late today!",
            "There as so many different fur coat cats! My favorite has to be the torishell cats. Their fur costs consist of browns, oragnes, black, and cream colors. They do tend to be only females tho and tend to have a feisty personality. But are very cute and loveable!",
            "I went to Trader Joe's today and I went at a good time because there were barely any people. Usually, the store is packed and the line is long to pay. So I took my time grabbing a bag of bagels, some vegetables, fruits, and condiments. I also grabbed some sweet treats like chips and ice cream.",
            "Plans for today are ruined for the kids. Last night rain poured down and today we had planned to go out to the park. They were so excited to see their friends today at the park. Instead, we will be watching a movie at home and I will make some delicious chocolate chip cookies.",
            "My computer was heating up real bad last night, when I was working on one of my homework assignments. I thought nothing of it and took it to class today but the fans of the computer sounded really loud so I closed it and wrote my notes in a notebook. After class I decided to take it to a repair shop and it turns out it needed a good deep clean. There was a lot of dust that was causing my computer to heat up. Good thing I decided to have it fixed today because this assignment is due tomorrow and I wanted to finish it by today.",
            "The most funny thing happened today. I was in a rush to leave home today because I overslept. When I quickly made lunch and packed it into my bag. I rushed out by putting on my shoes and ran towards the bus stop. When I finally sat down in the bus I realized I took the wrong pair of shoes. I accidentally took my brother's shoes who is still at home. I am not sure how I did not realize it while walking to the bus. Good thing the size is not too big so I should be fine for the day.",
            "Today was the first time I ever went on a rollercoaster. It was not because I wanted to but because I was FORCED to. Bets were made and I could get 100 bucks if I did go onto the rollercoaster. So with the peer pressure I finally decided to give it a try. Honestly I would not go on a ride again.. I do not like the feeling in my stomach as the ride dropped down.",
        ],
    },
    {
        "name": "log matches /submit output",
        "criterion": 4,
        "texts": [
            "In conclusion, we experimented to find the most efficient method to cook popcorn. The hypotheses was that popcorn machine method would be the most efficient method. But as a result Jiffy Pop was the most efficient method. Five of the seven groups showed Jiffy Pop as most efficient. The null hypothesis was correct that if the popcorn is made in different methods, then there will be no significant difference in the popcorn machine method to the efficiency of the popcorn. Instead it would be if the popcorn is made in different methods, and then there will be a significant difference in the Jiffy Pop method to the efficiency of the popcorn.",
            "Global warming is damaging the Earth in various ways. Global warming is the increase in temperatures worldwide. Two authors hypothesize what the cause of global warming. In the article \"How much will Earth warm if carbon dioxide doubles pre-industrial levels?\"  the author Rebecca Lindsey claims the doubling of pre-industrial carbon dioxide will cause the Earth's temperature to rise. On the other hand, the author Fred Pearce of the article \"Global warming is down to the Sun, not humans\" claims solar changes is the causing of warming temperatures. However, an alternative author claims differently on the cause of global warming. Yet the claims of each author compare to each other to some extent.",
            "Sterne’s amazement to the environment of New York City caused her art to begin to shift from surrealism to abstract expressionism. In Sterne’s 1950’s artwork she would use spray paint in combination with oil to paint her experience living in the city. However, for the art piece, New York #2, she had only used oil to create this piece. Looking at the artwork, we can see her use of lines shifts from a more wave form to a more structured area. On the top portion of the painting the lines are more flowy and bunched up together showing a more free and fast movement. There is a circular shape behind these lines that from the audio from THE MET mentioned how the cream color white in the back is like the moon that is rising behind the city.",
            "However, the truth of the matter is that the practical benefits of space travel far outweigh the costs. For example, many medicines and drugs have been created and tested in the zerogravity of space. One such test done aboard the International Space Station was conducted to try a new form of cancer treatment delivery, an experiment that provided, \"better drug delivery and new medical treatments for solid tumors and resistant infections\" (\"Cancer Treatment Delivery\"). Developments such as this can provide direct help for doctors on Earth. NASA’s space program provides new possibilities for experimentation. Another benefit from space travel lies in the excess of natural resources to be found in space",
            "It is safe, however, to state that animals have yet to exhibit a quality or sustainment of conscious abstraction, insight, synthesis, or any pursuit thereof. Non-hominid animals do not appear to grasp inner, ethereal concepts such as spirituality, the mysteries of existence, or scientific truths, nor can they apply any of these to a practice or to the development of complex technology—machines. While primates do have opposable thumbs, they still have not evolved the sustained mental focus to use their grasp for anything more complex than simple tools.",
            "I had a test yesterday and it was brutal. Two days ago I was none stop studying for the test and now I feel at ease! I had to study a lot for it because it is worth 40 percent on our final grade. I just hope I did well...",
            "You know I heard there is a new coffee shop that opened down the street. I heard that it has the best matcha drinks in town. We should go try them and see for ourself! I am kinda of craving a crossant dipped in chocalate with piece of almond on top. Yummm.",
            "I am sooo excited! The next best movie is just a month away! I have been counting down the days and I can't hold in my excitement. I know its going to be the best day ever this year. I even got my tickets during the pre-sale event!",
            "Today's commute to work was rough. Let me tell you why. When I arrived at my car, two other cars parked really close to mines! So I had to do multiple maneuvers just to take my car out of the tight spot. Once I got on the highway, two lanes were blocked due to construction. Once I was close by an object in the middle of the road so it slowed traffic down. Everything was trying to make me come in late today!",
            "There as so many different fur coat cats! My favorite has to be the torishell cats. Their fur costs consist of browns, oragnes, black, and cream colors. They do tend to be only females tho and tend to have a feisty personality. But are very cute and loveable!",
        ],
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                       # missing text
            {"text": "", "creator_id": "eval_bad_empty"},             # empty text
            {"text": "a" * 20001, "creator_id": "eval_bad_huge"},     # just over 20,000
            {"text": "aaa", "creator_id": "eval_bad_small"},          # under 50
        ],
    }
    
    #
    # A criterion about the appeal path can't be tested by sending text alone;
    # it needs a submission first and then an appeal against the content_id
    # that came back. You'll need to test that one by hand, or extend this file
    # and run_eval.py to do it. Saying which you did is part of the write-up.
]


def validate() -> list[str]:
    """
    Complain about anything malformed, before a long run rather than during.

    A "bodies" scenario is deliberately exempt from the empty check — an empty
    string is the whole point of a bad-input case, and refusing to run one
    would make that criterion untestable.
    """
    problems = []
    for i, scenario in enumerate(SCENARIOS, 1):
        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') has both texts and "
                f"bodies — pick one"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict — bodies are whole "
                        f"request bodies, like {{'text': '', 'creator_id': 'x'}}"
                    )
            continue

        if not texts:
            problems.append(f"scenario {i} has no texts and no bodies")
            continue

        for j, text in enumerate(texts, 1):
            if not str(text).strip():
                problems.append(
                    f"scenario {i}, text {j} is empty — if an empty submission is what "
                    f"you're testing, use 'bodies' instead of 'texts'"
                )
            elif str(text).startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i} ('{scenario.get('name')}'), text {j} is still "
                    f"the placeholder"
                )
    return problems
