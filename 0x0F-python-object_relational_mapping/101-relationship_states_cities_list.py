#!/usr/bin/python3
"""script to create city and state object"""

#!/usr/bin/python3
"""script to create city and state object"""

if __name__ == "__main__":
    from relationship_state import Base, State
    from relationship_city import City
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker
    from sys import argv

    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(user, passwd, db), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for state, city in session.query(State, City).filter(
            State.id == City.state_id).order_by(City.id):
        print("{}: {} -> {}".format(city.id, city.name, state.name))

    session.close()
