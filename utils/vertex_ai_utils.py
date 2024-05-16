from google.cloud import aiplatform

def initialize_vertex_ai():
    aiplatform.init(project='your-project-id', location='us-central1')

def generate_content(prompt):
    client = aiplatform.gapic.PredictionServiceClient()
    model = client.get_model(name="projects/your-project-id/locations/us-central1/models/your-model-id")

    request = aiplatform.gapic.PredictRequest(
        endpoint="your-endpoint",
        instances=[{"content": prompt}],
        parameters={"parameter_name": "parameter_value"},
    )

    response = client.predict(request=request)
    return response.predictions[0]["generated_text"]
