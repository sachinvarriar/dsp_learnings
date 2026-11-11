# Day 1 outline: Normalize vs Amplify, what Audacity's two loudness buttons really do

Notebook: `lessons/lesson03_levels.ipynb`

**The question:** Audacity has two effects that make a clip louder. Are they the same thing?

**Points to make**
1. Digital audio has a ceiling (0 dBFS). Levels are measured in decibels below it, and halving the amplitude takes about 6 dB off.
2. Amplify multiplies every sample by one number. Ask for more than fits and the peaks are cut flat (clipping). In the trumpet clip, 6 dB too much clipped 1.2% of the samples, and you can hear it.
3. Normalize is Amplify with the gain worked out for you, aimed at a target such as −1 dBFS. It can also remove a DC offset first, which frees up headroom the offset was wasting.
4. Equal peaks are not equal loudness. Normalized to −1 dBFS, the trumpet's RMS was −20 dBFS, a sine's −4 and a square's −1. That gap is why Loudness Normalization (LUFS) exists.

**Figure to use:** the clipping close-up (section 3): what the gain asked for vs what could be stored.
**Audio to embed:** the clean and the clipped trumpet, one after the other.
