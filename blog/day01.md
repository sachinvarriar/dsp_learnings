# What is sound to a computer?

*DSP Lab, Day 1 · draft · notebook: `lesson1_sampling.ipynb` (refresher)*

**The big idea:** a computer can't hear. It turns sound into a very long list of numbers, and everything else in this series starts from that list.

## Sound is wiggling air

When a trumpet plays, it pushes the air back and forth, very fast. That wiggle travels to your ear, and your ear turns it into the sound you hear. A microphone works the same way: it feels the air wiggling.

## Taking snapshots: sampling

A computer can't store a smooth wiggle, so it takes **snapshots**. Thousands of times every second it asks "how far is the air pushed right now?" and writes the answer down as a number. Each answer is called a **sample**.

Think of a **flip-book**. Each page is one still drawing, but flip through them fast enough and you see movement. Sound samples are the pages, and your speakers flip through them so fast that you hear smooth sound again.

Our trumpet clip took **22,050 snapshots every second**. That number is called the **sampling rate**. The whole clip is 117,601 snapshots long. Divide one by the other and you get the clip's length: about 5⅓ seconds.

## The speed limit: why some sounds get lost

There is a rule for snapshots: **to catch a wiggle, you need at least two snapshots for every back-and-forth.** If the air wiggles faster than that, the snapshots miss it, and worse, they can make it look like a slower wiggle that was never there. That trick is called **aliasing**. Spinning wheels in films sometimes look like they go backwards for the same reason.

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

## Try it yourself in Audacity

Audacity is a free sound editor you can download from audacityteam.org.

1. Open Audacity and choose **File › Import › Audio…** to open any song, or drag a song file into the window. It appears as a wobbly blue band: the waveform.
2. Click and drag across about two seconds of the song to select it.
3. Choose **Analyze › Plot Spectrum…**. A graph pops up showing which notes were in your selection: peaks mean "lots of this note".
4. Close the graph. Click the track's name at its left edge to open its menu, and choose **Spectrogram**. Now you see the picture of notes over time, just like in the notebook.

## How AI uses this

Every AI that listens, from a phone's voice assistant to a music app that names songs, starts exactly here. First the sound becomes samples. Then the samples become a spectrogram. Many AI models then look at that spectrogram almost like a photo, and learn to spot the patterns that mean "dog barking", "the word *hello*" or "this song".

## Words to remember

- **Sample:** one snapshot of the sound, stored as a number.
- **Sampling rate:** how many snapshots are taken each second.
- **Aliasing:** a fake, slower sound created by taking snapshots too slowly.
- **Spectrogram:** a picture of which notes are playing, and when.
- **Timbre:** the "colour" of a sound that makes a trumpet sound like a trumpet.

> **For older readers:** the Nyquist rule says the sampling rate must be more than twice the highest frequency in the sound: f_s > 2 × f_max.
