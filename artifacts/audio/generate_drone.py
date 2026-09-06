import wave, math

RATE = 44100
DURATION = 20
OUT = '/home/sky/red studio hermes/artifacts/audio/40hz_drone.wav'

def render_drone(path, duration, rate):
    carrier = 40.0
    samples = []
    for i in range(int(duration * rate)):
        t = i / rate
        envelope = 0.6 + 0.4 * math.sin(2 * math.pi * 0.05 * t)
        sig = math.sin(2 * math.pi * carrier * t)
        sig += 0.5 * math.sin(2 * math.pi * (carrier + 1.2) * t)
        sig += 0.3 * math.sin(2 * math.pi * 400 * t) * math.sin(2 * math.pi * 0.2 * t)
        sig *= envelope
        val = int(max(min(sig * 16000, 32767), -32767))
        samples.append(bytes([val & 0xff, (val >> 8) & 0xff]))
    with wave.open(path, 'w') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(b''.join(samples))

render_drone(OUT, DURATION, RATE)
print('wrote', OUT)
