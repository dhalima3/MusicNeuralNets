import pysynth
from MusicMatrix import MusicMatrix

musicLearner = MusicMatrix()
musicLearner.add(["c", 4])
musicLearner.add(["c", 4])
musicLearner.add(["c", 4])
musicLearner.add(["d", 8])
musicLearner.add(["e", 4])
musicLearner.add(["e", 4])
musicLearner.add(["d", 8])
musicLearner.add(["e", 4])
musicLearner.add(["f", 8])
musicLearner.add(["g", 2])

musicLearner.add(["c", 8])
musicLearner.add(["c", 8])
musicLearner.add(["c", 8])

musicLearner.add(["g", 8])
musicLearner.add(["g", 8])
musicLearner.add(["g", 8])

musicLearner.add(["e", 8])
musicLearner.add(["e", 8])
musicLearner.add(["e", 8])

musicLearner.add(["c", 8])
musicLearner.add(["c", 8])
musicLearner.add(["c", 8])

musicLearner.add(["g", 4])
musicLearner.add(["f", 8])
musicLearner.add(["e", 4])
musicLearner.add(["d", 8])
musicLearner.add(["c", 2])

random_score = []
current_note = ["c", 4]
for i in range(0, 100):
    print current_note[0] + ", " + str(current_note[1])
    current_note = musicLearner.next_note(current_note)
    random_score.append(current_note)

pysynth.make_wav(random_score, fn="result.wav")
