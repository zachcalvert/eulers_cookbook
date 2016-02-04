import datetime

from haystack import indexes
from problems.models import Problem


class ProblemIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.EdgeNgramField(document=True, use_template=True, template_name="search/indexes/problem.txt")
	title = indexes.CharField(model_attr='title', boost=1.3)
	number = indexes.CharField(model_attr='number')
	description = indexes.CharField(model_attr='description')

	def get_model(self):
		return Problem