# How loud is loud? Normalize vs Amplify

*DSP Lab, Day 3 · draft · notebook: `lessons/lesson03_levels.ipynb`*

**The big idea:** a computer stores sound as a long list of numbers, and making a sound louder just means making those numbers bigger, but only up to a ceiling.

## Sound is a list of numbers

When you record your voice, the microphone feels the air wiggling. The computer checks that wiggle thousands of times every second and writes down a number each time, like a flip-book where each page is one tiny moment. Our trumpet clip has 22,050 numbers for every second of sound.

Each number says how far the air was pushed at that moment. The numbers are allowed to go from −1 to +1, and not one bit further. Think of a room with a low ceiling: you can jump, but your head stops at the ceiling. In sound, that ceiling is called **full scale**.

## Measuring with decibels

People measure loudness in **decibels**, or dB for short. In computer sound we count down from the ceiling: the ceiling is 0 dB, and everything quieter is a negative number.

Here is the one trick to remember: **every time you halve a sound's size, it drops about 6 dB.** So a sound half as tall as the ceiling sits at about −6 dB.

## Two ways to measure "how loud"

- **Peak** is the very tallest number in the clip, like measuring the tallest kid in your class.
- **RMS** is more like the class's average height. It follows how loud something *sounds* much better than the peak does.

A trumpet note starts with a sharp spike and then settles down, so its peak is high but its average is much lower. A buzzing square wave stays at full height all the time, so its peak and its average are the same.

## Amplify: make every number bigger

**Amplify** multiplies every number by the same amount. Everything gets bigger together, so the sound keeps its shape.

But remember the ceiling. If you amplify too much, the tallest parts try to go past +1, and the computer just chops them off flat. That chopping is called **clipping**, and it sounds crunchy and harsh, like a speaker that is too loud.

## Normalize: let the computer pick the amount

**Normalize** is Amplify that works out the amount for you. You tell it "make the tallest part reach just under the ceiling" (usually −1 dB), and it does the maths.

It has one extra trick. Sometimes a recording is a little lopsided, sitting slightly above or below the middle line, like a see-saw that isn't level. That's called a **DC offset**. Normalize can straighten it first, which leaves more room before the ceiling.

## What we found

- Making the trumpet just 6 dB too loud chopped off 1,423 of its numbers, about 1 in every 80. You can hear the crunch in the notebook.
- Our lopsided test clip only reached −1 dB on one side. Once we straightened it, both sides could use the full height.
- We made a trumpet, a smooth tone and a buzzy square wave all exactly the same peak height. They did **not** sound equally loud. Their averages (RMS) were about −20 dB, −4 dB and −1 dB.

*Figure to use:* the clipping close-up from section 3 (what we asked for vs what got chopped). *Audio to embed:* the clean trumpet, then the clipped one.

## Try it yourself in Audacity

Audacity is a free sound editor you can download from audacityteam.org.

1. Open Audacity. Choose **Generate › Tone…**, set the *Amplitude* to 0.5, and press **Generate**. A blue band appears: that's your sound, drawn as its list of numbers.
2. Click inside the band and press **Ctrl+A** to select all of it.
3. Choose **Effect › Volume and Compression › Amplify…** (older versions: **Effect › Amplify…**). Audacity suggests about 6 dB, because half the ceiling is about 6 dB below it. Press **Cancel**.
4. Now choose **Effect › Volume and Compression › Normalize…**, set the peak to −1.0 dB and press **Apply**. Watch the band grow almost to the top and bottom.
5. Press the **space bar** to listen.

## How AI uses this

AI that listens, like the voice assistant on a phone, learns from thousands of recordings. Some were recorded loudly, some quietly, some on cheap microphones. Before the AI learns from them, the recordings are made about equally loud. Otherwise the AI might learn "this one was quiet" instead of learning which *word* was said. Clipped recordings cause trouble too, because the chopped tops add crunchy sounds that were never in the voice.

## Words to remember

- **Sample:** one number in the list, one tiny moment of sound.
- **Full scale:** the ceiling. Numbers can't go past −1 or +1.
- **Decibel (dB):** a way of measuring loudness. Halving the size takes off about 6 dB.
- **Clipping:** what happens when sound hits the ceiling and gets chopped flat.
- **Normalize:** make the loudest part reach a chosen level.

> **For older readers:** level in dB = 20 × log₁₀(amplitude). An amplitude of 0.5 gives 20 × log₁₀(0.5) ≈ −6.02 dB.
