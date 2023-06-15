import mlask
emotion_analyzer = mlask.MLAsk("-d 'C:/Program Files/MeCab/dic/ipadic'")
sentence = input("ここに文章をドロップ: ")
result = emotion_analyzer.analyze(sentence)

print(result)
