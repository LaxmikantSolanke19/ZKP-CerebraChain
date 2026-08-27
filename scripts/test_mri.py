import os
import numpy as np
import tensorflow as tf
from PIL import Image

MODEL_PATH = "model/brain_tumor_model.keras"
IMAGE_PATH = "test_tumor.jpg"

print("=" * 60)
print("ZKP-CerebraChain - MRI MODEL TEST")
print("=" * 60)

# 1. Check files
if not os.path.exists(MODEL_PATH):
    print("❌ MODEL NOT FOUND")
    raise SystemExit(1)

if not os.path.exists(IMAGE_PATH):
    print("❌ MRI IMAGE NOT FOUND")
    raise SystemExit(1)

# 2. Load actual model
print("\n[1] Loading actual model...")
model = tf.keras.models.load_model(MODEL_PATH)
print("✅ Model loaded")

print("Input:", model.input_shape)
print("Output:", model.output_shape)
print("Parameters:", model.count_params())

# 3. Load MRI
print("\n[2] Loading MRI image...")
img = Image.open(IMAGE_PATH)

print("Original size:", img.size)
print("Original mode:", img.mode)

# Convert RGB -> Grayscale
img = img.convert("L")

# Resize exactly as model expects
img = img.resize((240, 240))

# Convert to numpy
image_array = np.array(img, dtype=np.float32)

# Normalize
image_array = image_array / 255.0

# Add channel + batch dimensions
image_array = np.expand_dims(image_array, axis=-1)
image_array = np.expand_dims(image_array, axis=0)

print("Model input shape:", image_array.shape)

# 4. Actual inference
print("\n[3] Running ACTUAL model inference...")

prediction = model.predict(image_array, verbose=0)

score = float(prediction[0][0])

print("Prediction:", score)

# 5. Interpret prediction
print("\n[4] Prediction result")

if score >= 0.5:
    print("Prediction class: TUMOR")
else:
    print("Prediction class: NO TUMOR")

print("Confidence score:", score)

print("\n" + "=" * 60)
print("MODEL INFERENCE SUCCESSFUL")
print("=" * 60)