import requests
import json
import pymongo

# Authenticate with LinkedIn API and obtain access token
def get_access_token():
    client_id = 'your_client_id'
    client_secret = 'your_client_secret'
    redirect_uri = 'http://localhost:8000/auth/linkedin/callback'
    code = 'your_authorization_code'
    token_url = 'https://www.linkedin.com/oauth/v2/accessToken'
    payload = {
    'grant_type': 'authorization_code',
    'code': code,
    'redirect_uri': redirect_uri,
    'client_id': client_id,
    'client_secret': client_secret
    }
    response = requests.post(token_url, data=payload)
    access_token = json.loads(response.text)['access_token']
    return access_token

# Retrieve job listings from LinkedIn Jobs API

def get_job_listings(access_token):
    jobs_url = 'https://api.linkedin.com/v2/jobs'
    headers = {'Authorization': 'Bearer ' + access_token}
    params = {
          'keywords': 'python developer',
          'location': 'San Francisco Bay Area',
          'company': 'Google'
    }
    response = requests.get(jobs_url, headers=headers, params=params)
    job_listings = json.loads(response.text)
    return job_listings

# Connect to MongoDB and store job listings
def store_job_listings(job_listings):
    client = pymongo.MongoClient('mongodb://localhost:27017/')
    db = client['jobs_db']
    collection = db['job_listings']
    for job in job_listings:
        collection.insert_one(job)

# Main function
def main():
    access_token = get_access_token()
    job_listings = get_job_listings(access_token)
    store_job_listings(job_listings)

if __name__ == '__main__':
    main()


