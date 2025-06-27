import time
from database import sync_engine, Base, session_factory
from models import PriceOrm

def if_need_create_tables():
    Base.metadata.create_all(sync_engine)

def create_tables():
    sync_engine.echo = True
    Base.metadata.drop_all(sync_engine)
    Base.metadata.create_all(sync_engine)
    sync_engine.echo = True

def insert_data(price: float):
    with session_factory() as session:
        news_price = PriceOrm(price=price)
        session.add(news_price)
        session.commit()

def insert_data_source(source: str):
    with session_factory() as session:
        source = SourceORM(source_link=source[0])
        session.add(source)
        session.commit()


def insert_data_vk(filtered_content: dict):
    with session_factory() as session:
        content = ContentOrm(**filtered_content)
        session.add(content)
        #session.refresh()
        session.commit()

def update_data_vk():
    content_id = 1
    with session_factory() as session:
        content = session.get(ContentOrm, content_id)
        time.sleep(25)
        session.refresh(content)
        content.topic = "Какой то заголовок"
        session.commit()