from stylometry import (
    sentence_length_spread, type_token_ratio, punctuation_density, style_signal, words
)
from detector import model_signal


samples = {
    "clearly human": """I didn't sleep. Not properly, anyway — I lay there listening to the boiler tick and thinking about the thing I'd said to Marcus at the pub, which was stupid, and which he will absolutely bring up again. Twice now. So: coffee, and the long way round to work, and a plan. The plan lasted until about ten past nine, when Priya asked how the weekend was and I said "fine" in the voice that means it wasn't, and she put her mug down and looked at me. That's the trouble with Priya. She notices.""",
    "clearly AI": """The importance of effective time management cannot be overstated in today's fast-paced work environment. Professionals who develop strong organizational habits are better positioned to meet deadlines and reduce stress. There are several key strategies that can help individuals improve their productivity. First, prioritization is essential. By identifying the most important tasks and addressing them first, workers can ensure that critical objectives are met. Second, minimizing distractions plays a significant role. Setting aside dedicated blocks of time for concentrated work is widely considered beneficial. Finally, regular breaks are important for maintaining performance.""",
    "plain human": """Today's weather was windy. Which was perfect weather for wearing my white fluffly sweater with by uggs. I drank my morning coffee with toasted bread, perfect for this kind of weather.""",
    "lightly-edited AI": """The introduction of remote work has changed the way many teams communicate. People now rely on messaging apps and scheduled video calls, instead of an in-person chat. This shift has clear benefits, such as fewer interruptions and more flexible hours. It also has drawbacks. Without casual check-ins, small misunderstandings can grow into bigger problems — and they're harder to spot early. Teams that do well usually set clear expectations about response times and meeting etiquette. They also make time for informal conversation, even if it's just a few minutes at the start of a call. In the end, the tools matter less than the habits people build around them.""",
}

for name, t in samples.items():
    for name, t in samples.items():
        m = model_signal(t)
        s = style_signal(t)
        print(f"{name:20} model={m:.2f}  style={s:.2f}  avg={(m + s) / 2:.2f}")

