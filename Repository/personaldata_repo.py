from Mongo.Mongo_models import Personaldata


def get_all_personaldata():
    return Personaldata.all()


def get_personaldata_by_id(id):
    return Personaldata.find(PersonalDataId=int(id))


def get_personaldata_by_name(pattern):
    return  Personaldata.find(PersonalDataName={"$regex":pattern, "$options":"i"})


def store_new_name(personaldata, new_value):
    personaldata.PersonalDataName = new_value
    personaldata.save()


def store_new_phone(personaldata, new_value):
    personaldata.PersonalDataPhone = new_value
    personaldata.save()


def store_new_email(personaldata, new_value):
    personaldata.PersonalDataEmail = new_value
    personaldata.save()


def store_new_personaldata(personaldata):
    personaldata.save()


def delete_personaldata(personaldata):
    Personaldata.delete(_id=personaldata._id)
