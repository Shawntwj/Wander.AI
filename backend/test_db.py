# test_db.py
from src.core.database import engine, SessionLocal
from src.models.destination import Destination

def test_connection():
    try:
        # Create tables if they don't exist
        Destination.__table__.create(bind=engine, checkfirst=True)
        print("✅ Database connection successful!")
        
        # Test creating a destination
        db = SessionLocal()
        try:
            singapore = Destination(name="Singapore", country="Singapore")
            db.add(singapore)
            db.commit()
            print("✅ Successfully created destination!")
        finally:
            db.close()
            
    except Exception as e:
        print("❌ Error:")
        print(str(e))

if __name__ == "__main__":
    test_connection()