from operator import itemgetter

from JobParser import settings
from scraping.management import email_thread
from scraping.management.matcher import *


class EmployeeProcessor:

    def __init__(self, jobs):
        self.jobs = jobs

    def _process(self, employee):
        pass


    def _send_email(self, email, job_title):
        title = f'Regarding your "{job_title}" position'
        text = 'We have a candidate that might fit your position, please contact us if you are interested'
        print(email, ' -> ',title)
        email = settings.EMAIL_HOST_USER
        email_thread.send_html_mail(title, text, [email], settings.EMAIL_HOST_USER)

    def run(self, employee):
        print("###", employee.position)
        recommendations = self.load_csv()
        variants = list()
        employee_skills = employee.skills.splitlines()
        for job in self.jobs:
            if job.get('site') is None:
                continue
            percentage, must_have_skills = vacancy_percentage(employee_skills, job.get('description', ''))
            skill_courses, names = courses_advice(recommendations, must_have_skills)
            variants.append((percentage, job, skill_courses, names))

        if len(variants) > 0:
            top_list = sorted(variants, key=itemgetter(0), reverse=True)
            for variant in top_list[:3]:
                percentage = variant[0]
                job = variant[1]
                email = job.get('email')
                if not(email is None) & (email != ''):
                    #print(percentage, email, job.get('title', ''), '\n', variant[3])
                    self._send_email(email, job.get('title', ''))


    # csv_file = "Вакансии - Словарь скиллы.csv"
    def load_csv(self):
        with open("skills.csv", 'r', encoding="UTF-8") as fin:
            reader = csv.reader(fin, lineterminator='\n')
            recommendations = list(reader)
        return recommendations