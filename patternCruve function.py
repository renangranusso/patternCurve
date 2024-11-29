def create_ndvi_pattern_curve(self, start_date, code_culture):
    pattern_curve = []

    culture = self.get_culture_by_code(code_culture)
    table_culture_ndvi = list(
        filter(lambda x: x["culture"] == culture, self.satveg_planilha_ndvi)
    )
    count = 0

    for item in table_culture_ndvi:
        date = start_date + timedelta(days=8 * count)
        formated_date = date.strftime("%d/%m/%Y")
        pattern_curve.append({"date": formated_date, "value": item["ndvi"]})
        count = count + 1

return pattern_curve


def get_culture_by_code(self, codigo):
    cultures = {1: "SOJA", 3: "MILHO", 4: "CANA DE AÇUCAR", 9: "SORGO"}

    return cultures.get(codigo)


def satveg_planilha_ndvi():
    return [
        {"date":"2020-09-21", "ndvi":0.1576,"pre_filter": 0.1576, "culture":"SOJA"},
        {"date":"2020-09-29", "ndvi":0.212,"pre_filter": 0.1777, "culture":"SOJA"},
        {"date":"2020-10-07", "ndvi":0.2314,"pre_filter": 0.1977, "culture":"SOJA"},
        {"date":"2020-10-15", "ndvi":0.1846,"pre_filter": 0.2178, "culture":"SOJA"},
        {"date":"2020-10-23", "ndvi":0.2453,"pre_filter": 0.2378, "culture":"SOJA"},
        {"date":"2020-10-31", "ndvi":0.2579,"pre_filter": 0.2579, "culture":"SOJA"},
        {"date":"2020-11-08", "ndvi":0.298,"pre_filter": 0.2692, "culture":"SOJA"},
        {"date":"2020-11-16", "ndvi":0.2806,"pre_filter": 0.2806, "culture":"SOJA"},
        {"date":"2020-11-24", "ndvi":0.4733,"pre_filter": 0.4957, "culture":"SOJA"},
        {"date":"2020-12-02", "ndvi":0.7107,"pre_filter": 0.7107, "culture":"SOJA"},
        {"date":"2020-12-10", "ndvi":0.6584,"pre_filter": 0.6584, "culture":"SOJA"},
        {"date":"2020-12-18", "ndvi":0.787,"pre_filter": 0.787, "culture":"SOJA"},
        {"date":"2020-12-26", "ndvi":0.8874,"pre_filter": 0.8874, "culture":"SOJA"},
        {"date":"2021-01-01", "ndvi":0.8416,"pre_filter": 0.8945, "culture":"SOJA"},
        {"date":"2021-01-09", "ndvi":0.9016,"pre_filter": 0.9016, "culture":"SOJA"},
        {"date":"2021-01-17", "ndvi":0.9497,"pre_filter": 0.9497, "culture":"SOJA"},
        {"date":"2021-01-25", "ndvi":0.8749,"pre_filter": 0.8749, "culture":"SOJA"},
        {"date":"2021-02-02", "ndvi":0.8216,"pre_filter": 0.8216, "culture":"SOJA"},
        {"date":"2021-02-10", "ndvi":0.478,"pre_filter": 0.478, "culture":"SOJA"},
        {"date":"2021-02-18", "ndvi":0.3194,"pre_filter": 0.4567, "culture":"SOJA"},
        {"date":"2021-02-26", "ndvi":0.2609,"pre_filter": 0.4354, "culture":"SOJA"},
        {"date":"2021-03-06", "ndvi":0.2794,"pre_filter": 0.414, "culture":"SOJA"},
        {"date":"2021-03-14", "ndvi":0.3927,"pre_filter": 0.3927,"culture":"MILHO"},
        {"date":"2021-03-22", "ndvi":0.5789,"pre_filter": 0.5789,"culture":"MILHO"},
        {"date":"2021-03-30", "ndvi":0.619,"pre_filter": 0.6983,"culture":"MILHO"},
        {"date":"2021-04-15", "ndvi":0.8177,"pre_filter": 0.8177,"culture":"MILHO"},
        {"date":"2021-04-23", "ndvi":0.8105,"pre_filter": 0.8105,"culture":"MILHO"},
        {"date":"2021-05-01", "ndvi":0.7816,"pre_filter": 0.7816,"culture":"MILHO"},
        {"date":"2021-05-09", "ndvi":0.7596,"pre_filter": 0.7596,"culture":"MILHO"},
        {"date":"2021-05-17", "ndvi":0.6379,"pre_filter": 0.6379,"culture":"MILHO"},
        {"date":"2021-05-25", "ndvi":0.6779,"pre_filter": 0.6779,"culture":"MILHO"},
        {"date":"2021-06-02", "ndvi":0.3443,"pre_filter": 0.3443,"culture":"MILHO"},
        {"date":"2021-06-10", "ndvi":0.3486,"pre_filter": 0.3486,"culture":"MILHO"},
        {"date":"2021-06-18", "ndvi":0.2986,"pre_filter": 0.2986,"culture":"MILHO"},
        {"date":"2021-06-26", "ndvi":0.3089,"pre_filter": 0.3089,"culture":"MILHO"},
        {"date":"2021-07-04", "ndvi":0.2754,"pre_filter": 0.2754,"culture":"MILHO"},
        {"date":"2021-07-12", "ndvi":0.2775,"pre_filter": 0.2775,"culture":"MILHO"},
        {"date":"2021-07-20", "ndvi":0.2297,"pre_filter": 0.2297,"culture":"MILHO"},
        {"date":"2021-07-28", "ndvi":0.2355,"pre_filter": 0.2355,"culture":"MILHO"},
        {"date":"2021-08-05", "ndvi":0.2308,"pre_filter": 0.2308,"culture":"MILHO"},
        {"date":"2021-08-13", "ndvi":0.2275,"pre_filter": 0.2275,"culture":"MILHO"},
        {"date":"2021-08-21", "ndvi":0.2255,"pre_filter": 0.2255,"culture":"MILHO"},
        {"date":"2021-08-29", "ndvi":0.2289,"pre_filter": 0.2289,"culture":"MILHO"},
        {"date":"2021-08-29", "ndvi":0.2289,"pre_filter": 0.2289,"culture":"MILHO"},
        {"date":"2020-09-21", "ndvi":0.1576,"pre_filter": 0.1576, "culture":"SORGO"},
        {"date":"2020-09-29", "ndvi":0.212,"pre_filter": 0.1777, "culture":"SORGO"},
        {"date":"2020-10-07", "ndvi":0.2314,"pre_filter": 0.1977, "culture":"SORGO"},
        {"date":"2020-10-15", "ndvi":0.1846,"pre_filter": 0.2178, "culture":"SORGO"},
        {"date":"2020-10-23", "ndvi":0.2453,"pre_filter": 0.2378, "culture":"SORGO"},
        {"date":"2020-10-31", "ndvi":0.2579,"pre_filter": 0.2579, "culture":"SORGO"},
        {"date":"2020-11-08", "ndvi":0.298,"pre_filter": 0.2692, "culture":"SORGO"},
        {"date":"2020-11-16", "ndvi":0.2806,"pre_filter": 0.2806, "culture":"SORGO"},
        {"date":"2020-11-24", "ndvi":0.4733,"pre_filter": 0.4957, "culture":"SORGO"},
        {"date":"2020-12-02", "ndvi":0.7107,"pre_filter": 0.7107, "culture":"SORGO"},
        {"date":"2020-12-10", "ndvi":0.6584,"pre_filter": 0.6584, "culture":"SORGO"},
        {"date":"2020-12-18", "ndvi":0.787,"pre_filter": 0.787, "culture":"SORGO"},
        {"date":"2020-12-26", "ndvi":0.8874,"pre_filter": 0.8874, "culture":"SORGO"},
        {"date":"2021-01-01", "ndvi":0.8416,"pre_filter": 0.8945, "culture":"SORGO"},
        {"date":"2021-01-09", "ndvi":0.9016,"pre_filter": 0.9016, "culture":"SORGO"},
        {"date":"2021-01-17", "ndvi":0.9497,"pre_filter": 0.9497, "culture":"SORGO"},
        {"date":"2021-01-25", "ndvi":0.8749,"pre_filter": 0.8749, "culture":"SORGO"},
        {"date":"2021-02-02", "ndvi":0.8216,"pre_filter": 0.8216, "culture":"SORGO"},
        {"date":"2021-02-10", "ndvi":0.478,"pre_filter": 0.478, "culture":"SORGO"},
        {"date":"2021-02-18", "ndvi":0.3194,"pre_filter": 0.4567, "culture":"SORGO"},
        {"date":"2021-02-26", "ndvi":0.2609,"pre_filter": 0.4354, "culture":"SORGO"},
        {"date":"2021-03-06", "ndvi":0.2794,"pre_filter": 0.414, "culture":"SORGO"},
    ]

def satveg_planilha_evi():
    return [
        {"date":"2020-10-07","evi":0.1648,"pre_filter":0.1004,"culture":"SOJA"},
        {"date":"2020-10-15","evi":0.0948,"pre_filter":0.1114,"culture":"SOJA"},
        {"date":"2020-10-23","evi":0.1576,"pre_filter":0.1225,"culture":"SOJA"},
        {"date":"2020-10-31","evi":0.1336,"pre_filter":0.1336,"culture":"SOJA"},
        {"date":"2020-11-08","evi":0.1829,"pre_filter":0.1505,"culture":"SOJA"},
        {"date":"2020-11-16","evi":0.1673,"pre_filter":0.1673,"culture":"SOJA"},
        {"date":"2020-11-24","evi":0.3044,"pre_filter":0.3346,"culture":"SOJA"},
        {"date":"2020-12-02","evi":0.5018,"pre_filter":0.5018,"culture":"SOJA"},
        {"date":"2020-12-10","evi":0.4561,"pre_filter":0.4561,"culture":"SOJA"},
        {"date":"2020-12-18","evi":0.7345,"pre_filter":0.7345,"culture":"SOJA"},
        {"date":"2020-12-26","evi":0.8811,"pre_filter":0.8811,"culture":"SOJA"},
        {"date":"2021-01-01","evi":0.7717,"pre_filter":0.7563,"culture":"SOJA"},
        {"date":"2021-01-09","evi":0.6315,"pre_filter":0.6315,"culture":"SOJA"},
        {"date":"2021-01-17","evi":0.7871,"pre_filter":0.7871,"culture":"SOJA"},
        {"date":"2021-01-25","evi":0.7351,"pre_filter":0.7351,"culture":"SOJA"},
        {"date":"2021-02-02","evi":0.5858,"pre_filter":0.5858,"culture":"SOJA"},
        {"date":"2021-02-10","evi":0.1792,"pre_filter":0.1792,"culture":"SOJA"},
        {"date":"2021-02-18","evi":0.1495,"pre_filter":0.1969,"culture":"MILHO"},
        {"date":"2021-02-26","evi":0.194,"pre_filter":0.2146,"culture":"MILHO"},
        {"date":"2021-03-06","evi":0.2211,"pre_filter":0.2323,"culture":"MILHO"},
        {"date":"2021-03-14","evi":0.25,"pre_filter":0.25,"culture":"MILHO"},
        {"date":"2021-03-22","evi":0.3593,"pre_filter":0.3593,"culture":"MILHO"},
        {"date":"2021-03-30","evi":0.4328,"pre_filter":0.531,"culture":"MILHO"},
        {"date":"2021-04-15","evi":0.7027,"pre_filter":0.7027,"culture":"MILHO"},
        {"date":"2021-04-23","evi":0.6462,"pre_filter":0.6462,"culture":"MILHO"},
        {"date":"2021-05-01","evi":0.5761,"pre_filter":0.5761,"culture":"MILHO"},
        {"date":"2021-05-09","evi":0.4985,"pre_filter":0.4985,"culture":"MILHO"},
        {"date":"2021-05-17","evi":0.4094,"pre_filter":0.4094,"culture":"MILHO"},
        {"date":"2021-05-25","evi":0.4104,"pre_filter":0.4104,"culture":"MILHO"},
        {"date":"2021-06-02","evi":0.2425,"pre_filter":0.2425,"culture":"MILHO"},
        {"date":"2021-06-10","evi":0.1865,"pre_filter":0.1865,"culture":"MILHO"},
        {"date":"2021-06-18","evi":0.1626,"pre_filter":0.1626,"culture":"MILHO"},
        {"date":"2021-06-26","evi":0.1521,"pre_filter":0.1521,"culture":"MILHO"},
        {"date":"2021-06-26","evi":0.1521,"pre_filter":0.1521,"culture":"MILHO"},
        {"date":"2020-09-21","evi":0.1576,"pre_filter": 0.1576, "culture":"SORGO"},
        {"date":"2020-09-29","evi":0.212,"pre_filter": 0.1777, "culture":"SORGO"},
        {"date":"2020-10-07","evi":0.2314,"pre_filter": 0.1977, "culture":"SORGO"},
        {"date":"2020-10-15","evi":0.1846,"pre_filter": 0.2178, "culture":"SORGO"},
        {"date":"2020-10-23","evi":0.2453,"pre_filter": 0.2378, "culture":"SORGO"},
        {"date":"2020-10-31","evi":0.2579,"pre_filter": 0.2579, "culture":"SORGO"},
        {"date":"2020-11-08","evi":0.298,"pre_filter": 0.2692, "culture":"SORGO"},
        {"date":"2020-11-16","evi":0.2806,"pre_filter": 0.2806, "culture":"SORGO"},
        {"date":"2020-11-24","evi":0.4733,"pre_filter": 0.4957, "culture":"SORGO"},
        {"date":"2020-12-02","evi":0.7107,"pre_filter": 0.7107, "culture":"SORGO"},
        {"date":"2020-12-10","evi":0.6584,"pre_filter": 0.6584, "culture":"SORGO"},
        {"date":"2020-12-18","evi":0.787,"pre_filter": 0.787, "culture":"SORGO"},
        {"date":"2020-12-26","evi":0.8874,"pre_filter": 0.8874, "culture":"SORGO"},
        {"date":"2021-01-01","evi":0.8416,"pre_filter": 0.8945, "culture":"SORGO"},
        {"date":"2021-01-09","evi":0.9016,"pre_filter": 0.9016, "culture":"SORGO"},
        {"date":"2021-01-17","evi":0.9497,"pre_filter": 0.9497, "culture":"SORGO"},
        {"date":"2021-01-25","evi":0.8749,"pre_filter": 0.8749, "culture":"SORGO"},
        {"date":"2021-02-02","evi":0.8216,"pre_filter": 0.8216, "culture":"SORGO"},
        {"date":"2021-02-10","evi":0.478,"pre_filter": 0.478, "culture":"SORGO"},
        {"date":"2021-02-18","evi":0.3194,"pre_filter": 0.4567, "culture":"SORGO"},
        {"date":"2021-02-26","evi":0.2609,"pre_filter": 0.4354, "culture":"SORGO"},
        {"date":"2021-03-06","evi":0.2794,"pre_filter": 0.414, "culture":"SORGO"},
    ]
