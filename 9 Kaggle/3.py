# Iinitialize
import pandas
from numpy import NaN
from re import sub

df = pandas.read_csv("./3.0.csv")

# Rename columns

df.drop(columns="denominacion", inplace=True)
df.rename(
    columns={
        "nombre": "name",
        "cargo": "position",
        "area": "department",
        "sujetoobligado": "authority",
        "entidadfederativa": "state",
        "montoneto": "net",
        "montobruto": "gross",
        "periodoreportainicio": "reporting_start",
        "periodoreportafin": "reporting_end",
        "idInformacion": "id",
    },
    inplace=True,
)

# Reorder columns

df = df[
    [
        "id",
        "name",
        "position",
        "department",
        "authority",
        "state",
        "net",
        "gross",
        "reporting_start",
        "reporting_end",
    ]
]
df.set_index("id")

# Strip ALL fields

df = df.apply(
    lambda series: (
        series.str.strip().replace(r"\s\s+", " ", regex=True)
        if series.dtype == object
        else series
    )
)

# Parse dates


def parse(column: str):
    source = df[column].replace("/0208", "/2018", regex=True)
    one = pandas.to_datetime(source, format="%d/%m/%Y", errors="coerce")
    two = pandas.to_datetime(source, format="%d/%m/00%y", errors="coerce")
    three = pandas.to_datetime(source, format="%d/%m/02%y", errors="coerce")
    df[column] = one.fillna(two).fillna(three)


parse("reporting_start")
parse("reporting_end")

# Replace `position` defaults

df.position.replace("na", NaN, inplace=True)
df.position.replace("Ver nota", NaN, inplace=True)

# Condense if all three names are unavailable

df.name = df.name.apply(
    lambda field: (
        sub(r"^(.+) \1 \1 ?$", "\\1", field) if isinstance(field, str) else field
    )
)

# Replace default values in `name`

na_values = [
    r"(?i)&nbsp;",
    r"(?i)[*01-]",
    r"(?i)AAA",
    (
        r"(?i)CLASIFICADO NOMBRE DEL PERSONAL ADSCRITO\. ?VER NOTA(?: CLASIFICADO"
        r" PRIMER APELLIDO DEL PERSONAL ADSCRITO\. VER NOTA CLASIFICADO SEGUNDO"
        r" APELLIDO DEL(?: PERSONAL ADSCRITO\. VER NOTA)?)?"
    ),
    r"(?i)DIVERSOS EN REPORTE TRIMESTRAL FONE",
    r"(?i)ELIMINADO\.NOMBRE DE SERVIDOR PÚBLICO",
    r"(?i)ERROR:#N/A",
    r"(?i)INFORMACIÓN CLASIFICADA",
    r"(?i)INFORMACIÓN CLASIFICADA COMO RESERVADA",
    (
        r"(?i)INFORMACIÓN CLASIFICADA COMO RESERVADA INFORMACIÓN CLASIFICADA COMO"
        r" RESERVADA"
    ),
    r"(?i)INFORMACIÓN CONFIDENCIAL",
    (
        r"(?i)INFORMACION CONFIDENCIAL ART\. 20 PUNTO 1 Y 21 PUNTO 1 FRACCION I DE LA"
        r" LTAIPEJM"
    ),
    (
        r"(?i)INFORMACION DE CARÁCTER SENSIBLE ACUDIR A LAS OFICINAS CENTRALES PARA"
        r" INFORMACION DEALLADA"
    ),
    r"(?i)INFORMACIÓN NO DISPONIBLE\. VER NOTA\.",
    r"(?i)INFORMACION RESERVADA",
    r"(?i)INFORMACIÓN RESERVADA",
    r"(?i)INFORMACION RESERVADA \(\*\)",
    r"(?i)N/?[AD]",
    r"(?i)ND= NO HAY DATO VER CAMPO DE NOTA\.",
    r"(?i)NO DATO",
    r"(?i)NULL",
    r"(?i)PERSONAL ADSCRITO\. VER NOTA",
    r"(?i)POR DESIGNAR",
    r"(?i)RESERVAD[AO]",
    r"(?i)SIN ESPECIFICAR",
    r"(?i)VACANTE",
    r"(?i)VÉASE NOTA",
    r"(?i)X(?:XX(?:XXX)?)?",
]

df.name.replace(na_values, NaN, inplace=True, regex=True)

# Handle one unavailable name

df.name = df.name.apply(
    lambda field: (
        sub(r" ?N\A ?", " ", field).strip() if isinstance(field, str) else field
    )
)

# Output

df.to_csv("./3.5.csv")
