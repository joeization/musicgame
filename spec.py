import sys
import struct
import wave
import random


def show_wave_n_spec(speech):
    spf = wave.open(speech, 'rb')
    (nchannels, sampwidth, framerate,
        nframes, comptype, compname) = spf.getparams()
    frames = spf.readframes(nframes * nchannels)
    out = struct.unpack_from("%dh" % nframes * nchannels, frames)
    if nchannels == 2:
        left = list(out[0::2])
        right = list(out[1::2])
    else:
        left = array(out)
        right = left
    sound_info = left
    outfile = open('bmap.txt', 'w')
    last = 0
    cnt = 0
    prev = -30000
    rt = float(spf.getframerate())
    for i in range(len(sound_info)):
        if sound_info[i] > 0:
            # if abs(sound_info[i] - last)/last >= 1 and i - prev > rt/4:
            if abs(sound_info[i] - last) >= 7500 and i - prev > rt/8:
                t = round(i/rt, 2)
                n = random.randint(0, 3)
                outfile.write(str(t-1)+' '+str(n)+'\n')
                if abs(sound_info[i] - last) >= 15000:
                    m = random.randint(0, 3)
                    while n == m:
                        m = random.randint(0, 3)
                    outfile.write(str(t-1)+' '+str(m)+'\n')
                cnt += 1
                prev = i
            last = sound_info[i]
    print(cnt)
    outfile.close()
    spf.close()

fil = sys.argv[1]
print('generating from', fil)
show_wave_n_spec(fil)
