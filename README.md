# FastAPI Project

A FastAPI learning project with examples of Pydantic models, validation, serialization, and more.

## Project Structure

- `main.py` - Main FastAPI application
- `computed_field.py` - Examples of computed fields
- `field_validator.py` - Field validation examples
- `model_validator.py` - Model validation examples
- `nested_models.py` - Nested model examples
- `serialization.py` - Serialization examples
- `pydatic.py` - Pydantic examples
- `patients.json` - Sample data

## Setup

1. Create a virtual environment:
```bash
python -m venv myenv
```

2. Activate the virtual environment:
   - **Windows**: `myenv\Scripts\activate`
   - **Linux/Mac**: `source myenv/bin/activate`

3. Install dependencies:
```bash
pip install fastapi uvicorn
```

4. Run the application:
```bash
uvicorn main:app --reload
```

## License

MIT
