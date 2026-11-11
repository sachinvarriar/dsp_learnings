# DSP Lab: 44-day plan

One notebook and one blog post a day, from Thu 12 Nov to Fri 25 Dec 2026. Each day takes one Audacity feature, explains the B.Tech DSP idea underneath it, rebuilds it in Python, and ends with how AI uses it. Days 1 and 2 re-run the two October 2025 notebooks as refreshers; from Day 3 on, Day N is `lessons/lessonNN_*.ipynb`.

## Time budget
Sachin has **30 minutes to read** and **30 minutes to run and understand the code** each day. Keep every lesson inside that:
- 3 or 4 short sections, about 1,200 to 1,800 words of explanation in total, and 6 to 10 code cells, each running in seconds.
- If a topic does not fit, stop at a natural break and say what the next day picks up. Do not squeeze.
- Build on earlier lessons (including the two October 2025 notebooks) and link back to them instead of re-explaining.

## Notebook conventions
- File: the path in the table below. Python 3.11, dependencies in `requirements-lab.txt` only.
- Order of cells: title and date; what you will learn (3-5 bullets); references; then short sections, each a markdown explanation followed by code; "Try it in Audacity"; "How AI uses this"; exercises (2-3); summary.
- Make every step audible: `IPython.display.Audio(x, rate=sr, normalize=False)` so levels are heard as they are.
- Prefer synthetic signals and librosa's example clips (`librosa.ex(...)`), with a synthetic fallback if a download fails.
- **Practice sounds:** each lesson also saves 2 to 4 short clips (2-5 seconds, 16-bit mono WAV, under 300 KB each) to `audio/dayNN_<what>.wav`, generated in the notebook so they are free to share, and adds them to the table in `audio/README.md`. The notebook and the blog's Audacity steps both use them. Never copy third-party audio (including librosa's examples) into the repo.
- Plain, friendly English for someone who did B.Tech DSP years ago. Define a term the first time it appears.
- The notebook must run top to bottom without errors in under two minutes and be committed with its outputs.
- **Try it in Audacity** assumes the reader has never used Audacity: how to open or generate a clip, how to select audio, which menu to use and what they should see. Menu names differ between versions, so name the effect and say where it usually is (Audacity 3.2 and later group effects into submenus such as Effect > Volume and Compression).
- End with **How AI uses this**, using the AI link given for the day below.
- Refresher days (1 and 2) use the existing notebook; only the blog post is written.

## Blog post conventions
- Write `blog/dayNN.md` as a full draft blog post for Sachin to edit and publish.
- Write it for a curious 5th grader (about 10 years old) who wants to learn DSP and later use it for AI. Short sentences, everyday words, and one picture-in-your-head comparison for each idea (for example, sampling is like a flip-book). Explain any number before using it. No formulas in the main text; at most one, in a box at the end, for older readers.
- Sections: a title; the big idea in one sentence; the explanation with comparisons; "What we found" with 2-3 results from the notebook; "Sounds to try" (a table linking the day's clips on GitHub, `https://github.com/sachinvarriar/dsp_learnings/blob/main/audio/...`); "Try it yourself in Audacity" in beginner steps using those clips; "Try it with code" (one short, tested snippet that loads a clip with `librosa.load(path, sr=None)`); "How AI uses this"; "Words to remember" (3-5 terms with one-line meanings). Follow `blog/day01.md`.
- About a 5-minute read. Name the figure and audio clips from the notebook to embed.

## Days

| Day | Date | Notebook | Topic | Audacity | B.Tech DSP topic |
|---|---|---|---|---|---|
| 1 | Thu 12 Nov | `lesson1_sampling.ipynb` | Refresher: sampling, spectrum and timbre | Open any song, select a few seconds, then Analyze > Plot Spectrum | Sampling theorem, Fourier transform |
| 2 | Fri 13 Nov | `lesson2_vowelsound_comparison.ipynb` | Refresher: vowel formants | Record yourself saying a, i and u, then switch the track to Spectrogram view | Resonance |
| 3 | Sat 14 Nov | `lessons/lesson03_levels.ipynb` | Levels: peak, RMS and dBFS | Amplify, Normalize, Loudness Normalization | Signal energy and power |
| 4 | Sun 15 Nov | `lessons/lesson04_bit_depth.ipynb` | Bit depth and quantisation | Sample format, dither setting | Quantisation, SNR = 6.02N + 1.76 dB |
| 5 | Mon 16 Nov | `lessons/lesson05_aliasing.ipynb` | Aliasing, properly | Generate > Chirp, Resample | Sampling theorem, reconstruction |
| 6 | Tue 17 Nov | `lessons/lesson06_waveforms.ipynb` | Waveforms as sums of sines | Generate > Tone | Fourier series |
| 7 | Wed 18 Nov | `lessons/lesson07_noise_colours.ipynb` | Noise and its colours | Generate > Noise | Random signals, power spectral density |
| 8 | Thu 19 Nov | `lessons/lesson08_dft_by_hand.ipynb` | The DFT by hand | Plot Spectrum | DFT |
| 9 | Fri 20 Nov | `lessons/lesson09_fft_bins.ipynb` | The FFT and frequency bins | Plot Spectrum (Size) | Radix-2 FFT, O(N log N) |
| 10 | Sat 21 Nov | `lessons/lesson10_windows.ipynb` | Windowing and spectral leakage | Plot Spectrum (Function) | Windowing |
| 11 | Sun 22 Nov | `lessons/lesson11_spectrograms.ipynb` | Spectrograms and the STFT | Spectrogram view settings | STFT, time-frequency trade-off |
| 12 | Mon 23 Nov | `lessons/lesson12_review_seeing_sound.ipynb` | Review: seeing sound | (none) | Review |
| 13 | Tue 24 Nov | `lessons/lesson13_impulse_response.ipynb` | Impulse response | Record, trim | LTI systems |
| 14 | Wed 25 Nov | `lessons/lesson14_convolution.ipynb` | Convolution | (none) | Convolution sum |
| 15 | Thu 26 Nov | `lessons/lesson15_convolution_reverb.ipynb` | Convolution reverb | Effect > Reverb | Linear vs circular convolution, overlap-add |
| 16 | Fri 27 Nov | `lessons/lesson16_echo_comb.ipynb` | Echo and comb filters | Effect > Echo | Difference equations, FIR vs IIR |
| 17 | Sat 28 Nov | `lessons/lesson17_z_transform.ipynb` | The z-transform | (none) | Z-transform, transfer functions |
| 18 | Sun 29 Nov | `lessons/lesson18_poles_zeros.ipynb` | Poles, zeros and stability | (none) | Poles, zeros, stability |
| 19 | Mon 30 Nov | `lessons/lesson19_fir_design.ipynb` | FIR filter design | Low-Pass and High-Pass Filter | FIR design by windowing |
| 20 | Tue 01 Dec | `lessons/lesson20_iir_design.ipynb` | IIR filter design | (none) | Analog prototypes, bilinear transform |
| 21 | Wed 02 Dec | `lessons/lesson21_shelving_biquads.ipynb` | Shelving filters and biquads | Bass and Treble | Second-order sections |
| 22 | Thu 03 Dec | `lessons/lesson22_equaliser.ipynb` | A graphic equaliser | Graphic EQ, Filter Curve EQ | Biquads in cascade |
| 23 | Fri 04 Dec | `lessons/lesson23_review_filters.ipynb` | Review: systems and filters | (none) | Review |
| 24 | Sat 05 Dec | `lessons/lesson24_fades_envelopes.ipynb` | Fades and envelopes | Fade In/Out, Envelope tool, Auto Duck | Amplitude modulation |
| 25 | Sun 06 Dec | `lessons/lesson25_envelope_follower.ipynb` | Following loudness over time | Envelope tool | Smoothing filters |
| 26 | Mon 07 Dec | `lessons/lesson26_compressor_limiter.ipynb` | Compressors and limiters | Compressor, Limiter | Nonlinear systems |
| 27 | Tue 08 Dec | `lessons/lesson27_gate_silence.ipynb` | Noise gate and silence trimming | Noise Gate, Truncate Silence | Short-time energy, zero-crossing rate |
| 28 | Wed 09 Dec | `lessons/lesson28_noise_reduction.ipynb` | Noise reduction | Noise Reduction (Get Noise Profile) | Spectral subtraction, Wiener filter |
| 29 | Thu 10 Dec | `lessons/lesson29_hum_clicks.ipynb` | Hum and click removal | Notch Filter, Click Removal | Notch design, median filtering |
| 30 | Fri 11 Dec | `lessons/lesson30_speed_tempo.ipynb` | Speed vs tempo | Change Speed, Change Tempo | Multirate DSP, interpolation |
| 31 | Sat 12 Dec | `lessons/lesson31_pitch_shift.ipynb` | Pitch shifting | Change Pitch | Phase vocoder |
| 32 | Sun 13 Dec | `lessons/lesson32_stereo_vocals.ipynb` | Stereo and vocal removal | Vocal Reduction and Isolation | Phase cancellation |
| 33 | Mon 14 Dec | `lessons/lesson33_review_effects.ipynb` | Review: effects | (none) | Review |
| 34 | Tue 15 Dec | `lessons/lesson34_pitch_detection.ipynb` | Pitch detection | Plot Spectrum | Autocorrelation |
| 35 | Wed 16 Dec | `lessons/lesson35_source_filter.ipynb` | The source-filter model | (none) | Resonators, all-pole filters |
| 36 | Thu 17 Dec | `lessons/lesson36_lpc_formants.ipynb` | Linear prediction and formants | (none) | Linear prediction |
| 37 | Fri 18 Dec | `lessons/lesson37_mel_mfcc.ipynb` | Mel scale and MFCCs | Spectrogram view (Mel scale) | Filter banks, DCT |
| 38 | Sat 19 Dec | `lessons/lesson38_indic_speech.ipynb` | Malayalam and Hindi in the spectrogram | Record, spectrogram view, Label Tracks | Speech analysis |
| 39 | Sun 20 Dec | `lessons/lesson39_asr_frontend.ipynb` | The speech-to-text front end | Resample, Export | Feature extraction |
| 40 | Mon 21 Dec | `lessons/lesson40_onsets_beats.ipynb` | Onsets and beats | Beat Finder, Label Sounds | Novelty functions, peak picking |
| 41 | Tue 22 Dec | `lessons/lesson41_chroma_key.ipynb` | Chroma and key | Plot Spectrum (log frequency) | Constant-Q transform |
| 42 | Wed 23 Dec | `lessons/lesson42_realtime.ipynb` | Real-time DSP | Audio Settings (buffer length) | Frame-based processing |
| 43 | Thu 24 Dec | `lessons/lesson43_mini_audacity_build.ipynb` | Capstone, part 1: an effects chain | Macros | Systems in cascade |
| 44 | Fri 25 Dec | `lessons/lesson44_mini_audacity_compare.ipynb` | Capstone, part 2: me vs Audacity | Macros | Review |

### Day 1 (Thu 12 Nov 2026): Refresher: sampling, spectrum and timbre
- **Notebook:** `lesson1_sampling.ipynb`
- **Builds:** Re-run Lesson 1 (the trumpet clip as samples, waveform, FFT and spectrogram; harmonics and timbre). Then read the 'To tighten later' notes on the Obsidian Lesson 1 page; Days 5, 9, 10 and 34 deal with them.
- **Audacity:** Open any song, select a few seconds, then Analyze > Plot Spectrum
- **B.Tech DSP topic:** Sampling theorem, Fourier transform
- **How AI uses this:** Every speech and music AI starts here: sound turned into samples, then the samples turned into frequencies.
- **Blog post:** What is sound to a computer?
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 3: ADC and DAC (https://www.dspguide.com/ch3.htm)
    - The Scientist and Engineer's Guide to DSP, ch. 8: The Discrete Fourier Transform (https://www.dspguide.com/ch8.htm)

### Day 2 (Fri 13 Nov 2026): Refresher: vowel formants
- **Notebook:** `lesson2_vowelsound_comparison.ipynb`
- **Builds:** Re-run Lesson 2 (the vowels a, i and u built from two formant tones and compared as spectrograms). Day 35 rebuilds them the way a real voice makes them.
- **Audacity:** Record yourself saying a, i and u, then switch the track to Spectrogram view
- **B.Tech DSP topic:** Resonance
- **How AI uses this:** Speech recognisers tell vowels apart from the same formant patterns, which they learn from spectrograms.
- **Blog post:** How do we tell 'ee' from 'oo'?
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: acoustic phonetics: vowels and formants

### Day 3 (Sat 14 Nov 2026): Levels: peak, RMS and dBFS
- **Notebook:** `lessons/lesson03_levels.ipynb`
- **Builds:** Peak, RMS and crest factor in dBFS; Amplify and clipping; Normalize with DC-offset removal; equal peaks vs equal loudness
- **Audacity:** Amplify, Normalize, Loudness Normalization
- **B.Tech DSP topic:** Signal energy and power
- **How AI uses this:** Audio is brought to a similar level before it is used to train or run a speech model, so loud and quiet recordings look alike to the model.
- **Blog post:** How loud is loud? Normalize vs Amplify
- **References:**
    - J. O. Smith, Mathematics of the DFT: Decibels (https://ccrma.stanford.edu/~jos/mdft/Decibels.html)
    - The Scientist and Engineer's Guide to DSP, ch. 2: Statistics, Probability and Noise (https://www.dspguide.com/ch2.htm)
    - Audacity Manual (manual.audacityteam.org): Amplify, Normalize, Loudness Normalization

### Day 4 (Sun 15 Nov 2026): Bit depth and quantisation
- **Notebook:** `lessons/lesson04_bit_depth.ipynb`
- **Builds:** Requantise a clip to 16, 8 and 4 bits; measure quantisation noise and SNR; add dither and hear the difference
- **Audacity:** Sample format, dither setting
- **B.Tech DSP topic:** Quantisation, SNR = 6.02N + 1.76 dB
- **How AI uses this:** Models work on decimal numbers, and datasets are usually stored as 16-bit WAV files. Shrinking AI models to 8-bit numbers (quantisation) is the same rounding idea.
- **Blog post:** Why 16 bits is enough
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 3: ADC and DAC (https://www.dspguide.com/ch3.htm)
    - Proakis & Manolakis, Digital Signal Processing: sampling and quantisation of analog signals
    - Audacity Manual (manual.audacityteam.org): Quality preferences (dither)

### Day 5 (Mon 16 Nov 2026): Aliasing, properly
- **Notebook:** `lessons/lesson05_aliasing.ipynb`
- **Builds:** A chirp sweeping to 10 kHz, downsampled with and without an anti-aliasing filter; builds on Lesson 1's Nyquist note and corrects its description of aliasing
- **Audacity:** Generate > Chirp, Resample
- **B.Tech DSP topic:** Sampling theorem, reconstruction
- **How AI uses this:** Speech models usually expect 16,000 samples a second. Audio is resampled to that rate, with an anti-aliasing filter, before a model hears it.
- **Blog post:** The chirp that turns around: aliasing
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 3: ADC and DAC (https://www.dspguide.com/ch3.htm)
    - Oppenheim & Schafer, Discrete-Time Signal Processing: sampling of continuous-time signals
    - Audacity Manual (manual.audacityteam.org): Chirp, Resample

### Day 6 (Tue 17 Nov 2026): Waveforms as sums of sines
- **Notebook:** `lessons/lesson06_waveforms.ipynb`
- **Builds:** Square, sawtooth and triangle waves built by adding harmonics one at a time; Gibbs ringing; links back to Lesson 1's harmonics and timbre
- **Audacity:** Generate > Tone
- **B.Tech DSP topic:** Fourier series
- **How AI uses this:** Made-up tones are used to test audio models, because you know exactly which frequencies went in.
- **Blog post:** Every sound is a recipe of simple waves
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 13: Continuous Signal Processing (Fourier series) (https://www.dspguide.com/ch13.htm)
    - Audacity Manual (manual.audacityteam.org): Tone

### Day 7 (Wed 18 Nov 2026): Noise and its colours
- **Notebook:** `lessons/lesson07_noise_colours.ipynb`
- **Builds:** White, pink and brown noise made and compared by ear and by spectrum; mixing noise into a clip at a chosen signal-to-noise ratio
- **Audacity:** Generate > Noise
- **B.Tech DSP topic:** Random signals, power spectral density
- **How AI uses this:** Noise is mixed into training clips at chosen signal-to-noise ratios so speech models cope with real, messy sound.
- **Blog post:** Why is some noise 'pink'?
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 2: Statistics, Probability and Noise (https://www.dspguide.com/ch2.htm)
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Audacity Manual (manual.audacityteam.org): Noise

### Day 8 (Thu 19 Nov 2026): The DFT by hand
- **Notebook:** `lessons/lesson08_dft_by_hand.ipynb`
- **Builds:** The DFT written from its formula and tried on 8- and 64-sample signals; what each frequency bin means
- **Audacity:** Plot Spectrum
- **B.Tech DSP topic:** DFT
- **How AI uses this:** Most audio AI does not look at raw samples. It looks at frequencies, worked out with the Fourier transform.
- **Blog post:** Finding the notes inside a sound, by hand
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 8: The Discrete Fourier Transform (https://www.dspguide.com/ch8.htm)
    - J. O. Smith, Mathematics of the DFT (https://ccrma.stanford.edu/~jos/mdft/)

### Day 9 (Fri 20 Nov 2026): The FFT and frequency bins
- **Notebook:** `lessons/lesson09_fft_bins.ipynb`
- **Builds:** np.fft timed against the hand-written DFT; bin spacing fs/N; rfft and rfftfreq, fixing Lesson 1's frequency axis
- **Audacity:** Plot Spectrum (Size)
- **B.Tech DSP topic:** Radix-2 FFT, O(N log N)
- **How AI uses this:** The FFT makes it cheap enough to turn every second of audio into hundreds of spectra for a model to read.
- **Blog post:** Why the FFT is so fast
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 12: The Fast Fourier Transform (https://www.dspguide.com/ch12.htm)
    - Müller, FMP notebooks, chapter 2: Fourier analysis of signals (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C2/C2.html)

### Day 10 (Sat 21 Nov 2026): Windowing and spectral leakage
- **Notebook:** `lessons/lesson10_windows.ipynb`
- **Builds:** Two close tones analysed with rectangular, Hann, Hamming and Blackman windows; adds the missing window to Lesson 1's FFT
- **Audacity:** Plot Spectrum (Function)
- **B.Tech DSP topic:** Windowing
- **How AI uses this:** Every spectrogram a speech model sees is cut into windowed slices, usually with a Hann window.
- **Blog post:** Why Plot Spectrum asks you to pick a window
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 9: Applications of the DFT (https://www.dspguide.com/ch9.htm)
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - SciPy docs: scipy.signal.get_window (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html)

### Day 11 (Sun 22 Nov 2026): Spectrograms and the STFT
- **Notebook:** `lessons/lesson11_spectrograms.ipynb`
- **Builds:** STFT window and hop sizes on speech; linear, log and mel axes; the spectrograms from Lessons 1 and 2 revisited
- **Audacity:** Spectrogram view settings
- **B.Tech DSP topic:** STFT, time-frequency trade-off
- **How AI uses this:** Many audio models treat the spectrogram like a picture and use image-style neural networks on it.
- **Blog post:** Pictures of sound: spectrograms
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 9: Applications of the DFT (https://www.dspguide.com/ch9.htm)
    - Müller, FMP notebooks, chapter 2: Fourier analysis of signals (STFT) (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C2/C2.html)
    - Audacity Manual (manual.audacityteam.org): Spectrogram View, Spectrograms Preferences

### Day 12 (Mon 23 Nov 2026): Review: seeing sound
- **Notebook:** `lessons/lesson12_review_seeing_sound.ipynb`
- **Builds:** Short exercises on Days 3 to 11 with worked answers: levels, bits, aliasing, sums of sines, the DFT, windows, spectrograms
- **Audacity:** (none)
- **B.Tech DSP topic:** Review
- **How AI uses this:** Recap: the spectrogram is the picture most audio AI looks at.
- **Blog post:** Review: how a computer sees sound
- **References:**
    - The earlier lessons in this repo

### Day 13 (Tue 24 Nov 2026): Impulse response
- **Notebook:** `lessons/lesson13_impulse_response.ipynb`
- **Builds:** A click or clap as a system's impulse response; checking linearity and time-invariance with numbers
- **Audacity:** Record, trim
- **B.Tech DSP topic:** LTI systems
- **How AI uses this:** Recordings of real rooms' impulse responses are collected into datasets used to train speech models.
- **Blog post:** A clap tells you everything about a room
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 5: Linear Systems (https://www.dspguide.com/ch5.htm)
    - Oppenheim & Schafer, Discrete-Time Signal Processing: linear time-invariant systems

### Day 14 (Wed 25 Nov 2026): Convolution
- **Notebook:** `lessons/lesson14_convolution.ipynb`
- **Builds:** The convolution sum written by hand on short signals, checked against np.convolve; smoothing as convolution
- **Audacity:** (none)
- **B.Tech DSP topic:** Convolution sum
- **How AI uses this:** Convolution is also the main operation inside convolutional neural networks (CNNs). It is the same sliding multiply-and-add.
- **Blog post:** Convolution: the sliding multiply-and-add
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 6: Convolution (https://www.dspguide.com/ch6.htm)
    - Oppenheim & Schafer, Discrete-Time Signal Processing: linear time-invariant systems

### Day 15 (Thu 26 Nov 2026): Convolution reverb
- **Notebook:** `lessons/lesson15_convolution_reverb.ipynb`
- **Builds:** A dry voice convolved with a room impulse response; direct vs FFT convolution speed; overlap-add
- **Audacity:** Effect > Reverb
- **B.Tech DSP topic:** Linear vs circular convolution, overlap-add
- **How AI uses this:** Adding room echoes (convolving with room impulse responses) to training clips makes speech recognition work in real rooms, not just studios.
- **Blog post:** Fake a cathedral with one line of code
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 18: FFT Convolution (https://www.dspguide.com/ch18.htm)
    - J. O. Smith, Physical Audio Signal Processing (https://ccrma.stanford.edu/~jos/pasp/)
    - Audacity Manual (manual.audacityteam.org): Reverb

### Day 16 (Fri 27 Nov 2026): Echo and comb filters
- **Notebook:** `lessons/lesson16_echo_comb.ipynb`
- **Builds:** Feedforward and feedback comb filters from their difference equations; their notches heard and plotted
- **Audacity:** Effect > Echo
- **B.Tech DSP topic:** Difference equations, FIR vs IIR
- **How AI uses this:** Phones and video calls cancel echo before your voice reaches a speech recogniser.
- **Blog post:** Echo is a filter
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 19: Recursive Filters (https://www.dspguide.com/ch19.htm)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - Audacity Manual (manual.audacityteam.org): Echo

### Day 17 (Sat 28 Nov 2026): The z-transform
- **Notebook:** `lessons/lesson17_z_transform.ipynb`
- **Builds:** From a difference equation to a transfer function; frequency response with freqz
- **Audacity:** (none)
- **B.Tech DSP topic:** Z-transform, transfer functions
- **How AI uses this:** A filter is described by a few numbers (coefficients), much as a neural network is described by its weights. Designing a filter is a hand-made version of training one.
- **Blog post:** A filter described in a handful of numbers
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 33: The z-Transform (https://www.dspguide.com/ch33.htm)
    - SciPy docs: scipy.signal.freqz (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html)

### Day 18 (Sun 29 Nov 2026): Poles, zeros and stability
- **Notebook:** `lessons/lesson18_poles_zeros.ipynb`
- **Builds:** Pole-zero plots; the unit circle and stability; move a pole and listen to the result
- **Audacity:** (none)
- **B.Tech DSP topic:** Poles, zeros, stability
- **How AI uses this:** Recurrent neural networks feed outputs back in, like IIR filters. Feedback that grows without limit is the filter version of 'exploding gradients'.
- **Blog post:** Poles, zeros and the unit circle, by ear
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 33: The z-Transform (https://www.dspguide.com/ch33.htm)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)

### Day 19 (Mon 30 Nov 2026): FIR filter design
- **Notebook:** `lessons/lesson19_fir_design.ipynb`
- **Builds:** A windowed-sinc low-pass by hand, then with firwin; linear phase; high-pass by spectral inversion
- **Audacity:** Low-Pass and High-Pass Filter
- **B.Tech DSP topic:** FIR design by windowing
- **How AI uses this:** A 1-D convolution layer in a neural network is an FIR filter whose numbers are learned instead of designed.
- **Blog post:** Designing a low-pass filter
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 16: Windowed-Sinc Filters (https://www.dspguide.com/ch16.htm)
    - SciPy docs: scipy.signal.firwin (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html)
    - Audacity Manual (manual.audacityteam.org): Low-Pass Filter, High-Pass Filter

### Day 20 (Tue 01 Dec 2026): IIR filter design
- **Notebook:** `lessons/lesson20_iir_design.ipynb`
- **Builds:** Butterworth, Chebyshev and elliptic filters compared; their phase; filtfilt for zero phase
- **Audacity:** (none)
- **B.Tech DSP topic:** Analog prototypes, bilinear transform
- **How AI uses this:** Newer sequence models (state-space models such as S4 and Mamba) are related to IIR filters: they carry a state forward from sample to sample.
- **Blog post:** Flat or sharp? Butterworth vs Chebyshev
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 19: Recursive Filters (https://www.dspguide.com/ch19.htm)
    - The Scientist and Engineer's Guide to DSP, ch. 20: Chebyshev Filters (https://www.dspguide.com/ch20.htm)
    - SciPy docs: scipy.signal.butter (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html)

### Day 21 (Wed 02 Dec 2026): Shelving filters and biquads
- **Notebook:** `lessons/lesson21_shelving_biquads.ipynb`
- **Builds:** RBJ shelving and peaking biquads; a bass and treble control
- **Audacity:** Bass and Treble
- **B.Tech DSP topic:** Second-order sections
- **How AI uses this:** Random bass and treble changes are used to augment training audio, so models cope with different microphones and speakers.
- **Blog post:** How the bass and treble knobs work
- **References:**
    - Audio EQ Cookbook (Bristow-Johnson), W3C note (https://www.w3.org/TR/audio-eq-cookbook/)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - Audacity Manual (manual.audacityteam.org): Bass and Treble

### Day 22 (Thu 03 Dec 2026): A graphic equaliser
- **Notebook:** `lessons/lesson22_equaliser.ipynb`
- **Builds:** A 10-band graphic EQ from peaking biquads in cascade, applied to a song
- **Audacity:** Graphic EQ, Filter Curve EQ
- **B.Tech DSP topic:** Biquads in cascade
- **How AI uses this:** SpecAugment, a common training trick for speech models, hides bands of frequencies, a bit like an extreme equaliser.
- **Blog post:** Build your own graphic EQ
- **References:**
    - Audio EQ Cookbook (Bristow-Johnson), W3C note (https://www.w3.org/TR/audio-eq-cookbook/)
    - Audacity Manual (manual.audacityteam.org): Graphic EQ, Filter Curve EQ

### Day 23 (Fri 04 Dec 2026): Review: systems and filters
- **Notebook:** `lessons/lesson23_review_filters.ipynb`
- **Builds:** Short exercises on Days 13 to 22 with worked answers: impulse response, convolution, z-transform, FIR and IIR filters, EQ
- **Audacity:** (none)
- **B.Tech DSP topic:** Review
- **How AI uses this:** Recap: filters and convolution are the building blocks that neural networks learn for themselves.
- **Blog post:** Review: filters are everywhere
- **References:**
    - The earlier lessons in this repo

### Day 24 (Sat 05 Dec 2026): Fades and envelopes
- **Notebook:** `lessons/lesson24_fades_envelopes.ipynb`
- **Builds:** Linear, exponential and S-curve fades; an ADSR envelope; ducking music under a voice
- **Audacity:** Fade In/Out, Envelope tool, Auto Duck
- **B.Tech DSP topic:** Amplitude modulation
- **How AI uses this:** Clips cut out of recordings for AI training get short fades so the cuts do not add clicks the model might learn.
- **Blog post:** Fades are multiplication
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: amplitude modulation and envelopes
    - Audacity Manual (manual.audacityteam.org): Fade In, Fade Out, Envelope Tool, Auto Duck

### Day 25 (Sun 06 Dec 2026): Following loudness over time
- **Notebook:** `lessons/lesson25_envelope_follower.ipynb`
- **Builds:** An envelope follower: rectify and smooth; attack and release times
- **Audacity:** Envelope tool
- **B.Tech DSP topic:** Smoothing filters
- **How AI uses this:** Loudness curves are used to find speech, music and silence in long recordings before AI processes them.
- **Blog post:** Following the loudness of a sound
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: dynamics processing
    - The Scientist and Engineer's Guide to DSP, ch. 22: Audio Processing (https://www.dspguide.com/ch22.htm)

### Day 26 (Mon 07 Dec 2026): Compressors and limiters
- **Notebook:** `lessons/lesson26_compressor_limiter.ipynb`
- **Builds:** Threshold, ratio, attack and release on top of Day 25's envelope follower; a brick-wall limiter
- **Audacity:** Compressor, Limiter
- **B.Tech DSP topic:** Nonlinear systems
- **How AI uses this:** The log in a log-mel spectrogram squashes loud and quiet parts together, much as a compressor does.
- **Blog post:** How a compressor decides what's too loud
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: dynamics processing
    - Audacity Manual (manual.audacityteam.org): Compressor, Limiter

### Day 27 (Tue 08 Dec 2026): Noise gate and silence trimming
- **Notebook:** `lessons/lesson27_gate_silence.ipynb`
- **Builds:** Short-time energy and zero-crossing rate; energy-based voice detection; a noise gate; trimming long silences
- **Audacity:** Noise Gate, Truncate Silence
- **B.Tech DSP topic:** Short-time energy, zero-crossing rate
- **How AI uses this:** Voice activity detection removes silence before speech recognition, which saves time and avoids made-up words in the silence.
- **Blog post:** Cutting the silence out of a podcast
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: short-time energy and zero-crossing rate
    - Audacity Manual (manual.audacityteam.org): Noise Gate, Truncate Silence

### Day 28 (Wed 09 Dec 2026): Noise reduction
- **Notebook:** `lessons/lesson28_noise_reduction.ipynb`
- **Builds:** A noise profile and spectral subtraction; where 'musical noise' comes from; a simple Wiener-style gain
- **Audacity:** Noise Reduction (Get Noise Profile)
- **B.Tech DSP topic:** Spectral subtraction, Wiener filter
- **How AI uses this:** AI speech enhancement learns a 'mask' over the spectrogram, a learned version of the noise-reduction gain.
- **Blog post:** Inside Audacity's Noise Reduction
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 17: Custom Filters (optimal filters) (https://www.dspguide.com/ch17.htm)
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Audacity Manual (manual.audacityteam.org): Noise Reduction

### Day 29 (Thu 10 Dec 2026): Hum and click removal
- **Notebook:** `lessons/lesson29_hum_clicks.ipynb`
- **Builds:** A notch comb for 50 Hz mains hum and its harmonics; a median filter for clicks
- **Audacity:** Notch Filter, Click Removal
- **B.Tech DSP topic:** Notch design, median filtering
- **How AI uses this:** Clean training data matters: a steady 50 Hz hum can become a pattern a model wrongly relies on.
- **Blog post:** Removing the 50 Hz hum Indian mains leave behind
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 19: Recursive Filters (band-reject) (https://www.dspguide.com/ch19.htm)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - Audacity Manual (manual.audacityteam.org): Notch Filter, Click Removal

### Day 30 (Fri 11 Dec 2026): Speed vs tempo
- **Notebook:** `lessons/lesson30_speed_tempo.ipynb`
- **Builds:** Resampling (speed changes pitch too) vs time stretching (tempo only) on the same clip
- **Audacity:** Change Speed, Change Tempo
- **B.Tech DSP topic:** Multirate DSP, interpolation
- **How AI uses this:** Speech recognisers are trained on copies of clips played slightly faster and slower (speed perturbation) so they handle different speakers.
- **Blog post:** Faster, but not squeakier
- **References:**
    - Proakis & Manolakis, Digital Signal Processing: multirate digital signal processing
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Audacity Manual (manual.audacityteam.org): Change Speed, Change Tempo

### Day 31 (Sat 12 Dec 2026): Pitch shifting
- **Notebook:** `lessons/lesson31_pitch_shift.ipynb`
- **Builds:** A phase-vocoder pitch shift: time stretch plus resampling
- **Audacity:** Change Pitch
- **B.Tech DSP topic:** Phase vocoder
- **How AI uses this:** Pitch-shifted copies are another common training augmentation, and voice-conversion models change pitch to sound like another speaker.
- **Blog post:** Changing pitch without changing speed
- **References:**
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Zölzer (ed.), DAFX: Digital Audio Effects: pitch shifting and time stretching
    - Audacity Manual (manual.audacityteam.org): Change Pitch

### Day 32 (Sun 13 Dec 2026): Stereo and vocal removal
- **Notebook:** `lessons/lesson32_stereo_vocals.ipynb`
- **Builds:** Mid/side encoding; centre-channel cancellation; pan laws
- **Audacity:** Vocal Reduction and Isolation
- **B.Tech DSP topic:** Phase cancellation
- **How AI uses this:** AI source-separation models (such as Demucs) pull vocals out of songs by learning masks, doing much better than simple cancellation.
- **Blog post:** Why vocal removal only half works
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: spatial effects
    - Audacity Manual (manual.audacityteam.org): Vocal Reduction and Isolation

### Day 33 (Mon 14 Dec 2026): Review: effects
- **Notebook:** `lessons/lesson33_review_effects.ipynb`
- **Builds:** Short exercises on Days 24 to 32 with worked answers: fades, dynamics, gates, noise reduction, hum, speed and pitch, stereo
- **Audacity:** (none)
- **B.Tech DSP topic:** Review
- **How AI uses this:** Recap: much of audio AI is a learned version of these effects: masks, gains and filters.
- **Blog post:** Review: the effects rack
- **References:**
    - The earlier lessons in this repo

### Day 34 (Tue 15 Dec 2026): Pitch detection
- **Notebook:** `lessons/lesson34_pitch_detection.ipynb`
- **Builds:** Autocorrelation and pYIN on the trumpet; settles Lesson 1's 1,000 Hz vs 600 Hz question
- **Audacity:** Plot Spectrum
- **B.Tech DSP topic:** Autocorrelation
- **How AI uses this:** Pitch tracking is used to label singing and speech data, and pitch helps models hear emotion and the tones of a language.
- **Blog post:** Finding the pitch when the loudest note lies
- **References:**
    - Müller, FMP notebooks, chapter 8: fundamental frequency estimation (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C8/C8.html)
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: pitch period estimation
    - librosa documentation: librosa.pyin

### Day 35 (Wed 16 Dec 2026): The source-filter model
- **Notebook:** `lessons/lesson35_source_filter.ipynb`
- **Builds:** Lesson 2's vowels rebuilt as a buzzing pulse train through formant resonators, and compared with the two-tone versions
- **Audacity:** (none)
- **B.Tech DSP topic:** Resonators, all-pole filters
- **How AI uses this:** Text-to-speech systems and neural vocoders build on this source-filter idea.
- **Blog post:** Making vowels the way a throat does
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 22: Audio Processing (speech synthesis) (https://www.dspguide.com/ch22.htm)
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: models for speech production

### Day 36 (Thu 17 Dec 2026): Linear prediction and formants
- **Notebook:** `lessons/lesson36_lpc_formants.ipynb`
- **Builds:** LPC to estimate formants back from a vowel; compared with Lesson 2's formant values
- **Audacity:** (none)
- **B.Tech DSP topic:** Linear prediction
- **How AI uses this:** LPC was the heart of older speech codecs and still sits inside some neural vocoders, such as LPCNet.
- **Blog post:** Reading the mouth's shape from sound
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: linear predictive analysis
    - librosa documentation: librosa.lpc

### Day 37 (Fri 18 Dec 2026): Mel scale and MFCCs
- **Notebook:** `lessons/lesson37_mel_mfcc.ipynb`
- **Builds:** A mel filterbank by hand; log-mel spectrograms; MFCCs via the DCT
- **Audacity:** Spectrogram view (Mel scale)
- **B.Tech DSP topic:** Filter banks, DCT
- **How AI uses this:** The log-mel spectrogram is the input to speech recognisers such as Whisper. MFCCs powered earlier speech recognition.
- **Blog post:** The mel scale: how speech models hear
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: speech representations
    - Müller, FMP notebooks, chapter 3: log-frequency spectrogram (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C3/C3.html)
    - librosa documentation: librosa.feature.melspectrogram, librosa.feature.mfcc

### Day 38 (Sat 19 Dec 2026): Malayalam and Hindi in the spectrogram
- **Notebook:** `lessons/lesson38_indic_speech.ipynb`
- **Builds:** My recordings: vowel length, retroflex vs dental consonants, aspiration and voice onset time
- **Audacity:** Record, spectrogram view, Label Tracks
- **B.Tech DSP topic:** Speech analysis
- **How AI uses this:** Indian-language speech AI needs Indian training data: sounds such as retroflex consonants look different in the spectrogram from English ones.
- **Blog post:** What Malayalam and Hindi look like
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: acoustic phonetics
    - Audacity Manual (manual.audacityteam.org): Label Tracks

### Day 39 (Sun 20 Dec 2026): The speech-to-text front end
- **Notebook:** `lessons/lesson39_asr_frontend.ipynb`
- **Builds:** Resample to 16 kHz and build the 80-band log-mel input speech models use; compare with the sarvam_poc experiments
- **Audacity:** Resample, Export
- **B.Tech DSP topic:** Feature extraction
- **How AI uses this:** This is exactly what a speech-to-text model receives: 16 kHz audio turned into an 80-band log-mel spectrogram.
- **Blog post:** What a speech-to-text model sees before it hears
- **References:**
    - librosa documentation: librosa.feature.melspectrogram
    - Radford et al., Robust Speech Recognition via Large-Scale Weak Supervision (the Whisper paper), 2022
    - Audacity Manual (manual.audacityteam.org): Resample, Export

### Day 40 (Mon 21 Dec 2026): Onsets and beats
- **Notebook:** `lessons/lesson40_onsets_beats.ipynb`
- **Builds:** Spectral-flux onset detection; tempo estimation; beat tracking on a song
- **Audacity:** Beat Finder, Label Sounds
- **B.Tech DSP topic:** Novelty functions, peak picking
- **How AI uses this:** Music apps and AI music taggers find beats and onsets to line up, tag and recommend songs.
- **Blog post:** Finding the beat
- **References:**
    - Müller, FMP notebooks, chapter 6: tempo and beat tracking (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C6/C6.html)
    - librosa documentation: librosa.onset.onset_strength, librosa.beat.beat_track
    - Audacity Manual (manual.audacityteam.org): Beat Finder, Label Sounds

### Day 41 (Tue 22 Dec 2026): Chroma and key
- **Notebook:** `lessons/lesson41_chroma_key.ipynb`
- **Builds:** The constant-Q transform; chroma features; key estimation on a Carnatic or film song
- **Audacity:** Plot Spectrum (log frequency)
- **B.Tech DSP topic:** Constant-Q transform
- **How AI uses this:** Chroma features help music AI recognise songs, cover versions and keys.
- **Blog post:** Twelve notes in a spectrogram
- **References:**
    - Müller, FMP notebooks, chapter 3: music synchronization (chroma features) (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C3/C3.html)
    - librosa documentation: librosa.feature.chroma_cqt

### Day 42 (Wed 23 Dec 2026): Real-time DSP
- **Notebook:** `lessons/lesson42_realtime.ipynb`
- **Builds:** Block processing with sounddevice; buffer size vs latency; a live filter that carries its state between blocks
- **Audacity:** Audio Settings (buffer length)
- **B.Tech DSP topic:** Frame-based processing
- **How AI uses this:** Voice assistants and live captions process audio in small blocks, with a strict time limit for each one.
- **Blog post:** Real-time sound: latency and buffers
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 28: Digital Signal Processors (https://www.dspguide.com/ch28.htm)
    - python-sounddevice documentation (https://python-sounddevice.readthedocs.io/)
    - Audacity Manual (manual.audacityteam.org): Audio Settings preferences

### Day 43 (Thu 24 Dec 2026): Capstone, part 1: an effects chain
- **Notebook:** `lessons/lesson43_mini_audacity_build.ipynb`
- **Builds:** My own normalise, EQ, noise reduction and compressor from earlier lessons, chained into one function
- **Audacity:** Macros
- **B.Tech DSP topic:** Systems in cascade
- **How AI uses this:** Every audio AI system has a clean-up chain like this before the model: level, filter, denoise, then features.
- **Blog post:** Building my own effects rack
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: effect chains
    - The earlier lessons in this repo

### Day 44 (Fri 25 Dec 2026): Capstone, part 2: me vs Audacity
- **Notebook:** `lessons/lesson44_mini_audacity_compare.ipynb`
- **Builds:** The chain run on a voice memo and compared with Audacity's own effects; a look back at all 44 days
- **Audacity:** Macros
- **B.Tech DSP topic:** Review
- **How AI uses this:** The same clean-up chain sits in front of most audio AI. The next step is to put a model after it.
- **Blog post:** 44 days of DSP: what I learned
- **References:**
    - The earlier lessons in this repo
    - Audacity Manual (manual.audacityteam.org): Macros
