""" Formal-register check. It does not change the signal scores. It only flags text. """

import re
import config

TRANSITIONS = ["furthermore", "moreover", "addition", "additionally", "in conclusion", 
               "consequently", "therefore", "overall", "ultimately", "likewise", "thus", 
               "in summary", "specifically", "for example", "however", "nevertheless", "on the other hand",
               "nonetheless", "as a result", "accordingly"]

# Casual words only. "I", "my" and "we" are fine in formal essays, so they're not here.
CASUAL_WORDS = {"kinda", "gonna", "wanna", "gotta", "lol", "omg", "tbh", "yeah", "stuff"}

# Contractions only; skips possessive 's (e.g. "author's").
CONTRACTION = re.compile(r"[a-z]+(?:n't|'re|'ll|'ve|'m|'d)$")
# Other casual signals: stretched letters ("sooo") and all-caps words ("SCORE", 3+ letters so "I"/"AI" don't count).
STRETCHED = re.compile(r"([a-z])\1\1")
ALL_CAPS = re.compile(r"\b[A-Z]{3,}\b")
# Quoted text is removed before checking "!" so an essay quoting "Liberty or death!" stays formal.
QUOTED = re.compile(r"[\"“][^\"”]*[\"”]")

S_CONTRACTIONS = {"it's", "that's", "there's", "what's", "he's", "she's", "here's", "let's"}

def formal_register(text: str) -> tuple[bool, str]:
    lower = text.lower()
    words = re.findall(r"[a-z]+(?:'[a-z]+)?", lower)
    if not words:
        return False, ""
    transitions = sum(len(re.findall(rf"\b{t}\b", lower)) for t in TRANSITIONS)
    contraction_rate = sum(
        bool(CONTRACTION.match(w)) or w in S_CONTRACTIONS for w in words
    ) / len(words)
    casual = (any(w in CASUAL_WORDS for w in words)
              or "!" in QUOTED.sub("", text)
              or STRETCHED.search(lower) is not None
              or ALL_CAPS.search(text) is not None)

    # At least one transition is required: plain casual writing has no casual markers either,
    # so "no casual markers" alone let it pass as formal. Tradeoff: short formal paragraphs
    # with no transitions now go unflagged.
    is_formal = (contraction_rate <= config.FORMAL_MAX_CONTRACTION_RATE
                 and not casual
                 and transitions >= 1)
    reason = (f"Formal register: {contraction_rate:.1%} contractions, no casual words, "
              f"{transitions} transition phrases" if is_formal else "")
    
    return is_formal, reason