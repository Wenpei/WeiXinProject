# Create your views here.

from models import userpreference
def query_weather_preference(username):
    queryout = userpreference.objects.filter(weixin_user_name=username)
    if len(queryout) == 0: # If no record
        return "None"
    
    if queryout[0].weather_output_type == "T":
        return "text"
    elif queryout[0].weather_output_type == "N":
        return "news"
    else:
        return "None"

def save_weather_preference(username,weathertype):
 
    outType = ""
    for type in userpreference.output_type:
        if type[1] == weathertype:
            outType = type[0]
    queryout = userpreference.objects.filter(weixin_user_name=username)
    if len(queryout) > 1:
        return False
    if len(queryout) == 1:
        p = queryout[0]
        p.weather_output_type = outType
        p.save()
    else:
        p = userpreference(weixin_user_name = username,
                       weather_output_type = outType)
        p.save()
    return True