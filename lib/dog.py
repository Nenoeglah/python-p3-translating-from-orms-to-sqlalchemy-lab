# from models import Dog

# def create_table(base):
#     pass

# def save(session, dog):
#     pass

# def get_all(session):
#     pass

# def find_by_name(session, name):
#     pass

# def find_by_id(session, id):
#     pass

# def find_by_name_and_breed(session, name, breed):
#     pass

# def update_breed(session, dog, breed):
#     pass



from models import Dog

def create_table(base, engine):
    base.metadata.create_all(engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, id):
    return session.query(Dog).filter(Dog.id == id).first()

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name and Dog.breed == breed).first()

def update_breed(session, dog, breed):
    dog.breed = breed
    session.add(dog)
    session.commit()