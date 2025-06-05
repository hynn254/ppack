from scipy.signal import firwin, butter, filtfilt


class filters:
    def __init__(self, fs, cutoff, btype):
        self.fs = fs
        self.cutoff = cutoff    # [Hz]
        self.btype = btype      # 'bandpass', 'lowpass', 'highpass', 'bandstop' 
        # if btype is 'bandpass', cutoff should be [low, high] form.

    # Hamming window filter #
    def FIRfilter(self, signal, numtaps):
        b = firwin(numtaps=numtaps, cutoff=self.cutoff, pass_zero=self.btype, fs=self.fs)
        # numtaps: order = numtaps - 1, it must be odd if a passband includes the Nyquist frequency
        # cutoff: cutoff frequency [Hz]
        # pass_zero = contain DC?: True, False, 'bandpass', 'lowpass', 'highpass', 'bandstop' 

        y = filtfilt(b, 1.0, signal)
        # 어차피 fir 필터는 a 계수(출력신호 계수) 없음 - 1.0을 써서 피드백 없음을 나타내는 것

        return y


    def IIRfilter(self, signal, order):
        b, a = butter(N=order, Wn=self.cutoff, btype=self.btype, fs=self.fs)
        y = filtfilt(b, a, signal)

        return y