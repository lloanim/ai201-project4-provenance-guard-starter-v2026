"""
Signal two: the style signal. ← YOU BUILD THIS IN MILESTONE 4

Signal one reads the text for meaning. This one measures it *as text* — the
shape of it, without understanding a word.

Three measures are stubbed below because the brief names those three. They are
stubs, not implementations: what they compute is yours, and so is how you
combine them.

    sentence_length_spread   do sentences vary in length, or march in step?
    type_token_ratio         how much of the vocabulary repeats?
    punctuation_density      how much punctuation, and how varied?

Why these might differ between human and AI writing: generated prose tends
toward even, mid-length sentences and a narrower band of vocabulary, because
that's what "most likely next word" produces on average. Human writing is
lumpier — a three-word sentence next to a forty-word one.

⚠️ **The blind spot, which you have to name in Milestone 1.**

This signal cannot read. It has no idea what the text says. Anything that
changes the shape without changing the substance moves it — adding typos,
breaking up sentences, pasting in a quotation. That is a very cheap thing for
someone to do on purpose, and unit 8's attack set will do it to you.

Build each function on its own and call it from a terminal before you wire
anything together:

    python stylometry.py "some text to look at"
"""

import re
import statistics


def sentences(text: str) -> list[str]:
    """Split into sentences. Rough and good enough — given to you."""
    parts = re.split(r"(?<=[.!?])\s+", text.strip())
    return [p for p in parts if p.strip()]


def words(text: str) -> list[str]:
    """Split into lowercase words, punctuation stripped. Given to you."""
    return re.findall(r"[a-z0-9']+", text.lower())


# ── The three measures — YOU BUILD THESE ─────────────────────────────────────

def sentence_length_spread(text: str) -> float:
    """
    How much sentence length varies. 

    Returns:
        stdev / mean of words-per-sentence (>= 0). 
        Higher = more varied = more human-like
        Fewer than 2 sentence -> 0.0 (no spread to measure)
    """
    text_sentences = sentences(text)
    lengths = []

    for s in text_sentences:
        lengths.append(len(words(s)))

    if len(lengths) < 2:
        return 0.0

    mean = statistics.mean(lengths)
    if mean == 0:
        return 0.0
    
    stdev = statistics.stdev(lengths)
    
    return stdev / mean


def type_token_ratio(text: str) -> float:
    """
    Unique words over total words. 
    Returns:
        A float between 0 and 1. Higher means more varied vocabulary.
        Fewer than 2 sentences -> 0.0

    Worth knowing before you rely on it: this measure falls as text gets
    longer, because common words repeat. Two texts of different lengths aren't
    directly comparable on it, and if your test inputs vary a lot in length,
    that alone can look like a signal.
    """
    text_words = words(text)

    if not text_words:
        return 0.0

    unique = set(text_words)

    return len(unique) / len(text_words)


def punctuation_density(text: str) -> float:
    """
    How much punctuation, relative to length.

    Returns:
       Punctuation marks per word (>= 0). Counts commas, semicolons, 
       colons, dashes, etc. Ignores full stops since nearly every 
       sentence has one.
    """
    punct = ",;:—–-()!?\""
    count = 0

    text_words = words(text)
    
    if not text_words:
        return 0.0

    for ch in text:
        if ch in punct:
            count += 1
    
    return count / len(text_words)


# ── Combining them ───────────────────────────────────────────────────────────

def _scale(value: float, low: float, high: float) -> float:
    """Map value onto 0-1 between low and high, clamped at the ends"""
    if high == low:
        return 0.0
    return max(0.0, min(1.0, (value-low) / (high-low)))

def style_signal(text: str) -> float:
    """
    The style signal as a 0–1 score. **Higher means more likely AI.** ← TODO

    Combine your three measures into one number. Same direction as
    `detector.model_signal`, so that `scoring.combine_signals` can treat them
    the same way — if one of your signals runs backwards, everything above it
    is wrong in a way that's hard to see.

    Two things to decide and write down:

      1. Which direction each measure points. Low spread means more AI-ish, so
         it needs flipping. Work out which of your three need that.
      2. How to get each onto a comparable scale. A raw type-token ratio sits
         between 0 and 1; a raw punctuation count doesn't. Adding them
         unscaled means whichever has the bigger numbers wins by default.

    Test it on the four calibration inputs from Milestone 4 — clearly AI,
    clearly human, plain conventional human writing, lightly-edited AI — before
    you trust it. Plain and ordinary, not formal: formal prose reads as *human*
    to signal one, and it is plain writing that gets accused.
    """
    spread = 1 - _scale(sentence_length_spread(text), 0.3, 1.0)
    ttr = 1 - _scale(type_token_ratio(text), 0.4, 0.8)
    punct = 1 - _scale(punctuation_density(text), 0.0, 0.15)
    
    return 0.45 * spread + 0.1 * ttr + 0.45 * punct


if __name__ == "__main__":
    import sys

    text = " ".join(sys.argv[1:]) or (
        "The system works well. It handles most cases correctly and provides "
        "good results. Users generally find it easy to use and understand."
    )

    print(f"{len(sentences(text))} sentences, {len(words(text))} words\n")
    print(f"sentence_length_spread   {sentence_length_spread(text)}")
    print(f"type_token_ratio         {type_token_ratio(text)}")
    print(f"punctuation_density      {punctuation_density(text)}")
    print(f"style_signal             {style_signal(text)}   (higher = more likely AI)")
    print("\nAll zeros? These are stubs — Milestone 4 is where you build them.")
