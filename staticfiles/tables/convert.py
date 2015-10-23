import csv
import datetime
from midas_pr.stakeholders.models import Stakeholder, Category, StakeholderGroup, MidasOffice, CommunicationPreference

# run this inside django docker shell...
# docker-compose -f dev.yml run django python manage.py shell
# execfile('staticfiles/tables/convert.py')

with open('staticfiles/tables/Stakeholders.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if not row[0]:
            row[0] = 'Unknown'
        if not row[5]:
            row[5] = 'Unknown'
        if not row[6]:
            row[6] = 'None'
        if not row[7]:
            row[7] = 'None'
        if '/' in row[49]:
            try:
                (m, d, y) = map(int, row[49].split('/'))
                if y < 20:
                    y += 2000
                elif y < 100:
                    y += 1900
                row[49] = datetime.date(y, m, d)
            except:
                row[49] = datetime.date(2000, 1, 1)
        else:
            row[49] = datetime.date(2000, 1, 1)
        try:
            Stakeholder(category=Category.objects.get_or_create(category_name=row[0])[0],
                        stakeholder_group=StakeholderGroup.objects.get_or_create(group_name=row[5])[0],
                        communication_preference=CommunicationPreference.objects.get_or_create(preference_name=row[6])[0],
                        midas_office=MidasOffice.objects.get_or_create(office_name=row[7])[0],
                        name=row[1], first_name=row[2], last_name=row[3], spouse=row[4], title=row[8],
                        phone_work=row[9], phone_mobile=row[10], phone_fax=row[11], phone_home=row[12],
                        email_work=row[13], email_home=row[14], url=row[15], work_address1=row[16],
                        work_address2=row[17], work_address_city=row[18], work_address_state=row[19],
                        work_address_zip=row[20], work_address_country=row[21], home_address1=row[22],
                        home_address_city=row[23], home_address_state=row[24], home_address_zip=row[25],
                        home_address_country=row[26], stakeholder_notes=row[27], lf_open_house_2012=('X' in row[28]),
                        ea1_comment=('X' in row[29]), ea1_positive={'+': True, '-': False}.get(row[30]),
                        ea1_topic_1=row[31], ea1_topic_2=row[32], ea1_topic_3=row[33], ea1_format=row[34],
                        ea2_email=('X' in row[35]), ea2_letter=('X' in row[36]), ea2_rp=row[37],
                        ea2_comment=('X' in row[38]), ea2_positive={'+': True, '-': False}.get(row[39]),
                        ea2_topic_1=row[40], ea2_topic_2=row[41], ea2_topic_3=row[42], ea2_format=row[43],
                        ea3_outreach=('x' in row[44]), ea3_rp=row[45], contacted=('X' in row[46]),
                        ea3_email=('X' in row[47]), ea3_letter=('X' in row[48]), site_tour_date=row[49],
                        tour_group=row[50], lf_open_house_2013=('X' in row[51])).save()
        except:
            print 'ERROR:', row
