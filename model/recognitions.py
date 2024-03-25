import deepface as dp

objs = dp.analyze(
    img_path="img4.jpg", actions=["age", "gender", "race"]
)
