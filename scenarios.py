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
        "name": "score spread",
        "criterion": 2,
        "texts": [
            "I didn't sleep. Not properly, anyway — I lay there listening to the boiler tick and thinking about the thing I'd said to Marcus at the pub, which was stupid, and which he will absolutely bring up again. Twice now. So: coffee, and the long way round to work, and a plan. The plan lasted until about ten past nine, when Priya asked how the weekend was and I said \"fine\" in the voice that means it wasn't, and she put her mug down and looked at me. That's the trouble with Priya. She notices.",
            "Today was a great day for some warm coffee and a good book. I sat by the window listening to the rain fall as I read my book. My cat cuddle right next to me, not moving one inch for the time I was there. Best chill day ever! I wish for more days like this..",
            "I had soccer practice yesterday and now my legs hurt. I want to go out with my friends but I need this day for recovery. I scored 2 times! We won by a landslide 0-3! My team works great with coordination and that allows us to get closer to the goal post and SCORE! I might have to ask my friends if they want to come over instead to play some Mario games.",
            "I am sooo mad! I went to 5 different stores today in the city, to find a specific blue sweater I saw online. I need it by tomorrow for an event I am attending and its the only one that fits with the outfit I have in mind. I am going to one more store and if its not there then I am going to loseee my mindddd.",
            "My dog ate my homework... I did not think this would actually happend but it did. Now how am I supposed to explain this to my teacher? I stepped out my room for 10 minutes and come back to my dog all over my stuff. Once I push him out the way, I see that he had my homework assignment in this mouth all torn apart!",
            "The importance of effective time management cannot be overstated in todays fast-paced work environment. Professionals who develop strong organizational habits are better positioned to meet deadlines and reduce stress. There are several key strategies that can help individuals improve their productivity. First, prioritization is essential. By identifying the most important tasks and addressing them first, workers can ensure that critical objectives are met. Second, minimizing distractions plays a significant role. Setting aside dedicated blocks of time for concentrated work is widely considered beneficial. Finally, regular breaks are important for maintaining performance.",
            "Artificial intelligence is rapidly transforming the landscape of modern healthcare. From diagnostic tools to personalized treatment plans, AI-driven solutions offer unprecedented opportunities to improve patient outcomes. However, it is important to consider the ethical implications of these technologies. Issues such as data privacy, algorithmic bias, and transparency must be carefully addressed. By fostering collaboration between technologists, healthcare professionals, and policymakers, society can harness the benefits of AI while mitigating potential risks. Ultimately, a balanced approach will be essential to ensuring that innovation serves the best interests of all.",
            "Climate change represents one of the most pressing challenges facing humanity today. Rising global temperatures, extreme weather events, and sea level rise pose significant threats to ecosystems and communities worldwide. Addressing this issue requires a multifaceted approach. Governments must implement effective policies to reduce greenhouse gas emissions. Businesses can contribute by adopting sustainable practices and investing in renewable energy. Individuals also play a crucial role through mindful consumption and advocacy. By working together, we can build a more resilient and sustainable future for generations to come.",
            "Effective communication is a cornerstone of successful teamwork. When team members share information openly and clearly, they are better equipped to collaborate and achieve common goals. There are several strategies that can enhance communication within a team. First, active listening ensures that every voice is heard and valued. Second, regular check-ins help maintain alignment and address concerns early. Additionally, leveraging digital tools can streamline collaboration across remote environments. In summary, prioritizing communication fosters trust, boosts productivity, and creates a positive workplace culture.",
            "Reading offers numerous benefits that extend far beyond entertainment. Engaging with books can enhance vocabulary, improve concentration, and foster empathy by allowing readers to experience diverse perspectives. Furthermore, studies suggest that regular reading may reduce stress and support cognitive health as individuals age. In an increasingly digital world, cultivating a reading habit can provide a valuable opportunity to disconnect and reflect. Whether through fiction or nonfiction, reading remains a powerful tool for personal growth and lifelong learning.",
        ],
    },
    {
        "name": "label coverage",
        "criterion": 3,
        "texts": [
            "Before the printing press, it would take a long time to produce one book especially the bible. But after the invention of the printing press, it changed the lives of people. The impact of innovation is seen because the printing press is the method to addressing the problem of not being able to spread ideas quickly. With the printing press, more people were able to spread ideas and more learned how to read.",
            "Time management matters a lot in todays fast-paced work environment. People who build strong organizational habits are better placed to hit deadlines and keep stress down. There's a few strategies that can help people get more done. First, prioritization is essential - figure out the most important tasks and do those first, so the critical stuff gets done. Second, cutting distractions makes a big difference. Blocking off time for focused work is widely considered beneficial. Finally, regular breaks matter for keeping performance up.",
            "My grandma taught me how to make tamales every December. We'd spend the whole day in her kitchen, my hands sticky with masa, her laughing at how bad my folding was. These traditions serve as a vital link between generations, preserving cultural heritage and fostering a sense of identity and belonging within families.",
            "Time management matters more than people admit, especially now that work moves as fast as it does. If you're organised you hit deadlines, and you're less frazzled doing it. A few things actually help. Prioritise — work out what genuinely matters and do that first. Cut the interruptions; notifications wreck focus and the damage is worse than it feels at the time. And take breaks, short ones, often.",
        ]
    },
    {
        "name": "bad input",
        "criterion": 5,
        "bodies": [
            {"creator_id": "eval_bad_missing"},                       # missing text
            {"text": "", "creator_id": "eval_bad_empty"},             # empty text
            {"text": "a" * 20001, "creator_id": "eval_bad_huge"},     # just over 20,000
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
