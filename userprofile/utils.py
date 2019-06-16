
""" python modules """
import uuid
import operator
from collections import defaultdict

""" local django """
from formatter.formatter import Formatter
from django.core.paginator import Paginator


""" Utility class """
class Utils(object):

	""" pagination
	@param reqeust, items
	@return paginated item
	 """
	def custom_pagination(self, request, items):
	    import math
	    page_number = 1 if not request.GET.get('page') else request.GET.get('page')
	    paginate_by =  1000 if not request.GET.get('item') else request.GET.get('item')
	    paginator = Paginator(items, paginate_by)
	    try:
	        page_number = int(page_number)
	    except:
	        page_number = 1
	    try:
	        items = paginator.page(page_number)
	    except:
	        items = paginator.page(1)

	    pagination  = {
	        'total_count': paginator.count,
	        'total_pages': int(math.ceil(float(paginator.count)/float(paginate_by))),        
	        'item': paginate_by,
	        'page': page_number
	    }
	    return items, pagination