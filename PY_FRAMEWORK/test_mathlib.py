
from mathlib import MyDB
import pytest
@pytest.fixture(scope="module")#scope is used to run cur() method only one time. scope can be module, function, session and
#default scope is function.
def cur():
    print("setting up")
    db = MyDB()
    conn = db.connect("server")
    curs = conn.cursor()
    yield curs
    curs.close()
    conn.close()
    print("closing DB")

def test_johns_id(cur):
    id = cur.execute("select id from employee_db where name=John")
    assert id == 123

def test_toms_id(cur):
    id = cur.execute("select id from employee_db where name=Tom")
    assert id == 789

"""
import pytest
@pytest.fixture(autouse=True)
def fix():
    print("start")
    yield
    print("close")

def test_id1():
    print("id1")

def test_id2():
    print("id2")
"""
"""
import pytest

@pytest.fixture(params=[

    {"input":1,"response":1},
    {"input":2,"response":4},
    {"input":3,"response":9},
])
def testCase(request):
    return request.param



def test_square(testCase):
    result=testCase["input"]*testCase["input"]
    assert result==testCase["response"]
"""
"""
import pytest

@pytest.fixture(params=[
    {"input":1},
    {"input":2},
    {"input":3},
])
def testCase(request):
    return request.param

def test_square(testCase):
    result=testCase["input"]*testCase["input"]
    assert result==9
"""