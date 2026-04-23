import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app
from configs.database import get_db
from tests.conftest import engine


class BaseTestCase:
    client: TestClient
    session: Session

    def setup_method(self, method):
        self.connection = engine.connect()
        self.transaction = self.connection.begin()
        self.session = Session(bind=self.connection)

        # Override dependency
        def override_get_db():
            try:
                yield self.session
            finally:
                pass

        app.dependency_overrides[get_db] = override_get_db
        self.client = TestClient(app)

    def teardown_method(self, method):
        self.session.close()
        self.transaction.rollback()
        self.connection.close()
        app.dependency_overrides = {}
