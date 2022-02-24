from src.sorting import sort_by

"""
Alguns pontos a se atentar:
- Criar um mock de array contendo uma lista de dicionários com detalhes
    do emprego (date_posted, max_salary, min_salary)
- Criar um mock para cada ordenação esperada
- A ordenação de min_salary é crescente
- As oredenações de max_salary e date_posted são
    decrescentes
- Testar se cada ordenação é esperada após o mock ser passado como
    parâmtero da função sort_by
"""

jobs_mock_array = [
    {
        "date_posted": "2022-02-21",
        "max_salary": 10000,
        "min_salary": 9000
    },
    {
        "date_posted": "2022-02-22",
        "max_salary": 24000,
        "min_salary": 2300
    },
    {
        "date_posted": "2022-02-23",
        "max_salary": 18000,
        "min_salary": 13000
    },
]

order_min_salary = [
    jobs_mock_array[1],
    jobs_mock_array[0],
    jobs_mock_array[2]
]
order_max_salary = [
    jobs_mock_array[1],
    jobs_mock_array[2],
    jobs_mock_array[0]
]
order_by_date = [
    jobs_mock_array[2],
    jobs_mock_array[1],
    jobs_mock_array[0]
]


def test_sort_by_criteria():
    sort_by(jobs_mock_array, "max_salary")
    assert jobs_mock_array == order_max_salary

    sort_by(jobs_mock_array, "min_salary")
    assert jobs_mock_array == order_min_salary

    sort_by(jobs_mock_array, "date_posted")
    assert jobs_mock_array == order_by_date
