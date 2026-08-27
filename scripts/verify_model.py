import os
import numpy as np
import keras

MODEL_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "..",
        "model",
        "brain_tumor_model.keras"
    )
)

print("=" * 60)
print("ZKP-CerebraChain - ACTUAL MODEL VERIFICATION")
print("=" * 60)

print("\nModel path:")
print(MODEL_PATH)

print("\n[1] Loading .keras model...")

model = keras.saving.load_model(
    MODEL_PATH,
    compile=False
)

print("Model loaded successfully!")

print("\n[2] Model information")

print("Input shape:")
print(model.input_shape)

print("\nOutput shape:")
print(model.output_shape)

print("\nTotal parameters:")
print(model.count_params())

print("\n[3] Model architecture")

model.summary()

print("\n[4] Running test inference...")

dummy_input = np.random.rand(
    1, 240, 240, 1
).astype(np.float32)

prediction = model.predict(
    dummy_input,
    verbose=0
)

print("\nInference successful!")

print("Prediction shape:")
print(prediction.shape)

print("Prediction value:")
print(prediction)

print("\n" + "=" * 60)
print("ACTUAL MODEL VERIFIED SUCCESSFULLY")
print("=" * 60)