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

    return []


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
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    return []


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
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    pass


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
