import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI, HTTPException
from typing import List
from scholarly import scholarly

app = FastAPI()

# URL dasar dari profil dosen di Sinta & URL profil sinta unida
base_url = 'https://sinta.kemdikbud.go.id/authors/profile/'
unida_url = 'https://sinta.kemdikbud.go.id/affiliations/profile/2114'

def fetch_url_content(url: str):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Akan memunculkan HTTPError jika status code bukan 200
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengambil data dari {url}: {str(e)}")
    return BeautifulSoup(response.content, 'html.parser')   

def get_profile_unida():
    url = unida_url
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Akan memunculkan HTTPError jika status code bukan 200
        soup = BeautifulSoup(response.content, 'html.parser')

        # Mencari elemen nama dosen
        name_tag = soup.find('h3')
        name = name_tag.text.strip() if name_tag else 'Nama tidak ditemukan'

         # Menangkap semua elemen dengan class "stat-num"
        unida_details = soup.find_all('div', {'class': 'stat-num'})

        # Mengekstrak data dari elemen-elemen tersebut
        authors = unida_details[0].text.strip() if len(unida_details) > 0 else 'Tidak ditemukan'
        departements = unida_details[1].text.strip() if len(unida_details) > 1 else 'Tidak ditemukan'
        journals = unida_details[2].text.strip() if len(unida_details) > 2 else 'Tidak ditemukan'

         # Menangkap semua elemen dengan class "pr-num"
        sinta_scores = soup.find_all('div', {'class': 'pr-num'})

        # Mengekstrak data dari elemen-elemen tersebut
        sinta_score_overall = sinta_scores[0].text.strip() if len(sinta_scores) > 0 else 'Tidak ditemukan'
        sinta_score_3yr = sinta_scores[1].text.strip() if len(sinta_scores) > 1 else 'Tidak ditemukan'
        sinta_score_productivity = sinta_scores[2].text.strip() if len(sinta_scores) > 2 else 'Tidak ditemukan'
        sinta_score_productivity_3yr = sinta_scores[3].text.strip() if len(sinta_scores) > 3 else 'Tidak ditemukan'

        # Mencari tabel yang berisi data h-index
        table = soup.find('table', {'class': 'table table-borderless table-sm text-center stat-table'})
        rows = table.find_all('tr') if table else []

        # Mengambil data dokumen dari baris pertama tabel
        if rows:
            profile_table = rows[1]  # Baris ke-1 sesuai dengan struktur yang diberikan
            cells = profile_table.find_all('td')

            scopus_documents = cells[1].text.strip() if len(cells) > 1 else 'Tidak ditemukan'
            scholar_documents = cells[2].text.strip() if len(cells) > 2 else 'Tidak ditemukan'
            wos_documents = cells[3].text.strip() if len(cells) > 3 else 'Tidak ditemukan'
            garuda_documents = cells[4].text.strip() if len(cells) > 4 else 'Tidak ditemukan'
        else:
            scopus_documents = scholar_documents = wos_documents = garuda_documents = 'Tidak ditemukan'

        return {
            'ProfileID': '2114',
            'Nama': name,
            'authors': authors,
            'departements': departements,
            'journals': journals,
            'scopus_documents': scopus_documents,
            'scholar_documents': scholar_documents,
            'wos_documents': wos_documents,
            'garuda_documents': garuda_documents,
            'sinta_score_overall': sinta_score_overall,
            'sinta_score_3yr': sinta_score_3yr,
            'sinta_score_productivity': sinta_score_productivity,
            'sinta_score_productivity_3yr': sinta_score_productivity_3yr
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengambil data dari {url}: {str(e)}")

    return {
        'ProfileID': '2114',
        'Nama': '',
        'authors': '',
        'departements': '',
        'journals': '',
        'scopus_documents': '',
        'scholar_documents': '',
        'wos_documents': '',
        'garuda_documents': '',
        'sinta_score_overall': '',
        'sinta_score_3yr': '',
        'sinta_score_productivity': '',
        'sinta_score_productivity_3yr': ''
    }

# Fungsi untuk mengambil data h-index, nama dosen, dan Sinta Score
def get_h_index(profile_id: str):
    url = base_url + profile_id
    try:
        response = requests.get(url, timeout=10)
    
        soup = BeautifulSoup(response.content, 'html.parser')

        # Mencari elemen nama dosen
        name_tag = soup.find('h3')
        name = name_tag.text.strip() if name_tag else 'Nama tidak ditemukan'
        
        sinta_scores = soup.find_all('div', {'class': 'pr-num'})

        sinta_score_overall = sinta_scores[0].text.strip() if len(sinta_scores) > 0 else 'Tidak ditemukan'
        sinta_score_3yr = sinta_scores[1].text.strip() if len(sinta_scores) > 1 else 'Tidak ditemukan'

        
        # Mencari tabel yang berisi data h-index
        table = soup.find('table', {'class': 'table table-borderless table-sm text-center stat-table'})
        rows = table.find_all('tr')

        # Mengambil data h-index dari baris yang tepat
        h_index_row = rows[4]  # Baris ke-4 sesuai dengan struktur yang diberikan
        cells = h_index_row.find_all('td')

        scopus_h_index = cells[1].text.strip()
        scholar_h_index = cells[2].text.strip()
        wos_h_index = cells[3].text.strip()

        return {
            'ProfileID': profile_id,
            'Nama': name,
            'scopus_h_index': scopus_h_index,
            'gs_h_index': scholar_h_index,
            'wos_h_index': wos_h_index,
            'sinta_score_overall': sinta_score_overall,
            'sinta_score_3yr': sinta_score_3yr
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Gagal mengambil data dari {url}: {str(e)}")

    return {
        'ProfileID': '2114',
        'Nama': '',
        'scopus_h_index': '',
        'gs_h_index': '',
        'wos_h_index': '',
        'sinta_score_overall': '',
        'sinta_score_3yr': ''
    }

def get_list_publication(google_scholar_id: str):
    try:
        author = scholarly.search_author_id(google_scholar_id)
        author = scholarly.fill(author)
        return [{'title': pub['bib']['title'], 'num_citations': pub['num_citations']} for pub in author['publications']]
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Google Scholar ID tidak valid atau tidak ditemukan: {str(e)}")


@app.get("/sinta/profile/kampus")
def read_profile_unida():
    return get_profile_unida()
    
@app.get("/sinta/profile/dosen")
def read_h_index(profile_id: str):
    return get_h_index(profile_id)

# Multiple 
@app.get("/sinta/hindex/")
def read_multiple_h_indexes(profile_ids: str):
    # Memisahkan parameter menjadi list berdasarkan koma
    profile_id_list = profile_ids.split(',')
    data = [get_h_index(profile_id) for profile_id in profile_id_list]
    return data

@app.get("/gs/pub/list")
def get_pubs(gs_id: str):
    try:
        # Memanggil fungsi untuk mendapatkan publikasi dari Google Scholar
        item = get_list_publication(gs_id)
        results = {
            'status': 200,
            'values': item
        }
    except Exception as e:
        # Penanganan error jika terjadi kesalahan
        results = {
            'status': 500,
            'error': str(e)
        }
    return results
    
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=7000)