import requests

class bluePages():
    def badgesEarned(self,uid):
        try:
            url = "https://w3-services1.w3-969.ibm.com/myw3/unified-profile/v1/docs/instances/expertise?userId="+str(uid)
            petition = requests.get(url)
            response = petition.json()
            response = response['content']['certifications']
            if 'badges' in response:
                response = response['badges']
                return response
            response = {'badge': 'Without any badge'}
            return response
        except Exception as e:
            return e

    def certificationsEarned(self,uid):
        try:
            url = "https://w3-services1.w3-969.ibm.com/myw3/unified-profile/v1/docs/instances/expertise?userId="+str(uid)
            petition = requests.get(url)
            response = petition.json()
            response = response['content']['certifications']
            if 'certs' in response:
                response = response['certs']
                return response
            response = {'certification': 'Without any certification'}
            return response
        except Exception as e:
            return e

    def teamMembersByManager(self,uid):
        try:
            url = "https://unified-profile.w3ibm.mybluemix.net/myw3/unified-profile/v1/docs/instances/teamInfoResolved/"+str(uid)
            petition = requests.get(url)
            response = petition.json()
            response = response['doc']['content']['incountry']
            if 'reports' in response:
                response = response['reports']
                return response
            response = {'Employeer': 'Without any employee'}
            return response
        except Exception as e:
            return e

    def personalInformationByUID(self,uid,images='',size=''):
        try:
            uid = uid.split('@')
            new_uid = ''
            new_uid = uid[0]+'%40'+uid[1]
            if images == '':
                url="https://w3-services1.w3-969.ibm.com/myw3/unified-profile/v1/api/ibmer/email/"+new_uid
                petition = requests.get(url)
                return petition.json()
            else:
                url = "https://w3-services1.w3-969.ibm.com/myw3/unified-profile/v1/api/ibmer/email/"+new_uid+"?images="+images+"&imageSize="+size
                petition = requests.get(url)
                return petition.json()
        except Exception as e:
            return e


