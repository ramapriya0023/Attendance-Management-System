
from urllib import response
from fastapi.testclient import TestClient
from index import app
client=TestClient(app)

def test_create_leave():
    response=client.post('/applyleave',
    json={
        "empid":"emp10",
        "leaveid":"emp10l1",
        "reason":"paidleave",
        "status":"Approved"}
        #text="leave applied successfully."
        )
    assert response.status_code==200
    assert response.json()=={
        "empid":"emp10",
        "leaveid":"emp10l1",
        "reason":"paidleave",
        "status":"Applied"}
    #assert response.text()=="leave applied successfully."

def test_get_leave():
    response=client.get('/leaveapplied/emp10l1')
    assert response.status_code==200
    assert response.json()=={
        "empid":"emp10",
        "leaveid":"emp10l1",
        "reason":"paidleave",
        "status":"Applied"
    }

def test_approve_leave():
    response=client.put('/approve/emp10l1',
    json={"status":"Approved"}
    )
    assert response.status_code==20
    assert response.json()=={
        "empid":"emp10",
        "leaveid":"emp10l1",
        "reason":"paidleave",
        "status":"Approved"
    }

def test_gen_report():
    response=client.get('/report/emp10')
    assert response.status_code==200
    assert response.json()=={
        "empid":"emp10",
        "name":"ramapriya",
        "paidleave":1,
        "medicalleave":0,
        "privilegeleave":0,
        "lossofpay":0
    }