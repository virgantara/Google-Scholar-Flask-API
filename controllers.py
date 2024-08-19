from scholarly import scholarly

def get_list_publication(google_scholar_id):

	author_id = google_scholar_id
	author = scholarly.search_author_id(author_id)
	author = scholarly.fill(author)
	
	return [{'title': pub['bib']['title'], 'num_citations': pub['num_citations']} for pub in author['publications']]
	
	# return results
