# hours to minutes
def convert_hours_to_minutes(hours):
  if not isinstance(hours, (int, float)):
    return f"Error! Hours must be an int or a float. 'hours' is a {type(hours)}"
      
  return hours * 60
  