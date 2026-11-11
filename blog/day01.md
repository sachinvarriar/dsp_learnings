# What is sound to a computer?

*DSP Lab, Day 1 · draft · notebook: `lesson1_sampling.ipynb` (refresher)*

**The big idea:** a computer can't hear. It turns sound into a very long list of numbers, and everything else in this series starts from that list.

## Sound is wiggling air

When a trumpet plays, it pushes the air back and forth, very fast. That wiggle travels to your ear, and your ear turns it into the sound you hear. A microphone works the same way: it feels the air wiggling.

## Taking snapshots: sampling

A computer can't store a smooth wiggle, so it takes **snapshots**. Thousands of times every second it asks "how far is the air pushed right now?" and writes the answer down as a number. Each answer is called a **sample**.

Think of a **flip-book**. Each page is one still drawing, but flip through them fast enough and you see movement. Sound samples are the pages, and your speakers flip through them so fast that you hear smooth sound again.

Our trumpet clip took **22,050 snapshots every second**. That number is called the **sampling rate**. The whole clip is 117,601 snapshots long. Divide one by the other and you get the clip's length: about 5⅓ seconds.

The sampling rate is sound's version of a **frame rate**. A movie shows 24 pictures (frames) every second. Many video games show 30 or 60, and the 60 ones feel smoother because each movement is caught in more steps. Sound needs far more "frames" than video, because air wiggles much faster than anything moves on a screen: thousands of times a second.

## The speed limit: why some sounds get lost

There is a rule for snapshots: **to catch a wiggle, you need at least two snapshots for every back-and-forth.** If the air wiggles faster than that, the snapshots miss it, and worse, they can make it look like a slower wiggle that was never there. That trick is called **aliasing**.

You have probably seen aliasing in a movie. When a car speeds up, its wheels sometimes seem to slow down, stop, or even spin **backwards**. The wheel is really spinning forwards, fast. But between one frame and the next, each spoke moves almost all the way to where the next spoke was. The camera only sees the frames, so your brain joins the dots the wrong way. Games do something similar: at a low frame rate, a fast-spinning fan or helicopter blade can look slow, jumpy or backwards.

Sound works the same way. A wiggle that is too fast for the sampling rate doesn't just disappear. It shows up in disguise, as a lower sound that was never really there.

So 22,050 snapshots a second can catch wiggles up to about 11,000 per second. That's enough for most music and speech.

## Seeing the notes inside a sound

If you draw all the samples as a line, you get a **waveform**: a wobbly line that shows when the sound is loud or quiet. But a waveform doesn't tell you *which notes* are in the sound.

For that we use a clever bit of maths called the **Fourier transform**. Think of a smoothie. You can taste it, but you can't see the banana and the strawberries any more. The Fourier transform is like a machine that un-blends the smoothie and tells you how much of each fruit went in. For sound, the "fruits" are pure, simple notes.

A **spectrogram** does this over and over, slice by slice, and draws a picture. Time goes left to right, low notes are at the bottom, high notes at the top, and brighter means louder.

## What we found

- In the trumpet's spectrogram there's a bright line near **600 wiggles per second**. That's the note we hear, called the **fundamental**.
- Above it are more bright lines, evenly stacked. These are **harmonics**: quieter, higher notes that ride along with the main one.
- When we looked at one short slice, the strongest note was near 1,000 wiggles per second, not 600. It's a puzzle! The loudest line isn't always the note you hear. We'll solve it on Day 34.

*Figure to use:* the trumpet spectrogram from the notebook. *Audio to embed:* the trumpet clip.

## Why a trumpet doesn't sound like a flute

A trumpet and a flute can play the same note and still sound different. The difference is in the harmonics: how many there are, and how loud each one is. This is called **timbre** (say "TAM-ber"). It's like two people singing the same word: you can still tell who is who.

## Sounds to try

Four short sounds made for this post. Click one, then press **Download raw file** on GitHub.

| Sound | What you'll hear |
|---|---|
| [Pure tone](https://github.com/sachinvarriar/dsp_learnings/blob/main/audio/day01_pure_tone_440hz.wav) | One clean note, 3 seconds. |
| [Rich tone](https://github.com/sachinvarriar/dsp_learnings/blob/main/audio/day01_rich_tone_220hz.wav) | A buzzy note full of harmonics, 3 seconds. |
| [Sweep, enough snapshots](https://github.com/sachinvarriar/dsp_learnings/blob/main/audio/day01_chirp_ok_22050hz.wav) | A whistle that keeps going up, 4 seconds. |
| [Sweep, too few snapshots](https://github.com/sachinvarriar/dsp_learnings/blob/main/audio/day01_chirp_aliased_8000hz.wav) | The same whistle, but it goes up, comes back down and goes up again. That's aliasing! |

## Try it yourself in Audacity

Audacity is a free sound editor you can download from audacityteam.org.

1. Open Audacity and choose **File › Import › Audio…**, then pick the two sweep sounds. (You can also drag them into the window.) Each one appears as a band: its waveform.
2. Press the **space bar** to play. Click **Solo** on one track at a time to hear them separately. Hear how the second one turns around?
3. Click each track's name at its left edge to open its menu, and choose **Spectrogram**. The first sweep draws a line that climbs all the way up. The second one climbs, bounces off a ceiling and comes back down: that ceiling is half its snapshot rate.
4. Now import the **pure tone** and the **rich tone** and look at their spectrograms. The pure tone is a single line. The rich tone is a ladder of lines: its harmonics, the "colour" of the sound.
5. Want to try a real song? Import any song, drag across about two seconds of it, and choose **Analyze › Plot Spectrum…** to see which notes are in it.

## Try it with code

For grown-ups and curious kids. This loads the aliased sweep and draws its spectrogram:

```python
import librosa, librosa.display
import numpy as np
import matplotlib.pyplot as plt

# sr=None keeps the file's own snapshot rate: 8,000 a second
y, sr = librosa.load("audio/day01_chirp_aliased_8000hz.wav", sr=None)
print(f"{len(y)} snapshots at {sr} a second = {len(y) / sr:.1f} seconds")

S = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
librosa.display.specshow(S, sr=sr, x_axis="time", y_axis="hz")
plt.title("A sweep with too few snapshots")
plt.show()
```

Swap in the other files, or try librosa's built-in sounds: `librosa.ex('libri1')` is a person reading a story, and `librosa.ex('robin')` is a bird.

## How AI uses this

Every AI that listens, from a phone's voice assistant to a music app that names songs, starts exactly here. First the sound becomes samples. Then the samples become a spectrogram. Many AI models then look at that spectrogram almost like a photo, and learn to spot the patterns that mean "dog barking", "the word *hello*" or "this song".

## Words to remember

- **Sample:** one snapshot of the sound, stored as a number.
- **Sampling rate:** how many snapshots are taken each second, like a frame rate for sound.
- **Aliasing:** a fake, slower sound created by taking snapshots too slowly, like wheels that seem to spin backwards in a movie.
- **Spectrogram:** a picture of which notes are playing, and when.
- **Timbre:** the "colour" of a sound that makes a trumpet sound like a trumpet.

> **For older readers:** the Nyquist rule says the sampling rate must be more than twice the highest frequency in the sound: f_s > 2 × f_max.
