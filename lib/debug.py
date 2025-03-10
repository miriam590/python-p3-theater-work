#!/usr/bin/env python3

from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from models import Base, engine, Role, Audition

# Initialize session
Session = sessionmaker(bind=engine)
session = Session()

# Create tables if they don't exist
Base.metadata.create_all(engine)
print("Database successfully created!")

# Function to add roles safely
def add_role(character_name):
    """Adds a role only if it does not already exist."""
    existing_role = session.query(Role).filter_by(character_name=character_name).first()
    if existing_role:
        print(f"Role '{character_name}' already exists, skipping.")
    else:
        new_role = Role(character_name=character_name)
        session.add(new_role)
        try:
            session.commit()
            print(f"Role '{character_name}' added successfully!")
        except IntegrityError:
            session.rollback()
            print(f"Failed to add role '{character_name}'. It might already exist.")

# Add roles
add_role("Mirriam")
add_role("Joy")
add_role("Shelcy") 



# Fetch roles after insertion
role1 = session.query(Role).filter_by(character_name="Mirriam").first()
role2 = session.query(Role).filter_by(character_name="Joy").first()
role3 = session.query(Role).filter_by(character_name="Shelcy").first()

# Add auditions with correct foreign key references
if role1 and role2 and role3:  # Ensure roles exist before adding auditions
    auditions = [
        Audition(actor="Jane Kemboi", location="Reception", phone="254722034321", hired=False, role_id=role1.id),
        Audition(actor="Marion Ken", location="Counter", phone="254787734322", hired=False, role_id=role2.id),
        Audition(actor="Tess Carl", location="Theatre", phone="254789033323", hired=False, role_id=role1.id)
    ]
    
    session.add_all(auditions)
    try:
        session.commit()
        print("Auditions added successfully!")
    except IntegrityError:
        session.rollback()
        print("Failed to add some auditions. Check for data conflicts.")

# Debugging mode
if __name__ == '__main__':
    import ipdb
    ipdb.set_trace()
