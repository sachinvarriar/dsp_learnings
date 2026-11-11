# DSP Lab: 30-day plan

One notebook a day from Thu 12 Nov to Fri 11 Dec 2026, with a blog post written from it. Each day takes one Audacity feature, explains the B.Tech DSP idea underneath it, and rebuilds it in Python. Lessons 1 and 2 (in the repo root) came first, so Day 1 is Lesson 3.

## Notebook conventions
- File: `lessons/<slug>.ipynb` (slug in the table below). Python 3.11, dependencies in `requirements-lab.txt` only.
- Order of cells: title and date; what you will learn (3-5 bullets); references; then short sections, each a markdown explanation followed by code; "Try it in Audacity"; exercises (2-3); summary.
- Make every step audible: `IPython.display.Audio(x, rate=sr, normalize=False)` so levels are heard as they are.
- Prefer synthetic signals and librosa's example clips (`librosa.ex(...)`). Never commit large audio; write any clips to `audio/` and keep them under 1 MB.
- Plain, friendly English for someone who did B.Tech DSP years ago. Define a term the first time it appears. No unexplained jargon.
- The notebook must run top to bottom without errors in under two minutes and be committed with its outputs.
- Also write `blog/dayNN.md`: a short outline (title, the question, 3-5 points, the one figure to use) for Sachin to write the post from. Not a finished post.

## Days

| Day | Date | Notebook | Topic | Audacity | B.Tech DSP topic |
|---|---|---|---|---|---|
| 1 | Thu 12 Nov | `lessons/lesson03_levels.ipynb` | Levels: peak, RMS and dBFS | Amplify, Normalize, waveform (dB) view | Signal energy and power |
| 2 | Fri 13 Nov | `lessons/lesson04_bit_depth.ipynb` | Bit depth and quantisation | Sample format, dither setting | Quantisation, SNR = 6.02N + 1.76 dB |
| 3 | Sat 14 Nov | `lessons/lesson05_aliasing.ipynb` | Aliasing, properly | Generate > Chirp, Resample | Sampling theorem, reconstruction |
| 4 | Sun 15 Nov | `lessons/lesson06_waveforms.ipynb` | Waveforms as sums of sines | Generate > Tone, Noise | Fourier series |
| 5 | Mon 16 Nov | `lessons/lesson07_dft_by_hand.ipynb` | The DFT by hand | Plot Spectrum (Size) | DFT, radix-2 FFT, O(N log N) |
| 6 | Tue 17 Nov | `lessons/lesson08_windows.ipynb` | Windowing and spectral leakage | Plot Spectrum (Function) | Windowing |
| 7 | Wed 18 Nov | `lessons/lesson09_spectrograms.ipynb` | Spectrograms and the STFT | Spectrogram view settings | STFT, time-frequency uncertainty |
| 8 | Thu 19 Nov | `lessons/lesson10_impulse_response.ipynb` | Impulse response and convolution | Record, trim | LTI systems, convolution sum |
| 9 | Fri 20 Nov | `lessons/lesson11_convolution_reverb.ipynb` | Convolution reverb | Effect > Reverb | Linear vs circular convolution, overlap-add |
| 10 | Sat 21 Nov | `lessons/lesson12_echo_comb.ipynb` | Echo and comb filters | Effect > Echo | Difference equations, FIR vs IIR |
| 11 | Sun 22 Nov | `lessons/lesson13_z_transform.ipynb` | Z-transform, poles and zeros | (none) | Z-transform, region of convergence, stability |
| 12 | Mon 23 Nov | `lessons/lesson14_fir_design.ipynb` | FIR filter design | Low-Pass and High-Pass Filter | FIR design by windowing |
| 13 | Tue 24 Nov | `lessons/lesson15_iir_design.ipynb` | IIR filter design | Bass and Treble | Analog prototypes, bilinear transform |
| 14 | Wed 25 Nov | `lessons/lesson16_equaliser.ipynb` | A graphic equaliser | Graphic EQ, Filter Curve EQ | Biquads, second-order sections |
| 15 | Thu 26 Nov | `lessons/lesson17_fades_envelopes.ipynb` | Fades and envelopes | Fade In/Out, Envelope tool, Auto Duck | Amplitude modulation |
| 16 | Fri 27 Nov | `lessons/lesson18_compressor.ipynb` | Compressors and limiters | Compressor, Limiter | Nonlinear systems, smoothing filters |
| 17 | Sat 28 Nov | `lessons/lesson19_gate_silence.ipynb` | Noise gate and silence trimming | Noise Gate, Truncate Silence | Short-time energy, zero-crossing rate |
| 18 | Sun 29 Nov | `lessons/lesson20_noise_reduction.ipynb` | Noise reduction | Noise Reduction (Get Noise Profile) | Spectral subtraction, Wiener filter |
| 19 | Mon 30 Nov | `lessons/lesson21_hum_clicks.ipynb` | Hum and click removal | Notch Filter, Click Removal | Notch design, median filtering |
| 20 | Tue 01 Dec | `lessons/lesson22_speed_tempo_pitch.ipynb` | Speed, tempo and pitch | Change Speed, Change Tempo, Change Pitch | Multirate DSP, interpolation, phase vocoder |
| 21 | Wed 02 Dec | `lessons/lesson23_stereo_vocals.ipynb` | Stereo and vocal removal | Vocal Reduction and Isolation | Phase cancellation |
| 22 | Thu 03 Dec | `lessons/lesson24_pitch_detection.ipynb` | Pitch detection | Plot Spectrum | Autocorrelation |
| 23 | Fri 04 Dec | `lessons/lesson25_source_filter.ipynb` | The source-filter model | (none) | All-pole models, linear prediction |
| 24 | Sat 05 Dec | `lessons/lesson26_mel_mfcc.ipynb` | Mel scale and MFCCs | Spectrogram view (Mel scale) | Filter banks, DCT |
| 25 | Sun 06 Dec | `lessons/lesson27_indic_speech.ipynb` | Malayalam and Hindi in the spectrogram | Record, spectrogram view, Label Tracks | Speech analysis |
| 26 | Mon 07 Dec | `lessons/lesson28_asr_frontend.ipynb` | The speech-to-text front end | Resample, Export | Feature extraction |
| 27 | Tue 08 Dec | `lessons/lesson29_onsets_beats.ipynb` | Onsets and beats | Beat Finder, Label Sounds | Novelty functions, peak picking |
| 28 | Wed 09 Dec | `lessons/lesson30_chroma_key.ipynb` | Chroma and key | Plot Spectrum (log frequency) | Constant-Q transform |
| 29 | Thu 10 Dec | `lessons/lesson31_realtime.ipynb` | Real-time DSP | Real-time effect preview, Audio Settings (buffer length) | Frame-based processing |
| 30 | Fri 11 Dec | `lessons/lesson32_mini_audacity.ipynb` | Capstone: a mini Audacity | Macros | Systems in cascade |

### Day 1 (Thu 12 Nov 2026): Levels: peak, RMS and dBFS
- **Notebook:** `lessons/lesson03_levels.ipynb`
- **Builds:** Peak, RMS and crest factor in dBFS; Amplify with a gain in dB and what clipping sounds like; Normalize to -1 dBFS with DC-offset removal; why two clips with the same peak can differ in loudness
- **Audacity:** Amplify, Normalize, waveform (dB) view
- **B.Tech DSP topic:** Signal energy and power
- **Blog post:** Normalize vs Amplify: what Audacity's two loudness buttons really do
- **References:**
    - J. O. Smith, Mathematics of the DFT: Decibels (https://ccrma.stanford.edu/~jos/mdft/Decibels.html)
    - The Scientist and Engineer's Guide to DSP, ch. 2: Statistics, Probability and Noise (https://www.dspguide.com/ch2.htm)
    - Audacity Manual (manual.audacityteam.org): Amplify, Normalize, Loudness Normalization

### Day 2 (Fri 13 Nov 2026): Bit depth and quantisation
- **Notebook:** `lessons/lesson04_bit_depth.ipynb`
- **Builds:** Requantise a clip to 16, 8 and 4 bits; measure quantisation noise and SNR; add dither and hear the difference
- **Audacity:** Sample format, dither setting
- **B.Tech DSP topic:** Quantisation, SNR = 6.02N + 1.76 dB
- **Blog post:** Why 16 bits is enough: hearing quantisation noise
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 3: ADC and DAC (https://www.dspguide.com/ch3.htm)
    - Proakis & Manolakis, Digital Signal Processing: sampling and quantisation of analog signals
    - Audacity Manual (manual.audacityteam.org): Quality preferences (dither)

### Day 3 (Sat 14 Nov 2026): Aliasing, properly
- **Notebook:** `lessons/lesson05_aliasing.ipynb`
- **Builds:** A chirp sweeping to 10 kHz, downsampled with and without an anti-aliasing filter; hear and see the folded frequencies
- **Audacity:** Generate > Chirp, Resample
- **B.Tech DSP topic:** Sampling theorem, reconstruction
- **Blog post:** Aliasing you can hear: the chirp that turns around
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 3: ADC and DAC (https://www.dspguide.com/ch3.htm)
    - Oppenheim & Schafer, Discrete-Time Signal Processing: sampling of continuous-time signals
    - Audacity Manual (manual.audacityteam.org): Chirp, Resample

### Day 4 (Sun 15 Nov 2026): Waveforms as sums of sines
- **Notebook:** `lessons/lesson06_waveforms.ipynb`
- **Builds:** Square, sawtooth and triangle waves built from harmonic sums (Gibbs ringing included); white, pink and brown noise and their spectra
- **Audacity:** Generate > Tone, Noise
- **B.Tech DSP topic:** Fourier series
- **Blog post:** Every waveform is a recipe of sines
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 13: Continuous Signal Processing (Fourier series) (https://www.dspguide.com/ch13.htm)
    - The Scientist and Engineer's Guide to DSP, ch. 2: Statistics, Probability and Noise (https://www.dspguide.com/ch2.htm)
    - Audacity Manual (manual.audacityteam.org): Tone, Noise

### Day 5 (Mon 16 Nov 2026): The DFT by hand
- **Notebook:** `lessons/lesson07_dft_by_hand.ipynb`
- **Builds:** The DFT written from its formula, checked and timed against np.fft; bin spacing fs/N; rfft and rfftfreq, fixing Lesson 1's frequency axis
- **Audacity:** Plot Spectrum (Size)
- **B.Tech DSP topic:** DFT, radix-2 FFT, O(N log N)
- **Blog post:** Writing the DFT by hand, then never again
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 8: The Discrete Fourier Transform (https://www.dspguide.com/ch8.htm)
    - The Scientist and Engineer's Guide to DSP, ch. 12: The Fast Fourier Transform (https://www.dspguide.com/ch12.htm)
    - J. O. Smith, Mathematics of the DFT (https://ccrma.stanford.edu/~jos/mdft/)
    - Müller, FMP notebooks, chapter 2: Fourier analysis of signals (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C2/C2.html)

### Day 6 (Tue 17 Nov 2026): Windowing and spectral leakage
- **Notebook:** `lessons/lesson08_windows.ipynb`
- **Builds:** Two close tones analysed with rectangular, Hann, Hamming and Blackman windows; main-lobe width vs side-lobe level
- **Audacity:** Plot Spectrum (Function)
- **B.Tech DSP topic:** Windowing
- **Blog post:** Why Plot Spectrum asks you to pick a window
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 9: Applications of the DFT (https://www.dspguide.com/ch9.htm)
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - SciPy docs: scipy.signal.get_window (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.get_window.html)

### Day 7 (Wed 18 Nov 2026): Spectrograms and the STFT
- **Notebook:** `lessons/lesson09_spectrograms.ipynb`
- **Builds:** STFT window and hop sizes swept on speech; linear, log and mel frequency axes; the time-frequency trade-off
- **Audacity:** Spectrogram view settings
- **B.Tech DSP topic:** STFT, time-frequency uncertainty
- **Blog post:** Week 1 review: seeing time and frequency at once
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 9: Applications of the DFT (https://www.dspguide.com/ch9.htm)
    - Müller, FMP notebooks, chapter 2: Fourier analysis of signals (STFT) (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C2/C2.html)
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Audacity Manual (manual.audacityteam.org): Spectrogram View, Spectrograms Preferences

### Day 8 (Thu 19 Nov 2026): Impulse response and convolution
- **Notebook:** `lessons/lesson10_impulse_response.ipynb`
- **Builds:** A clap as a room's impulse response; LTI properties checked numerically; the convolution sum written by hand
- **Audacity:** Record, trim
- **B.Tech DSP topic:** LTI systems, convolution sum
- **Blog post:** A clap tells you everything about a room
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 5: Linear Systems (https://www.dspguide.com/ch5.htm)
    - The Scientist and Engineer's Guide to DSP, ch. 6: Convolution (https://www.dspguide.com/ch6.htm)
    - Oppenheim & Schafer, Discrete-Time Signal Processing: linear time-invariant systems

### Day 9 (Fri 20 Nov 2026): Convolution reverb
- **Notebook:** `lessons/lesson11_convolution_reverb.ipynb`
- **Builds:** A dry voice convolved with a room impulse response; direct vs FFT convolution speed; overlap-add
- **Audacity:** Effect > Reverb
- **B.Tech DSP topic:** Linear vs circular convolution, overlap-add
- **Blog post:** Fake a cathedral with one line of NumPy
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 18: FFT Convolution (https://www.dspguide.com/ch18.htm)
    - J. O. Smith, Physical Audio Signal Processing (https://ccrma.stanford.edu/~jos/pasp/)
    - Audacity Manual (manual.audacityteam.org): Reverb

### Day 10 (Sat 21 Nov 2026): Echo and comb filters
- **Notebook:** `lessons/lesson12_echo_comb.ipynb`
- **Builds:** Feedforward and feedback comb filters from their difference equations; their notches and peaks plotted and heard
- **Audacity:** Effect > Echo
- **B.Tech DSP topic:** Difference equations, FIR vs IIR
- **Blog post:** Echo is a filter
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 19: Recursive Filters (https://www.dspguide.com/ch19.htm)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - J. O. Smith, Physical Audio Signal Processing (https://ccrma.stanford.edu/~jos/pasp/)
    - Audacity Manual (manual.audacityteam.org): Echo

### Day 11 (Sun 22 Nov 2026): Z-transform, poles and zeros
- **Notebook:** `lessons/lesson13_z_transform.ipynb`
- **Builds:** Pole-zero plots and freqz; stability and the unit circle; move a pole and listen to the result
- **Audacity:** (none)
- **B.Tech DSP topic:** Z-transform, region of convergence, stability
- **Blog post:** Poles, zeros and the unit circle, finally with sound
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 33: The z-Transform (https://www.dspguide.com/ch33.htm)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - SciPy docs: scipy.signal.freqz (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.freqz.html)

### Day 12 (Mon 23 Nov 2026): FIR filter design
- **Notebook:** `lessons/lesson14_fir_design.ipynb`
- **Builds:** A windowed-sinc low-pass by hand, then with scipy firwin; linear phase; high-pass by spectral inversion
- **Audacity:** Low-Pass and High-Pass Filter
- **B.Tech DSP topic:** FIR design by windowing
- **Blog post:** Designing a low-pass filter from a sinc
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 16: Windowed-Sinc Filters (https://www.dspguide.com/ch16.htm)
    - SciPy docs: scipy.signal.firwin (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.firwin.html)
    - Audacity Manual (manual.audacityteam.org): Low-Pass Filter, High-Pass Filter

### Day 13 (Tue 24 Nov 2026): IIR filter design
- **Notebook:** `lessons/lesson15_iir_design.ipynb`
- **Builds:** Butterworth, Chebyshev and elliptic filters compared; phase response; filtfilt for zero phase; shelving filters
- **Audacity:** Bass and Treble
- **B.Tech DSP topic:** Analog prototypes, bilinear transform
- **Blog post:** Butterworth vs Chebyshev: flat or sharp?
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 19: Recursive Filters (https://www.dspguide.com/ch19.htm)
    - The Scientist and Engineer's Guide to DSP, ch. 20: Chebyshev Filters (https://www.dspguide.com/ch20.htm)
    - SciPy docs: scipy.signal.butter (https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html)
    - Audio EQ Cookbook (Bristow-Johnson), W3C note (https://www.w3.org/TR/audio-eq-cookbook/)
    - Audacity Manual (manual.audacityteam.org): Bass and Treble

### Day 14 (Wed 25 Nov 2026): A graphic equaliser
- **Notebook:** `lessons/lesson16_equaliser.ipynb`
- **Builds:** A 10-band graphic EQ from RBJ peaking biquads in cascade, applied to a song
- **Audacity:** Graphic EQ, Filter Curve EQ
- **B.Tech DSP topic:** Biquads, second-order sections
- **Blog post:** Week 2 review: build your own graphic EQ
- **References:**
    - Audio EQ Cookbook (Bristow-Johnson), W3C note (https://www.w3.org/TR/audio-eq-cookbook/)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - Audacity Manual (manual.audacityteam.org): Graphic EQ, Filter Curve EQ

### Day 15 (Thu 26 Nov 2026): Fades and envelopes
- **Notebook:** `lessons/lesson17_fades_envelopes.ipynb`
- **Builds:** Linear, exponential and S-curve fades; an ADSR envelope; ducking music under a voice
- **Audacity:** Fade In/Out, Envelope tool, Auto Duck
- **B.Tech DSP topic:** Amplitude modulation
- **Blog post:** Fades are multiplication
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: amplitude modulation and envelopes
    - The Scientist and Engineer's Guide to DSP, ch. 22: Audio Processing (https://www.dspguide.com/ch22.htm)
    - Audacity Manual (manual.audacityteam.org): Fade In, Fade Out, Envelope Tool, Auto Duck

### Day 16 (Fri 27 Nov 2026): Compressors and limiters
- **Notebook:** `lessons/lesson18_compressor.ipynb`
- **Builds:** An envelope follower; threshold, ratio, attack and release; a brick-wall limiter
- **Audacity:** Compressor, Limiter
- **B.Tech DSP topic:** Nonlinear systems, smoothing filters
- **Blog post:** How a compressor decides what's too loud
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: dynamics processing
    - The Scientist and Engineer's Guide to DSP, ch. 22: Audio Processing (https://www.dspguide.com/ch22.htm)
    - Audacity Manual (manual.audacityteam.org): Compressor, Limiter

### Day 17 (Sat 28 Nov 2026): Noise gate and silence trimming
- **Notebook:** `lessons/lesson19_gate_silence.ipynb`
- **Builds:** Short-time energy and zero-crossing rate; energy-based voice detection; a noise gate; trimming long silences
- **Audacity:** Noise Gate, Truncate Silence
- **B.Tech DSP topic:** Short-time energy, zero-crossing rate
- **Blog post:** Cutting the silence out of a podcast
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: short-time energy and zero-crossing rate
    - Audacity Manual (manual.audacityteam.org): Noise Gate, Truncate Silence

### Day 18 (Sun 29 Nov 2026): Noise reduction
- **Notebook:** `lessons/lesson20_noise_reduction.ipynb`
- **Builds:** A noise profile and spectral subtraction; where 'musical noise' comes from; a simple Wiener-style gain
- **Audacity:** Noise Reduction (Get Noise Profile)
- **B.Tech DSP topic:** Spectral subtraction, Wiener filter
- **Blog post:** Inside Audacity's Noise Reduction
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 17: Custom Filters (optimal filters) (https://www.dspguide.com/ch17.htm)
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Audacity Manual (manual.audacityteam.org): Noise Reduction

### Day 19 (Mon 30 Nov 2026): Hum and click removal
- **Notebook:** `lessons/lesson21_hum_clicks.ipynb`
- **Builds:** A notch comb for 50 Hz mains hum and its harmonics; a median filter for clicks
- **Audacity:** Notch Filter, Click Removal
- **B.Tech DSP topic:** Notch design, median filtering
- **Blog post:** Removing the 50 Hz hum Indian mains leave behind
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 19: Recursive Filters (band-reject) (https://www.dspguide.com/ch19.htm)
    - J. O. Smith, Introduction to Digital Filters (https://ccrma.stanford.edu/~jos/filters/)
    - Audacity Manual (manual.audacityteam.org): Notch Filter, Click Removal

### Day 20 (Tue 01 Dec 2026): Speed, tempo and pitch
- **Notebook:** `lessons/lesson22_speed_tempo_pitch.ipynb`
- **Builds:** Resampling (speed) vs phase-vocoder time stretch (tempo) vs pitch shift, compared on the same clip
- **Audacity:** Change Speed, Change Tempo, Change Pitch
- **B.Tech DSP topic:** Multirate DSP, interpolation, phase vocoder
- **Blog post:** Speed, tempo and pitch: Audacity's three different knobs
- **References:**
    - J. O. Smith, Spectral Audio Signal Processing (https://ccrma.stanford.edu/~jos/sasp/)
    - Proakis & Manolakis, Digital Signal Processing: multirate digital signal processing
    - Audacity Manual (manual.audacityteam.org): Change Speed, Change Tempo, Change Pitch

### Day 21 (Wed 02 Dec 2026): Stereo and vocal removal
- **Notebook:** `lessons/lesson23_stereo_vocals.ipynb`
- **Builds:** Mid/side encoding; centre-channel cancellation; pan laws
- **Audacity:** Vocal Reduction and Isolation
- **B.Tech DSP topic:** Phase cancellation
- **Blog post:** Week 3 review: why vocal removal only half works
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: spatial effects
    - Audacity Manual (manual.audacityteam.org): Vocal Reduction and Isolation

### Day 22 (Thu 03 Dec 2026): Pitch detection
- **Notebook:** `lessons/lesson24_pitch_detection.ipynb`
- **Builds:** Autocorrelation and pYIN on the trumpet; settles Lesson 1's 1,000 Hz vs 600 Hz question
- **Audacity:** Plot Spectrum
- **B.Tech DSP topic:** Autocorrelation
- **Blog post:** Finding the pitch when the loudest note lies
- **References:**
    - Müller, FMP notebooks, chapter 8: fundamental frequency estimation (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C8/C8.html)
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: pitch period estimation
    - librosa documentation: librosa.pyin

### Day 23 (Fri 04 Dec 2026): The source-filter model
- **Notebook:** `lessons/lesson25_source_filter.ipynb`
- **Builds:** Lesson 2's vowels rebuilt as a pulse train through formant resonators; LPC to estimate the formants back
- **Audacity:** (none)
- **B.Tech DSP topic:** All-pole models, linear prediction
- **Blog post:** Rebuilding vowels the way a throat does
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 22: Audio Processing (speech synthesis) (https://www.dspguide.com/ch22.htm)
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: linear predictive analysis
    - librosa documentation: librosa.lpc

### Day 24 (Sat 05 Dec 2026): Mel scale and MFCCs
- **Notebook:** `lessons/lesson26_mel_mfcc.ipynb`
- **Builds:** A mel filterbank by hand; log-mel spectrograms; MFCCs via the DCT
- **Audacity:** Spectrogram view (Mel scale)
- **B.Tech DSP topic:** Filter banks, DCT
- **Blog post:** The mel scale: how speech models hear
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: speech representations
    - Müller, FMP notebooks, chapter 3: log-frequency spectrogram (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C3/C3.html)
    - librosa documentation: librosa.feature.melspectrogram, librosa.feature.mfcc

### Day 25 (Sun 06 Dec 2026): Malayalam and Hindi in the spectrogram
- **Notebook:** `lessons/lesson27_indic_speech.ipynb`
- **Builds:** My recordings: vowel length, retroflex vs dental consonants, aspiration and voice onset time
- **Audacity:** Record, spectrogram view, Label Tracks
- **B.Tech DSP topic:** Speech analysis
- **Blog post:** Malayalam and Hindi in the spectrogram
- **References:**
    - Rabiner & Schafer, Theory and Applications of Digital Speech Processing: acoustic phonetics
    - Audacity Manual (manual.audacityteam.org): Label Tracks

### Day 26 (Mon 07 Dec 2026): The speech-to-text front end
- **Notebook:** `lessons/lesson28_asr_frontend.ipynb`
- **Builds:** Resample to 16 kHz and build the 80-bin log-mel input speech models use; compare with the sarvam_poc experiments
- **Audacity:** Resample, Export
- **B.Tech DSP topic:** Feature extraction
- **Blog post:** What a speech-to-text model sees before it hears
- **References:**
    - librosa documentation: librosa.feature.melspectrogram
    - Radford et al., Robust Speech Recognition via Large-Scale Weak Supervision (the Whisper paper), 2022
    - Audacity Manual (manual.audacityteam.org): Resample, Export

### Day 27 (Tue 08 Dec 2026): Onsets and beats
- **Notebook:** `lessons/lesson29_onsets_beats.ipynb`
- **Builds:** Spectral-flux onset detection; tempo estimation; beat tracking on a song
- **Audacity:** Beat Finder, Label Sounds
- **B.Tech DSP topic:** Novelty functions, peak picking
- **Blog post:** Finding the beat with spectral flux
- **References:**
    - Müller, FMP notebooks, chapter 6: tempo and beat tracking (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C6/C6.html)
    - librosa documentation: librosa.onset.onset_strength, librosa.beat.beat_track
    - Audacity Manual (manual.audacityteam.org): Beat Finder, Label Sounds

### Day 28 (Wed 09 Dec 2026): Chroma and key
- **Notebook:** `lessons/lesson30_chroma_key.ipynb`
- **Builds:** The constant-Q transform; chroma features; key estimation on a Carnatic or film song
- **Audacity:** Plot Spectrum (log frequency)
- **B.Tech DSP topic:** Constant-Q transform
- **Blog post:** Twelve notes in a spectrogram
- **References:**
    - Müller, FMP notebooks, chapter 3: music synchronization (chroma features) (https://www.audiolabs-erlangen.de/resources/MIR/FMP/C3/C3.html)
    - librosa documentation: librosa.feature.chroma_cqt

### Day 29 (Thu 10 Dec 2026): Real-time DSP
- **Notebook:** `lessons/lesson31_realtime.ipynb`
- **Builds:** Block processing with sounddevice; buffer size vs latency; a live filter with carried-over state
- **Audacity:** Real-time effect preview, Audio Settings (buffer length)
- **B.Tech DSP topic:** Frame-based processing
- **Blog post:** Real-time DSP: latency and buffers
- **References:**
    - The Scientist and Engineer's Guide to DSP, ch. 28: Digital Signal Processors (https://www.dspguide.com/ch28.htm)
    - python-sounddevice documentation (https://python-sounddevice.readthedocs.io/)
    - Audacity Manual (manual.audacityteam.org): Audio Settings preferences

### Day 30 (Fri 11 Dec 2026): Capstone: a mini Audacity
- **Notebook:** `lessons/lesson32_mini_audacity.ipynb`
- **Builds:** My own normalise, EQ, noise reduction and compressor chained on a voice memo, compared with Audacity's output
- **Audacity:** Macros
- **B.Tech DSP topic:** Systems in cascade
- **Blog post:** 30 days of DSP: I rebuilt Audacity's effects rack
- **References:**
    - Zölzer (ed.), DAFX: Digital Audio Effects: effect chains
    - Audacity Manual (manual.audacityteam.org): Macros
