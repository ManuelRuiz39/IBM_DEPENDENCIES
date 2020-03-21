import requests
import datetime
import xml.etree.ElementTree as ET    

class blueGroups():
    def addMemberTo(self,group,uid,email,password):
        """ 
            This method add a new member to your bluegroup previously created. 
            This method requires the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param uid: User id of new member (9 digits) :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=Members&mebox="+uid+"&Select=Add+Members&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'User added successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '4 The following members have not been added':
                    status = {'Status': 'Invalid user, verify your UID. it been expect 9 digit.'}
                    return status
                elif message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error
    
    def deleteMemberTo(self,group,uid,email,password):
        """ 
            This method deletes a member from your bluegroup previously created. 
            This method requires the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param uid: User id of member to remove (9 digits) :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=DelMem&mebox="+uid+"&Delete=Delete+Checked&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'User deleted successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '4 The following members have not been added':
                    status = {'Status': 'Invalid user, verify your UID. it been expect 9 digit.'}
                    return status
                elif message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error

    def addAdminTo(self,group,uid,email,password):
        """ 
            This method add a new administrator to your bluegroup previously created. 
            This method requires the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param uid: User id of new administrator (9 digits) :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=Administrators&mebox="+uid+"&Submit=Add+Administrators&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Admin added successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '4 The following admin have not been added':
                    status = {'Status': 'Invalid user, verify your UID. it been expect 9 digit.'}
                    return status
                elif message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error

    def deleteAdminTo(self,group,uid,email,password):
        """ 
            This method deletes an administrator to your bluegroup previously created. 
            This method requires the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param uid: User id of administrator to remove (9 digits) :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=DelAdm&mebox="+uid+"&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Admin deleted successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '4 The following members have not been added':
                    status = {'Status': 'Invalid admin, verify your UID. it been expect 9 digit.'}
                    return status
                elif message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error

    def createGroup(self,group,description,access,email,password):
        """ 
            This method create a new bluegroup. 
            This method require the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param description: Short description about your bluegroup :str : string.
                :param access: Access type (Everyone or Owner/Admins):str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            day = datetime.datetime.now()
            day = str(day).split(' ')
            day = day[0].split('-')
            group = group.split(' ')
            year = int(day[0]) + 1
            year = str(year)
            description = description.split(' ')
            new_group = ''
            new_description = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            if len(description) == 1:
                new_description = description[0]
            else:
                for item in description:
                    new_description = new_description+item+'%20'
                new_description = new_description[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?selectOn="+new_group+"&task=GoNew&gDesc="+new_description+"&mode=members&vAcc="+access+"&Y="+year+"&M="+day[1]+"&D="+day[2]+"&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Group created successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid information, please verify your information that is correct.'}
                    return status
        except Exception as error:
            return error

    def deleteGroup(self,group,email,password):
        """ 
            This method deletes a bluegroup. 
            This method requires the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=GoDel&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Group deleted successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error

    def memberInGroup(self,group,email):
        """ 
            This method shows the member that belongs to bluegroup. 
            This method require the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param email: Email from the person that you are looking for :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/groupsxml.wss?task=listMembers&group="+new_group
            petition = requests.get(url)
            root = ET.fromstring(petition.text)
            emails = []
            for element in root:
                if element.tag == "member":
                    emails.append(element.text)
            for correo in emails:
                if correo == email:
                    return True
            return False
        except Exception as error:
            return error

    def listGroup(self,group):
        """ 
            This method shows all members that  belong to bluegroup. 
            This method require the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/groupsxml.wss?task=listMembers&group="+new_group
            petition = requests.get(url)
            root = ET.fromstring(petition.text)
            response = []
            for element in root:
                if element.tag == "member":
                    json = {
                        'user': element.text
                    }
                    response.append(json)
            return response
        except Exception as error:
            return error

    def changeOwnerGroup(self,group,uid,email,password):
        """ 
            This method changes the current owner of bluegroup. 
            This method require the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param uid: User id which will be the owner :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=GoCO&mebox="+uid+"&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'The new owner of group is ' +uid}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '4 The following members have not been added':
                    status = {'Status': 'Invalid user, verify your UID. it been expect 9 digit.'}
                    return status
                elif message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error

    def renameGroup(self,group,name,email,password):
        """ 
            This method renames to bluegroup. 
            This method requires the next parameters:
                :param bluegroup: Name of current bluegroup :str : string.
                :param name: New name of bluegroup :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            new_name = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            name = name.split(' ')
            if len(name) == 1:
                new_name = name[0]
            else:
                for item in name:
                    new_name = new_name+item+'%20'
                new_name = new_name[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=GoCc&selectOn="+new_name+"&API=1"
            petition = requests.get(url,auth=(email,password))
            print(petition.text)
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Group renamed successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup, verify your BlueGroup it is correct.'}
                    return status
        except Exception as error:
            return error

    def changeDescription(self,group,description,email,password):
        """ 
            This method changes description from your bluegroup. 
            This method requires the next parameters:
                :param bluegroup: Name of bluegroup :str : string.
                :param description: New short description about your bluegroup :str : string.
                :param email: Your Email with domain @ibm :str : string.
                :param password: Your password of intranet :str : string.
        """
        try:
            group = group.split(' ')
            new_group = ''
            description = description.split(' ')
            new_description = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            if len(description) == 1:
                new_description = description[0]
            else:
                for item in description:
                    new_description = new_description+item+'%20'
                new_description = new_description[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=GoCc&gDesc="+new_description+"&API=1"
            petition = requests.get(url,auth=(email,password))
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Description changed successfully'}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid BlueGroup or description verify your information.'}
                    return status
        except Exception as error:
            return error

    """def changeExpirationDate(self,group,day,month,year,email,password):
        try:
            group = group.split(' ')
            new_group = ''
            if len(group) == 1:
                new_group = group[0]
            else:
                for item in group:
                    new_group = new_group+item+'%20'
                new_group = new_group[:-3]
            url = "https://bluepages.ibm.com/tools/groups/protect/groups.wss?gName="+new_group+"&task=GoCc&Y="+year+"&M="+month+"&D="+day+"&API=1"
            petition = requests.get(url,auth=(email,password))
            print(petition.text)
            response = int(petition.text)
            if response == 0:
                status = {'Status':'Change expiration date for group '+group}
                return status
            else:
                message = petition.text.split(':')
                if message[0] == '5 An Error Has Occurred During Processing.Error':
                    status = {'Status': 'Invalid information verify that is correct.'}
                    return status
        except Exception as error:
            return error"""






