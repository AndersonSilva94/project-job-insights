from markdown import markdown
from flask import Flask, Blueprint, render_template, request

from .jobs import read
from .insights import (
    get_unique_industries,
    get_unique_job_types,
    filter_by_salary_range,
    filter_by_industry,
    filter_by_job_type,
    get_min_salary,
    get_max_salary,
)
from .more_insights import (
    slice_jobs,
    get_int_from_args,
    build_jobs_urls,
    get_job
)

bp = Blueprint("client", __name__, template_folder="templates")


@bp.route("/")
def index():
    with open("README.md", encoding="UTF-8") as file:
        md = markdown(file.read())
    return render_template("index.jinja2", md=md)


@bp.route("/jobs")
def list_jobs():
    first_job = get_int_from_args("first_job", 0)
    amount = get_int_from_args("amount", 20)
    salary = get_int_from_args("salary", None)
    industry = request.args.get("industry", None)
    job_type = request.args.get("job_type", None)

    jobs = read(path="src/jobs.csv")
    if industry:
        jobs = filter_by_industry(jobs, industry)
    if job_type:
        jobs = filter_by_job_type(jobs, job_type)
    if salary:
        jobs = filter_by_salary_range(jobs, salary)

    jobs = slice_jobs(jobs, first_job, amount)

    build_jobs_urls(jobs)

    ctx = {
        "jobs": jobs,
        "industries": sorted(get_unique_industries("src/jobs.csv")),
        "job_types": sorted(get_unique_job_types("src/jobs.csv")),
        "previous_job_type": job_type,
        "previous_first": first_job,
        "previous_amount": amount,
        "previous_industry": industry,
        "previous_salary": salary,
        "min_salary": get_min_salary("src/jobs.csv"),
        "max_salary": get_max_salary("src/jobs.csv"),
    }

    return render_template("list_jobs.jinja2", ctx=ctx)


"""
Passos a se seguir:
1 - importar a def get_job de more_insights
2 - Criar a rota que vai fazer a função renderizar a página
    Deve ser: /job/<index>
3 - A função deve ser job e recebe index como parâmetro
4 - Chamar a função read para acessar a lista de jobs
    Passar o caminho onde está o arquivo como parâmetro
    Deve ser: src/jobs.csv
5 - Chamar get_job passsando a lista de jobs e o index como parâmetro
6 - Deve renderizar o template job.jinja2, e um parâmetro job contendo
    o job que é retornado pela get_job
"""


@bp.route("/job/<index>")
def job(index):
    list_all_jobs = read("src/jobs.csv")
    find_job_element = get_job(list_all_jobs, index)
    return render_template("job.jinja2", job=find_job_element)


def init_app(app: Flask):
    app.register_blueprint(bp)
