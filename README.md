# Face Match

This is a project that uses facial recognition to match a given face with a pre-defined set of faces. It utilizes the VGGFace model and MTCNN for face detection. The project is built using [Streamlit](https://streamlit.io/), a Python library for creating web applications.

## Installation

1. Clone the repository:

   ```shell
   git clone https://github.com/nasserml/Face-Match.git
   ```

2. Navigate to the project directory:

   ```shell
   cd Face-Match
   ```

3. Install the required dependencies:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```shell
   streamlit run app.py
   ```

2. Open your web browser and go to [http://localhost:8501](http://localhost:8501) to access the application.

3. Choose an image to upload and click the "Submit" button.

4. The application will analyze the uploaded image and provide a recommendation on which pre-defined face it matches the most.

## Project Structure

The project repository has the following structure:

- `app.py`: The main application file containing the Streamlit code.
- `src/`: A directory containing utility functions and modules.
- `data.rar`: Compressed file containing pre-processed data and features.
- `params.yaml`: YAML file containing configuration parameters for the project.
- `requirements.txt`: Text file listing the required Python packages.
- `LICENSE`: The license file for the project.
- `README.md`: This file, providing information and instructions for the project.

## License

This project is licensed under the [MIT License](LICENSE).
```

In this version, the links to Streamlit and `http://localhost:8501` are clickable and will direct the reader to the respective webpages.
