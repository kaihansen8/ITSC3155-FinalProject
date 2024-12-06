from fastapi.testclient import TestClient
from ..controllers import customers as controllers
from ..main import app
import pytest
from ..models import customers as models

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()

def test_customers_create_delete(db_session):
    customer_data = {
        "name": "Kai Hansen",
        "email": "khanse11@charlotte.edu",
        "phone": "123-456-7890",
        "address": "UNC Charlotte Main Campus"
    }

    customer_object = models.Customers(**customer_data)

    # Class the create function
    created_customer = controllers.create(db_session, customer_object)

    # Assertions
    assert created_customer is not None
    assert created_customer.name == "Kai Hansen"
    assert created_customer.email == "khanse11@charlotte.edu"
    assert created_customer.phone == "123-456-7890"
    assert created_customer.address == "UNC Charlotte Main Campus"

    delete_customer = controllers.delete(db_session, 1)

    assert delete_customer == "Customer deleted successfully"