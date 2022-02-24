from src.jobs import read


def get_unique_job_types(path):
    """
    Passos a se seguir:
    1 - Buscar os dados que foram encontrados na def jobs.read
    2 - Criar um array que vai receber os valores apenas do tipo de job
    3 - Percorrer o array de dados do def jobs.read inserindo apenas o
        tipo de job no novo array
    4 - Verificar se o tipo já não existe para não inserir dois iguais
    5 - Retornar a lista de tipos de jobs
    """
    list_all_jobs = read(path)
    type_of_jobs_list = []
    for job_type in list_all_jobs:
        if job_type["job_type"] not in type_of_jobs_list:
            type_of_jobs_list.append(job_type["job_type"])
    return type_of_jobs_list


def filter_by_job_type(jobs, job_type):
    """
    Passos a se seguir:
    1 - Criar um array que vai receber os jobs que forem iguais
         ao tipo passado como segundo parâmetro
    2 - Percorrer o array passado como primeiro parâmetro
    3 - Verificar se o tipo do elemento percorrido é igual ao
         job_type
    4 - Inserir o job no novo array
    5 - Retornar a lista de jobs
    """
    list_job_by_type = []
    for job_element in jobs:
        if job_element["job_type"] == job_type:
            list_job_by_type.append(job_element)
    return list_job_by_type


def get_unique_industries(path):
    """
    Passos a se seguir:
    1 - Buscar os dados que foram encontrados na def jobs.read
    2 - Criar um array que vai receber os valores de indústrias
    3 - Percorrer o array de dados do def jobs.read inserindo apenas
        a indústria no novo array
    4 - Verificar se a indústria já não existe para não inserir dois iguais
        e/ou vazios
    5 - Retornar a lista de indústrias
    """
    list_all_jobs = read(path)
    industries_list = []
    for industry in list_all_jobs:
        if industry["industry"] not in industries_list:
            if industry["industry"] != "":
                industries_list.append(industry["industry"])
    return industries_list


def filter_by_industry(jobs, industry):
    """
    Passos a se seguir:
    1 - Criar um array que vai receber os jobs que forem iguais
         à indústria passada como segundo parâmetro
    2 - Percorrer o array passado como primeiro parâmetro
    3 - Verificar se a indústria do elemento percorrido é igual ao
         industry
    4 - Inserir o job no novo array
    5 - Retornar a lista de jobs
    """
    list_job_by_industry = []
    for job_element in jobs:
        if job_element["industry"] == industry:
            list_job_by_industry.append(job_element)
    return list_job_by_industry


def get_max_salary(path):
    """
    Passos a se seguir:
    1 - Buscar os dados que foram encontrados na def jobs.read
    2 - Verificar se o salário não é vazio ou inválido
    3 - Percorrer o novo array verificando qual é o maior salário
    """
    list_all_jobs = read(path)
    max_salary = 0
    for salary in list_all_jobs:
        if salary["max_salary"] != "" and salary["max_salary"] != "invalid":
            if max_salary < int(salary["max_salary"]):
                max_salary = int(salary["max_salary"])
    return max_salary


def get_min_salary(path):
    """
    Passos a se seguir:
    1 - Buscar os dados que foram encontrados na def jobs.read
    2 - Atribuir a uma variável o valor encontrado na função
        anterior e começar a compará-lo com os outros da lista
    3 - Verificar se o salário não é vazio ou inválido
    4- Percorrer o novo array verificando qual é o menor salário
    """
    list_all_jobs = read(path)
    min_salary = get_max_salary(path)
    for salary in list_all_jobs:
        if salary["min_salary"] != "" and salary["min_salary"] != "invalid":
            if min_salary > int(salary["min_salary"]):
                min_salary = int(salary["min_salary"])
    return min_salary


def matches_salary_range(job, salary):
    """
    Passos a se seguir:
    1 - Verificar se existe min_salary e max_salary em job
        Caso não exista, retornar um erro
    2 - Verificar se o tipo destes valores é igual a int
        Caso sejam diferente, retornar um erro
    3 - Verificar se o tipo de salary é igual a int
        Caso seja diferente, retornar um erro
    4 - Verificar se o min_salary é maior que max_salary
        Caso seja, retornar um erro
    5 - Retornar se o salário está entre os valores de máximo e mínimo
    """
    if "max_salary" not in job or "min_salary" not in job:
        raise ValueError("Campos não estão presentes no diciomário")
    elif type(job["max_salary"]) != int or type(job["min_salary"]) != int:
        raise ValueError("Valores com tipos diferentes de int")
    elif type(salary) != int:
        raise ValueError("Salary possui valor diferente de int")
    elif job["min_salary"] >= job["max_salary"]:
        raise ValueError("Salário mínimo maior que o máximo")
    true_or_false = job["max_salary"] >= salary >= job["min_salary"]
    return true_or_false


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []
