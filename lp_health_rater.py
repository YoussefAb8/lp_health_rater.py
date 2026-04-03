from sklearn.ensemble import RandomForestRegressor
import skl2onnx
from skl2onnx.common.data_types import FloatTensorType

# 1. Training Data: [Volume/TVL, Volatility, Concentration]
X = [
    [0.01, 0.10, 0.20], # Low health pool
    [0.10, 0.05, 0.70], # Medium health pool
    [0.25, 0.02, 0.90], # Excellent health pool
    [0.05, 0.15, 0.40]  # High risk pool
]

# 2. Target Scores (0-100)
y = [20, 65, 95, 40] 

# 3. Model Training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# 4. Define Input Type for ONNX (3 Features)
initial_type = [('float_input', FloatTensorType([None, 3]))]

# 5. Convert to ONNX format
onx = skl2onnx.convert_sklearn(model, initial_types=initial_type)

# 6. Save the final ONNX file
with open("lp_health_rater.onnx", "wb") as f:
    f.write(onx.SerializeToString())

print("✅ Done! 'lp_health_rater.onnx' has been created using 'lp_health_rater.py'")
