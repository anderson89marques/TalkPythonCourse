import unittest
import transaction

from pyramid import testing

class BaseTest(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp(
            settings={
                'sqlalchemy.url': 'sqlite:///:memory'
            }
        )
        self.config.include('..models')
        settings =self.config.get_settings()

        from pypi.models import (
            get_engine,
            get_session_factory,
            get_tm_session
        )

        self.engine = get_engine(settings)
        session_factory = get_session_factory(self.engine)
        self.session = get_tm_session(session_factory, transaction.manager)

    def init_database(self):
        from pypi.models.meta import Base
        Base.metadata.create_all(self.engine)

    def tearDown(self):
        from pypi.models.meta import Base

        testing.tearDown()
        transaction.abort()
        Base.metadata.drop_all(self.engine)


class AccountControllerTests(BaseTest):
    # 3 A's of test: Arrange, Act, then Assert

    def setUp(self):
        super(AccountControllerTests, self).setUp()
        self.init_database()

    def test_register_validation_valid(self):
        dummy_req = testing.DummyRequest(dbsession=self.session)
        dummy_req.POST = {'email': 'andersonoanjo18@gmail.com',
                             'name': 'Anderson Marques',
                             'password': '12345'}
        from pypi.views.account_controller import register_post
        info = register_post(dummy_req)
        self.assertEqual(info.status_code, 302)        

    def test_register_validation_no_email(self):
        pass