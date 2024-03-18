def convertTime(seconds):
    minutes = seconds//60
    seconds = seconds - (minutes*60)
    hours = minutes//60
    minutes = minutes - hours*60
    return print(f'{hours}h:{minutes}m:{seconds}s')
convertTime(1234)
convertTime(4567)