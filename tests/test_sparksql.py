import pytest
from pyspark import Row
from unittest import mock
from sparksql_magic.sparksql import bind_variables, get_results, make_tag


@pytest.fixture
def df():
    return mock.MagicMock(
        columns=['col1', 'col2', 'col3'],
        take=lambda n: [Row(col1=i, col2=str(i), col3=None) for i in range(n)]
    )


@pytest.fixture
def user_ns():
    return {
        'month': 5,
        'day': '10',
    }


def test_get_results(df):
    assert get_results(df, 0) == (['col1', 'col2', 'col3'], [['0', '0', 'null']])
    assert get_results(df, 1) == (['col1', 'col2', 'col3'], [['0', '0', 'null'], ['1', '1', 'null']])


def test_bind_variables(user_ns):
    assert bind_variables('SELECT * FROM table', user_ns) == 'SELECT * FROM table'
    assert bind_variables("SELECT * FROM table WHERE month='{month}'", user_ns) == "SELECT * FROM table WHERE month='5'"
    assert bind_variables("SELECT * FROM table WHERE month='{month}' AND day='{day}'", user_ns) == "SELECT * FROM table WHERE month='5' AND day='10'"

    with pytest.raises(NameError):
        bind_variables("SELECT * FROM table WHERE hour='{hour}'", user_ns)


def test_make_tag():
    assert make_tag('td') == '<td></td>'
    assert make_tag('td', 'body') == '<td>body</td>'
    assert make_tag('td', 'body', style='font-weight: bold') == '<td style="font-weight: bold">body</td>'
