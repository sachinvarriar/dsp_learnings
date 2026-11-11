"""Makes the short practice clips in audio/ for the refresher days (1 and 2): open them in Audacity or load them in code.
From Day 3 on, each lesson's notebook makes its own clips.
All sounds are generated here, so there are no licence questions.
    python tools/make_clips.py
"""
from pathlib import Path

import numpy as np
from scipy.io import wavfile

OUT = Path(__file__).resolve().parent.parent / "audio"
OUT.mkdir(exist_ok=True)


def save(name, x, sr):
    """Fade 20 ms in and out (no clicks) and save as 16-bit mono WAV."""
    n = int(0.02 * sr)
    ramp = np.linspace(0, 1, n)
    x = x.copy()
    x[:n] *= ramp
    x[-n:] *= ramp[::-1]
    wavfile.write(OUT / name, sr, np.round(x * 32767).astype(np.int16))
    print(f"{name:32s} {len(x) / sr:4.1f} s at {sr} Hz")


def chirp_phase(t, f0, f1, dur):
    """Phase of a sweep whose frequency rises linearly from f0 to f1 over dur seconds."""
    return 2 * np.pi * (f0 * t + (f1 - f0) * t**2 / (2 * dur))


SR = 22050

# 1. One clean note: A above middle C, 440 wiggles a second
t = np.arange(3 * SR) / SR
save("day01_pure_tone_440hz.wav", 0.4 * np.sin(2 * np.pi * 440 * t), SR)

# 2. A "rich" note: 220 Hz plus its harmonics (each k-th harmonic at 1/k strength), like a buzzy instrument
rich = sum(np.sin(2 * np.pi * 220 * k * t) / k for k in range(1, int((SR / 2) // 220)))
save("day01_rich_tone_220hz.wav", 0.4 * rich / np.max(np.abs(rich)), SR)

# 3. A sweep from 100 Hz to 10,000 Hz, taken with plenty of snapshots: the pitch keeps rising
dur = 4.0
t = np.arange(int(dur * SR)) / SR
save("day01_chirp_ok_22050hz.wav", 0.3 * np.sin(chirp_phase(t, 100, 10_000, dur)), SR)

# 4. The same sweep, but only 8,000 snapshots a second and no filter first.
#    Above 4,000 Hz the snapshots can't keep up: the pitch "turns around" and falls (aliasing)
SR_LOW = 8000
t = np.arange(int(dur * SR_LOW)) / SR_LOW
save("day01_chirp_aliased_8000hz.wav", 0.3 * np.sin(chirp_phase(t, 100, 10_000, dur)), SR_LOW)

# Day 2: Lesson 2's vowels, each built from its first two formants (F1, F2) as two pure tones
VOWELS = {"a_had": (660, 1720), "i_heed": (270, 2290), "u_hood": (300, 870)}
t = np.arange(2 * SR) / SR
for name, (f1, f2) in VOWELS.items():
    save(f"day02_vowel_{name}.wav", 0.2 * (np.sin(2 * np.pi * f1 * t) + np.sin(2 * np.pi * f2 * t)), SR)
