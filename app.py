import os
import gdown
import tensorflow as tf

MODEL_PATH = "best_model.keras"
GOOGLE_DRIVE_FILE_ID = "1VdvGFP1o6_DcVEb_4Y_5xdUNCUnzF5IZ"  # Replace with your actual file ID

# 📌 Download model if not exists
if not os.path.exists(MODEL_PATH):
    print("Downloading model from Google Drive...")
    gdown.download(f"https://drive.google.com/uc?export=download&id=1VdvGFP1o6_DcVEb_4Y_5xdUNCUnzF5IZ", MODEL_PATH, quiet=False)

# ✅ Load the model
model = tf.keras.models.load_model(MODEL_PATH)
