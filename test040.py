fmedia = float(input('Type your first mark: '))
smedia = float(input('Type your second mark: '))
media = (fmedia + smedia) /2
if media >= 7.0:
    print('With {},You´re aproved'.format(media))
elif media >= 5.0 and media < 6.9:
    print('With {},You´re in recovery'.format(media))
elif media < 5.0:
    print('with {},You´re not aproved'.format(media))
