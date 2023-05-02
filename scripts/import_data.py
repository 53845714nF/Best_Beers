import csv
from beers.models import Brewery, BreweryGeocode, Category, Style, AccuracyEnum, Beer


def run():
    print('Info: Start import breweries.')
    with open('data/breweries.csv') as breweries_file:
        breweries_csv = csv.reader(breweries_file)
        next(breweries_file)

        Brewery.objects.all().delete()

        for row in breweries_csv:
            brewery_id = row[0]
            name = row[1]
            address = row[2]
            city = row[4]
            state = row[5]
            code = row[6]
            country = row[7]
            phone = row[8]
            website = row[9]
            descript = row[11]
            last_mod = row[12]

            breweries = Brewery(id=brewery_id,
                                name=name,
                                address=address,
                                city=city,
                                state=state,
                                code=code,
                                country=country,
                                phone=phone,
                                website=website,
                                description=descript,
                                last_mod=last_mod
                                )
            breweries.save()
    print('Info: Done with breweries.')

    print('Info: Start import breweries geocode.')
    with open('data/breweries_geocode.csv') as breweries_geocode_file:
        breweries_geocode_csv = csv.reader(breweries_geocode_file)
        next(breweries_geocode_file)

        BreweryGeocode.objects.all().delete()

        for row in breweries_geocode_csv:
            brewery_geocode_id = row[0]
            brewery_id = row[1]
            latitude = float(row[2])
            longitude = float(row[3])
            accuracy = row[4]

            if accuracy == 'ROOFTOP':
                accuracy_enum = AccuracyEnum.ROOFTOP
            elif accuracy == 'APPROXIMATE':
                accuracy_enum = AccuracyEnum.APPROXIMATE
            elif accuracy == 'GEOMETRIC_CENTER':
                accuracy_enum = AccuracyEnum.GEOMETRIC_CENTER
            elif accuracy == 'RANGE_INTERPOLATED':
                accuracy_enum = AccuracyEnum.RANGE_INTERPOLATED

            try:
                b_id = Brewery.objects.get(id=brewery_id)

                breweries_geocode = BreweryGeocode(id=brewery_geocode_id,
                                                   brewery_id=b_id,
                                                   latitude=latitude,
                                                   longitude=longitude,
                                                   accuracy=accuracy_enum
                                                   )
                breweries_geocode.save()
            except:
                print(f'Info: Breweries with Id {brewery_id} not found')
    print('Info: Done with breweries geocode.')

    print('Info: Start import categories.')
    with open('data/categories.csv') as categories_file:
        categories_csv = csv.reader(categories_file)
        next(categories_file)

        Category.objects.all().delete()

        for row in categories_csv:
            category_id = row[0]
            cat_name = row[1]
            last_mod = row[2]

            categories = Category(id=category_id,
                                  name=cat_name,
                                  last_mod=last_mod
                                  )
            categories.save()
    print('Info: Done with categories.')

    print('Info: Start import styles.')
    with open('data/styles.csv') as styles_file:
        styles_csv = csv.reader(styles_file)
        next(styles_csv)

        Style.objects.all().delete()

        for row in styles_csv:
            style_id = row[0]
            cat_id = row[1]
            style_name = row[2]
            last_mod = row[3]

            c_id = Category.objects.get(id=cat_id)

            style = Style(id=style_id,
                          cat_id=c_id,
                          name=style_name,
                          last_mod=last_mod
                          )
            style.save()
    print('Info: Done with styles.')

    print('Info: Start import beer.')
    csv.register_dialect('mydialect',
                         doublequote=True,
                         escapechar='\\',
                         quotechar='"',
                         quoting=csv.QUOTE_ALL,
                         )

    with open('data/beers_e.csv') as beers_file:
        beers_csv = csv.reader(beers_file, dialect='mydialect')
        next(beers_csv)

        Beer.objects.all().delete()

        for row in beers_csv:
            print(row)
            beer_id = row[0]
            brewery_id = row[1]
            name = row[2]
            cat_id = row[3]
            style_id = row[4]
            abv = float(row[5])
            descript = row[10]

            if row[11] == '0':
                last_mod = row[12]
            else:
                last_mod = row[11]



            try:
                b_id = Brewery.objects.get(id=brewery_id)
            except:
                print(f'Info: Brewery with Id {brewery_id} not fond.')
                b_id = None

            try:
                s_id = Style.objects.get(id=style_id)
            except:
                print(f'Info: Style with Id {brewery_id} not fond.')
                s_id = None

            try:
                c_id = Category.objects.get(id=cat_id)
            except:
                print(f'Info: Category with Id {cat_id} not fond.')
                c_id = None

            beer = Beer(id=beer_id,
                        brewery_id=b_id,
                        name=name,
                        cat_id=c_id,
                        style_id=s_id,
                        alcohol_by_volume=abv,
                        description=descript,
                        last_mod=last_mod
                        )
            beer.save()
    print('Info: Done with beer.')
