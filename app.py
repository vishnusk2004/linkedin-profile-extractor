from linkedin_api import Linkedin
import json

# For this package we need to enter our linkedin username/email and password
# For this I made an demo linkedin account and updated below
api = Linkedin('sravankumar.82470@gmail.com', 'vishnu@2004')

profile_username = 'ahren-pradhan'
profile_data = api.get_profile(profile_username)

user_details = {
    "firstname": profile_data.get('firstName', ''),
    "lastname": profile_data.get('lastName', ''),
    "headline": profile_data.get('headline', ''),
    "location": profile_data.get('locationName', ''),
    "industry": profile_data.get('industryName', ''),
    "summary": profile_data.get('summary', ''),
    "public_id": profile_data.get('publicIdentifier', ''),
}

experience = []
for exp in profile_data.get('experience', []):
    experience.append({
        "title": exp.get('title', ''),
        "companyName" : exp.get('companyName', ''),
        "location": exp.get('locationName', ''),
        "startDate": exp.get('timePeriod', {}).get('startDate', {}),
        "endDate": exp.get('timePeriod', {}).get('endDate', {}),
        "description": exp.get('description', ''),
    })

skills = []
for skill in profile_data.get('skills', []):
    skills.append({
        "skill": skill.get('name', ''),
    })

education = []
for edu in profile_data.get('education', []):
    education.append({
        "schoolName": edu.get('schoolName', ''),
        "degreeName": edu.get('degreeName', ''),
        "fieldOfStudy": edu.get('fieldOfStudy', ''),
        "startDate": edu.get('timePeriod', {}).get('startDate', {}),
        "endDate": edu.get('timePeriod', {}).get('endDate', {}),
    })

profile_info = {
    "userDetails": user_details,
    "experience": experience,
    "skills": skills,
    "education": education
}

with open('profile_info.json', 'w') as json_file:
    json.dump(profile_info, json_file, indent=4)

print("profile information saved")
