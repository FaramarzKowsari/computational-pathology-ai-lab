from pathlib import Path

from PIL import Image

from cpathlab.inference.predictor import Predictor

checkpoint = Path("models/baseline.pt")
if not checkpoint.exists():
    raise SystemExit("Train or provide an authorized checkpoint first.")
predictor = Predictor.from_checkpoint(checkpoint)
with Image.open("data/example/images/synthetic_0000.png") as image:
    print(predictor.predict(image))
