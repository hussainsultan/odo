import pytest


@pytest.fixture
def t():
    bz = pytest.importorskip('blaze')
    return bz.Symbol('t', 'var * {name: string, id: int64, amount: float64, '
                     'when: datetime, on: date}')


@pytest.fixture
def rt():
    bz = pytest.importorskip('blaze')
    return bz.Symbol('rt', 'var * {name: string, tax: float64, street: string}')


@pytest.fixture
def st():
    bz = pytest.importorskip('blaze')
    return bz.Symbol('st', 'var * {name: string, jobcode: int64, tree: string, '
                     'alias: string}')


@pytest.fixture
def q(rstring, kdb):
    pytest.importorskip('kdbpy.compute')
    from kdbpy.compute.qtable import QTable
    return QTable(rstring, tablename='t')


@pytest.fixture
def rq(rstring, kdb):
    pytest.importorskip('kdbpy.compute')
    from kdbpy.compute.qtable import QTable
    return QTable(rstring, tablename='rt')


@pytest.fixture
def sq(rstring, kdb):
    pytest.importorskip('kdbpy.compute')
    from kdbpy.compute.qtable import QTable
    return QTable(rstring, tablename='st')


@pytest.fixture
def ktq(rstring, kdb):
    pytest.importorskip('kdbpy.compute')
    from kdbpy.compute.qtable import QTable
    return QTable(rstring, tablename='kt')


@pytest.fixture
def rstring(creds):
    return 'kdb://%s@%s:%d' % (creds.username, creds.host, creds.port)
