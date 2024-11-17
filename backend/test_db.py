# test_db.py
from src.core.database import engine
from src.models.destination import Destination  # Import Destination instead

def test_connection():
    try:
        # Create tables for all models that inherit from Base
        Destination.__table__.create(bind=engine)
        print("✅ Database connection successful!")
    except Exception as e:
        print("❌ Database connection failed!")
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    test_connection()