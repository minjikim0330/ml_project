import random
import pandas as pd

weather_options = ['맑음', '비', '눈', '흐림']
genders = ['남', '여']

male_bottoms = {
    'hot': ['반바지', '면반바지'],
    'mild': ['청바지', '슬랙스', '면바지'],
    'cold': ['기모바지', '기모청바지']
}

female_bottoms = {
    'hot': ['치마', '반바지'],
    'mild': ['청바지', '슬랙스', '롱스커트'],
    'cold': ['기모레깅스', '기모치마', '기모바지']
}

outer_dict = {
    'hot': ['없음', '얇은 가디건'],
    'mild': ['가디건', '후드집업', '자켓'],
    'cold': ['패딩', '롱패딩', '코트']
}

top_dict = {
    'hot': ['반팔', '민소매'],
    'mild': ['긴팔티', '맨투맨', '후드티'],
    'cold': ['니트', '기모후드', '히트텍']
}

inner_dict = {
    'hot': ['없음'],
    'mild': ['없음', '얇은 이너'],
    'cold': ['히트텍']
}

rows = []

for _ in range(1000):

    temp = random.randint(-10, 35)
    feel_temp = temp + random.randint(-5, 3)

    weather = random.choice(weather_options)
    gender = random.choice(genders)

    if temp >= 25:
        season = 'hot'
    elif temp >= 10:
        season = 'mild'
    else:
        season = 'cold'

    outer = random.choice(outer_dict[season])
    top = random.choice(top_dict[season])

    if gender == '남':
        bottom = random.choice(male_bottoms[season])
    else:
        bottom = random.choice(female_bottoms[season])

    inner = random.choice(inner_dict[season])

    accessories = []

    if temp <= 5:
        accessories.extend(['목도리', '장갑', '핫팩'])

    if temp >= 25:
        accessories.extend(['선글라스', '모자', '양산'])

    if weather == '비':
        accessories.extend(['우산', '레인부츠'])

    if weather == '눈':
        accessories.extend(['부츠', '장갑'])

    if not accessories:
        accessories = ['없음']

    rows.append({
        'temp': temp,
        'feel_temp': feel_temp,
        'weather': weather,
        'gender': gender,
        'outer': outer,
        'top': top,
        'bottom': bottom,
        'inner': inner,
        'accessories': ', '.join(sorted(set(accessories)))
    })

df = pd.DataFrame(rows)

df.to_csv('weather_clothing_dataset.csv', index=False, encoding='utf-8-sig')

print(df.head())
