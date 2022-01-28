from turtle import title
from flask import Blueprint, render_template, request, url_for
from webapp import article
from webapp.article.models import Article

from webapp.db import db
blueprint = Blueprint("article", __name__)

@blueprint.route("/create-article")
def create_article():
    return render_template('article/create-article.html')
